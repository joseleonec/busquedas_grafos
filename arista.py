from nodo import Nodo


class Arista():

    def __init__(self, nodoOrigen: Nodo, nodoDestino: Nodo, peso=0):
        self.nodoOrigen = nodoOrigen
        self.nodoDestino = nodoDestino
        self.peso = peso

    def __str__(self):
        return "  (" + self.nodoOrigen.nombre + ") ---" + str(self.peso) + "---> (" + self.nodoDestino.nombre + ")  "

    def __repr__(self):
        return str(self)

    def __eq__(self, other):
        return self.nodoDestino == other.nodoDestino and self.nodoOrigen == other.nodoOrigen and self.peso == other.peso
