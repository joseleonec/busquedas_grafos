from pip._internal.cli.cmdoptions import abi

from nodo import Nodo


class Grafo():

    def __init__(self):
        self.contadorNodos = 0
        self.nodos = dict()
        self.aristas = dict()
        self.profundidad = 0
        # self.matriz = [[None] * 0 for i in range(0)]

    def graph_from_dict(self, dic):
        for k, v in dic.items():
            for ka, g in v.items():
                self.addEdge(k, ka, g, False, 0, 0, 0)

    def addNodo(self, nombre: str, heuristica=0):
        if not nombre in self.nodos:
            self.nodos[nombre] = Nodo(nombre, heuristica=heuristica)
            self.contadorNodos += 1

    def addEdge(self, nodoOrigen: str, nodoDestino: str, peso1=0, bidireccional=False, peso2=0, h1=0, h2=0):

        if nodoOrigen in self.nodos and nodoDestino in self.nodos:
            n1 = self.nodos[nodoOrigen]
            n2 = self.nodos[nodoDestino]
            if h1 != 0:
                n1.heuristica = h1
            if h2 != 0:
                n2.heuristica = h2
            n2.profundidad = n1.profundidad + 1
            n1.addNodoAdyacentes(n2, peso1)
            self.aristas[(nodoOrigen, nodoDestino)] = peso1
            if bidireccional:
                n2.addNodoAdyacentes(n1, peso2)
                self.aristas[(nodoDestino, nodoOrigen)] = peso2
        else:
            n1 = None
            n2 = None
            if not nodoOrigen in self.nodos:
                n1 = Nodo(nodoOrigen, h1)
            if not nodoDestino in self.nodos:
                n2 = Nodo(nodoDestino, h2)
            if not n1:
                n1 = self.nodos[nodoOrigen]
            if not n2:
                n2 = self.nodos[nodoDestino]
            if n1 and n2:
                if h1 != 0:
                    n1.heuristica = h1
                if h2 != 0:
                    n2.heuristica = h2
                self.nodos[nodoOrigen] = n1
                self.nodos[nodoDestino] = n2
                n1.addNodoAdyacentes(n2, peso1)
                self.aristas[(nodoOrigen, nodoDestino)] = peso1
                if bidireccional:
                    n2.addNodoAdyacentes(n1, peso2)
                    self.aristas[(nodoDestino, nodoOrigen)] = peso2

    def asignarProfundidad(self, root: str):
        visitados = list()
        self.nodos[root].profundidad = 0

        cola = list()
        cola.append(self.nodos[root])
        visitados.append(root)
        while len(cola) > 0:
            nodo = cola.pop(0)
            p = nodo.profundidad
            for k in nodo.nodosAdyacentes.keys():
                if k not in visitados:
                    na = self.nodos[k]
                    na.profundidad = p + 1
                    if na.profundidad > self.profundidad:
                        self.profundidad = na.profundidad
                    cola.append(na)
                    visitados.append(k)

    def __str__(self):
        s = ""
        for key in self.nodos:
            n = self.nodos[key]
            s += (str(n) + ": " if n else " ")
            s += str(list(n.nodosAdyacentes.keys())) + "\n" if len(n.nodosAdyacentes) else "\n"
        return s
