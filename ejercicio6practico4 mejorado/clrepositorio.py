from clprovincia import Provincia
from clobjectencoder import ObjectEncoder
from clmanejador import ManejadorProvincias


class RespositorioProvincias(object):
    __conn=None
    __manejador=None

    def __init__(self, conn):
        self.__conn = conn
        diccionario = self.__conn.leerJSONArchivo()
        self.__manejador = self.__conn.decodificarDiccionario(diccionario)

    def to_values(self, provincia):
        return provincia.getNombre(), provincia.getCapital(), provincia.getHabitantes(), provincia.getDepartamentos()

    def obtenerListaProvincias(self):
        return self.__manejador.getListaProvincias()

    def agregarProvincia(self, provincia):
        self.__manejador.agregarProvincia(provincia)
        return provincia

    def grabarDatos(self):
        self.__conn.guardarJSONArchivo(self.__manejador.toJSON())

    def borrarProvincia(self, provincia):
        self.__manejador.deleteProvincia(provincia)

    def modificarProvincia(self, provincia):
        self.__manejador.updateProvincia(provincia)
        return provincia
