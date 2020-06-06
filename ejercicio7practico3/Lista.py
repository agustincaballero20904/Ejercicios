from zope.interface import Interface
from zope.interface import implementer
from interfa import IInter
from clnodo import Nodo
from cldocente import Docente
from clapoyo import PersonaldeApoyo
from clinvestigador import Investigador
from cldocinv import DocenteInvestigador

@implementer(IInter)
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

    def agregarElemento(self, agente):
        nodo = Nodo(agente)
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

    def insertarElemento(self, agente, posicion):
        if posicion > self.__tope + 1:
            raise IndexError()
        else:
            nodo = Nodo(agente)
            if posicion == 1:
                nodo.setSiguiente(self.__comienzo)
                self.__comienzo = nodo
                self.__actual = nodo
                self.__tope += 1
            else:
                aux = self.__comienzo
                for i in range(posicion - 1):
                    ant = aux
                    aux = aux.getSiguiente()
                nodo.setSiguiente(aux)
                ant.setSiguiente(nodo)
                self.__tope += 1

    def buscarElemento(self, posicion):
        if posicion > self.__tope:
            raise IndexError()
        else:
            aux = self.__comienzo
            for i in range(posicion - 1):
                aux = aux.getSiguiente()
            agente = aux.getDato()
            return agente


    def getTope(self):
        return self.__tope


    def getnombreoapellido(self, agente, band):
        if band:
            devolver = agente.getNombre()
        else:
            devolver = agente.getApellido()
        return devolver


    def ordenar(self, cantidad, band):
        for i in range(cantidad - 1):
            ant = self.__comienzo
            aux = ant.getSiguiente()
            ban = True
            fin = cantidad - (i + 1)
            for j in range(fin):
                if ant == self.__comienzo and j == 0:
                    agente1 = ant.getDato()
                    agente2 = aux.getDato()
                    if self.getnombreoapellido(agente1,band) > self.getnombreoapellido(agente2,band):
                        sig = aux.getSiguiente()
                        ant.setSiguiente(sig)
                        self.__comienzo = aux
                        aux.setSiguiente(ant)
                        self.__actual = self.__comienzo
                else:
                    if ban:
                        sig = aux.getSiguiente()
                        ban = False
                        agente1 = aux.getDato()
                        agente2 = sig.getDato()
                        if self.getnombreoapellido(agente1,band) > self.getnombreoapellido(agente2,band):
                            ant.setSiguiente(sig)
                            aux.setSiguiente(sig.getSiguiente())
                            sig.setSiguiente(aux)
                    else:
                        ant = aux
                        aux = sig
                        sig = aux.getSiguiente()
                        agente1 = aux.getDato()
                        agente2 = sig.getDato()
                        if self.getnombreoapellido(agente1,band) > self.getnombreoapellido(agente2,band):
                            ant.setSiguiente(sig)
                            aux.setSiguiente(sig.getSiguiente())
                            sig.setSiguiente(aux)



    def toJSON(self):
        d = dict(
                __class__=self.__class__.__name__,
                nodos = [agente.toJSON() for agente in self]
                )
        return d
