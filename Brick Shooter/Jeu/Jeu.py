import pygame
from Vaisseau import Vaisseau
import time
from ThreadGame import ThreadGame
from ListBullet import ListBullet
from Config import Config
from Ennemi import Ennemi

class Jeu :
    
    def __init__(self, jeu, *groupes) :
        self._fenetre = jeu.fenetre
        #jeu.fond = (0, 0, 0)
 
        self.config = Config()
      
        
       
        self.Vaisseau = Vaisseau(self.config)
        self.listBullet = ListBullet(self.config)
        self.ennemi = Ennemi(self.config)
        self.run()
        

    
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
        #t1 = ThreadGame() 
        #t1.setInformations(self.Vaisseau, self)
        #t1.start()

        
        vitesse = self.Vaisseau.getMouvementSpeed()
        while True:
            
            for event in pygame.event.get():
              
                if event.type == pygame.QUIT:
                    pygame.quit()
                    quit()
                
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_UP:
                        ya_mvt = -vitesse
                        da = 1

                    if event.key == pygame.K_DOWN:
                        yb_mvt = vitesse
                        db = 1
                        

                    if event.key == pygame.K_LEFT:
                        xa_mvt = -vitesse
                        dc = 1
                       

                    if event.key == pygame.K_RIGHT:
                        xb_mvt = vitesse
                        dd = 1
                       

                    if event.key == pygame.K_a:
                        tir = True
                        

                if event.type == pygame.KEYUP:
                    if event.key == pygame.K_UP:
                        ya_mvt = 0
                        da = 0
                    if event.key == pygame.K_DOWN:
                        yb_mvt = 0
                        db = 0
                    if event.key == pygame.K_LEFT:
                        xa_mvt = 0
                        dc = 0
                    if event.key == pygame.K_RIGHT:
                        xb_mvt = 0
                        dd = 0

                    if event.key == pygame.K_a:
                        tir = False

                        
            time.sleep(0.02)
            self._fenetre.fill(self.config.getBlue())
            ###### ajout un enemey
            self.position(self.loadImg(self.ennemi.getImg()),self.ennemi.getx(),self.ennemi.getx())
            #######
           
            if tir:
                self.listBullet.addElemListB(self.Vaisseau.getZoneTir()[0],self.Vaisseau.getZoneTir()[1],self.Vaisseau.getDirection())

            self.listBullet.update()
            for elem in self.listBullet.getListB():
                self.position(self.loadImg(self.listBullet.getImgElemListB(elem)),self.listBullet.getxElemListB(elem),self.listBullet.getyElemListB(elem)) 

            self.Vaisseau.setDirection(da,db,dc,dd)
            self.Vaisseau.setx(xa_mvt+xb_mvt)
           
            self.Vaisseau.sety(ya_mvt+yb_mvt)
            self.position(self.loadImg(self.Vaisseau.getImg()),self.Vaisseau.getx(),self.Vaisseau.gety())
            self.update()