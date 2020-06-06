from Lista import Lista
from cldocente import Docente
from clapoyo import PersonaldeApoyo
from clinvestigador import Investigador
from cldocinv import DocenteInvestigador
from ObjectEncoder import ObjectEncoder


class menu:
    __switcher = None

    def __init__(self):
        self.__switcher = {0: self.salir,
                           1: self.opcion1,
                           2: self.opcion2,
                           3: self.opcion3,
                           4: self.opcion4,
                           5: self.opcion5,
                           6: self.opcion6,
                           7: self.opcion7,
                           8: self.opcion8
                           }

    def getswitcher(self):
        return self.__switcher

    def opcion(self, op, lista):
        func = self.__switcher.get(op, lambda: print("Opcion no válida"))
        func(lista)



    def fordocente(self):
        cargoselec = ["simple", "semiexclusivo", "exclusivo"]
        carrera = input("Ingrese carrera: ")
        seleccargo = int(input("Ingrese cargo:\n1: Simple\n2: Semiexclusivo\n3: Exclusivo\n"))
        cargo = cargoselec[seleccargo - 1]
        catedra = input("Ingrese catedra: ")
        return carrera, cargo, catedra

    def forinvestigador(self):
        area = input("Ingrese area de investigacion: ")
        tipo = input("Ingrese tipo de investigacion: ")
        return area, tipo


    def crearagente(self):
        print("Ingrese datos del personal que se desea agregar:")
        cuil = input("Ingrese cuil: ")
        apellido = input("Ingrese apellido: ")
        nombre = input("Ingrese nombre: ")
        sueldobase = int(input("Ingrese sueldo base: "))
        antig = int(input("Ingrese antiguedad: "))
        personal = int(input("Ingrese el tipo de personal:\n1: Docente\n2: Investigador\n3: Personal de apoyo\n4: Docente Investigador\n"))
        if personal == 1:
            carrera, cargo, catedra = self.fordocente()
            agente = Docente(cuil, apellido, nombre, sueldobase, antig, carrera, cargo, catedra)
        else:
            if personal == 2:
                area, tipo = self.forinvestigador()
                agente = Investigador(cuil, apellido, nombre, sueldobase, antig, carrera, cargo, catedra, area, tipo)
            else:
                if personal == 3:
                    categoria = int(input("Ingrese categoria(entre 1 y 22): "))
                    agente = PersonaldeApoyo(cuil, apellido, nombre, sueldobase, antig, categoria)
                else:
                    carrera, cargo, catedra = self.fordocente()
                    area, tipo = self.forinvestigador()
                    extra = int(input("Ingrese extra por docencia e investigacion: "))
                    categoria = int(input("Ingrese categoria:\n1: Categoria I\n2: Categoria II\n3: Categoria III\n4: Categoria IV\n5: Categoria V\n"))
                    agente = DocenteInvestigador(cuil, apellido, nombre, sueldobase, antig, carrera, cargo, catedra, area, tipo, extra, categoria)
        return agente


    def salir(self, lista):
        for agente in lista:
            agente.mostrar()
        print("Salir")


    def opcion1(self, lista):
        try:
            agente = self.crearagente()
            posicion = int(input("Ingrese la posicion en la que agregar el auto: "))
            lista.insertarElemento(agente, posicion)

        except IndexError:
            print("No es posible ingresar en la posicion ingresada")
        except:
            print("La posicion ingresada no es valida")
        else:
            print("Elemento agregado exitosamente")


    def opcion2(self, lista):
        agente = self.crearagente()
        lista.agregarElemento(agente)


    def opcion3(self, lista):
        try:
            posicion = int(input("Ingrese la posicion que desea buscar"))
            agente = lista.buscarElemento(posicion)

        except IndexError:
            print("No es posible ingresar en la posicion ingresada")

        except SyntaxError:
            print("La posicion ingresada no es valida")
        else:
            print(type(agente))
            agente.mostrar()


    def opcion4(self, lista):
        carrera = input("Ingrese carrera en la que buscar: ")
        contar = 0
        lista1 = Lista()
        for agente in lista:
            if type(agente) == DocenteInvestigador:
                carr = agente.getCarrera()
                if carr.lower() == carrera.lower():
                    contar += 1
                    lista1.agregarElemento(agente)
        lista1.ordenar(contar, True)
        for agente in lista1:
            agente.mostrar()


    def opcion5(self, lista):
        area = input("Ingrese area en la que buscar: ")
        contarinv = 0
        contardocinv = 0
        for agente in lista:
            if type(agente) == DocenteInvestigador:
                ar = agente.getArea()
                if ar.lower() == area.lower():
                    contardocinv += 1
            else:
                if type(agente) == Investigador:
                    ar = agente.getArea()
                    if ar.lower() == area.lower():
                        contarinv += 1
        print("En el area {}, trabajan {} investigadores y {} docentes investigadores".format(area, contarinv, contardocinv))


    def opcion6(self, lista):
        lista1 = Lista()
        for agente in lista:
            lista1.agregarElemento(agente)
        contar = lista.getTope()
        lista1.ordenar(contar, False)
        for agente in lista1:
            print("--------------------------")
            print("Apellido: {}\nNombre: {}".format(agente.getApellido(), agente.getNombre()))
            print("Sueldo: {}".format(agente.Sueldo()))

    def opcion7(self, lista):
        try:
            aux = ["i","ii","iii","iv","v"]
            categoria = input("Ingrese una categoria de investigacion(I,II,III,IV,V): ")
            cat = aux.index(categoria.lower()) + 1

        except ValueError:
            print("Categoria invalida")

        else:
            tot = 0
            for agente in lista:
                if type(agente) == DocenteInvestigador:
                    if agente.getCategoria() == cat:
                        print("--------------------------")
                        print("Apellido: {}\nNombre: {}".format(agente.getApellido(), agente.getNombre()))
                        extra = agente.getExtra()
                        tot += extra
                        print("Importe extra:", extra)
            print("--------------------------")
            print("Total de dinero que se debe solicitar al ministerio: ",tot)


    def opcion8(self, lista):
        json = ObjectEncoder()
        d = lista.toJSON()
        json.guardarJSONArchivo(d, 'personal.json')
