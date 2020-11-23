from grafo import Grafo
from collections import deque
from math import inf
import time


def busquedaAmplitud(grafo: Grafo, nombreNodoInicial: str, nombreBuscado: str = ""):
    cola = list()  # cola para los vertices que se procesan
    cola.append(grafo.nodos[nombreNodoInicial])  # agregar el vertice a la cola

    visitados = list()  # lista para los visitados
    visitados.append(grafo.nodos[nombreNodoInicial])  # agregar el vertice de inicio a los visitados

    camino = list()  # lista para los nodos encontrados
    encontrado = False
    print("-----------------BFS------------------")
    print("Busqueda del nodo: " + nombreBuscado if nombreBuscado else "Recorrido completo")
    while len(cola) > 0 and not encontrado:
        print(cola)
        n = cola.pop(0)
        camino.append(n)
        print("\t" * max(6, len(cola)), "\t", n.nombre)
        if n.nombre != nombreBuscado:
            for na in n.nodosAdyacentes:
                if grafo.nodos[na] not in visitados:
                    cola.append(grafo.nodos[na])
                    visitados.append(grafo.nodos[na])
        else:
            encontrado = True
    if not encontrado:
        print("No existe el nodo ingresado.")


def busquedaAmplitudTodos(grafo, nombreNodoOrigen=None):
    for nodo in grafo.nodos.values():
        if nombreNodoOrigen:
            busquedaAmplitud(grafo, nombreNodoOrigen, nodo.nombre)
        else:
            busquedaAmplitud(grafo, list(grafo.nodos.keys())[0], nodo.nombre)


def busquedaProfundidad(grafo, nombreNodoInicial: str, nombreBuscado: str):
    pila = list()  # pila para los vertices que se procesan
    pila.append(grafo.nodos[nombreNodoInicial])  # agregar el vertice a la pila

    visitados = list()  # lista para los visitados
    visitados.append(grafo.nodos[nombreNodoInicial])  # agregar el vertice de inicio a los visitados

    camino = list()  # lista para los nodos encontrados
    encontrado = False
    print("-----------------DFS------------------")
    print("Busqueda del nodo: " + nombreBuscado if nombreBuscado else "Recorrido completo")
    while len(pila) > 0 and not encontrado:
        print(pila)
        n = pila.pop()
        camino.append(n)
        print("\t" * max(6, len(pila)), "\t", n)
        if n.nombre != nombreBuscado:
            for na in reversed(n.nodosAdyacentes):
                if grafo.nodos[na] not in visitados:
                    pila.append(grafo.nodos[na])
                    visitados.append(grafo.nodos[na])
        else:
            encontrado = True
    if not encontrado:
        print("No existe el nodo ingresado.")
        # print("Camino (" + nombreBuscado + "): ", end="")
        # for i in camino:
        #     print(" -> " + i.nombre, end="")
        # print()
        # else:
        #     print("No existe el nodo ingresado.")


def busquedaProfundidadLimitada(grafo, nombreNodoInicial: str, nombreBuscado: str, limite):
    pila = list()  # pila para los vertices que se procesan
    pila.append(grafo.nodos[nombreNodoInicial])  # agregar el vertice a la pila

    visitados = list()  # lista para los visitados
    visitados.append(grafo.nodos[nombreNodoInicial])  # agregar el vertice de inicio a los visitados

    camino = list()  # lista para los nodos encontrados
    encontrado = False
    print(f"-----------------LDFS------- P = {limite}-----------")
    print("Busqueda del nodo: " + nombreBuscado if nombreBuscado else "Recorrido completo")
    p = -1
    while len(pila) > 0 and not encontrado:
        print(pila)
        n = pila.pop()
        p = n.profundidad
        camino.append(n)
        print("\t" * max(6, len(pila)), "\t", n)
        if n.nombre != nombreBuscado:
            for na in reversed(n.nodosAdyacentes):
                if grafo.nodos[na] not in visitados and grafo.nodos[na].profundidad <= limite:
                    pila.append(grafo.nodos[na])
                    visitados.append(grafo.nodos[na])
        else:
            encontrado = True
    if not encontrado:
        print("No existe el nodo ingresado.")
    return encontrado
    # print("Camino (" + nombreBuscado + "): ", end="")
    # for i in camino:
    #     print(" -> " + i.nombre, end="")
    # print()
    # else:
    #     print("No existe el nodo ingresado.")


