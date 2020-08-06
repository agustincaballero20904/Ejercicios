import requests


class Provincia(object):
    __nombre = None
    __capital = None
    __habitantes = None
    __departamentos = None

    def __init__(self, nombre, capital, habitantes, departamentos):
        self.__nombre = self.requerido(nombre, 'Nombre de provincia es un valor requerido')
        self.__capital = self.verificaCapital(capital, 'La capital ingresada no es un nombre de ciudad valido', 'Capital es un valor requerido')
        self.__habitantes = self.requerido(habitantes, 'La cantidad de habitantes es un valor requerido')
        self.__departamentos = self.requerido(departamentos, 'La cantidad de departamentos es un valor requerido')

    def getCapital(self):
        return self.__capital

    def getNombre(self):
        return self.__nombre

    def getHabitantes(self):
        return self.__habitantes

    def getDepartamentos(self):
        return self.__departamentos

    def getJson(self, capi):
        complete_url = 'https://api.openweathermap.org/data/2.5/weather?q='+ capi +'&units=metric&appid=9fa1d4da7f3fd09739c2ccf02aea28f9'
        r = requests.get(complete_url)
        v = r.json()
        return v

    def getTemperatura(self):
        v = self.getJson(self.__capital)
        return v["main"]["temp"]

    def getSensacion(self):
        v = self.getJson(self.__capital)
        return v["main"]["feels_like"]

    def getHumedad(self):
        v = self.getJson(self.__capital)
        return v["main"]["humidity"]

    def requerido(self, valor, mensaje):
        if not valor:
            raise ValueError(mensaje)
        return valor

    def verificaCapital(self, valor, mensaje, mensaje2):
        if not valor:
            raise ValueError(mensaje2)
        else:
            v = self.getJson(valor)
            try:
                v["main"]
            except:
                raise ValueError(mensaje)
        return valor

    def toJSON(self):
        d = dict(
                __class__=self.__class__.__name__,
                __atributos__=dict(
                                    nombre=self.__nombre,
                                    capital=self.__capital,
                                    habitantes=self.__habitantes,
                                    departamentos=self.__departamentos
                                )
                )
        return d