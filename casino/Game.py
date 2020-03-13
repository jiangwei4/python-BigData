
class Game:

    def __init__(self):
        self.niveau = 1
        self.essai = 5
        self.rang = 10

    def addNiveau(self):
        self.niveau = self.niveau + 1

    def getNiveau(self):
        return self.niveau

    def setEssai(self, essai):
        self.essai = essai 

    def getEssai(self):
        return self.essai

    def setRang(self, rang):
        self.rang = rang

    def debut(self,j):
        print('Je suis Python. Quel est votre pseudo ? ')
        joueurName = input()
        j.setName(joueurName)
        print('Hello ', j.name, ', vous avez 10 €, Très bien ! Installez vous SVP à la table de pari.')
        print('Je vous expliquerai le principe du jeu :')
        print('Je viens de penser à un nombre entre 1 et 10. Devinez lequel ?')
        print('Att : vous avez le droit à trois essais !')
        print('Si vous devinez mon nombre dès le premier coup, vous gagnez le double de votre mise !')
        print('Si vous le devinez au 2è coup, vous gagnez la moitiè de votre mise !')
        print('Si vous le devinez au 3è coup, vous perdez votre mise !')
        print('Si vous ne le devinez pas au troisième coup, vous perdez évidemment votre mise et vous avez le droit : ')
        print('- de retenter votre chance avec l\'argent qu\'il vous reste pour reconquérir le level perdu.')
        print('- de quitter le jeu.')
        print('Dès que vous devinez mon nombre et tant que votre solde est positif : vous avez le droit de quitter le jeu et de partir avec vos gains OU de continuer le jeu en passant au level supérieur.')
