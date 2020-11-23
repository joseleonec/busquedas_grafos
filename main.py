from busquedas import *

if __name__ == '__main__':
    opc = ""
    grafo = Grafo()
    while opc != "5":
        print("\tGRAFO")
        print("1. Agregar nodo")
        print("2. Relacionar nodos")
        print("3. Busqueda en Amplitud")
        print("4. Busqueda en Profundidad")
        print("5. Salir")
        opc = input("Ingrese una opción: ")
        cadena = ""
        if opc == "1":
            print("Ingrese el nombre del nodo: ")
            cadena = input()
            grafo.addNodo(cadena)
            print("Nodo agregado al grafo\n")
        elif opc == "2":
            print("\tLISTA DE NODOS DISPONIBLES")
            for n in grafo.nodos:
                print("Nodo: " + n.nombre)

            print("\nAgregar enlace desde nodo1 a nodo 2")
            print("Nodo 1: ")
            n1 = input()
            print("Nodo 2: ")
            n2 = input()
            grafo.addEdge(n1, n2)
            print("Nodos correctamente enlazados\n")
        elif opc == "3":
            print("Ingrese el nodo de busqueda: ")
            cadena, c2 = input()
            if cadena == "":
                busquedaAmplitudTodos(grafo)
            else:
                busquedaAmplitud(grafo.nodos[0], cadena)
        elif opc == "4":
            print("Ingrese el nodo de busqueda: ")
            cadena = input()
            if cadena == "":
                buscarProfundidadTodos(grafo)
            else:
                busquedaProfundidad(grafo.nodos[0], cadena)
        elif opc == "5":
            print("Saliendo...")
        else:
            print("Opcion erronea\n")

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
