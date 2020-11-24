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
            for na in sorted(n.nodosAdyacentes.keys()):
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
            for na in sorted(n.nodosAdyacentes, reverse=True):
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
            for na in sorted(n.nodosAdyacentes, reverse=True):
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


def busquedaProfundidadIterativa(grafo, nodoInicial: str, nombreBuscado: str, limiteDeProfundidad=100):
    for i in range(limiteDeProfundidad + 1):
        if busquedaProfundidadLimitada(grafo, nodoInicial, nombreBuscado, i):
            print(f"--------Solucion encontrada en el nivel {i}--------")
            break


def Bidirectional_Search_visit(grafo: Grafo, nombreNodoInicial: str, nombreBuscado: str):
    collisionChecker = False
    q1 = list()  # cola para los vertices que se procesan
    q1.append(grafo.nodos[nombreNodoInicial])  # agregar el vertice a la cola

    q2 = list()  # cola para los vertices que se procesan
    q2.append(grafo.nodos[nombreBuscado])  # agregar el vertice a la cola

    visitados_1 = list()  # lista para los visitados
    # visitados_1.append(grafo.nodos[nombreNodoInicial])  # agregar el vertice de inicio a los visitados

    visitados_2 = list()  # lista para los visitados
    # visitados_2.append(grafo.nodos[nombreBuscado])  # agregar el vertice de inicio a los visitados
    str_tf = ""
    str_tb = ""
    while len(q1) > 0 and len(q2) > 0 and not collisionChecker:
        str_tf += str(q1) + "\n"
        str_tb += str(q2) + "\n"
        ntf = q1.pop(0)
        ntb = q2.pop(0)
        visitados_1.append(ntf)
        visitados_2.append(ntb)
        str_tf += ("\t" * max(6, len(q1))) + "\t" + str(ntf) + "\n"
        str_tb += ("\t" * max(6, len(q2))) + "\t" + str(ntb) + "\n"
        for i in ntf.nodosAdyacentes.keys():
            if grafo.nodos[i] not in visitados_2:
                q1.append(grafo.nodos[i])
                visitados_1.append(grafo.nodos[i])

        for i in ntb.nodosAdyacentes.keys():
            if grafo.nodos[i] not in visitados_2:
                q2.append(grafo.nodos[i])
                visitados_2.append(grafo.nodos[i])
                # visited_node_for_desti[dCounter + +] = city_list[i]

        # after finding each neighbors road of a city, check for collision
        if ntf in visitados_2:
            collisionNode = ntf
            collisionChecker = True
            print("Busqueda hacia adelante \n" + str_tf)
            print("Busqueda hacia atras \n" + str_tb)
            print("Choque en: " + str(collisionNode))
            break
        elif ntb in visitados_1:
            collisionNode = ntb
            # System.out.prln("Found collision at " + visited_node_for_start[i])
            collisionChecker = True
            print("Busqueda hacia adelante \n" + str_tf)
            print("Busqueda hacia atras \n" + str_tb)
            print("Choque en: " + str(collisionNode))
            break


