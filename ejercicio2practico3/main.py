import os
from menu import Menu
from manejasabores import manejasabor
from manejahelad import manejadorhelado


if __name__ == '__main__':

    listahelados = manejadorhelado()
    listasabores = manejasabor()
    listasabores.cargardatos()

    listaventa = []
    for i in range(listasabores.getlong()):
        listaventa.append(0)

    menus = Menu()
    salir = False
    while not salir:
        print("\n----------Menu----------")
        print("0: Salir")
        print("1: Añadir pedido de helado")
        print("2: 5 sabores mas pedidos")
        print("3: Estimar peso vendido de un sabor")
        print("4: Sabores vendidos para tipo de helado")
        op = int(input("Ingrese una opcion: "))
        os.system('cls')
        menus.opcion(op, listahelados, listasabores, listaventa)
        salir = op == 0
    print(salir)
