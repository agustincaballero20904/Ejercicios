from Lista import Lista
from clvehiculo import vehiculo
from clnuevo import nuevo
from clusado import usado
from ObjectEncoder import ObjectEncoder


class menu:
    __switcher = None

    def __init__(self):
        self.__switcher = {0: self.salir,
                           1: self.opcion1,
                           2: self.opcion2,
                           3: self.opcion3,
                           4: self.opcion4,
                           5: self.opcion5,
                           6: self.opcion6,
                           7: self.opcion7
                           }

    def getswitcher(self):
        return self.__switcher

    def opcion(self, op, lista):
        func = self.__switcher.get(op, lambda: print("Opcion no válida"))
        func(lista)


    def salir(self, lista):
        for auto in lista:
            auto.mostrar()
        print("Salir")


    def opcion1(self, lista):
        try:
            auto = self.crearauto()
            posicion = int(input("Ingrese la posicion en la que agregar el auto: "))
            lista.insertarElemento(auto, posicion)
            
        except IndexError:
            print("No es posible ingresar en la posicion ingresada")
        except:
            print("La posicion ingresada no es valida")
        else:
            print("Elemento agregado exitosamente")


    def opcion2(self, lista):
        auto = self.crearauto()
        lista.agregarElemento(auto)


    def opcion3(self, lista):
        try:
            posicion = int(input("Ingrese la posicion que desea buscar"))
            auto = lista.buscarElemento(posicion)

        except IndexError:
            print("No es posible ingresar en la posicion ingresada")

        except SyntaxError:
            print("La posicion ingresada no es valida")
        else:
            print(type(auto))
            auto.mostrar()


    def opcion4(self, lista):
        try:
            patente = input("Ingrese patente del vehiculo: ")
            auto = lista.buscarPatente(patente)

        except IndexError:
            print("Patente no encontrada")

        else:
            precio = int(input("Ingrese el nuevo precio base: "))
            auto.modifprecio(precio)
            venta = auto.precioventa()
            print("Precio de venta:{}".format(venta))


    def opcion5(self, lista):
        minimo = 9999999
        auxm = None
        for auto in lista:
            if auto.precioventa() <= minimo:
                minimo = auto.precioventa()
                auxm = auto
        auxm.mostrar()
        print("Precio de venta: {}".format(minimo))


    def opcion6(self, lista):
        for auto in lista:
            auto.punto6()
            print("{}".format(auto.precioventa()))


    def opcion7(self, lista):
        json = ObjectEncoder()
        d = lista.toJSON()
        json.guardarJSONArchivo(d, 'vehiculos.json')


    def crearauto(self):
        modelo = input("Ingrese modelo del auto: ")
        cantpuertas = int(input("Ingrese cantidad de puertas: "))
        color = input("Ingrese color del auto: ")
        preciobase = int(input("Ingrese el precio base: "))
        marca = input("Ingrese marca del auto: ")
        nuevousado = int(input("Ingrese:\n1: Auto usado\n2: Auto nuevo\n"))
        while nuevousado != 1 and nuevousado != 2:
            print("Opcion elegida no valida")
            nuevousado = int(input("Ingrese:\n1: Auto usado\n2: Auto nuevo\n"))

        if nuevousado == 1:
            patente = input("Ingrese patente del auto: ")
            anio = int(input("Ingrese año del auto: "))
            km = int(input("Ingrese kilometraje del auto: "))
            auto = usado(modelo, cantpuertas, color, preciobase, marca, patente, anio, km)

        else:
            basefull = input("Ingrese la version: Base o Full\n")
            full = False
            if basefull.lower() == "full":
                full = True
            auto = nuevo(modelo, cantpuertas, color, preciobase, marca, full)
        return auto
