import pygame

class Config:
    def __init__(self):
        #couleur
        self.surfaceW = 1920
        self.surfaceH = 1080
        self.blue = (113, 117, 227)
        self.white = (255,255,255)
        self.min = 0
        self.couleurButton = (92, 66, 61)
        self.couleurButtonHover = (96, 51, 42)



        ##important
        self.direcitonPossible = [[0,0,0,1],[0,0,1,0],[0,0,1,1],[0,1,0,0],[0,1,1,0],[1,0,0,0],[1,0,0,1],[1,1,0,0]]
        self.valeurDirection = [2,4,3,6,5,0,1,7]
        self.zoneTirPossible = [[15,-20],[48,-16],[48,15],[46,46],[15,46],[-16,44],[-20,15],[-16,-16]]


        #vaisseau
        self.rapidFire = 400000000 
        self.mouvementSpeed = 4
        self.life = 1
        self.shield = 0
        self.speedshield = 5
        self.invincible = 2

        #bullet
        self.mouvementSpeedBullet = 6

        #ennemi
        self.apparition = 3000000000
        self.mouvementSpeedEnnemi = 1
        self.rapidFireEnnemi = 1000000000

        #keyboard
        self.fireKey = pygame.K_a
        self.upKey = pygame.K_UP
        self.downKey = pygame.K_DOWN
        self.rightKey = pygame.K_RIGHT
        self.leftKey = pygame.K_LEFT

        #meteorite
        self.apparitionMeteorite = 7000000000

    def getInvincible(self):
        return self.invincible

    def getApparitionMeteorite(self):
        return self.apparitionMeteorite

    def getRapidFireEnnemi(self):
        return self.rapidFireEnnemi

    def getMouvementSpeedEnnemi(self):
        return self.mouvementSpeedEnnemi

    def getApparition(self):
        return self.apparition

    def getMouvementSpeedBullet(self):
        return self.mouvementSpeedBullet

    def getMouvementSpeed(self):
        return self.mouvementSpeed

    def setMouvementSpeed(self,mvt):
        self.mouvementSpeed = mvt

    def getLife(self):
        return self.life
    
    def setLife(self, life):
        self.life = life

    def getShield(self):
        return self.shield

    def setShield(self, shield):
        self.shield = shield

    def getSpeedShield(self):
        return self.speedshield

    def setSpeedShield(self,val):
        self.speedshield = val

    def getRapidFire(self):
        return self.rapidFire

    def setRapidFire(self,val):
        self.rapidFire = val

    def getH(self):
        return self.surfaceH

    def getW(self):
        return self.surfaceW

    def getBlue(self):
        return self.blue

    def getSurfaceW(self):
        return self.surfaceW

    def getSurfaceH(self):
        return self.surfaceH

    def getMin(self):
        return self.min

    def getZoneTirPossible(self):
        return self.zoneTirPossible

    def getDirecitonPossible(self):
        return self.direcitonPossible

    def getValeurDirection(self):
        return self.valeurDirection

    def getCouleurButtonHover(self):
        return self.couleurButtonHover

    def getCouleurButton(self):
        return self.couleurButton

    def getFireKey(self):
        return self.fireKey
    
    def setFireKey(self, key):
        self.fireKey = key

    def getUpKey(self):
        return self.upKey
    
    def setUpKey(self, key):
        self.upKey = key

    def getDownKey(self):
        return self.downKey
    
    def setDownKey(self, key):
        self.downKey = key

    def getRightKey(self):
        return self.rightKey
    
    def setRightKey(self, key):
        self.rightKey = key

    def getLeftKey(self):
        return self.leftKey
    
    def setLeftKey(self, key):
        self.leftKey = key