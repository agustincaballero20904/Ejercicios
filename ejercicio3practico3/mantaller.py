import csv
import numpy as np
from cltaller import TallerCapacitacion


class manejataller:
    __dimension = 0

    def __init__(self, cantidad=1):
        self.__dimension = cantidad
        self.__talleres = np.empty(self.__dimension, dtype=TallerCapacitacion)

        archivo = open("talleres.csv")
        reader = csv.reader(archivo, delimiter=",")
        cont = 0
        band = False
        for fila in reader:
            if not band:
                self.__dimension = int(fila[0])
                self.__talleres.resize(self.__dimension)
                band = True
            else:
                self.__talleres[cont] = TallerCapacitacion(int(fila[0]), fila[1], int(fila[2]), int(fila[3]))
                cont += 1

    def listartalleres(self):
        for taller in self.__talleres:
            print("------------------------")
            print(taller)
            print("------------------------")

    def getporid(self, idta):
        i = 0
        while i < self.__dimension and self.__talleres[i].getid() != idta:
            i += 1
        if i == self.__dimension:
            return None
        else:
            return self.__talleres[i]
