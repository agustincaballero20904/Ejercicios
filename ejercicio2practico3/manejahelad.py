from helad import helado
from sabores import sabor


class manejadorhelado:
    __listapedidos = []

    def __init__(self):
        self.__lista = []

    def addpedido(self, unpedido):
        if type(unpedido) == helado:
            self.__listapedidos.append(unpedido)

    def calculapeso(self, nomsab):
        cont = 0
        j = len(self.__listapedidos)
        for w in range(j):
            cont += self.__listapedidos[w].compara(nomsab)
        print("Se vendieron {}gr del sabor {}".format(cont, nomsab))

    def mostrasabor(self, tipo):
        sabs = []
        for i in range(len(self.__listapedidos)):
            if self.__listapedidos[i].getpeso() == tipo:
                if sabs == []:
                    sabs = self.__listapedidos[i].getsabs()
                else:
                    k = self.__listapedidos[i].getsabs()
                    for j in range(len(k)):
                        w = 0
                        while k[j] != sabs[w] and w < len(sabs):
                            w += 1
                            if w == len(sabs):
                                if k[j] != sabs[w-1]:
                                    sabs.append(k[j])
        print("Sabores pertenecientes al tipo de helado ingresado:")
        for n in range(len(sabs)):
            print(sabs[n])
