import csv
from Libro import libro


class manejalibros:
    __listalibro = []

    def __init__(self):
        self.__listalibro = []

    def cargardatos(self):
        archivo = open("libros.csv")
        reader = csv.reader(archivo, delimiter=",")
        for fila in reader:
            if len(fila) > 2:
                unlibro = libro(int(fila[0]), fila[1], fila[2], fila[3], int(fila[4]), int(fila[5]))
                self.__listalibro.append(unlibro)
            else:
                x = len(self.__listalibro) - 1
                self.__listalibro[x].addcapitulo(fila[0], int(fila[1]))


    def buscaidentif(self, id):
        print(id)
        if type(id) == int:
            j = 0
            x = len(self.__listalibro)-1
            i = self.__listalibro[j].getid()
            print(i)
            while (id != i) and (j != x):
                j += 1
                i = self.__listalibro[j].getid()
            if id != i:
                print("No se encuentra ningun libro con ese identificador")
            else:
                self.__listalibro[j].mostrar()
        else:
            print("Dato ingresado no valido")

    def buscarpalabra(self, palabra):
        print("Libros con la palabra ", palabra)
        for i in range(len(self.__listalibro)):
            self.__listalibro[i].buscapalabra(palabra)
