class Nodo(object):

    def __init__(self, nombre, heuristica=0, profundidad=0):
        self.nombre = nombre
        self.nodosAdyacentes = dict()
        self.heuristica = heuristica
        self.profundidad = profundidad

    def addNodoAdyacentes(self, nodo, peso=0):
        self.nodosAdyacentes[nodo.nombre] = peso

    def __ne__(self, other):
        if self.nombre != other.nombre:
            return True
        else:
            return False

    def __lt__(self, other):
        if self.nombre < other.nombre:
            return True
        else:
            return False

    def __gt__(self, other):
        if self.nombre > other.nombre:
            return True
        else:
            return False

    def __eq__(self, other):
        if self.nombre == other.nombre:
            return True
        else:
            return False

    def __str__(self):
        # return self.nombre + ": " + str(self.costo)
        return "(" + self.nombre + ") " + str(self.profundidad)

    def __repr__(self):
        return str(self.nombre)


if __name__ == '__main__':
    n1 = Nodo("n1")
    n2 = Nodo("n2")
    n3 = Nodo("n3")
    n4 = Nodo("n4")
    a = list()
    a.append(n2)
    a.append(n4)
    a.append(n3)
    a.append(n1)
    for i in a:
        print(i)
    a.sort()
    print("----------------------")
    for i in a:
        print(i)
    print(n1 < n2)
