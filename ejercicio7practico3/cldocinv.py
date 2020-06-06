from cldocente import Docente
from clinvestigador import Investigador


class DocenteInvestigador(Docente,Investigador):
    __extra = 0
    __categoria = 0

    def __init__(self, cuil, apellido, nombre, sueldobase, antig, carrera, cargo, catedra, area, tipo, extra, categoria):
        super().__init__(cuil, apellido, nombre, sueldobase, antig, carrera, cargo, catedra, area, tipo)
        self.__extra = int(extra)
        self.__categoria = int(categoria)

    def mostrar(self):
        super().mostrar()
        print("Datos Docente Investigador")
        print("Extra por docencia e investigacion: {}".format(self.__extra))
        print("Categoria en el programa de incentivos: {}".format(self.__categoria))

    def Sueldo(self):
        sueldoc = Docente.Sueldo(self)
        return sueldoc + self.__extra

    def getCategoria(self):
        return self.__categoria

    def getExtra(self):
        return self.__extra

    def toJSON(self):
        d = dict(
            __class__=self.__class__.__name__,
            atributos=dict(
                cuil = self.getCuil(),
                apellido = self.getApellido(),
                nombre = self.getNombre(),
                sueldobase = self.getSueldobase(),
                antig = self.getAntig(),
                carrera = super().getCarrera(),
                cargo = super().getCargo(),
                catedra = super().getCatedra(),
                area = super().getArea(),
                tipo = super().getTipo(),
                extra = self.__extra,
                categoria = self.__categoria
            )
        )
        return d
