import pygame
from Config import Config
from MenuBouton import MenuBouton
from Jeu import Jeu

class Reglages:
    def __init__(self, reglages, application, *groupes):
        self.config = Config()
        self._fenetre = reglages.fenetre
        self.listenToKey = False
        self.fireKey = self.config.getFireKey()
        self.app = application
        
        self.couleurs = dict(
            normal=self.config.getCouleurButton(),
            survol=self.config.getCouleurButtonHover(),
        )
        font = pygame.font.SysFont('Helvetica', 24, bold=True)
        
        # noms des menus et commandes associées
        
        items = (
            ('BOUTON TIR', self.updateListen),
            ('JOUER', self.jouer),
        )
        self.keys = [
            {"name": "fireKey", "value": self.getKeyString(self.config.getFireKey())},
        ]
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
        
            
        x = 800
        y = 180
        for key in self.keys :
            y += 120


    def changeKey(self):
        while self.listenToKey:
            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        print("I quit")
                        pygame.quit()
                        quit()
                    else:
                        self.config.setFireKey(event.key)
                        self.updateKey(event.key)
                        self.listenToKey = False
    
    def updateListen(self):
        self.listenToKey = True
        self.changeKey()

    def updateKey(self, key):
        self.keys[0]["value"] = self.getKeyString(key)
        print(self.config.getFireKey())
    
    def getKeyString(self, key):
        return pygame.key.name(key)
    
    def jouer(self):
        self.app.continuer()
 
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
 