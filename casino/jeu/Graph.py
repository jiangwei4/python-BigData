import matplotlib.pyplot as plt
from Api import Api

class Graph:

    def __init__(self):
        self.api = Api()

    def getGraph(self, niveau):
        print(self.api.get({'niveau': niveau}))
        plt.plot([1, 2, 3, 4])
        plt.ylabel('some numbers')
        plt.show()