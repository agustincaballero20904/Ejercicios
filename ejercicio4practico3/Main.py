import os
from Menu import menu
from coleccion import coleccion


if __name__ == '__main__':

    cant = int(input("Ingrese la cantidad de empleados: "))
    colempleados = coleccion(cant)
    colempleados.mostrar()

    menus = menu()
    salir = False
    while not salir:
        print("\n----------Menu----------")
        print("0: Salir")
        print("1: Registrar horas")
        print("2: Total de tarea")
        print("3: Ayuda")
        print("4: Calcular sueldo")
        op = int(input("Ingrese una opcion: "))
        os.system('cls')
        menus.opcion(op, colempleados)
        salir = op == 0
    print(salir)
