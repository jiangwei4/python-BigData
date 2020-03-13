import matplotlib.pyplot as plt
from Api import Api

class Graph:

    def __init__(self):
        self.api = Api()

    def getGraph(self, niveau, essai):
        sets = self.api.get({'niveau':niveau})
        print(sets)

        names = []
        values = []

        for ess in range(1, essai + 1):
            names.append(ess)
            count = 0
            for set in sets:
                if set['valeurJouer'] == set['randomOrdi'] and set['essai'] == ess:
                    count += 1
            values.append(count)


        plt.figure(figsize=(9, 3))

        plt.bar(names, values)
        plt.suptitle('Nombre de réussite')
        plt.show()



        def graphValMoy(self):
            
            for niveau in range(0,4):
                tab = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
                data = self.api.get({'niveau':niveau})
                for dat in data:
                    tab[dat.valeurJouer] += 1
                
                plt.bar('niveau : '+str(niveau), tab)
                plt.suptitle('valeur choisi')
                plt.show()
            
