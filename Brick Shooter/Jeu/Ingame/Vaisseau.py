
import time
import os

class Vaisseau:
    def __init__(self, config,listBullet):
        self.img = 'vaisseau'
        self.config = config
        self.x=self.config.getSurfaceW()/2-40
        self.y=self.config.getSurfaceH()/2-40
        self.lastBulletCreat = 0
        self.invincible = False
        self.invincibleLancer = False

        self.larg = 40
        self.haut = 40
        self.mouvementSpeed = self.config.getMouvementSpeed()
        self.life = self.config.getLife()
        self.shield = self.config.getShield()
        self.speedshield = self.config.getSpeedShield()
        self.point = 0
        self.direction = 0 #0haut 2droite 4bas 6gauche
        self.listBullet = listBullet
        self.type = 0

        self.lastTouch = 0##en sec
        self.shieldLastTouch = 0

        self.zoneTirx = 0
        self.zoneTiry = 0
        self.centre = [self.x+(self.larg/2),self.y+(self.haut/2)]

    def getInvincibleLancer(self):
        return self.invincibleLancer
    
    def setInvincibleLancer(self,bool):
        self.invincibleLancer = bool

    def getInvincible(self):
        return self.invincible

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
        self.centre = [self.x+(self.larg/2),self.y+(self.haut/2)]



    def getImg(self):
        return os.path.join('images',self.img+str(self.direction)+'.png')

    def getImgDirection(self,direction):
        return os.path.join('images',self.img+str(direction)+'.png')

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
        if self.shield > 0:
            self.shieldLastTouch = time.time()
            self.shield -= 1
        else :
            if time.time() > self.lastTouch + self.config.getInvincible():
                self.life = life
                self.lastTouch = time.time()
                self.invincible = True

    def getShield(self):
        return self.shield

    def setShield(self, shield):
        self.shield = shield

    def getSpeedShield(self):
        return self.speedshield

    def tirer(self):
        if self.lastBulletCreat + self.config.getRapidFire() < time.time_ns():
            self.lastBulletCreat = self.listBullet.addElemListB(self.zoneTirx,self.zoneTiry,self.direction,self.type)

    def setPoint(self,point):
        self.point = point

    def getPoint(self):
        return self.point

    def update(self):
        if time.time() > self.lastTouch + self.config.getInvincible():
            self.invincible = False
        if time.time() > self.shieldLastTouch + self.config.speedshield:
            self.shield = self.config.getShield()


    def vaisseauUpdate(self):
        self.mouvementSpeed = self.config.getMouvementSpeed()
        self.life = self.config.getLife()
        self.shield = self.config.getShield()
        self.speedshield = self.config.getSpeedShield()

    def getShieldLastTouch(self):
        return self.shieldLastTouch


    
