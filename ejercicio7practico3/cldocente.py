from clpersonal import Personal


class Docente(Personal):
    __carrera = ""
    __cargo = ""
    __catedra = ""

    def __init__(self, cuil, apellido, nombre, sueldobase, antig, carrera, cargo, catedra, area=None, tipo=None):
        super().__init__(cuil, apellido, nombre, sueldobase, antig, carrera, cargo, catedra, area, tipo)
        self.__carrera = carrera
        self.__cargo = cargo
        self.__catedra = catedra

    def getCarrera(self):
        return self.__carrera

    def getCargo(self):
        return self.__cargo

    def getCatedra(self):
        return self.__catedra

    def mostrar(self):
        super().mostrar()
        print("Datos Docente")
        print("Carrera: {}".format(self.__carrera))
        print("Cargo: {}".format(self.__cargo))
        print("Catedra: {}".format(self.__catedra))

    def Sueldo(self):
        base = super().getSueldobase()
        antig = super().getAntig()
        uno = base / 100
        sueldo = base + uno*antig
        if self.__cargo.lower() == "simple":
            sueldo += uno*10
        else:
            if self.__cargo.lower() == "semiexclusivo":
                sueldo += uno*20
            else:
                if self.__cargo.lower() == "exclusivo":
                    sueldo += uno*50
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
                carrera = self.__carrera,
                cargo = self.__cargo,
                catedra = self.__catedra,
                area = None,
                tipo = None
            )
        )
        return d
