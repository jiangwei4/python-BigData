import pygame
from MenuBouton import MenuBouton
from BlocTexte import BlocTexte


class Reglages:
    def __init__(self, reglages, config, app, *groupes):
        self.config = config
        self.app = app
        self.listenToKey = False
        self._fenetre = reglages.fenetre
        self.fireKey = self.config.getFireKey()
        
        self.couleurs = dict(
            normal=self.config.getCouleurButton(),
            survol=self.config.getCouleurButtonHover(),
        )
        font = pygame.font.SysFont('Helvetica', 24, bold=True)
        self._fenetre.fill(self.config.getBlue())
        
        # noms des menus et commandes associées
        
        items = (
            ('BOUTON TIR', self.changeFireKey),
            ('BOUTON HAUT', self.changeUpKey),
            ('BOUTON BAS', self.changeDownKey),
            ('BOUTON DROITE', self.changeRightKey),
            ('BOUTON GAUCHE', self.changeLeftKey),
            ('RETOUR', self.retourMenu),
        )
        self.keys = [
            {"name": "fireKey", "value": self.getKeyString(self.config.getFireKey())},
            {"name": "upKey", "value": self.getKeyString(self.config.getUpKey())},
            {"name": "downKey", "value": self.getKeyString(self.config.getDownKey())},
            {"name": "rightKey", "value": self.getKeyString(self.config.getRightKey())},
            {"name": "leftKey", "value": self.getKeyString(self.config.getLeftKey())},
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
            y += 60
            for groupe in groupes :
                groupe.add(mb)
           
        x = 800
        y = 180
        self._keys = []
        for key in self.keys :
            bt = BlocTexte(
                key["value"],
                self.couleurs['normal'],
                font,
                x,
                y,
                300,
                50
            )
            self._keys.append(bt)
            y += 60
            for groupe in groupes :
                groupe.add(bt)

    def changeFireKey(self):
        self.listenToKey = True
        while self.listenToKey:
            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        print("I quit")
                        pygame.quit()
                        quit()
                    else:
                        self.config.setFireKey(event.key)
                        self.updateKey(event.key, 0)
                        self.listenToKey = False

    def changeUpKey(self):
        self.listenToKey = True
        while self.listenToKey:
            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        print("I quit")
                        pygame.quit()
                        quit()
                    else:
                        self.config.setUpKey(event.key)
                        self.updateKey(event.key, 1)
                        self.listenToKey = False

    def changeDownKey(self):
        self.listenToKey = True
        while self.listenToKey:
            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        print("I quit")
                        pygame.quit()
                        quit()
                    else:
                        self.config.setDownKey(event.key)
                        self.updateKey(event.key, 2)
                        self.listenToKey = False

    def changeRightKey(self):
        self.listenToKey = True
        while self.listenToKey:
            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        print("I quit")
                        pygame.quit()
                        quit()
                    else:
                        self.config.setRightKey(event.key)
                        self.updateKey(event.key, 3)
                        self.listenToKey = False

    def changeLeftKey(self):
        self.listenToKey = True
        while self.listenToKey:
            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        print("I quit")
                        pygame.quit()
                        quit()
                    else:
                        self.config.setLeftKey(event.key)
                        self.updateKey(event.key, 4)
                        self.listenToKey = False

    def updateKey(self, key, index):
        self.keys[index]["value"] = self.getKeyString(key)
        self._keys[index].changeTexte(self.getKeyString(key))
    
    def getKeyString(self, key):
        return pygame.key.name(key)
    
    def retourMenu(self):
        self.app.menu()
 
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