from nodo import Nodo


class Arista():

    def __init__(self, nodoOrigen: Nodo, nodoDestino: Nodo, peso):
        self.nodoOrigen = nodoOrigen
        self.nodoDestino = nodoDestino
        self.peso = peso

    def __str__(self):
        return "  (" + self.nodoOrigen.nombre + ") ---" +str(self.peso)+ "--- (" + self.nodoDestino.nombre + ")  "
