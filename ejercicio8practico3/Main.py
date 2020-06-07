import os
from Menu import menu
from Lista import Lista


if __name__ == '__main__':

    colempleados = Lista()
    colempleados.cargarDatos()

    menus = menu()
    salir = False
    while not salir:
        print("\n----------Menu----------")
        print("0: Salir")
        print("1: Registrar horas")
        print("2: Total de tarea")
        print("3: Ayuda")
        print("4: Calcular sueldo")
        print("5: Opciones de tesorero")
        print("6: Opciones de gerente")
        op = int(input("Ingrese una opcion: "))
        os.system('cls')
        menus.opcion(op, colempleados)
        salir = op == 0
    print(salir)