def buscarProfundidadTodos(grafo, nombreNodoOrigen=None):
    for nodo in grafo.nodos.values():
        if nombreNodoOrigen:
            busquedaProfundidad(grafo, nombreNodoOrigen, nodo.nombre)
        else:
            busquedaProfundidad(grafo, list(grafo.nodos.keys())[0], nodo.nombre)


def busquedaProfundidadIterativa(grafo, nodoInicial: str, nombreBuscado: str, limiteDeProfundidad=3):
    for i in range(limiteDeProfundidad + 1):
        if busquedaProfundidadLimitada(grafo, nodoInicial, nombreBuscado, i):
            print(f"--------Solucion encontrada en el nivel {i}--------")
            break

def busquedaBidireccional(grafo, nombreNodoInicial: str, nombreBuscado: str):
    if nombreNodoInicial == nombreBuscado:
        print("EL nodo inical es igual al nodo final")
        return
    cola_to_front = list()  # cola para los vertices que se procesan
    cola_to_front.append(grafo.nodos[nombreNodoInicial])  # agregar el vertice a la cola

    cola_to_back = list()  # cola para los vertices que se procesan
    cola_to_back.append(grafo.nodos[nombreBuscado])  # agregar el vertice a la cola

    visitados_to_front = list()  # lista para los visitados
    visitados_to_front.append(grafo.nodos[nombreNodoInicial])  # agregar el vertice de inicio a los visitados

    visitados_to_back = list()  # lista para los visitados
    visitados_to_back.append(grafo.nodos[nombreBuscado])  # agregar el vertice de inicio a los visitados

    camino_tf = list()  # lista para los nodos encontrados
    camino_tb = list()  # lista para los nodos encontrados
    str_tf = ""
    str_tb = ""
    encontrado = False
    print("-----------------Bidirectional Search------------------")
    print("Busqueda del nodo: " + nombreBuscado if nombreBuscado else "Recorrido completo",
          "Desde " + nombreNodoInicial)
    while len(cola_to_front) > 0 and len(cola_to_back) > 0 and not encontrado:
        str_tf += str(cola_to_front) + "\n"
        str_tb += str(cola_to_back) + "\n"
        ntf = cola_to_front.pop(0)
        ntb = cola_to_back.pop(0)
        camino_tf.append(ntf)
        camino_tb.append(ntb)
        str_tf += ("\t" * max(6, len(cola_to_front))) + "\t" + str(ntf) + "\n"
        str_tb += ("\t" * max(6, len(cola_to_back))) + "\t" + str(ntb) + "\n"
        if ntb.nombre == ntf.nombre:
            print("Busqueda hacia adelante \n" + str_tf)
            print("Busqueda hacia atras \n" + str_tb)
            encontrado = True
            break
        else:
            for natf in ntf.nodosAdyacentes.keys():
                if grafo.nodos[natf] not in visitados_to_front:
                    cola_to_front.append(grafo.nodos[natf])
                    visitados_to_front.append(grafo.nodos[natf])
            for natb in ntb.nodosAdyacentes.keys():
                if grafo.nodos[natb] not in visitados_to_back:
                    cola_to_back.append(grafo.nodos[natb])
                    visitados_to_back.append(grafo.nodos[natb])
    if not encontrado:
        print("No existe el nodo ingresado.")


