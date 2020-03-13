import matplotlib.pyplot as plt
from Api import Api

class Graph:

    def __init__(self):
        self.api = Api()

    def getGraph(self, niveau, essai):
        sets = self.api.get({'niveau':niveau})

        names = []
        values = []

        for ess in range(1, essai + 1):
            names.append(ess)
            count = 0
            for set in sets:
                if set['valeurJouer'] == set['randomOrdi'] and set['essai'] == ess:
                    count += 1
            values.append(count)

        plt.ylabel('Nombre de personne')
        plt.xlabel('Essai')
        plt.bar(names, values)
        plt.suptitle('Réussite par essai')
        plt.show()



    def graphValMoy(self):
        names = []
        results = []

        for i in range(1, 30 + 1):
            names.append(str(i))

        for niveau in range(1,4):
            tab = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
            data = self.api.get({'niveau':niveau})
            
            for dat in data:
                tab[dat['valeurJouer']-1] += 1
            
            results.append(tab)

        plt.ylabel('Nombre de fois jouer')
        plt.xlabel('Valeur')
        plt.plot(names, results[0], label='niveau : 1')
        plt.plot(names, results[1], label='niveau : 2')
        plt.plot(names, results[2], label='niveau : 3')
        plt.legend()

        plt.show()

    def graphFin(self):
        moys = []
        names = []

        for niveau in range(1, 4):
            names.append(str(niveau))

            mises = 0
            gains = 0
            solds = 0

            datas = self.api.getSold({'niveau':niveau})

            for data in datas:
                mises += data['mise']
                gains += data['gain']
                solds += data['sold']

            if len(datas) != 0:
                miseMoy = mises/len(datas)
                gainMoy = gains/len(datas)
                soldMoy = solds/len(datas)
            else:
                miseMoy = 0
                gainMoy = 0
                soldMoy = 0

            moys.append({'miseMoy': miseMoy, 'gainMoy': gainMoy, 'soldMoy': soldMoy})

        valuesMise = []
        valuesGain = []
        valuesSold = []
        for moy in moys:
            valuesMise.append(moy['miseMoy'])
            valuesGain.append(moy['gainMoy'])
            valuesSold.append(moy['soldMoy'])
        
        plt.ylabel('Valeur en €')
        plt.xlabel('Niveau')
        plt.plot(names, valuesMise, label='Mises moyennes')
        plt.plot(names, valuesGain, label='Gains moyens')
        plt.plot(names, valuesSold, label='Soldes moyens')
        plt.legend()

        plt.suptitle('Mises/Gains/Soldes moyen.ne.s par niveau')

        plt.show()
            
