from cldocente import Docente
from clapoyo import PersonaldeApoyo
from clinvestigador import Investigador
from cldocinv import DocenteInvestigador


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