from zope.interface import Interface
from zope.interface import implementer
from tesorero import ITesorero
from gerente import IGerente
import csv
from datetime import date
from clplanta import planta
from clcontratados import contratado
from clexternos import externo
from clnodo import Nodo


@implementer(ITesorero)
@implementer(IGerente)
class Lista:
    __comienzo = None
    __actual = None
    __indice = 0
    __tope = 0

    def __init__(self):
        self.__comienzo = None
        self.__actual = None
        self.__tope = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.__indice == self.__tope:
             self.__actual = self.__comienzo
             self.__indice = 0
             raise StopIteration
        else:
             self.__indice += 1
             dato = self.__actual.getDato()
             self.__actual = self.__actual.getSiguiente()
             return dato

    def agregarElemento(self, empleado):
        nodo = Nodo(empleado)
        aux = self.__comienzo
        if aux == None:
            nodo.setSiguiente(self.__comienzo)
            self.__comienzo = nodo
            self.__actual = nodo
            self.__tope += 1
        else:
            while aux != None:
                ant = aux
                aux = aux.getSiguiente()
            nodo.setSiguiente(aux)
            ant.setSiguiente(nodo)
            self.__tope += 1

    def cargarDatos(self):
        valor = int(input("Ingrese el valor por hora de los empleados contratados: "))
        contratado.valorhora = valor
        for i in range(3):
            nombres = ["planta.csv", "contratados.csv", "externos.csv"]
            nom = nombres[i]
            archivo = open(nom)
            reader = csv.reader(archivo, delimiter=",")
            for fila in reader:
                if i == 0:
                    self.agregarElemento(planta(fila[0], fila[1], fila[2], int(fila[3]), int(fila[4]), int(fila[5])))
                else:
                    fechaini = date.fromisoformat(fila[4])
                    fechafin = date.fromisoformat(fila[5])
                    if i == 1:
                        self.agregarElemento(contratado(fila[0], fila[1], fila[2], int(fila[3]), fechaini, fechafin))
                    else:
                        self.agregarElemento(externo(fila[0], fila[1], fila[2], int(fila[3]), fechaini, fechafin, int(fila[6]), int(fila[7]), int(fila[8]), fila[9]))

    def mostrar(self):
        for emp in self:
            print("------------------------")
            print(emp)
            print("------------------------")

    def buscadni(self, dni):
        aux = self.__comienzo
        empleado = aux.getDato()
        band = True
        while empleado.getdni() != dni and band:
            aux = aux.getSiguiente()
            if aux != None:
                empleado = aux.getDato()
            else:
                band = False
        if empleado.getdni() == dni:
            retorno = empleado
        else:
            retorno = None
        return retorno



    def gastosSueldoPorEmpleado(self, dni):
        emp = self.buscadni(dni)
        if emp != None:
            print("Gasto en sueldo para el empleado ingresado {}".format(emp.getsueldo))
        else:
            print("Empleado no encontrado")


    def modificarBasicoEPlanta(self, dni, nuevoBasico):
        emp = self.buscadni(dni)
        if emp != None:
            emp.cambiosueldo(nuevoBasico)
        else:
            print("Empleado no encontrado")

    def modificarViaticoEExterno(self, dni, nuevoViatico):
        emp = self.buscadni(dni)
        if emp != None:
            emp.cambioviatico(nuevoViatico)
        else:
            print("Empleado no encontrado")

    def modificarValorEPorHora(self, nuevoValorHora):
        contratado.valorhora = nuevoValorHora
