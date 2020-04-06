import pygame
import time

class Animation:
    def __init__(self,Jeu) :
        self._fenetre = Jeu.fenetre
        self.imgExplosion = "images/explosion"
    
    def loadImg(self,name):
        return pygame.image.load(name)

    def position(self,img,x,y):
        self._fenetre.blit(img,(x,y))

    def explosion(self,x,y):
        for i in range(6):
            self.position(self.loadImg(self.imgExplosion+str(i)+'.png'),x-30,y-30) 
            pygame.display.flip()
            time.sleep(0.2)



        