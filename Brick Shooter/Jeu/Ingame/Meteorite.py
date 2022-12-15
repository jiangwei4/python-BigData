import os
import random
class Meteorite:
    def __init__(self,config):
        self.config = config
        self.img = 'meteorite'
        self.x=0
        self.y=0
        self.larg = 153
        self.haut = 166
        self.mouvementSpeed = random.randint(1, 10)
        self.direction = 0 #0haut 2droite 4bas 6gauche
        self.direction


        
    def getLarg(self):
        return self.larg

    def getHaut(self):
        return self.haut

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

    def getImg(self):
        return os.path.join('images',self.img+'.png')