from datetime import date
from clvehiculo import vehiculo


class usado(vehiculo):
    __patente = ""
    __anio = 0
    __km = 0

    def __init__(self, modelo, cantpuertas, color, preciobase, marca, patente, anio, km):
        super().__init__(modelo, cantpuertas, color, preciobase, marca)
        self.__patente = patente
        self.__anio = int(anio)
        self.__km = int(km)

    def mostrar(self):
        super().mostrar()
        print("Patente: {}\nAño: {}\nKilometraje: {}".format(self.__patente, self.__anio, self.__km))

    def getPatente(self):
        return self.__patente

    def precioventa(self):
        precio = self.getPrecio()
        a = date.today()
        b = a.isoformat()
        a,c = b.split("-",1)
        c = int(a) - self.__anio
        b = precio/100
        if self.__km > 100000:
            preciodeventa = precio - b * c - 2 * b
        else:
            preciodeventa = precio - b * c
        return(int(preciodeventa))


    def toJSON(self):
            d = dict(
                __class__=self.__class__.__name__,
                atributos=dict(
                    modelo = super().getModelo(),
                    cantpuertas = super().getPuertas(),
                    color = super().getColor(),
                    preciobase = super().getPrecio(),
                    marca = super().getMarca(),
                    patente = self.__patente,
                    anio = self.__anio,
                    km = self.__km
                )
            )
            return d
