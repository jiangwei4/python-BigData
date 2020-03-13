import matplotlib.pyplot as plt
from Api import Api

class Graph:

    def __init__(self):
        self.api = Api()

    def getGraph(self, niveau):
        self.api.get(1)
        plt.plot([1, 2, 3, 4])
        plt.ylabel('some numbers')
        plt.show()