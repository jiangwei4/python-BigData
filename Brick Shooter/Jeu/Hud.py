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
        self.textRect.center = (100, 20) 
        self._fenetre.blit(self.text, self.textRect)
        
        self.text2 = self.font.render('Vie : '+str(self.vaisseau.getLife()), True, self.green) 
        self.textRect2 = self.text2.get_rect()   
        self.textRect2.center = (80, 1000) 
        self._fenetre.blit(self.text2, self.textRect2)
        
        self.text4 = self.font.render('Bouclier : '+str(self.vaisseau.getShield()), True, self.green) 
        self.textRect4 = self.text4.get_rect()   
        self.textRect4.center = (120, 1040) 
        self._fenetre.blit(self.text4, self.textRect4)
