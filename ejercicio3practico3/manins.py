from clpersona import Persona
from clinscripcion import Inscripcion
from cltaller import TallerCapacitacion

class manejins:
    __lista = []

    def __init__(self):
        self.__lista = []

    def inscribir(self, person, eltaller):
        if type(person) == Persona:
            if type(eltaller) == TallerCapacitacion:
                unainscrip = eltaller.inscribir(Inscripcion(person, eltaller))
                self.__lista.append(unainscrip)

    def buscarpers(self, dni):
        band = True
        i = 0
        while band and i < len(self.__lista):
            auxp = self.__lista[i].getpers()
            if auxp.getdni() == dni:
                band = False
            else:
                i += 1

        if not band:
            auxt = self.__lista[i].gettaller()
            print("Esta persona se inscribio en el taller ", auxt.getnombre())
            if not self.__lista[i].getpago():
                print("Adeuda {}".format(auxt.getmonto()))
            else:
                print("No adeuda pago")
        else:
            print("No seinscribio en ningun taller")

    def cambiarpago(self, dni):
        band = True
        i = 0
        while band and i < len(self.__lista):
            auxp = self.__lista[i].getpers()
            if auxp.getdni() == dni:
                band = False
            else:
                i += 1

        if not band:
            self.__lista[i].setPago(True)
            print("Se registro el pago")

    def toJSON(self):
        d = dict(
            __class__=self.__class__.__name__,
            lista=[ins.toJSON() for ins in self.__lista]
        )
        print(d)
        return d
