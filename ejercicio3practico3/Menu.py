from clpersona import Persona
from manpers import manejaper
from mantaller import manejataller
from manins import manejins
from cltaller import TallerCapacitacion
from objectEncoder import ObjectEncoder


class menu:
    __switcher = None

    def __init__(self):
        self.__switcher = {0: self.salir,
                           1: self.opcion1,
                           2: self.opcion2,
                           3: self.opcion3,
                           4: self.opcion4,
                           5: self.opcion5
                           }

    def getswitcher(self):
        return self.__switcher

    def opcion(self, op, arrp, arrt, listains):
        func = self.__switcher.get(op, lambda: print("Opcion no válida"))
        if op == 0:
            func()
        else:
            if op == 1:
                func(arrp, arrt, listains)
            else:
                if op == 3:
                    func(arrt)
                else:
                    func(listains)

    def salir(self):
        print("Salir")

    def opcion1(self, arrp, arrt, listains):
        print("\n-----Talleres-----")
        arrt.listartalleres()
        taller = int(input("\nIngrese el id del taller al que desea inscribirse: "))
        auxtaller = arrt.getporid(taller)
        if auxtaller != None:
            if auxtaller.getvac() != 0:
                print("Ingreso de datos de la persona a inscribir: ")
                nom = input("Ingrese el nombre: ")
                direcc = input("Ingrese la direccion: ")
                dni = input("Ingrese el dni: ")
                auxpersona = Persona(nom, direcc, dni)
                listains.inscribir(auxpersona, auxtaller)
            else:
                print("\nNo hay vacantes en el taller")
        else:
            print("\nId de taller incorrecto")

    def opcion2(self, listains):
        dni = input("Ingrese el dni: ")
        listains.buscarpers(dni)

    def opcion3(self, arrt):
        print("\n-----Talleres-----")
        arrt.listartalleres()
        idt = int(input("Ingrese id del taller: "))
        auxt = arrt.getporid(idt)
        if auxt != None:
            print("\n-----Alumnos inscriptos-----")
            auxt.listarinscriptos()
        else:
            print("Id de taller incorrecto")

    def opcion4(self, listains):
        dni = input("Ingrese el dni: ")
        listains.cambiarpago(dni)

    def opcion5(self, listains):
        json = ObjectEncoder()
        json.guardarJSONArchivo(listains.toJSON(), 'ins.json')
