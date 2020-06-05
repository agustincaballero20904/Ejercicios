from datetime import date
from empleado import empleado


class planta(empleado):
    __sueldo = 0
    __antig = 0
    
    def __init__(self, dni, nom, direc, tele, suel, anti):
        super().__init__(dni,nom,direc,tele)
        self.__sueldo = suel
        self.__antig = anti

    def __str__(self):
        print(super().mostrar())
        return ("Sueldo: {}\nAntiguedad: {} años".format(self.__sueldo, self.__antig))

    def getemp(self):
        return self

    def getdni(self):
        return super().getdni()

    def getsueldo(self):
        sueldo = int(self.__sueldo + self.__sueldo / 100 * self.__antig)
        return sueldo

    def getdir(self):
        return super().getdir()

    def gettel(self):
        return super().gettel()

    def getnombre(self):
        return super().getnombre()
