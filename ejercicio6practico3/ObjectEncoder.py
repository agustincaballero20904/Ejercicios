import json
from pathlib import Path
from clnuevo import nuevo
from clusado import usado
from clvehiculo import vehiculo
from Lista import Lista
from clnodo import Nodo


class ObjectEncoder(object):

    def decodificarDiccionario(self, d):
        if '__class__' not in d:
            return d
        else:
            class_name = d['__class__']
            class_ = eval(class_name)
            if class_name == 'Lista':
                nodos = d['nodos']
                lista = class_()
                for i in range(len(nodos)):
                    nodo = nodos[i]
                    class_name = nodo.pop('__class__')
                    class_ = eval(class_name)
                    atributos = nodo['atributos']
                    unauto = class_(**atributos)
                    lista.agregarElemento(unauto)
            return lista

    def guardarJSONArchivo(self, diccionario, archivo):
        with Path(archivo).open("w", encoding="UTF-8") as destino:
            json.dump(diccionario, destino, indent=4)
            destino.close()

    def leerJSONArchivo(self,archivo):
        with Path(archivo).open(encoding="UTF-8") as fuente:
            diccionario=json.load(fuente)
            fuente.close()
            return diccionario