def busquedaBidireccional(grafo, nombreNodoInicial: str, nombreBuscado: str):
    if nombreNodoInicial == nombreBuscado:
        print("EL nodo inical es igual al nodo final")
        return
    q1 = list()  # cola para los vertices que se procesan
    q1.append(grafo.nodos[nombreNodoInicial])  # agregar el vertice a la cola

    q2 = list()  # cola para los vertices que se procesan
    q2.append(grafo.nodos[nombreBuscado])  # agregar el vertice a la cola

    visitados_1 = list()  # lista para los visitados
    visitados_1.append(grafo.nodos[nombreNodoInicial])  # agregar el vertice de inicio a los visitados

    visitados_2 = list()  # lista para los visitados
    visitados_2.append(grafo.nodos[nombreBuscado])  # agregar el vertice de inicio a los visitados

    camino_tf = list()  # lista para los nodos encontrados
    camino_tb = list()  # lista para los nodos encontrados
    str_tf = ""
    str_tb = ""
    encontrado = False
    print("-----------------Bidirectional Search------------------")
    print("Busqueda del nodo: " + nombreBuscado if nombreBuscado else "Recorrido completo",
          "Desde " + nombreNodoInicial)
    while len(q1) > 0 and len(q2) > 0 and not encontrado:
        str_tf += str(q1) + "\n"
        str_tb += str(q2) + "\n"
        ntf = q1.pop(0)
        ntb = q2.pop(0)
        # visitados_1.append(ntf)
        # visitados_2.append(ntb)
        camino_tf.append(ntf)
        camino_tb.append(ntb)
        str_tf += ("\t" * max(6, len(q1))) + "\t" + str(ntf) + "\n"
        str_tb += ("\t" * max(6, len(q2))) + "\t" + str(ntb) + "\n"
        if ntb.nombre == ntf.nombre:
            print("Busqueda hacia adelante \n" + str_tf)
            print("Busqueda hacia atras \n" + str_tb)
            encontrado = True
            break
        else:
            for natf in ntf.nodosAdyacentes.keys():
                if grafo.nodos[natf] not in visitados_1:
                    q1.append(grafo.nodos[natf])
                    visitados_1.append(grafo.nodos[natf])
            for natb in ntb.nodosAdyacentes.keys():
                if grafo.nodos[natb] not in visitados_2:
                    q2.append(grafo.nodos[natb])
                    visitados_2.append(grafo.nodos[natb])
    if not encontrado:
        print("No existe el nodo ingresado.")


