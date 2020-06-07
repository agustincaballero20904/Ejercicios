from Lista import Lista
from datetime import date
from clplanta import planta
from clcontratados import contratado
from clexternos import externo
from tesorero import ITesorero
from gerente import IGerente


class menu:
    __switcher = None

    def __init__(self):
        self.__switcher = {0: self.salir,
                           1: self.opcion1,
                           2: self.opcion2,
                           3: self.opcion3,
                           4: self.opcion4,
                           5: self.opcion5,
                           6: self.opcion6
                           }

    def getswitcher(self):
        return self.__switcher

    def opcion(self, op, lista):
        func = self.__switcher.get(op, lambda: print("Opcion no válida"))
        func(lista)

    def salir(self, lista):
        for emp in lista:
            print("--------------------")
            print(emp)
        print("Salir")

    def opcion1(self, lista):
        dni = input("Ingrese el dni del empleado: ")
        empleado = lista.buscadni(dni)
        if empleado != None:
            if type(empleado) == contratado:
                aumento = int(input("Ingrese cantidad de horas: "))
                empleado.aumenta(aumento)
            else:
                print("El empleado buscado no es un empleado contratado")
        else:
            print("No se encontro ningun empleado con el dni ingresado")

    def opcion2(self, lista):
        tareas = ["carpinteria", "electricidad", "plomeria"]
        print("---Tareas---")
        print("1: {}\n2: {}\n3: {}".format(tareas[0], tareas[1], tareas[2]))
        tarea = int(input("Ingrese el numero de tarea: "))
        tareaele = tareas[tarea-1]
        tot = 0
        for emp in lista:
            if type(emp) == externo:
                if emp.gettarea() == tareaele:
                    if date.today() < emp.getfechafin():
                        tot += emp.getsueldo()
        print("El total a pagar por la tarea es de : ")
        print(tot)

    def opcion3(self, lista):
        print("\nEmpleados a los que les corresponde la ayuda:")
        for emp in lista:
            if emp.getsueldo() <= 25000:
                print("--------------")
                print("Nombre: {}\nDireccion: {}\nDNI: {}".format(emp.getnombre(), emp.getdir(), emp.getdni()))
                print("--------------")

    def opcion4(self, lista):
         for emp in lista:
            print("--------------")
            print("Nombre: {}\nTelefono: {}\nSueldo: {}".format(emp.getnombre(), emp.gettel(), emp.getsueldo()))
            print("--------------")




    def tesorero(self, lista):
        print("------------------------")
        print("Consultar gasto de sueldo para empleado empleado")
        dni = input("Ingrese dni del empleado")
        lista.gastosSueldoPorEmpleado(dni)

    def ingresar(self, tes):
        usuario = input("Ingrese usuario: ")
        contra = input("Ingrese contrasena: ")
        if tes:
            retorno = usuario == "uTesorero" and contra == "ag@74ck"
        else:
            retorno = usuario == "uGerente" and contra == "ufC77#!1"
        return retorno

    def opcion5(self, lista):
        if self.ingresar(True):
            self.tesorero(ITesorero(lista))
        else:
            print("Datos incorrectos")



    def gerente(self, lista):
        option = -1
        while option != 0:
            print("------------------------")
            print("Menu gerente:")
            print("0: Salir")
            print("1: Modificar sueldo basico de empleado de planta")
            print("2: Modificar valor por hora de empleados contratados")
            print("3: Modificar valor de viatico de empleado externo")
            option = int(input("Ingrese una opcion: "))
            if option == 1:
                dni = input("Ingrese dni del empleado")
                valor = int(input("Ingrese nuevo valor"))
                lista.modificarBasicoEPlanta(dni, valor)
            else:
                if option == 2:
                    valor = int(input("Ingrese nuevo valor"))
                    lista.modificarValorEPorHora(valor)
                else:
                    if option == 3:
                        dni = input("Ingrese dni del empleado")
                        valor = int(input("Ingrese nuevo valor"))
                        lista.modificarViaticoEExterno(dni, valor)

    def opcion6(self, lista):
        if self.ingresar(False):
            self.gerente(IGerente(lista))
        else:
            print("Datos incorrectos")
