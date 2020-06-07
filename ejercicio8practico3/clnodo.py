from clplanta import planta
from clcontratados import contratado
from clexternos import externo


class Nodo:
    __agente = None
    __siguiente = None

    def __init__(self, agente):
        self.__agente = agente
        self.__siguiente = None

    def setSiguiente(self, siguiente):
        self.__siguiente = siguiente

    def getSiguiente(self):
        return self.__siguiente

    def getDato(self):
        return self.__agente