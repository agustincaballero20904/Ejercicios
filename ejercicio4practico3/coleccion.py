import csv
import numpy as np
from datetime import date
from empleado import empleado
from planta import planta
from contratados import contratado
from externos import externo


class coleccion:
    __dimension = 0
    
    def __init__(self, cantidad):
        self.__dimension = cantidad
        self.__colecc = np.empty(self.__dimension, dtype=empleado)

        valor = int(input("Ingrese el valor por hora de los empleados contratados: "))
        contratado.valorhora = valor
        cont = 0
        for i in range(3):
            nombres = ["planta.csv", "contratados.csv", "externos.csv"]
            nom = nombres[i]
            archivo = open(nom)
            reader = csv.reader(archivo, delimiter=",")
            for fila in reader:
                if cont < self.__dimension:
                    if i == 0:
                        self.__colecc[cont] = planta(fila[0], fila[1], fila[2], int(fila[3]), int(fila[4]), int(fila[5]))
                    else:
                        fechaini = date.fromisoformat(fila[4])
                        fechafin = date.fromisoformat(fila[5])
                        if i == 1:
                            self.__colecc[cont] = contratado(fila[0], fila[1], fila[2], int(fila[3]), fechaini, fechafin)
                        else:
                            self.__colecc[cont] = externo(fila[0], fila[1], fila[2], int(fila[3]), fechaini, fechafin, int(fila[6]), int(fila[7]), int(fila[8]), fila[9])
                    cont += 1


    def mostrar(self):
        for emp in self.__colecc:
            print("------------------------")
            print(emp)
            print("------------------------")


    def buscadni(self, dni):
        i = 0
        auxe = self.__colecc[i].getemp()
        while dni != auxe.getdni() and i < self.__dimension:
            i += 1
            auxe = self.__colecc[i].getemp()
        if i != self.__dimension:
            if type(auxe) == contratado:
                aumento = int(input("Ingrese cantidad de horas: "))
                auxe.aumenta(aumento)
            else:
                print("El empleado buscado no es un empleado contratado")
        else:
            print("El dni ingresado no corresponde a ningun empleado")


    def buscatarea(self, tarea):
        tot = 0
        for emp in self.__colecc:
            if type(emp) == externo:
                if emp.gettarea() == tarea:
                    if date.today() < emp.getfechafin():
                        tot += emp.getsueldo()
        print("El total a pagar por la tarea es de : ")
        print(tot)

    def ayuda(self):
        print("\nEmpleados a los que les corresponde la ayuda:")
        for emp in self.__colecc:
            if emp.getsueldo() <= 25000:
                print("--------------")
                print("Nombre: {}\nDireccion: {}\nDNI: {}".format(emp.getnombre(), emp.getdir(), emp.getdni()))
                print("--------------")

    def sueldos(self):
        for emp in self.__colecc:
            print("--------------")
            print("Nombre: {}\nTelefono: {}\nSueldo: {}".format(emp.getnombre(), emp.gettel(), emp.getsueldo()))
            print("--------------")