from Meteorite import Meteorite
import time
import random
from Animation import Animation

class ListMeteorite:
    def __init__(self,config,listBullet,listEnnemi,sound,jeu,vaisseau):
        self.listM = []
        self.config = config
        self.listEnnemi = listEnnemi
        self.listBullet = listBullet
        self.lastMeteoriteCreat = 0
        self.jeu = jeu
        self.sound = sound
        self.vaisseau = vaisseau

    def getListM(self):
        return self.listM

    def getImgElemListM(self, elem):
        return elem.getImg()

    def addElemListM(self):
        if self.lastMeteoriteCreat + self.config.getApparitionMeteorite() < time.time_ns():
            self.lastMeteoriteCreat = time.time_ns()
            meteorite = Meteorite(self.config)
            rd = random.randint(0, 3)
            rdH = random.randint(0,self.config.getSurfaceH())
            rdL = random.randint(0,self.config.getSurfaceW())
            if rd == 0:
                x = random.randint(0,self.config.getSurfaceW()-(meteorite.getHaut()+1))
                y = 0
                direction = random.choice([3,4,5])

            if rd == 1:
                x = 0
                y = random.randint(0,self.config.getSurfaceH()-(meteorite.getHaut()+1))
                direction = random.choice([1,2,3])

            if rd == 2:
                x = random.randint(0,self.config.getSurfaceW()-(meteorite.getLarg()+1))
                y = self.config.getSurfaceH()-(meteorite.getHaut()+1)
                direction = random.choice([0,1,7])

            if rd == 3:
                x = self.config.getSurfaceW()-(meteorite.getLarg()+1)
                y = random.randint(0,self.config.getSurfaceH()-(meteorite.getHaut()+1))
                direction = random.choice([5,6,7])
            
            meteorite.setx(x)
            meteorite.sety(y)
            meteorite.setDirection(direction)
            self.listM.append(meteorite)


    def supprElemListM(self,elemp):
        tmp = []

        for  elem in self.listM:
            if elem != elemp:
                tmp.append(elem)
        self.listM = tmp

    def getxElemListM(self,elem):
        return elem.getx()

    def getyElemListM(self,elem):
        return elem.gety()

    def setxElemListM(self,elem,x):
        elem.setx()

    def setyElemListM(self,elem,y):
        elem.sety()

    def update(self):
        cpt = 0
        for elem in self.listM:
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
                self.supprElemListM(elem)

            ##suppresion des bullet qui touhe la meteorite
            for elemB in self.listBullet.getListB():
                if(elemB.getCentre()[0]>elem.getx() and elemB.getCentre()[0]<(elem.getx()+elem.getLarg())):
                    if(elemB.getCentre()[1]>elem.gety() and elemB.getCentre()[1]<(elem.gety()+elem.getHaut())):
                        #suppr bullet 
                        self.listBullet.supprElemListB(elemB)
                       
                            

            ##suppresion des ennemi qui touhe la meteorite
            for elemE in self.listEnnemi.getListE():
                if(elemE.getCentre()[0]>elem.getx() and elemE.getCentre()[0]<(elem.getx()+elem.getLarg())):
                    if(elemE.getCentre()[1]>elem.gety() and elemE.getCentre()[1]<(elem.gety()+elem.getHaut())):
                        # ennemi + explosion
                        t1 = Animation(self.jeu,elemE.getx(),elemE.gety())
                        t1.start()
                        self.sound.explosion()
                        self.listEnnemi.supprElemListE(elemE)
                        
                            
            
            ##moins une vie si on se fait toucher
            if(self.vaisseau.getCentre()[0]>elem.getx() and self.vaisseau.getCentre()[0]<(elem.getx()+elem.getLarg())):
                if(self.vaisseau.getCentre()[1]>elem.gety() and self.vaisseau.getCentre()[1]<(elem.gety()+elem.getHaut())):
                    self.vaisseau.setLife(self.vaisseau.getLife()-1)
                    if self.vaisseau.getLife() <= 0:
                        t1 = Animation(self.jeu,self.vaisseau.getx(),self.vaisseau.gety())
                        t1.start()

                    
                            
        #print(cpt)