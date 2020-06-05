from datetime import date
from empleado import empleado


class contratado(empleado):
    __fechini = None
    __fechfin = None
    __canthoras = 0
    valorhora = 0
    
    def __init__(self, dni, nom, direc, tele, fechini, fechfin):
        super().__init__(dni,nom,direc,tele)
        self.__fechini = fechini
        self.__fechfin = fechfin

    def __str__(self):
        print(super().mostrar())
        return ("Fecha de inicio: {}\nFecha de fin: {}\nCantidad de horas: {}".format(self.__fechini, self.__fechfin, self.__canthoras))

    def getemp(self):
        return self

    def getdni(self):
        return super().getdni()

    def aumenta(self, inc):
        self.__canthoras += inc

    def getsueldo(self):
        return(self.__canthoras * contratado.getval())

    def getdir(self):
        return super().getdir()

    def gettel(self):
        return super().gettel()

    def getnombre(self):
        return super().getnombre()

    @classmethod
    def getval(cls):
        return cls.valorhora
