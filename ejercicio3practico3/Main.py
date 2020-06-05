import os
from Menu import menu
from manpers import manejaper
from mantaller import manejataller
from manins import manejins


if __name__ == '__main__':

    arrepers = manejaper()
    arretaller = manejataller()
    listains = manejins()

    menus = menu()
    salir = False
    while not salir:
        print("\n----------Menu----------")
        print("0: Salir")
        print("1: Inscribir en un taller")
        print("2: Consultar inscripcion")
        print("3: Consultar inscriptos")
        print("4: Registrar pago")
        print("5: Guardar inscripciones")
        op = int(input("Ingrese una opcion: "))
        os.system('cls')
        menus.opcion(op, arrepers, arretaller, listains)
        salir = op == 0
    print(salir)
