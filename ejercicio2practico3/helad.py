from sabores import sabor


class helado:
    __gramos = 0
    __sabpedid = []

    def __init__(self, gr):
        int(gr)
        if gr == 100 or gr == 150 or gr == 250 or gr == 500 or gr == 1000:
            self.__gramos = gr
        self.__sabpedid = []

    def addsab(self, unsabor):
        if type(unsabor) == sabor:
            self.__sabpedid.append(unsabor)

    def compara(self, nomsab):
        repet = 0
        for i in range(len(self.__sabpedid)):
            if nomsab == self.__sabpedid[i].darnum():
                repet += 1
        return int(self.__gramos*repet/len(self.__sabpedid))

    def getsabs(self):
        l = self.__sabpedid
        return l

    def getpeso(self):
        return self.__gramos
