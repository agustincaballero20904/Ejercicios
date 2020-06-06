class Personal:
    __cuil = ""
    __apellido = ""
    __nombre = ""
    __sueldobase = 0
    __antig = 0

    def __init__(self, cuil, apellido, nombre, sueldobase, antig, carrera=None, cargo=None, catedra=None, area=None, tipo=None, categoria=None):
        self.__cuil = cuil
        self.__apellido = apellido
        self.__nombre = nombre
        self.__sueldobase = int(sueldobase)
        self.__antig = int(antig)

    def getCuil(self):
        return self.__cuil

    def getNombre(self):
        return self.__nombre

    def getApellido(self):
        return self.__apellido

    def getSueldobase(self):
        return self.__sueldobase

    def getAntig(self):
        return self.__antig

    def mostrar(self):
        print("-----------------------")
        print("Datos Personal")
        print("Cuil: {}".format(self.__cuil))
        print("Apellido: {}".format(self.__apellido))
        print("Nombre: {}".format(self.__nombre))
        print("Sueldo base: {}".format(self.__sueldobase))
        print("Antiguedad: {}".format(self.__antig))
