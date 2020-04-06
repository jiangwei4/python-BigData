class Bullet:
    def __init__(self,config):
        self.config = config
        self.img = 'images/bullet'
        self.x=0
        self.y=0
        self.larg = 11
        self.haut = 11
        self.mouvementSpeed = self.config.getMouvementSpeedBullet()
        self.direction = 0 #0haut 2droite 4bas 6gauche
        self.type = 0 #couleur du tir
        self.direction



    def setDirection(self, direction):
        self.direction = direction

    def getDirection(self):
        return self.direction

    def mvtx(self,x):
        if x == 'n':
            self.x -= self.mouvementSpeed
        else :
            self.x += self.mouvementSpeed

    def mvty(self,y):
        if y == 'n':
            self.y -= self.mouvementSpeed
        else :
            self.y += self.mouvementSpeed


    def setx(self,x):
        self.x+= x

    def sety(self,y):
        self.y += y

    def getx(self):
        return self.x

    def gety(self):
        return self.y

    def setType(self,type):
        self.type = type

    def getImg(self):
        return str(self.img)+str(self.type)+'.png'