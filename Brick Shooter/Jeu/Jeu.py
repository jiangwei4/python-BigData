import pygame
from Vaisseau import Vaisseau
import time
from ListBullet import ListBullet
from Config import Config
from ListEnnemi import ListEnnemi
from Sound import Sound
from Hud import Hud
from AnimationInvincible import AnimationInvincible
from GameOver import GameOver

from ListMeteorite import ListMeteorite
from Meteorite import Meteorite
from Bullet import Bullet
from Ennemi import Ennemi

class Jeu :
    
    def __init__(self, jeu, config,vaisseau,listBullet,app, *groupes) :
        self.app = app
        self._fenetre = jeu.fenetre
        #jeu.fond = (0, 0, 0)
 
        self.config = config
        self.jeu = jeu
        self.sound = Sound()#jeu)
        self.listBullet = listBullet
        self.Vaisseau = vaisseau
        self.hud = Hud(jeu,self.Vaisseau)
        self.gameover = GameOver(self.jeu)
        
        self.listEnnemi = ListEnnemi(self.config,self.listBullet, self.Vaisseau,self.listBullet,jeu,self.sound)
        self.listMeteorite = ListMeteorite(self.config,self.listBullet,self.listEnnemi,self.sound,jeu,self.Vaisseau)


        self.vaisseauInit = Vaisseau(self.config,[])
        self.BulletInit = Bullet(self.config)
        self.EnnemiInit = Ennemi(self.config,[])
        self.MeteoriteInit = Meteorite(self.config)

        self.imgMeteorite = self.loadImg(self.MeteoriteInit.getImg())
        self.imgBullet = [self.loadImg(self.BulletInit.getImgType(0)),self.loadImg(self.BulletInit.getImgType(1))]
        self.imgFond = self.loadImg("images/fond.png")

        self.imgVaisseau = []
        self.imgEnnemi = []
        for i in range(8):
            imgV = self.loadImg(self.vaisseauInit.getImgDirection(i))
            imgE = self.loadImg(self.EnnemiInit.getImgDirection(i))
            self.imgVaisseau.append(imgV)
            self.imgEnnemi.append(imgE)

        
    
    def getSurface(self):
        return self._fenetre

    def update(self):
        pygame.display.update()

    

    def loadImg(self,name):
        return pygame.image.load(name)

    def position(self,img,x,y):
        self._fenetre.blit(img,(x,y))

    def run(self):
        xa_mvt = 0
        ya_mvt = 0
        xb_mvt = 0
        yb_mvt = 0
        da=0
        db=0
        dc=0
        dd=0
        tir = False
        listsBullet = []

        self.sound.start()
        vitesse = self.Vaisseau.getMouvementSpeed()
        mybool = True
        while mybool:
            if self.Vaisseau.getLife()<=0:
                ##game over 
                self.gameover.go()
                self.update()
                time.sleep(2)
                mybool = False

            
            for event in pygame.event.get():
              
                if event.type == pygame.QUIT:
                    pygame.quit()
                    quit()
                
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        pygame.quit()
                        quit()

                    if event.key == self.config.getUpKey():
                        ya_mvt = -vitesse
                        da = 1

                    if event.key == self.config.getDownKey():
                        yb_mvt = vitesse
                        db = 1
                        

                    if event.key == self.config.getLeftKey():
                        xa_mvt = -vitesse
                        dc = 1
                       

                    if event.key == self.config.getRightKey():
                        xb_mvt = vitesse
                        dd = 1
                       

                    if event.key == self.config.getFireKey():
                        tir = True
                        

                if event.type == pygame.KEYUP:
                    if event.key == self.config.getUpKey():
                        ya_mvt = 0
                        da = 0
                    if event.key == self.config.getDownKey():
                        yb_mvt = 0
                        db = 0
                    if event.key == self.config.getLeftKey():
                        xa_mvt = 0
                        dc = 0
                    if event.key == self.config.getRightKey():
                        xb_mvt = 0
                        dd = 0

                    if event.key == self.config.getFireKey():
                        tir = False

                        
            time.sleep(0.02)
            #self._fenetre.fill(self.config.getBlue())
            self.position(self.imgFond,0,0)
            ###### ajout un enemey
            self.listEnnemi.addElemListE()

            self.listEnnemi.update()
            for elem in self.listEnnemi.getListE():
                self.position(self.imgEnnemi[elem.getDirection()],self.listEnnemi.getxElemListE(elem),self.listEnnemi.getyElemListE(elem))
                #self.position(self.loadImg(self.listEnnemi.getImgElemListE(elem)),self.listEnnemi.getxElemListE(elem),self.listEnnemi.getyElemListE(elem)) 

            #######

            ###### ajout une meteorite
            self.listMeteorite.addElemListM()

            self.listMeteorite.update()
            for elem in self.listMeteorite.getListM():
                self.position(self.imgMeteorite,self.listMeteorite.getxElemListM(elem),self.listMeteorite.getyElemListM(elem)) 

            #######
           
            if tir:
                self.Vaisseau.tirer()

            self.listBullet.update()
            for elem in self.listBullet.getListB():
                self.position(self.imgBullet[elem.getType()],self.listBullet.getxElemListB(elem),self.listBullet.getyElemListB(elem)) 

            self.Vaisseau.setDirection(da,db,dc,dd)
            self.Vaisseau.setx(xa_mvt+xb_mvt)
           
            self.Vaisseau.sety(ya_mvt+yb_mvt)
            self.Vaisseau.update()
            if self.Vaisseau.getInvincible():
                if self.Vaisseau.getInvincibleLancer() == False:
                    self.Vaisseau.setInvincibleLancer(True)
                    t1 = AnimationInvincible(self.jeu,self.Vaisseau,self.config)
                    t1.start()            
            else :
                self.position(self.imgVaisseau[self.Vaisseau.getDirection()],self.Vaisseau.getx(),self.Vaisseau.gety())
            self.hud.hud()
            self.update()
                
        
        
        self.app.menu()

        