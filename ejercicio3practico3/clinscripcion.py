from datetime import date


class Inscripcion:
    __fechainsc = None
    __pago = False
    __pers = None
    __taller = None
    
    def __init__(self, person, eltaller):
        self.__fechainsc = date.today()
        self.__pago = False
        self.__pers = person
        self.__taller = eltaller

    def getpers(self):
        return self.__pers

    def gettaller(self):
        return self.__taller

    def getpago(self):
        return self.__pago

    def setPago(self, nuevo):
        self.__pago = nuevo

    def toJSON(self):
        d = dict(
            __class__=self.__class__.__name__,
            __atributos__=dict(
                dniPersona=self.__pers.getdni(),
                idTaller=self.__taller.getid(),
                fechaInscripcion=str(self.__fechainsc),
                pago=self.__pago
                )
        )
        return d
