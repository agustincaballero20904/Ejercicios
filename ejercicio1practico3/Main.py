import os
from Menu import menu
from ManejaLibros import manejalibros


if __name__ == '__main__':

    listalibros = manejalibros()

    listalibros.cargardatos()

    menus = menu()
    salir = False
    while not salir:
        print("\n----------Menu----------")
        print("1: Buscar libro por id")
        print("2: Buscar palabra")
        print("3: Salir")
        op = int(input("Ingrese una opcion: "))
        os.system('cls')
        menus.opcion(op, listalibros)
        salir = op == 3
    print(salir)
