from Bullet import Bullet
import time

class ListBullet:
    def __init__(self,config):
        self.listB = []
        self.config = config
        self.lastBulletCreat = 0

    def getListB(self):
        return self.listB

    def getImgElemListB(self, elem):
        return elem.getImg()

    def addElemListB(self,x,y,direction,type):
        bullet = Bullet(self.config)
        bullet.setx(x)
        bullet.sety(y)
        bullet.setType(type)
        bullet.setDirection(direction)
        self.listB.append(bullet)
        return time.time_ns()

    def supprElemListB(self,elemp):
        tmp = []

        for  elem in self.listB:
            if elem != elemp:
                tmp.append(elem)
        self.listB = tmp

    def getxElemListB(self,elem):
        return elem.getx()

    def getyElemListB(self,elem):
        return elem.gety()

    def setxElemListB(self,elem,x):
        elem.setx()

    def setyElemListB(self,elem,y):
        elem.sety()

    def update(self):
        cpt = 0
        for elem in self.listB:
            cpt += 1
            if elem.getDirection() == 0:
                elem.mvty('n')

            if elem.getDirection() == 1:
                elem.mvty('n')
                elem.mvtx('p')

            if elem.getDirection() == 2:
                elem.mvtx('p')

            if elem.getDirection() == 3:
                elem.mvtx('p')
                elem.mvty('p')

            if elem.getDirection() == 4:
                elem.mvty('p')
            
            if elem.getDirection() == 5:
                elem.mvty('p')
                elem.mvtx('n')

            if elem.getDirection() == 6:
                elem.mvtx('n')

            if elem.getDirection() == 7:
                elem.mvtx('n')
                elem.mvty('n')

            #si elem sort du cadre on le supr     
            
            if  elem.getx() < self.config.getMin() or elem.getx() > self.config.getSurfaceW() or elem.gety() < self.config.getMin() or elem.gety() > self.config.getSurfaceH():
                self.supprElemListB(elem)
                            
        #print(cpt)