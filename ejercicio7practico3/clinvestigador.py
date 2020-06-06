from clpersonal import Personal


class Investigador(Personal):
    __area = ""
    __tipo = ""

    def __init__(self, cuil, apellido, nombre, sueldobase, antig, carrera, cargo, catedra, area, tipo):
        super().__init__(cuil, apellido, nombre, sueldobase, antig, carrera, cargo, catedra, area, tipo)
        self.__carrera = carrera
        self.__area = area
        self.__tipo = tipo

    def mostrar(self):
        super().mostrar()
        print("Datos Investigador")
        print("Area de investigacion: {}".format(self.__area))
        print("Tipo de investigacion: {}".format(self.__tipo))

    def getArea(self):
        return self.__area

    def getTipo(self):
        return self.__tipo

    def Sueldo(self):
        base = super().getSueldobase()
        antig = super().getAntig()
        uno = base / 100
        sueldo = base + uno*antig
        return sueldo

    def toJSON(self):
        d = dict(
            __class__=self.__class__.__name__,
            atributos=dict(
                cuil = super().getCuil(),
                apellido = super().getApellido(),
                nombre = super().getNombre(),
                sueldobase = super().getSueldobase(),
                antig = super().getAntig(),
                carrera = None,
                cargo = None,
                catedra = None,
                area = self.__area,
                tipo = self.__tipo
            )
        )
        return d
