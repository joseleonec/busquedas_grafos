from pip._internal.cli.cmdoptions import abi

from nodo import Nodo
from collections import deque


class Grafo():

    def __init__(self):
        self.contadorNodos = 0
        self.nodos = list()
        # self.matriz = [[None] * 0 for i in range(0)]

    def addNodo(self, nombre):
        self.nodos.append(Nodo(nombre))
        self.contadorNodos += 1

    def enlazar(self, nodoOrigen: str, nodoDestino: str):

        for i in self.nodos:
            if i.nombre == nodoOrigen:
                n1 = i
            elif i.nombre == nodoDestino:
                n2 = i
        if n1 is None or n2 is None:
            print("Algun nodo no existe")
        else:
            n1.addNodoAdyacentes(n2)

    def busquedaAmplitud(self, nodoInicial: Nodo, nombreBuscado: str = ""):

        cola = deque()  # cola para los vertices que se procesan
        cola.append(nodoInicial)  # agregar el vertice a la cola

        visitados = list()  # lista para los visitados
        visitados.append(nodoInicial)  # agregar el vertice de inicio a los visitados

        camino = list()  # lista para los nodos encontrados
        encontrado = False

        while len(cola) > 0 and not encontrado:
            n = cola.popleft()
            camino.append(n)
            if n.nombre != nombreBuscado:
                for na in n.nodosAdyacentes:
                    if na not in visitados:
                        cola.append(na)
                        visitados.append(na)
            else:
                encontrado = True
        if encontrado:
            print("Camino (" + nombreBuscado + "): ", end="")
            for i in camino:
                print(" " + i.nombre, end=" ")
            print()
        else:
            print("No existe el nodo ingresado.")

    def busquedaAmplitudTodos(self):
        for nodo in self.nodos:
            self.busquedaAmplitud(self.nodos[0], nodo.nombre)

    def busquedaProfundidad(self, nodoInicial: Nodo, nombreBuscado: str):

        pila = list()  # pila para los vertices que se procesan
        pila.append(nodoInicial)  # agregar el vertice a la pila

        visitados = list()  # lista para los visitados
        visitados.append(nodoInicial)  # agregar el vertice de inicio a los visitados

        camino = list()  # lista para los nodos encontrados
        encontrado = False

        while len(pila) > 0 and not encontrado:
            n = pila.pop()
            camino.append(n)
            if n.nombre != nombreBuscado:
                for na in reversed(n.nodosAdyacentes):
                    if na not in visitados:
                        pila.append(na)
                        visitados.append(na)
            else:
                encontrado = True
        if encontrado:
            print("Camino (" + nombreBuscado + "): ", end="")
            for i in camino:
                print(" -> " + i.nombre, end="")
            print()
        else:
            print("No existe el nodo ingresado.")

    def buscarProfundidadTodos(self):
        for nodo in self.nodos:
            self.busquedaProfundidad(self.nodos[0], nodo.nombre)

    def busquedaProfundidadIterativa(self, nodoInicial: Nodo, nombreBuscado: str):

        lp = 1  # Limite de exploración

        pila = list()  # pila para los vertices que se procesan
        pila.append(nodoInicial)  # agregar el vertice a la pila

        visitados = list()  # lista para los visitados
        visitados.append(nodoInicial)  # agregar el vertice de inicio a los visitados

        camino = list()  # lista para los nodos encontrados
        encontrado = False

        lp = 1
        contador_nivel = 0
        while len(pila) > 0 and not encontrado:

            n = pila.pop()
            camino.append(n)
            if n.nombre != nombreBuscado:
                contador_nivel += 1
                for na in reversed(n.nodosAdyacentes):
                    if na not in visitados and contador_nivel <= lp:
                        pila.append(na)
                        visitados.append(na)
            else:
                encontrado = True
        if encontrado:
            print("Camino (" + nombreBuscado + "): ", end="")
            for i in camino:
                print(" -> " + i.nombre, end="")
            print()
        else:
            print("No existe el nodo ingresado.")


if __name__ == '__main__':
    grafo = Grafo()
    grafo.addNodo("n1")
    grafo.addNodo("n2")
    grafo.addNodo("n3")
    grafo.addNodo("n4")
    grafo.addNodo("n5")
    grafo.addNodo("n6")

    grafo.enlazar("n1", "n2")
    grafo.enlazar("n1", "n3")

    grafo.enlazar("n2", "n1")
    grafo.enlazar("n2", "n4")
    grafo.enlazar("n2", "n5")

    grafo.enlazar("n3", "n1")
    grafo.enlazar("n3", "n6")

    grafo.enlazar("n5", "n2")
    # grafo.busquedaAmplitud(grafo.nodos[0], "n6")
    grafo.busquedaAmplitudTodos()
    # grafo.busquedaProfundidad(grafo.nodos[0], "n6")
    grafo.buscarProfundidadTodos()

#     opc = ""
#     while opc != "5":
#         print("\tGRAFO")
#         print("1. Agregar nodo")
#         print("2. Relacionar nodos")
#         print("3. Busqueda en Amplitud")
#         print("4. Busqueda en Profundidad")
#         print("5. Salir")
#         opc = input("Ingrese una opción: ")
#         cadena = ""
#         if opc == "1":
#             print("Ingrese el nombre del nodo: ")
#             cadena = input()
#             grafo.addNodo(cadena)
#             print("Nodo agregado al grafo\n")
#         elif opc == "2":
#             print("\tLISTA DE NODOS DISPONIBLES")
#             for n in grafo.nodos:
#                 print("Nodo: " + n.nombre)
#
#             print("\nAgregar enlace desde nodo1 a nodo 2")
#             print("Nodo 1: ")
#             n1 = input()
#             print("Nodo 2: ")
#             n2 = input()
#             grafo.enlazar(n1, n2)
#             print("Nodos correctamente enlazados\n")
#         elif opc == "3":
#             print("Ingrese el nodo de busqueda: ")
#             cadena = input()
#             if cadena == "":
#                 grafo.busquedaAmplitudTodos()
#             else:
#                 grafo.busquedaAmplitud(grafo.nodos[0], cadena)
#         elif opc == "4":
#             print("Ingrese el nodo de busqueda: ")
#             cadena = input()
#             if cadena == "":
#                 grafo.buscarProfundidadTodos()
#             else:
#                 grafo.busquedaProfundidad(grafo.nodos[0], cadena)
#         elif opc == "5":
#             print("Saliendo...")
#         else:
#             print("Opcion erronea\n")
