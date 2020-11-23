from busquedas import *
import time
if __name__ == '__main__':
    cities = Grafo()
    initialStateAdjacencyList = {"Arad": {"Zerind": 75, "Timisoara": 118, "Sibiu": 140},
                                 "Zerind": {"Oradea": 71, "Arad": 75},
                                 "Timisoara": {"Arad": 118, "Lugoj": 111},
                                 "Sibiu": {"Arad": 140, "Oradea": 151, "Fagaras": 99, "Rimnicu Vilcea": 80},
                                 "Oradea": {"Sibiu": 151, "Zerind": 71},
                                 "Lugoj": {"Timisoara": 111, "Mehadia": 70},
                                 "Fagaras": {"Sibiu": 99, "Bucharest": 211},
                                 "Rimnicu Vilcea": {"Sibiu": 80, "Pitesti": 97, "Craiova": 146},
                                 "Mehadia": {"Lugoj": 70, "Dobreta": 75},
                                 "Dobreta": {"Mehadia": 75, "Craiova": 120},
                                 "Craiova": {"Dobreta": 120, "Rimnicu Vilcea": 146, "Pitesti": 138},
                                 "Pitesti": {"Rimnicu Vilcea": 97, "Craiova": 138, "Bucharest": 101},
                                 "Bucharest": {"Fagaras": 211, "Pitesti": 101, "Giurgiu": 90},
                                 "Giurgiu": {"Bucharest": 90}}
    initialStateHeuristics = {"Arad": 366, "Zerind": 374, "Timisoara": 329, "Sibiu": 253,
                              "Oradea": 380,
                              "Lugoj": 244, "Fagaras": 178, "Rimnicu Vilcea": 193, "Mehadia": 241,
                              "Dobreta": 242,
                              "Craiova": 160, "Pitesti": 98, "Bucharest": 0, "Giurgiu": 77}
    for k in initialStateHeuristics:
        cities.addNodo(k, initialStateHeuristics[k])
    cities.graph_from_dict(initialStateAdjacencyList)
    cities.asignarProfundidad("Arad")
    print(cities)
    start_time = time.time()
    busquedaAmplitud(cities, "Arad", "Bucharest")
    print("--- %s milisegundos ---" % ((time.time() - start_time)*1000))
    start_time = time.time()
    busquedaProfundidad(cities, "Arad", "Bucharest")
    print("--- %s milisegundos ---" % ((time.time() - start_time)*1000))
    start_time = time.time()
    busquedaProfundidadIterativa(cities, "Arad", "Bucharest", 5)
    print("--- %s milisegundos ---" % ((time.time() - start_time)*1000))
    start_time = time.time()
    best_first_search(cities, "Arad", "Bucharest")
    print("--- %s milisegundos ---" % ((time.time() - start_time)*1000))
    start_time = time.time()
    busquedaBidireccional(cities, "Arad", "Bucharest")
    print("--- %s milisegundos ---" % ((time.time() - start_time)*1000))
    start_time = time.time()
    busquedaCostoUniforme(cities, "Arad", "Bucharest")
    print("--- %s milisegundos ---" % ((time.time() - start_time)*1000))
    start_time = time.time()
    hillClimbing(cities, "Arad", "Bucharest")
    print("--- %s milisegundos ---" % ((time.time() - start_time)*1000))
    start_time = time.time()
    best_first_search(cities, "Arad", "Bucharest")
    print("--- %s milisegundos ---" % ((time.time() - start_time)*1000))
    start_time = time.time()
    a_star(cities, "Arad", "Bucharest")
    print("--- %s milisegundos ---" % ((time.time() - start_time)*1000))
    start_time = time.time()
    greddy_search(cities, "Arad", "Bucharest")
    print("--- %s milisegundos ---" % ((time.time() - start_time)*1000))


    g4 = Grafo()
    g4.addEdge("S", "A", 5, False, inf, 10, 8)
    g4.addEdge("S", "B", 9, False, inf, 10, 7)
    g4.addEdge("A", "B", 3, True, 2, 8, 7)
    g4.addEdge("A", "I", 9, False, inf, 8, 18)
    g4.addEdge("B", "C", 1, False, inf, 7, 10)
    g4.addEdge("C", "S", 6, False, inf, 10, 10)
    g4.addEdge("C", "F", 7, False, inf, 10, 15)
    g4.addEdge("C", "H", 5, False, inf, 10, 28)
    g4.addEdge("D", "S", 1, True, 6, 15, 10)
    g4.addEdge("D", "C", 2, False, inf, 15, 10)
    g4.addEdge("D", "E", 2, False, inf, 15, 25)
    g4.addEdge("E", "G", 7, False, inf, 25, 0)
    g4.addEdge("F", "D", 2, False, inf, 15, 15)
    g4.addEdge("F", "G", 8, False, inf, 15, 0)
    # g4.asignarProfundidad("S")
    # print(g4)
    # busquedaProfundidad(g4, "S", "G")
    # busquedaProfundidadIterativa(g4, "S", "G",3)
    # best_search(g4, "S", "G")
    # hillClimbing(g4, "S", "G")

    g3 = Grafo()
    g3.addEdge("A", "B", 0, True, 0)
    g3.addEdge("A", "C", 0, True, 0)
    g3.addEdge("A", "D", 0, True, 0)
    g3.addEdge("B", "E", 0, True, 0)
    g3.addEdge("B", "F", 0, True, 0)
    g3.addEdge("D", "G", 0, True, 0)
    g3.addEdge("D", "H", 0, True, 0)
    g3.addEdge("G", "I", 0, True, 0)
    g3.addEdge("I", "J", 0, True, 0)
    # print(g3)
    # busquedaBidireccional(g3, "A", "J")
    # busquedaProfundidadIterativa(g3, "A", "J")
    g = Grafo()
    g.addNodo("I")
    g.addNodo("A")
    g.addNodo("B")
    g.addNodo("C")
    g.addNodo("M")
    g.addEdge("I", "A", 1)
    g.addEdge("I", "B", 5)
    g.addEdge("I", "C", 15)
    g.addEdge("A", "M", 10)
    g.addEdge("B", "M", 5)
    g.addEdge("C", "M", 5)
    # g.busquedaCostoUniforme("I", "M")
    # busquedaCostoUniformeTodos(g)
    # print(str(g))

    grafo = Grafo()
    grafo.addNodo("S", 7)
    grafo.addNodo("A", 9)
    grafo.addNodo("B", 4)
    grafo.addNodo("C", 2)
    grafo.addNodo("E", 3)
    grafo.addNodo("D", 5)
    grafo.addNodo("G", 0)
    grafo.addEdge("A", "B")
    grafo.addEdge("A", "G")
    grafo.addEdge("B", "E")
    grafo.addEdge("B", "C")
    grafo.addEdge("C", "G")
    grafo.addEdge("D", "B")
    grafo.addEdge("D", "E")
    grafo.addEdge("E", "G")
    grafo.addEdge("S", "A")
    grafo.addEdge("S", "D")
    # print(grafo)
    # hillClimbing(grafo, "S", "G")
    # grafo.busquedaAmplitud(grafo.nodos[0], "n6")
    # grafo.busquedaAmplitudTodos()
    # grafo.busquedaProfundidad(grafo.nodos[0], "n6")
    # grafo.buscarProfundidadTodos()
    # g.busquedaCostoUniformeTodos()
