from ManejaLibros import manejalibros


class menu:
    __switcher = None

    def __init__(self):
        self.__switcher = {1: self.opcion1,
                           2: self.opcion2,
                           3: self.salir
                           }

    def getswitcher(self):
        return self.__switcher

    def opcion(self, op, listalibros):
        func = self.__switcher.get(op, lambda: print("Opcion no             válida"))
        func(listalibros)

    def salir(self, libros):
        print("Salir")

    def opcion1(self, libros):
        id = int(input("Ingrese el id del libro: "))
        libros.buscaidentif(id)

    def opcion2(self, libros):
        palabra = input("Ingrese una palabra: ")
        libros.buscarpalabra(palabra)
