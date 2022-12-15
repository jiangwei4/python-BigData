
import pygame
from ElementsNavigation.Config import Config
from ElementsNavigation.MenuBouton import MenuBouton
class Menu :
    """ Création et gestion des boutons d'un menu """
    def __init__(self,application, *groupes) :
        self.config = Config()
        self.fenetre = application.fenetre
        self.fenetre.blit(pygame.image.load("images/acceuil.jpg"),(0,0))
        self.couleurs = dict(
            normal=self.config.getCouleurButton(),
            survol=self.config.getCouleurButtonHover(),
        )
        font = pygame.font.SysFont('Helvetica', 24, bold=True)
        # noms des menus et commandes associées
        items = (
            ('JOUER', application.continuer),
            ('NOUVELLE PARTIE', application.nouvellePartie),
            ('CHARGER PARTIE', application.chargerPartie),
            ('MAGASIN', application.magasin),
            ('SAUVEGARDER', application.sauvegarder),
            ('REGLAGES', application.reglages),
            ('CREDITS', application.credits),
            ('QUITTER', application.quitter)
        )
        x = 200
        y = 180
        self._boutons = []
        for texte, cmd in items :
            mb = MenuBouton(
                texte,
                self.couleurs['normal'],
                font,
                x,
                y,
                300,
                50,
                cmd
            )
            self._boutons.append(mb)
            y += 120
            for groupe in groupes :
                groupe.add(mb)
 
    def update(self, events) :
        clicGauche, *_ = pygame.mouse.get_pressed()
        posPointeur = pygame.mouse.get_pos()
        for bouton in self._boutons :
            # Si le pointeur souris est au-dessus d'un bouton
            if bouton.rect.collidepoint(*posPointeur) :
                # Changement du curseur par un quelconque
                pygame.mouse.set_cursor(*pygame.cursors.tri_left)
                # Changement de la couleur du bouton
                bouton.dessiner(self.couleurs['survol'])
                # Si le clic gauche a été pressé
                if clicGauche :
                    # Appel de la fonction du bouton
                    bouton.executerCommande()
                break
            else :
                # Le pointeur n'est pas au-dessus du bouton
                bouton.dessiner(self.couleurs['normal'])
        else :
            # Le pointeur n'est pas au-dessus d'un des boutons
            # initialisation au pointeur par défaut
            pygame.mouse.set_cursor(*pygame.cursors.arrow)
 
    def detruire(self) :
        pygame.mouse.set_cursor(*pygame.cursors.arrow) # initialisation du pointeur