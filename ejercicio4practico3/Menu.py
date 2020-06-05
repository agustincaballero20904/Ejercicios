from coleccion import coleccion


class menu:
    __switcher = None

    def __init__(self):
        self.__switcher = {0: self.salir,
                           1: self.opcion1,
                           2: self.opcion2,
                           3: self.opcion3,
                           4: self.opcion4
                           }

    def getswitcher(self):
        return self.__switcher

    def opcion(self, op, colecc):
        func = self.__switcher.get(op, lambda: print("Opcion no válida"))
        func(colecc)

    def salir(self, colecc):
        colecc.mostrar()
        print("Salir")

    def opcion1(self, colecc):
        dni = input("Ingrese el dni del empleado: ")
        colecc.buscadni(dni)

    def opcion2(self, colecc):
        tareas = ["carpinteria", "electricidad", "plomeria"]
        print("---Tareas---")
        print("1: {}\n2: {}\n3: {}".format(tareas[0], tareas[1], tareas[2]))
        tarea = int(input("Ingrese el numero de tarea: "))
        tareaele = tareas[tarea-1]
        colecc.buscatarea(tareaele)

    def opcion3(self, colecc):
        colecc.ayuda()

    def opcion4(self, colecc):
        colecc.sueldos()