def busquedaCostoUniforme(grafo, nombreNodoInicial, nombreBuscado):
    visitados = set()
    cola = list()
    cola.append((0, nombreNodoInicial, None))
    print("-----------------UCS------------------")
    print("Busqueda del nodo: " + nombreBuscado if nombreBuscado else "Recorrido completo")
    camino = list()
    camino.append((0, nombreNodoInicial, None))
    while len(cola) > 0:
        cola.sort()
        for i in range(len(cola)):
            print(cola[i], end=" ")
        print()
        costo, nodo_actual, padre = cola.pop(0)
        print("\t" * max(10, 6 * len(cola)), nodo_actual, costo)
        if nodo_actual not in visitados:
            visitados.add(nodo_actual)
            if nodo_actual == nombreBuscado:
                get_path(grafo, camino, nodo_actual, padre)
                return
            for i in grafo.nodos[nodo_actual].nodosAdyacentes:
                if i not in visitados:
                    total_cost = costo + grafo.aristas[(nodo_actual, i)]
                    cola.append((total_cost, i, nodo_actual))
                    camino.append((total_cost, i, nodo_actual))
    print("No se a encontrado el nodo")


def get_path(grafo, vistados, nodo_actual, p):
    l = [nodo_actual, p]
    while p:
        for i in vistados:
            if i[1] == p:
                if i[2]:
                    l.append(i[2])
                p = i[2]
                vistados.pop(vistados.index(i))
                break
    print("Ruta: " + str(list(reversed(l))))
    l = list(reversed(l))
    costo = 0
    for i in range(len(l) - 1):
        costo += grafo.nodos[l[i]].nodosAdyacentes[l[i + 1]]
    print("Costo: " + str(costo))


def busquedaCostoUniformeTodos(grafo, nombreNodoOrigen=None):
    for nodo in grafo.nodos.values():
        if nombreNodoOrigen:
            busquedaCostoUniforme(grafo, nombreNodoOrigen, nodo.nombre)
        else:
            busquedaCostoUniforme(grafo, list(grafo.nodos.keys())[0], nodo.nombre)


def hillClimbing(grafo: Grafo, nombreNodoInicial: str, nombreBuscado: str):
    if nombreNodoInicial == nombreBuscado:
        return
    max_iterations = 1000
    nodo_actual = grafo.nodos[nombreNodoInicial]
    id_mejor = nodo_actual.nombre
    c = 0
    camino = list()
    camino.append(nombreNodoInicial)
    print("-----------------Hill Climbing Search------------------")
    while c <= max_iterations:
        h_mejor = nodo_actual.heuristica
        # h_mejor = inf
        if (ids_nodosAdyacentes := nodo_actual.nodosAdyacentes.keys()):
            for id_nodo in ids_nodosAdyacentes:
                h_actual = grafo.nodos[id_nodo].heuristica
                if h_actual < h_mejor:
                    h_mejor = h_actual
                    id_mejor = id_nodo
            if h_mejor == nodo_actual.heuristica:
                c += 1
            if id_mejor != nodo_actual.nombre:
                nodo_actual = grafo.nodos[id_mejor]
                camino.append(id_mejor)
            if h_mejor == 0:
                print("Encontrado")
                for i in camino:
                    print(i + " -> " if camino.index(i) != len(camino) - 1 else str(i), end=" ")
                print()
                break
        else:
            print("No se ha encontrado la solucion")
            break
    if c >= max_iterations:
        print("No se ha encontrado la solucion")
        print("Se ha llegado al numero maximo de iteraciones")
        print("el camino ha sido: " + str(camino))
        print("Mejor valor encontrado:", h_mejor)


