def get_graph(file="grafo.txt"):
    try:
        from grafo import Grafo
        f = open(file, "r")
        g = Grafo()
        for linea in f:
            if linea[0] != "#":
                aux = linea.split(" ")
                if len(aux) == 2:
                    g.addNodo(aux[0], aux[1])
                elif len(aux) == 3:
                    g.addEdge(aux[0], aux[1], aux[2])
        f.close()
        return g
    except:
        return None


if __name__ == '__main__':
    print(get_graph("graf.txt"))
