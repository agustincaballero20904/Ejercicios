import os
from Menu import menu
from Lista import Lista
from ObjectEncoder import ObjectEncoder


if __name__ == '__main__':

    json = ObjectEncoder()
    d = json.leerJSONArchivo('vehiculos.json')
    listaautos = json.decodificarDiccionario(d)

    menus = menu()
    salir = False
    while not salir:
        print("\n----------Menu----------")
        print("0: Salir")
        print("1: Insertar un vehiculo en la colección")
        print("2: Agregar un vehiculo al final de la colección")
        print("3: Mostrar objeto en posicion ingresada")
        print("4: Modificar precio base de vehiculo usado")
        print("5: Mostrar datos del vehiculo más barato")
        print("6: Mostrar vehiculos a la venta")
        print("7: Guardar colección")
        op = int(input("Ingrese una opcion: "))
        os.system('cls')
        menus.opcion(op, listaautos)
        salir = op == 0
    print(salir)
