import os
from Menu import menu
from Lista import Lista
from ObjectEncoder import ObjectEncoder


if __name__ == '__main__':

    json = ObjectEncoder()
    d = json.leerJSONArchivo('personal.json')
    listapersonal = json.decodificarDiccionario(d)

    menus = menu()
    salir = False
    while not salir:
        print("\n----------Menu----------")
        print("0: Salir")
        print("1: Insertar un agente en la colección")
        print("2: Agregar un agente al final de la colección")
        print("3: Mostrar objeto en posicion ingresada")
        print("4: Buscar docentes investigadores en una carrera")
        print("5: Buscar en area cantidad de investigadores y docentes investigadores")
        print("6: Mostrar todos los agentes ordenados por apellido")
        print("7: Buscar extra de los docentes investigadores y obtener el total a pagar en extras")
        print("8: Guardar colección")
        op = int(input("Ingrese una opcion: "))
        os.system('cls')
        menus.opcion(op, listapersonal)
        salir = op == 0
    print(salir)
