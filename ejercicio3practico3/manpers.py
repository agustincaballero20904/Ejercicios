import numpy as np
from clpersona import Persona


class manejaper:
    __cont = 0
    __dimension = 0

    def __init__(self, cantidad=1):
        self.__dimension = cantidad
        self.__personas = np.empty(self.__dimension, dtype=Persona)

    def addpersona(self, unapersona):
        if type(unapersona) == Persona:
            if self.__cont == self.__dimension:
                self.__dimension += 1
                self.__personas.resize(self.__dimension)
            self.__personas[self.__cont] = unapersona
            self.__cont += 1
