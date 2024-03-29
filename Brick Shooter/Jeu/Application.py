import pygame
from ElementsNavigation.Menu import Menu
from ElementsNavigation.Jeu import Jeu
from ElementsNavigation.Config import Config
from ElementsNavigation.Reglages import Reglages
from ElementsNavigation.Magasin import Magasin
from Extra.Sound import Sound
from Ingame.Vaisseau import Vaisseau
from Ingame.ListBullet import ListBullet
pygame.mixer.init()

class Application :
    """ Classe maîtresse gérant les différentes interfaces du jeu """
    def __init__(self) :
        self.config = Config()
        pygame.init()
        pygame.display.set_caption("XANAX")
 
        self.fond = self.config.getBlue()
 
        #self.fenetre = pygame.display.set_mode((self.config.getSurfaceW(),self.config.getSurfaceH()),pygame.FULLSCREEN)#pygame.display.set_mode((surfaceW,surfaceH))
        self.fenetre = pygame.display.set_mode((self.config.getSurfaceW(),self.config.getSurfaceH()))

        self.sound = Sound()
        self.sound.inAcceuil()
        # Groupe de sprites utilisé pour l'affichage
        self.groupeGlobal = pygame.sprite.Group()
        self.statut = True
        self.listBullet = ListBullet(self.config)
        self.vaisseau = Vaisseau(self.config,self.listBullet)
 
    def _initialiser(self) :
        try:
            self.ecran.detruire()
            # Suppression de tous les sprites du groupe
            self.groupeGlobal.empty()
        except AttributeError:
            pass
 
    def menu(self) :
        # Affichage du menu
        self._initialiser()
        self.ecran = Menu(self, self.groupeGlobal)
 
    def jeu(self) :
        # Affichage du jeu
        self._initialiser()
        self.ecran = Jeu(self, self.config, self.vaisseau,self.listBullet,app, self.groupeGlobal)
 
    def continuer(self):
        self._initialiser()
        self.listBullet = ListBullet(self.config)
        self.vaisseau = Vaisseau(self.config,self.listBullet)
        self.ecran = Jeu(self, self.config, self.vaisseau,self.listBullet,app, self.groupeGlobal)
        self.ecran.run()

    def nouvellePartie(self):
        self._initialiser()
        self.listBullet = ListBullet(self.config)
        self.vaisseau = Vaisseau(self.config,self.listBullet)
        self.ecran = Jeu(self, self.config, self.vaisseau,self.listBullet,app, self.groupeGlobal)
        self.ecran.run()

        #self.ecran = Affichage(self, self.groupeGlobal)
    def chargerPartie(self):
        self._initialiser()
    def magasin(self):
        self._initialiser()
        self.ecran = Magasin(self, self.config,self.vaisseau, app, self.groupeGlobal)
        
    def credits(self):
        self._initialiser()
    def sauvegarder(self):
        self._initialiser()
    def reglages(self):
        self._initialiser()
        self.ecran = Reglages(self, self.config, app, self.groupeGlobal)

    def quitter(self) :
        self.statut = False
 
    def update(self) :
        events = pygame.event.get()
 
        for event in events :
            if event.type == pygame.QUIT :
                self.quitter()
                return
 
       # self.fenetre.fill(self.fond)
        self.ecran.update(events)
        self.groupeGlobal.update()
        self.groupeGlobal.draw(self.fenetre)
        pygame.display.update()
 

app = Application()
app.menu()
 
clock = pygame.time.Clock()
 
while app.statut :
    app.update()
    clock.tick(30)
 
pygame.quit()