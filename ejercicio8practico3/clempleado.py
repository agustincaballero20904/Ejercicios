class empleado:
    __dni = ""
    __nombre = ""
    __direccion = ""
    __telefono = 0

    def __init__(self, dni, nom, direc, tele):
        self.__dni = dni
        self.__nombre = nom
        self.__direccion = direc
        self.__telefono = tele

    def mostrar(self):
        return ("Nombre: {}\nDNI: {}\nDireccion: {}\nTelefono: {}".format(self.__nombre, self.__dni, self.__direccion, self.__telefono))

    def getdni(self):
        return self.__dni

    def getnombre(self):
        return self.__nombre

    def getdir(self):
        return self.__direccion

    def gettel(self):
        return self.__telefono