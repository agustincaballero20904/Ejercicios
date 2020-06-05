from zope.interface import Interface
from zope.interface import implementer
from interfa import IInter
from clnodo import Nodo
from clvehiculo import vehiculo
from clnuevo import nuevo
from clusado import usado


@implementer(IInter)
class Lista:
    __comienzo = None
    __actual = None
    __indice = 0
    __tope = 0

    def __init__(self):
        self.__comienzo = None
        self.__actual = None

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

    def agregarElemento(self, auto):
        nodo = Nodo(auto)
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

    def insertarElemento(self, auto, posicion):
        if posicion > self.__tope + 1:
            raise IndexError()
        else:
            nodo = Nodo(auto)
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
            auto = aux.getDato()
            return auto

    def buscarPatente(self, patente):
        aux = self.__comienzo
        if aux != None:
            band = True
            auto = None
            while aux != None and band:
                auto = aux.getDato()
                if type(auto) == usado:
                    if auto.getPatente() == patente:
                        band = False
                aux = aux.getSiguiente()
            if auto.getPatente() == patente:
                return auto
            else:
                raise IndexError()
        else:
            raise IndexError()


    def toJSON(self):
        d = dict(
                __class__=self.__class__.__name__,
                nodos = [auto.toJSON() for auto in self]
                )
        return d
