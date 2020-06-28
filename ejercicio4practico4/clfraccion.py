class Fraccion():
    __num = 0
    __den = 0

    def __init__(self, n, d=1):
        self.__num = n
        self.__den = d

    def getden(self):
        return self.__den

    def getnum(self):
        return self.__num

    def __add__(self, otro):
        numer = self.__num * otro.getden() + self.__den * otro.getnum()
        denom = self.__den * otro.getden()
        return self.simp(numer, denom)

    def __sub__(self, otro):
        numer = self.__num * otro.getden() - self.__den * otro.getnum()
        denom = self.__den * otro.getden()
        return self.simp(numer, denom)

    def __mul__(self, otro):
        numer = self.__num * otro.getnum()
        denom = self.__den * otro.getden()
        return self.simp(numer, denom)

    def __truediv__(self, otro):
        numer = self.__num * otro.getden()
        denom = self.__den * otro.getnum()
        return self.simp(numer, denom)

    def simp(self, n, d):
        if n != d:
            band = True
            z = max(n, d)
            aux = z
            while band:
                if z % n == 0 and z % d == 0:
                    band = False
                else:
                    z += aux
            n = z // n
            d = z // d
            if n == 0:
                res = str(d)
            else:
                res = '{}/{}'.format(d, n)
        else:
            res = '1'
        return res
