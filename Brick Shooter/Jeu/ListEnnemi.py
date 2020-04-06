from Ennemi import Ennemi
import time

class ListEnnemi:
    def __init__(self,config,listB):
        self.listE = []
        self.config = config
        self.lastEnnemiCreat = 0
        self.listeBullet = listB

    def addElemListE(self,x,y):
        if self.lastEnnemiCreat + self.config.getApparition() < time.time_ns():
            self.lastEnnemiCreat = time.time_ns()
            ennemi = Ennemi(self.config)
            ennemi.setx(x)
            ennemi.sety(y)
            self.listE.append(ennemi)

    def getImgElemListE(self, elem):
        return elem.getImg()

    def getListE(self):
        return self.listE


    def getxElemListE(self,elem):
        return elem.getx()

    def getyElemListE(self,elem):
        return elem.gety()

    def setxElemListE(self,elem,x):
        elem.setx()

    def setyElemListE(self,elem,y):
        elem.sety()

    def supprElemListE(self,elemp):
        tmp = []

        for  elem in self.listE:
            if elem != elemp:
                tmp.append(elem)
        self.listE = tmp

    def update():
        return True


    def IA():
        return True
