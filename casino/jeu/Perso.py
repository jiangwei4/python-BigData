class Perso: 
    def __init__(self):
        self.sold = 10
        self.essai = 0

    def setName(self,name):
        self.name = name

    def getSold(self):
        return self.sold

    def setSold(self,sold):
        self.sold = sold

    def getEssai(self):
        return self.essai
    
    def setEssai(self,essai):
        self.essai = essai
    
    def getName(self):
        return self.name

    def getMise(self):
        return self.mise

    def setMise(self):
        joueurMise = int(input())
        while(type(joueurMise) != int or joueurMise < 1 or joueurMise > self.sold ):
            print('Le montant saisi n\'est pas valide. Entrer SVP un montant entre 1 et ',self.sold,' € :  ?')
            joueurMise = int(input())
        self.mise = joueurMise

    def getNombreDeviner(self):
        return self.nombre 
    
    def setNombreDeviner(self):
        joueurDevineNombre = int(input())
        while(type(joueurDevineNombre) != int or joueurDevineNombre < 0):
            print('Je ne comprends pas votre nombre. Entrez SVP un nombre entier :  ?')
            joueurDevineNombre = int(input())
        self.nombre = joueurDevineNombre

    def getContinuer(self):
        return self.continuer

    def setContinuer(self):
        print('Souhaitez-vous continuer la partie (O/N) ?')
        joueurContinue = input()
        while( joueurContinue != "o" and joueurContinue != "n" ):
            print('Je ne comprends pas votre réponse. Souhaitez-vous continuer la partie (O/N) ?')
            joueurContinue = input()
        self.continuer = joueurContinue