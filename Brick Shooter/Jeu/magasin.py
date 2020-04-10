
import pygame
from Config import Config
from MenuBouton import MenuBouton
class Magasin :
    """ Création et gestion des boutons d'un menu """
    def __init__(self,magasin,config, app, *groupes) :
        self.config = config
        self.app = app
        self.listenToKey = False
        self._fenetre = magasin.fenetre
        
        self.couleurs = dict(
            normal=self.config.getCouleurButton(),
            survol=self.config.getCouleurButtonHover(),
        )
        font = pygame.font.SysFont('Helvetica', 24, bold=True)
        self._fenetre.blit(pygame.image.load("images/acceuil.jpg"),(0,0))
        
        # noms des menus et commandes associées
        
        items = (
            ('Vie', self.vie),
            ('Bouclier', self.bouclier),
            ('Vitesse de tir', self.vitesseTir),
            ('Vitesse rechargement du bouclier', self.vitesseBouclier),
            ('Vitesse de deplacement', self.vitesseDeplacement),
            ('RETOUR', self.retourMenu),
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
            y += 60
            for groupe in groupes :
                groupe.add(mb)
           
        x = 800
        y = 180
        

    def vie(self):
        return True

    def bouclier(self):
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

    def vitesseBouclier(self):
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

    def vitesseDeplacement(self):
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

    def vitesseTir(self):
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