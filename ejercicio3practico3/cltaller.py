from clinscripcion import Inscripcion


class TallerCapacitacion:
    __idtaller = 0
    __nombre = ""
    __vacantes = 0
    __montoins = 0
    __inscrip = None

    def __init__(self, idt, nom, vac, monto):
        self.__idtaller = idt
        self.__nombre = nom
        self.__vacantes = vac
        self.__montoins = monto
        self.__inscrip = []

    def inscribir(self, insc):
        if type(insc) == Inscripcion:
            self.__vacantes -= 1
            self.__inscrip.append(insc)
        return insc

    def __str__(self):
        return ("id: {}\nNombre: {}\nVacantes: {}\nMonto de inscripcion: {}".format(self.__idtaller, self.__nombre, self.__vacantes, self.__montoins))

    def getid(self):
        return self.__idtaller

    def getvac(self):
        return self.__vacantes

    def getmonto(self):
        return self.__montoins

    def getnombre(self):
        return self.__nombre

    def listarinscriptos(self):
        if len(self.__inscrip) > 0:
            for inscripcion in self.__inscrip:
                auxp = inscripcion.getpers()
                print("----------------------")
                print(auxp)
                print("----------------------")
        else:
            print("No hay inscriptos")