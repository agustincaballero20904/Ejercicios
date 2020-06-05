from clvehiculo import vehiculo
from clnuevo import nuevo
from clusado import usado


class Nodo:
    __auto = None
    __siguiente = None

    def __init__(self, auto):
        self.__auto = auto
        self.__siguiente = None

    def setSiguiente(self, siguiente):
        self.__siguiente = siguiente

    def getSiguiente(self):
        return self.__siguiente

    def getDato(self):
        return self.__auto
