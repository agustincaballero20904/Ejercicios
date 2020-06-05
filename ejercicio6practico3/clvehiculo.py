class vehiculo:
    __modelo = ""
    __cantpuertas = 0
    __color = ""
    __preciobase = 0
    __marca = ""
    
    def __init__(self, modelo, cantpuertas, color, preciobase, marca):
        self.__modelo = modelo
        self.__cantpuertas = int(cantpuertas)
        self.__color = color
        self.__preciobase = int(preciobase)
        self.__marca = marca

    def mostrar(self):
        print("----------------------------")
        print("Modelo: {}\nPuertas: {}\nColor: {}\nPrecio base: {}\nMarca: {}".format(self.__modelo, self.__cantpuertas, self.__color, self.__preciobase, self.__marca))

    def modifprecio(self, precio):
        self.__preciobase = precio
        print("Nuevo precio base: {}".format(self.__preciobase))

    def getPrecio(self):
        return self.__preciobase

    def punto6(self):
        print("-------------------")
        print("Modelo: {}\nCantidad de puertas: {}".format(self.__modelo, self.__cantpuertas))

    def getModelo(self):
        return self.__modelo

    def getPuertas(self):
        return self.__cantpuertas

    def getColor(self):
        return self.__color

    def getMarca(self):
        return self.__marca
