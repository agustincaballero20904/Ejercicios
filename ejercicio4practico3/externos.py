from empleado import empleado


class externo(empleado):
    __tarea = ""
    __fechini = None
    __fechfin = None
    __viatico = 0
    __costoobra = 0
    __seguro = 0

    def __init__(self, dni, nom, direc, tele, fechini, fechfin, viatico, costo, seguro, tarea):
        super().__init__(dni,nom,direc,tele)
        self.__fechini = fechini
        self.__fechfin = fechfin
        self.__viatico = viatico
        self.__costoobra = costo
        self.__seguro = seguro
        self.__tarea = tarea

    def __str__(self):
        print(super().mostrar())
        return ("Tarea: {}\nFecha de inicio: {}\nFecha de fin: {}\nViatico: {}\nCosto obra: {}\nSeguro: {}".format(self.__tarea, self.__fechini, self.__fechfin, self.__viatico, self.__costoobra, self.__seguro))

    def getemp(self):
        return self

    def getdni(self):
        return super().getdni()

    def getsueldo(self):
        return(self.__costoobra - self.__viatico - self.__seguro)

    def gettarea(self):
        return self.__tarea

    def getfechafin(self):
        return self.__fechfin

    def getdir(self):
        return super().getdir()

    def gettel(self):
        return super().gettel()

    def getnombre(self):
        return super().getnombre()
