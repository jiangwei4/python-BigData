import pygame
from Config import Config
from MenuBouton import MenuBouton

class Reglages:
    def __init__(self, reglages, *groupes):
        self.config = Config()
        self._fenetre = reglages.fenetre
        self.getKey = False
        self.fireKey = pygame.K_a
        
        self.couleurs = dict(
            normal=self.config.getCouleurButton(),
            survol=self.config.getCouleurButtonHover(),
        )
        font = pygame.font.SysFont('Helvetica', 24, bold=True)
        
        # noms des menus et commandes associées
        keys = [
            [self.config.getKeyString(self.config.getFireKey()), self.comd],
        ]
        items = (
            ('BOUTON TIR', self.changeKey(keys)),
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

        x = 800
        y = 180
        self._keys = []
        for key in keys :
            mb = MenuBouton(
                key[0],
                self.couleurs['normal'],
                font,
                x,
                y,
                300,
                50,
                key[1]
            )
            self._keys.append(mb)
            y += 120
            for groupe in groupes :
                groupe.add(mb)


    def changeKey(self, keys):
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                print(event.key)
                key[0] = [config.getKeyString(event.key), key[0][1]]
                self.config.setFireKey(event.key)

    def comd(self):
        return True

 
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