def colina(grafo: Grafo, nombreNodoInicial: str, nombreBuscado: str):
    if nombreNodoInicial == nombreBuscado:
        return
    max_iterations = 1000
    visitados = list()
    nodo_actual = grafo.nodos[nombreNodoInicial]
    visitados.append(nodo_actual.nombre)
    id_mejor = nodo_actual.nombre
    c = 0
    camino = list()
    camino.append(nombreNodoInicial)
    while c <= max_iterations:
        h_mejor = nodo_actual.heuristica
        # h_mejor = inf
        # print(h_mejor, end=" ")
        if (ids_nodosAdyacentes := nodo_actual.nodosAdyacentes.keys()):
            # print(ids_nodosAdyacentes)
            for id_nodo in ids_nodosAdyacentes:
                h_actual = grafo.nodos[id_nodo].heuristica
                if id_nodo not in visitados:
                    visitados.append(id_nodo)
                    if h_actual < h_mejor:
                        h_mejor = h_actual
                        id_mejor = id_nodo
            # print(nodo_actual.nombre, id_mejor)
            # print(visitados)
            if h_mejor == nodo_actual.heuristica:
                c += 1
            if id_mejor != nodo_actual.nombre:
                nodo_actual = grafo.nodos[id_mejor]
                camino.append(id_mejor)

            if h_mejor == 0:
                print("Encontrado")
                for i in camino:
                    print(i + " -> " if camino.index(i) != len(camino) - 1 else str(i), end=" ")
                break
        else:
            print("No se ha encontrado la solucion")
            break
    if c >= max_iterations:
        print("No se ha encontrado la solucion")
        print("Se ha llegado al numero maximo de iteraciones")
        print("el camino ha sido: " + str(camino))
        print("Mejor valor encontrado:", h_mejor)


def best_first_search(graph: Grafo, nombreNodoInicial: str, nombreBuscado: str):
    pq = list()
    pq.append((0, graph.nodos[nombreNodoInicial]))
    visitados = list()
    visitados.append(nombreNodoInicial)
    print("-----------------Best First Search------------------")
    while len(pq) > 0:
        pq.sort()
        print(list(pq))
        nodo_actual = pq.pop(0)[1]
        # Displaying the path having lowest cost
        print("\t" * max(len(pq), 10), nodo_actual)
        if nodo_actual.nombre == nombreBuscado:
            break
        for v in graph.nodos[nodo_actual.nombre].nodosAdyacentes.keys():
            if v not in visitados:
                visitados.append(v)
                aux = graph.nodos[v]
                pq.append((aux.heuristica, aux))
    # print(visitados)


def a_star(grafo: Grafo, nombreNodoInicial: str, nombreBuscado: str):
    visitados = set()
    cola = list()
    cola.append((0, grafo.nodos[nombreNodoInicial].heuristica, nombreNodoInicial, None))
    print("----------------- A* ------------------")
    print("Busqueda del nodo: " + nombreBuscado if nombreBuscado else "Recorrido completo")
    camino = list()
    camino.append((0, nombreNodoInicial, None))
    while len(cola) > 0:
        cola.sort()
        for i in range(len(cola)):
            print(cola[i], end=" ")
        print()
        costo, _, nodo_actual, padre = cola.pop(0)
        print("\t" * max(10, 6 * len(cola)), nodo_actual, costo)
        if nodo_actual not in visitados:
            visitados.add(nodo_actual)
            if nodo_actual == nombreBuscado:
                get_path(grafo, camino, nodo_actual, padre)
                return
            for i in grafo.nodos[nodo_actual].nodosAdyacentes:
                if i not in visitados:
                    path_cost = costo + grafo.aristas[(nodo_actual, i)]
                    f = path_cost + grafo.nodos[i].heuristica
                    cola.append((path_cost, f, i, nodo_actual))
                    camino.append((path_cost, i, nodo_actual))
    print("No se a encontrado el nodo")


def greddy_search(graph: Grafo, source: str, nombreBuscado: str):
    pq = list()
    pq.append((0, graph.nodos[source]))
    visitados = list()
    visitados.append(source)
    print("-----------------Greedy Search------------------")
    while len(pq) > 0:
        pq.sort()
        print(list(pq))
        nodo_actual = pq.pop(0)[1]
        # Displaying the path having lowest cost
        print("\t" * max(len(pq), 10), nodo_actual)
        if nodo_actual.nombre == nombreBuscado:
            break
        for v in graph.nodos[nodo_actual.nombre].nodosAdyacentes.keys():
            if v not in visitados:
                visitados.append(v)
                aux = graph.nodos[v]
                pq.append((aux.heuristica, aux))
    # print(visitados)
