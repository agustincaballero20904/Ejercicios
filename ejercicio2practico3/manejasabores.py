import csv
from sabores import sabor
from helad import helado


class manejasabor:
    __listasabores = []
    
    def __init__(self):
        self.__listasabores = []

    def obtenernum(self):
        return (len(self.__listasabores)+1)

    def __str__(self):
        print("-----Lista de sabores-----")
        for i in range(len(self.__listasabores)):
            print(self.__listasabores[i])
        return "---------------"

    def addsabped(self, unhelado, numsab):
        if type(unhelado) == helado:
            unhelado.addsab(self.__listasabores[numsab])

    def getlong(self):
        return len(self.__listasabores)

    def getnombre(self, num):
        return self.__listasabores[num].darnombre()

    def cargardatos(self):
        archivo = open("sabores.csv")
        reader = csv.reader(archivo, delimiter=",")
        for fila in reader:
            sabr = sabor(self.obtenernum(), fila[0], fila[1])
            self.__listasabores.append(sabr)
