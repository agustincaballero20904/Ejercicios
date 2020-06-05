# -*- coding: utf-8 -*-
"""
Created on Mon May 18 14:30:25 2020

@author: alumno
"""


class capitulo:

    __titulo = ""
    __cantidadpaginas = 0

    def __init__(self, titu, pags):
        self.__titulo = titu
        self.__cantidadpaginas = pags

    def gettitu(self):
        return self.__titulo

    def getpags(self):
        return self.__cantidadpaginas
