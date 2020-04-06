
class Vaisseau:
    def __init__(self, config):
        self.img = 'images/vaisseau'
        self.config = config
        self.x=self.config.getSurfaceW()/2-40
        self.y=self.config.getSurfaceH()-40
        self.larg = 40
        self.haut = 40
        self.mouvementSpeed = self.config.getMouvementSpeed()
        self.life = self.config.getLife()
        self.shield = self.config.getShield()
        self.speedshield = self.config.getSpeedShield()
        self.direction = 0 #0haut 2droite 4bas 6gauche

        self.zoneTirx = 0
        self.zoneTiry = 0

    def getZoneTir(self):
        return [self.zoneTirx,self.zoneTiry]

    def getDirection(self):
        return self.direction

    def setDirection(self,da,db,dc,dd):
        if da == db:
            da = 0
            db = 0
        if dc == dd:
            dc = 0
            dd = 0
        
        tmp = [da,dc,db,dd]
        
        if tmp in self.config.getDirecitonPossible():
            self.direction = self.config.getValeurDirection()[self.config.getDirecitonPossible().index(tmp)]

        ##update zoneTir
        
        zoneTir = self.config.getZoneTirPossible()[self.direction]
        self.zoneTirx = zoneTir[0]+self.x
        self.zoneTiry = zoneTir[1]+self.y



    def getImg(self):
        return str(self.img)+str(self.direction)+'.png'

    def setx(self,x):
        if self.x+x > self.config.getMin() and self.x+x < self.config.getSurfaceW()-self.larg:
            self.x += x

    def getx(self):
        return self.x

    def sety(self,y): 
        if self.y+y > self.config.getMin() and self.y+y < self.config.getSurfaceH()-self.haut:
            self.y += y
    
    def gety(self):
        return self.y

    def getMouvementSpeed(self):
        return self.mouvementSpeed

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


    
