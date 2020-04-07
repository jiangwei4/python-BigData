import time
import os
class Ennemi:
    def __init__(self,config,listBullet):
        self.img = 'ennemi'
        self.config = config
        self.larg = 40
        self.haut = 40
        self.mouvementSpeed = self.config.getMouvementSpeedEnnemi()
        self.life = 1
        self.x=0
        self.y=0
        self.listBullet = listBullet
        self.direction = 0 #0haut 2droite 4bas 6gauche
        self.type=1
        self.lastBulletCreat = 0
        self.centre = [self.x+(self.larg/2),self.y+(self.haut/2)]

        self.zoneTirx = 0
        self.zoneTiry = 0

    def getCentre(self):
        return self.centre

    def getLarg(self):
        return self.larg

    def getHaut(self):
        return self.haut

    def getZoneTir(self):
        return [self.zoneTirx,self.zoneTiry]

    def getDirection(self):
        return self.direction

    def setDirection(self,da,db,dc,dd):
        if da == db:
            da = 0
            db = 0
        if dc == dd:
            dc = 0
            dd = 0
        
        tmp = [da,dc,db,dd]
        
        if tmp in self.config.getDirecitonPossible():
            self.direction = self.config.getValeurDirection()[self.config.getDirecitonPossible().index(tmp)]

        ##update zoneTir
        
        zoneTir = self.config.getZoneTirPossible()[self.direction]
        self.zoneTirx = zoneTir[0]+self.x
        self.zoneTiry = zoneTir[1]+self.y



    def getImg(self):
        return os.path.join('images',self.img+str(self.direction)+'.png')

    def setx(self,x):
        if self.x+x > self.config.getMin() and self.x+x < self.config.getSurfaceW()-self.larg:
            self.x += x

    def getx(self):
        return self.x

    def sety(self,y): 
        if self.y+y > self.config.getMin() and self.y+y < self.config.getSurfaceH()-self.haut:
            self.y += y
    
    def gety(self):
        return self.y

    def getMouvementSpeed(self):
        return self.mouvementSpeed

    def getLife(self):
        return self.life
    
    def setLife(self, life):
        self.life = life

    def avance(self):
        if self.direction == 0:
            self.y -= self.mouvementSpeed

        if self.direction == 1:
            self.y -= self.mouvementSpeed
            self.x += self.mouvementSpeed

        if self.direction == 2:
            self.x += self.mouvementSpeed
        
        if self.direction == 3:
            self.x += self.mouvementSpeed
            self.y += self.mouvementSpeed

        if self.direction == 4:
            self.y += self.mouvementSpeed

        if self.direction == 5:
            self.y += self.mouvementSpeed
            self.x -= self.mouvementSpeed
            

        if self.direction == 6:
            self.x -= self.mouvementSpeed

        if self.direction == 7:
            self.x -= self.mouvementSpeed
            self.y -= self.mouvementSpeed
            
        self.centre = [self.x+(self.larg/2),self.y+(self.haut/2)]


    def tirer(self):
        if self.lastBulletCreat + self.config.getRapidFireEnnemi() < time.time_ns():
            self.lastBulletCreat = self.listBullet.addElemListB(self.zoneTirx,self.zoneTiry,self.direction,self.type)