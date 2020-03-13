from Game import Game
from Perso import Perso
import random
from ThreadGame import ThreadGame
import sys
from Api import Api
from Graph import Graph

class Jeu:
    def __init__(self):
        self.g = Game()
        self.j = Perso()
        self.g.debut(self.j)
        self.api = Api()
        self.graph = Graph()
        self.jouer()
#g.jouer()

    def jouer(self):
        if(self.g.getNiveau() >= 4):
            print('Bravo vous avez réussi à finir le jeu') 
            ### graph fin
            self.graph.graphFin()
            ###
            sys.exit()
        else:
            print('Le jeu commence, entrez votre mise : ?')
            while(self.j.getSold() > 0):
                self.j.setMise()
                resultat = self.lancerPartie()
                self.j.setSold(self.j.getSold() + resultat[0])
                self.api.postSold({'name':self.j.name,'niveau':self.g.getNiveau(),'sold':self.j.getSold(),'mise':self.j.getMise(),'gain':resultat[0]}) 
                ##Les statistiques du level 
                self.graph.getGraph(self.g.getNiveau(), self.g.getEssai())
                ###
                if(resultat[1] < self.g.essai):
                    print('Bingo ', self.j.name, ', vous avez gagné en "',resultat[1],'" coup(s) et vous avez emporté "',resultat[0],'" € !')
                    print('Souhaitez-vous continuer la partie (o/n) ?')
                    self.j.setContinuer()
                    if(self.j.getContinuer() == 'o'):
                        self.g.addNiveau()
                        print('Super ! Vous passez au Level ',self.g.getNiveau(),'.')
                        print('Rappelez vous, le principe est le même sauf que mon nombre est maintenant entre 1 et ',self.g.getNiveau()*10,' !')
                        self.j.setEssai(0)
                        self.jouer()
                    else:
                        print('Au revoir ! Vous finissez la partie avec "',self.j.getSold(),'" €')
                        ### graph fin
                        self.graph.graphFin()
                        ###
                        sys.exit()
                if(self.j.getSold() <= 0):
                    print('Votre solde est null') 
            
    def lancerPartie(self):
        nombreRandom = random.randint(1, self.g.rang)
        print(' Alors mon nombre est : ?')
        print(nombreRandom)
        while(self.j.getEssai() < self.g.essai):
            t1 = ThreadGame() 
            t1.setInformations(self.g.getEssai(), self.j)
            t1.start() 
            self.j.setNombreDeviner()
            
            if not(t1.stopped()):
                self.api.post({'name':self.j.name,'valeurJouer':self.j.getNombreDeviner(),'niveau':self.g.getNiveau(),'essai':self.j.getEssai()+1,'randomOrdi':nombreRandom})
                if(self.j.getNombreDeviner() == nombreRandom):
                    if(self.j.getEssai() == 0):
                        t1.stop() 
                        return [2*self.j.getMise(),1]
                    if(self.j.getEssai() == 1):
                        t1.stop() 
                        return [self.j.getMise()/2,2]
                    if(self.j.getEssai() > 1):
                        t1.stop() 
                        return [-self.j.getMise(),3]
                if(self.j.getNombreDeviner() > nombreRandom):
                    print('Votre nbre est trop grand !')
                    self.j.setEssai(self.j.getEssai()+1)
                if(self.j.getNombreDeviner() < nombreRandom):
                    print('Votre nbre est trop petit !')
                    self.j.setEssai(self.j.getEssai()+1)
                if(self.j.getEssai() == self.g.essai - 1):
                    print('Il vous reste une chance !')
                if(self.j.getEssai() == self.g.essai):
                    print('Vous avez perdu ! Mon nombre est "',nombreRandom,'" !')
                    t1.stop() 
                    return [-self.j.getMise(),self.j.getEssai()]
                t1.stop() 

jeu = Jeu()
