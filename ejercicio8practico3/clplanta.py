from datetime import date
from clempleado import empleado


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

    def getsueldo(self):
        sueldo = int(self.__sueldo + self.__sueldo / 100 * self.__antig)
        return sueldo

    def cambiosueldo(self, nuevo):
        self.__sueldo = nuevo
