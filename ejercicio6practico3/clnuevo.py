from clvehiculo import vehiculo


class nuevo(vehiculo):
    __full = False
    
    def __init__(self, modelo, cantpuertas, color, preciobase, marca, full):
        super().__init__(modelo, cantpuertas, color, preciobase, marca)
        self.__full = full

    def mostrar(self):
        super().mostrar()
        f = "full" if self.__full else "base"
        print("El auto es",f)

    def precioventa(self):
        precio = self.getPrecio()
        uno = precio / 100
        if self.__full:
            preciodeventa = precio + 10*uno + 2*uno
        else:
            preciodeventa = precio + 10*uno
        return int(preciodeventa)

    def toJSON(self):
            d = dict(
                __class__=self.__class__.__name__,
                atributos=dict(
                    modelo = super().getModelo(),
                    cantpuertas = super().getPuertas(),
                    color = super().getColor(),
                    preciobase = super().getPrecio(),
                    marca = super().getMarca(),
                    full = self.__full
                )
            )
            return d
