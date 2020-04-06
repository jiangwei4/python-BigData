from Ennemi import Ennemi
import time

class ListEnnemi:
    def __init__(self,config,listB,vaisseau):
        self.listE = []
        self.config = config
        self.lastEnnemiCreat = 0
        self.listeBullet = listB
        self.vaisseau = vaisseau

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

    def update(self):
        cpt = 0
        for elem in self.listE:
            cpt += 1
            da=0
            db=0
            dc=0
            dd=0
            #direction
            if elem.getx() > self.vaisseau.getx():
                dd=1

            if elem.getx() < self.vaisseau.getx():
                dc=1
            
            if elem.gety() > self.vaisseau.gety():
                db=1

            if elem.gety() < self.vaisseau.gety():
                da=1

            elem.setDirection(da,db,dc,dd)

            #avance
            elem.avance()

            #suppr si vie ==0
            if  elem.getLife() <= 0:
                self.supprElemListE(elem)

            #deplacement +tir

            


    def IA():
        return True
