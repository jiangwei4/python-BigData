from Ennemi import Ennemi
import time
import random
from Animation import Animation

class ListEnnemi:
    def __init__(self,config,listB,vaisseau, listeBullet,jeu,sound):
        self.listE = []
        self.config = config
        self.lastEnnemiCreat = 0
        self.listeBullet = listB
        self.vaisseau = vaisseau
        self.listeBullet = listeBullet
        self.jeu = jeu
        self.sound = sound
        

    def addElemListE(self):
        if self.lastEnnemiCreat + self.config.getApparition() < time.time_ns():
            self.lastEnnemiCreat = time.time_ns()
            ennemi = Ennemi(self.config,self.listeBullet)
            #randomisation
            x = 0
            y = 0

            rd = random.randint(0, 3)
            rdH = random.randint(0,self.config.getSurfaceH())
            rdL = random.randint(0,self.config.getSurfaceW())
            if rd == 0:
                x = random.randint(0,self.config.getSurfaceW()-41)
                y = 0

            if rd == 1:
                x = 0
                y = random.randint(0,self.config.getSurfaceH()-41)

            if rd == 2:
                x = random.randint(0,self.config.getSurfaceW()-41)
                y = self.config.getSurfaceH()-41

            if rd == 3:
                x = self.config.getSurfaceW()-41
                y = random.randint(0,self.config.getSurfaceH()-41)

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
                dc=1

            if elem.getx() < self.vaisseau.getx():
                dd=1
            
            if elem.gety() > self.vaisseau.gety():
                da=1

            if elem.gety() < self.vaisseau.gety():
                db=1


            elem.setDirection(da,db,dc,dd)

            #avance
            elem.avance()

            
            #tirer
            elem.tirer()

            for elemB in self.listeBullet.getListB():
                if(elemB.getType() == 0):
                    if(elemB.getCentre()[0]>elem.getx() and elemB.getCentre()[0]<(elem.getx()+elem.getLarg())):
                        if(elemB.getCentre()[1]>elem.gety() and elemB.getCentre()[1]<(elem.gety()+elem.getHaut())):
                            #suppr bullet + ennemi
                            self.listeBullet.supprElemListB(elemB)
                            #self.animation.explosion(elem.getx(),elem.gety())
                            
                            #t1.setInformations(self.Vaisseau, self)
                            t1 = Animation(self.jeu,elem.getx(),elem.gety())
                            t1.start()
                            self.vaisseau.setPoint(self.vaisseau.getPoint()+10)
                            self.sound.explosion()
                            self.supprElemListE(elem)


                if(elemB.getType() == 1):
                    if(elemB.getCentre()[0]>self.vaisseau.getx() and elemB.getCentre()[0]<(self.vaisseau.getx()+self.vaisseau.getLarg())):
                        if(elemB.getCentre()[1]>self.vaisseau.gety() and elemB.getCentre()[1]<(self.vaisseau.gety()+self.vaisseau.getHaut())):
                            self.vaisseau.setLife(self.vaisseau.getLife()-1)
                            self.listeBullet.supprElemListB(elemB)



            #suppr si vie ==0
            if  elem.getLife() <= 0:
                self.supprElemListE(elem)

        

