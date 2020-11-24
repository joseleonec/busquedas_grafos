import busquedas


def get_graph(file="grafo.txt"):

        from grafo import Grafo
        f = open(file, "r")
        g = Grafo()
        for linea in f:
            if linea[0] != "#":
                aux = linea.split(" ")
                if len(aux) == 2:
                    g.addNodo(aux[0], int(aux[1]))
                elif len(aux) == 3:
                    g.addEdge(aux[0], aux[1], int(aux[2]))
        f.close()
        return g



if __name__ == '__main__':
    g = get_graph("grafo.txt")
    print(g)
    busquedas.hillClimbing(g, "S", "G")
    busquedas.best_first_search(g, "S", "G")
    busquedas.greddy_search(g, "S", "G")
    busquedas.busquedaCostoUniforme(g, "S", "G")
