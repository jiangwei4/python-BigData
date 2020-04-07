import pygame

class Hud:
    def __init__(self,Jeu,vaisseau):
        self.green = (0, 255, 0)
        self.vaisseau = vaisseau
        self._fenetre = Jeu.fenetre
        self.font = pygame.font.Font('freesansbold.ttf', 32) 
        

    def hud(self):
        self.text = self.font.render('Points : '+str(self.vaisseau.getPoint()), True, self.green) 
        self.textRect = self.text.get_rect()   
        self.textRect.center = (100, 1000) 
        self._fenetre.blit(self.text, self.textRect)
        
        self.text2 = self.font.render('Vie : '+str(self.vaisseau.getLife()), True, self.green) 
        self.textRect2 = self.text2.get_rect()   
        self.textRect2.center = (80, 1040) 
        self._fenetre.blit(self.text2, self.textRect2)
