
import pygame
from MenuBouton import MenuBouton
from BlocTexte import BlocTexte
class Magasin :
    """ Création et gestion des boutons d'un menu """
    def __init__(self,magasin,config,vaisseau, app, *groupes) :
        self.config = config
        self.app = app
        self.listenToKey = False
        self._fenetre = magasin.fenetre
        self.vaisseau = vaisseau
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
        self.keys = [
            {"name": "vie", "value": str(self.config.getLife())},
            {"name": "bouclier", "value": str(self.config.getShield())},
            {"name": "vitessetir", "value": str(self.config.getRapidFire())},
            {"name": "vitesserechargement", "value": str(self.config.getSpeedShield())},
            {"name": "vitessedeplacement", "value": str(self.config.getMouvementSpeed())},
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
        

    def vie(self):
        self.config.setLife(self.config.getLife()+1)
        self.vaisseau.vaisseauUpdate()
        self.updateKey(self.config.getLife(), 0)


    def bouclier(self):
        self.config.setShield(self.config.getShield()+1)
        self.vaisseau.vaisseauUpdate()
        self.updateKey(self.config.getShield(), 1)


    
    def vitesseTir(self):
        self.config.setRapidFire(self.config.getRapidFire()+50000000)
        self.vaisseau.vaisseauUpdate()
        self.updateKey(self.config.getRapidFire(), 2)

    
    def vitesseBouclier(self):
        self.config.setSpeedShield(self.config.getSpeedShield()+1)
        self.vaisseau.vaisseauUpdate()
        self.updateKey(self.config.getSpeedShield(), 3)

    def vitesseDeplacement(self):
        self.config.setMouvementSpeed(self.config.getMouvementSpeed()+1)
        self.vaisseau.vaisseauUpdate()
        self.updateKey(self.config.getMouvementSpeed(), 4)


    def updateKey(self, key, index):
        self.keys[index]["value"] = key
        self._keys[index].changeTexte(str(key))
    
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