
import pygame

class BlocTexte(pygame.sprite.Sprite) :
    """ Création d'un simple bouton rectangulaire """
    def __init__(self, texte, couleur, font, x, y, largeur, hauteur) :
        super().__init__()
        self.image = pygame.Surface((largeur, hauteur))
        self.font = font
        self.couleur = couleur
        
        self.rect = self.image.get_rect()
        self.rect.center = (x, y)
 
        self.texte = font.render(texte, True, (0, 0, 0))
        self.rectTexte = self.texte.get_rect()
        self.rectTexte.center = (largeur/2, hauteur/2)
 
        self.dessiner(couleur)
 
    def dessiner(self, couleur) :
        self.image.fill(couleur)
        self.image.blit(self.texte, self.rectTexte)
    
    def changeTexte(self, texte):
        self.texte = self.font.render(texte, True, (0, 0, 0))
        self.dessiner(self.couleur)
