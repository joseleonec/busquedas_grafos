class Nodo(object):

    def __init__(self, nombre, costo=0):
        self.nombre = nombre
        self.nodosAdyacentes = list()
        self.costo = costo

    def addNodoAdyacentes(self, nodo):
        self.nodosAdyacentes.append(nodo)

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
        return self.nombre + ": " + str(self.costo)


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
