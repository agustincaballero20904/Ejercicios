from manejahelad import manejadorhelado
from manejasabores import manejasabor
from helad import helado


class Menu:
    __switcher = None

    def __init__(self):
        self.__switcher = {1: self.opcion1,
                           2: self.opcion2,
                           3: self.opcion3,
                           4: self.opcion4,
                           0: self.salir
                           }

    def getswitcher(self):
        return self.__switcher

    def opcion(self, op, hela, sabo, venta):
        func = self.__switcher.get(op, lambda: print("Opcion no válida"))
        if op == 0:
            func()
        else:
            func(hela, sabo, venta)

    def salir(self):
        print("Salir")

    def opcion1(self, hela, sabo, venta):
        pesos = [100, 150, 250, 500, 1000]
        sal = False
        while not sal:
            gramos = int(input("Elija el tipo de helado:\n1: 100gr\n2: 150gr\n3: 250gr\n4: 500gr\n5: 1000gr"))
            sal = gramos in range(1,6)
            if not sal:
                print("Opción no válida")

        unhelado = helado(pesos[gramos-1])
        sab = gramos
        if sab > 2:
            sab -= 1

        print("Para este tipo de helados puede seleccionar hasta {} sabores".format(sab))
        print("----------Sabores----------")
        print(sabo)

        i = 0
        while i < sab:
            saborselecc = int(input("Seleccione un numero de sabor"))
            if saborselecc in range(len(venta)+1):
                venta[saborselecc-1] += 1
                sabo.addsabped(unhelado, saborselecc-1)
                i += 1
                print("Sabor añadido")
            else:
                print("No existe ese numero de sabor")
        print(gramos)
        hela.addpedido(unhelado)

    def opcion2(self, hela, sabo, venta):
        venta2 = venta[:]
        cont = 0
        i = 0
        d = len(venta2)
        maximo = -1
        band = False
        if d > 5:
            d = 5
        print("Los cinco sabores mas pedidos son:")
        while not band and i < len(venta2):
            if venta2[i] >= maximo:
                maximo = venta2[i]
                j = i
            i += 1
            if i == len(venta2):
                i = 0
                cont += 1
                if maximo != -1:
                    print("-{}, con {} ventas".format(sabo.getnombre(j),maximo))
                    maximo = -1
                    venta2[j] = -1
            if cont == d:
                band = True

    def opcion3(self, hela, sabo, venta):
        print("----------Sabores----------")
        print(sabo)
        sabele = int(input("Ingrese un numero de sabor:"))
        hela.calculapeso(sabele)

    def opcion4(self, hela, sabo, venta):
        pesos = [100, 150, 250, 500, 1000]
        tiphel = int(input("Elija el tipo de helado:\n1: 100gr\n2: 150gr\n3: 250gr\n4: 500gr\n5: 1000gr"))
        hela.mostrasabor(pesos[tiphel-1])
