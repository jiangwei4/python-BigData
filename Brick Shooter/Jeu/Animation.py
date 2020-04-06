import pygame
import time
import threading 

class Animation(threading.Thread):
    def __init__(self,Jeu,x,y, *args, **kwargs): 
        super(Animation, self).__init__(*args, **kwargs) 
        self._stop = threading.Event()
        self._fenetre = Jeu.fenetre
        self.imgExplosion = "images/explosion"
        self.lastFrame = 0
        self.delai = 20
        self.x = x
        self.y = y

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
            for i in range(13):
                t = time.time_ns()+50000000 #+0.5sec
                while time.time_ns()-t < 0.5:
                    self.position(self.loadImg(self.imgExplosion+str(i)+'.png'),self.x-30,self.y-30)
            self.stop()
    

        




        