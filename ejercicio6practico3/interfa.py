from zope.interface import Interface


class IInter(Interface):
    def insertarElemento(objeto, posicion):
        pass
    def agregarElemento(objeto):
        pass
    def mostrarElemento(posicion):
        pass
