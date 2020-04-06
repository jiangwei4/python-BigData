import os
import pygame
class Sound:
    def __init__(self,Jeu):
        self._fenetre = Jeu.fenetre
        pygame.mixer.init(44100, -16, 2, 2048)


    def explosion(self):
        return True
        #pygame.mixer.music.load(os.path.join('sons',"1428.mp3"))
        #pygame.mixer.Channel(1).play(pygame.mixer.music.load(os.path.join('sons',"1428.mp3")))

    def start(self):
        pygame.mixer.music.load(os.path.join('sons',"E1M1.mid"))
        pygame.mixer.music.play()