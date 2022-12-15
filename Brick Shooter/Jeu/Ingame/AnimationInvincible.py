import pygame
import time
import threading 
from Ingame.Vaisseau import Vaisseau

class AnimationInvincible(threading.Thread):
    def __init__(self,Jeu,vaisseau,config, *args, **kwargs): 
        super(AnimationInvincible, self).__init__(*args, **kwargs) 
        self._stop = threading.Event()
        self._fenetre = Jeu.fenetre
        self.vaisseau = vaisseau
        self.lastFrame = 0
        self.delai = 20
        self.config= config
        self.x = self.vaisseau.getx()
        self.y = self.vaisseau.gety()

        self.vaisseauInit = Vaisseau(self.config,[])
        self.imgVaisseau = []
        for i in range(8):
            imgV = self.loadImg(self.vaisseauInit.getImgDirection(i))
            self.imgVaisseau.append(imgV)

    def stop(self): 
        self._stop.set() 
  
    def stopped(self): 
        return self._stop.isSet() 

    def loadImg(self,name):
        return pygame.image.load(name)

    def position(self,img,x,y):
        self._fenetre.blit(img,(x,y))
  
    def run(self): 
        while True:
            if self.stopped(): 
                return
            t = time.time()
            i = 0

            while time.time()-t < self.config.getInvincible():
                e = time.time_ns()
                time.sleep(0.1)
                while  e + 200000000 > time.time_ns():
                    self.position(self.loadImg(self.vaisseau.getImgDirection(self.vaisseau.getDirection())),self.vaisseau.getx(),self.vaisseau.gety())

            self.vaisseau.setInvincibleLancer(False)
            self.stop()
    

        




        