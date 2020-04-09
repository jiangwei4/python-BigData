import pygame
class GameOver:
    def __init__(self,Jeu):
        self._fenetre = Jeu.fenetre
        self.green = (0, 255, 0)
        self.font = pygame.font.Font('freesansbold.ttf', 100) 

    def go(self):
        self.text = self.font.render('Game Over', True, self.green) 
        self.textRect = self.text.get_rect()   
        self.textRect.center = (1920/2, 1080/2) 
        self._fenetre.blit(self.text, self.textRect)
