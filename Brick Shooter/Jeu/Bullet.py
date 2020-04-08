import os
class Bullet:
    def __init__(self,config):
        self.config = config
        self.img = 'bullet'
        self.x=0
        self.y=0
        self.larg = 11
        self.haut = 11
        self.mouvementSpeed = self.config.getMouvementSpeedBullet()
        self.direction = 0 #0haut 2droite 4bas 6gauche
        self.type = 0 #couleur du tir
        self.direction
        self.centre = [self.x+(self.larg/2),self.y+(self.haut/2)]

    def getCentre(self):
        return self.centre

    def setDirection(self, direction):
        self.direction = direction

    def getDirection(self):
        return self.direction

    def mvtx(self,x):
        if x == 'n':
            self.x -= self.mouvementSpeed
        else :
            self.x += self.mouvementSpeed
        self.centre = [self.x+(self.larg/2),self.y+(self.haut/2)]

    def mvty(self,y):
        if y == 'n':
            self.y -= self.mouvementSpeed
        else :
            self.y += self.mouvementSpeed
        self.centre = [self.x+(self.larg/2),self.y+(self.haut/2)]


    def setx(self,x):
        self.x+= x

    def sety(self,y):
        self.y += y

    def getx(self):
        return self.x

    def gety(self):
        return self.y

    def getType(self):
        return self.type

    def setType(self,type):
        self.type = type

    def getImg(self):
        return os.path.join('images',self.img+str(self.type)+'.png')

    def getImgType(self,type):
        return os.path.join('images',self.img+str(type)+'.png')