# def busquedaBidireccional(grafo, nombreNodoInicial: str, nombreBuscado: str):
#     if nombreNodoInicial == nombreBuscado:
#         print("EL nodo inical es igual al nodo final")
#         return
#     Q_i = list()  # cola para los vertices que se procesan
#     Q_i.append(grafo.nodos[nombreNodoInicial])  # agregar el vertice a la cola
#     t_i = list()
#     t_g = list()
#     Q_g = list()  # cola para los vertices que se procesan
#     Q_g.append(grafo.nodos[nombreBuscado])  # agregar el vertice a la cola
#
#     visitados_i = list()  # lista para los visitados
#     visitados_i.append(grafo.nodos[nombreNodoInicial])  # agregar el vertice de inicio a los visitados
#
#     visitados_g = list()
#     visitados_g.append(grafo.nodos[nombreBuscado])  # agregar el vertice de inicio a los visitados
#
#     camino_tf = list()  # lista para los nodos encontrados
#     camino_tb = list()  # lista para los nodos encontrados
#     str_tf = ""
#     str_tb = ""
#     encontrado = False
#     print("-----------------Bidirectional Search------------------")
#     print("Busqueda del nodo: " + nombreBuscado if nombreBuscado else "Recorrido completo",
#           "Desde " + nombreNodoInicial)
#     while len(Q_i) > 0 and len(Q_g) > 0 and not encontrado:
#         if len(Q_i) > 0:
#             str_tf += str(Q_i) + "\n"
#             nodo_actual = Q_i.pop(0)
#             camino_tf.append(nodo_actual)
#             str_tf += ("\t" * max(6, len(Q_i))) + "\t" + str(nodo_actual) + "\n"
#             if nodo_actual not in visitados_i:
#                 visitados_i.append(nodo_actual)
#                 if nodo_actual.nombre == nombreBuscado or nodo_actual in t_g:
#                     while len(Q_g) > 0:
#                         nodo = Q_g.pop(0)
#                         if nodo == nodo_actual:
#                             print("Busqueda hacia adelante \n" + str_tf)
#                             encontrado = True
#                             break
#                     if encontrado:
#                         break
#                 for sucesor in grafo.nodos[nodo_actual.nombre].nodosAdyacentes.keys():
#                     nodo_sucesor = grafo.nodos[sucesor]
#                     Q_i.append(nodo_sucesor)
#                     t_i.append(nodo_sucesor)
#         if len(Q_g) > 0:
#             str_tb += str(Q_g) + "\n"
#             nodo_actual = Q_g.pop(0)
#             camino_tb.append(nodo_actual)
#             str_tb += ("\t" * max(6, len(Q_g))) + "\t" + str(nodo_actual) + "\n"
#             if nodo_actual not in visitados_g:
#                 visitados_g.append(nodo_actual)
#                 if nodo_actual in t_i:
#                     while len(Q_i) > 0:
#                         nodo = Q_i.pop(0)
#                         if nodo == nodo_actual:
#                             print("Busqueda hacia adelante \n" + str_tb)
#                             encontrado = True
#                             break
#                     if encontrado:
#                         break
#                 for sucesor in grafo.nodos[nodo_actual.nombre].nodosAdyacentes.keys():
#                     nodo_sucesor = grafo.nodos[sucesor]
#                     Q_g.append(nodo_sucesor)
#                     t_g.append(nodo_sucesor)
#     if not encontrado:
#         print("No existe el nodo ingresado.")
#

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
                print("Costo:", costo)
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
    # for i in range(len(l) - 1):
    #     costo += grafo.nodos[l[i]].nodosAdyacentes[l[i + 1]]
    # print("Costo: " + str(costo))


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
    ids_nodosAdyacentes = [nombreNodoInicial]
    print("\t" * 5 + "|", [(str(i) + ":" + str(grafo.nodos[i].heuristica)) for i in ids_nodosAdyacentes])
    print(nodo_actual.nombre, "\t" * 4 + "|")
    while c <= max_iterations:
        h_mejor = nodo_actual.heuristica
        if (ids_nodosAdyacentes := nodo_actual.nodosAdyacentes.keys()):
            for id_nodo in ids_nodosAdyacentes:
                h_actual = grafo.nodos[id_nodo].heuristica
                if h_actual < h_mejor:
                    h_mejor = h_actual
                    id_mejor = id_nodo
            if h_mejor == nodo_actual.heuristica:
                c += 1
                print("\t" * 5 + "|", [(str(i) + ":" + str(grafo.nodos[i].heuristica)) for i in ids_nodosAdyacentes])
                print("---")
                print("Se ha llegado a un maximo local")
                break
            if id_mejor != nodo_actual.nombre:
                nodo_actual = grafo.nodos[id_mejor]
                camino.append(id_mejor)
                print("\t" * 5 + "|", [(str(i) + ":" + str(grafo.nodos[i].heuristica)) for i in ids_nodosAdyacentes])
                print(nodo_actual.nombre, "\t" * 4 + "|")
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
    costo = 0
    while len(pq) > 0:
        # pq.sort()
        print(list(pq))
        # costo += nodo_actual
        nodo_actual = pq.pop()[1]
        # Displaying the path having lowest cost
        print("\t" * max(len(pq), 10), nodo_actual)
        if nodo_actual.nombre == nombreBuscado:
            break
        list_aux = list()
        for v in sorted(graph.nodos[nodo_actual.nombre].nodosAdyacentes.keys()):
            if v not in visitados:
                visitados.append(v)
                aux = graph.nodos[v]
                list_aux.append((aux.heuristica, aux))
            # list_aux.sort(key=lambda i:i[0])
        # print("la",list_aux)
        for i in sorted(list_aux,reverse=True):
            pq.append(i)
        list_aux.clear()
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
        cola.sort(key=lambda i: i[1])
        for i in range(len(cola)):
            print(f"({cola[i][1]},{cola[i][2]} )", end=" ")
        print()
        costo, _, nodo_actual, padre = cola.pop(0)
        print("\t" * max(6, 3 * len(cola)), nodo_actual, costo)
        if nodo_actual not in visitados:
            visitados.add(nodo_actual)
            if nodo_actual == nombreBuscado:
                get_path(grafo, camino, nodo_actual, padre)
                print("Costo:", costo)
                return
            for i in sorted(grafo.nodos[nodo_actual].nodosAdyacentes):
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
        pq.clear()
        for v in graph.nodos[nodo_actual.nombre].nodosAdyacentes.keys():
            if v not in visitados:
                visitados.append(v)
                aux = graph.nodos[v]
                pq.append((aux.heuristica, aux))
    # print(visitados)
