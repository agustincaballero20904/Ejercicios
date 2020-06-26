import tkinter as tk
from tkinter import ttk
from datetime import datetime
import requests
import json
from pathlib import Path


class aplicacion(tk.Tk):
    __horaact = None

    def __init__(self):
        super().__init__()
        self.title('Cambios dolar')
        self.__horaact = tk.StringVar()

        self.listita = ttk.Frame(self)
        self.listita.grid(column=0,row=0,columnspan=2, pady=5, padx=5)
        self.lista = tk.Listbox(self.listita, height=7, width=100, fg='white', bg='black')
        scroll = tk.Scrollbar(self.listita, command=self.lista.yview)
        self.lista.config(yscrollcommand=scroll.set)
        scroll.grid(column=0, row=0, sticky=('E', 'N', 'S'))
        self.lista.grid(column=0, row=0, sticky=('W', 'N', 'S'))

        lab1 = ttk.Label(self, text='Ultima vez actualizado:').grid(column=0,row=1,sticky='E')
        lab2 = ttk.Label(self, textvariable=self.__horaact).grid(column=1, row=1,sticky='W')
        but1 = ttk.Button(self, text='Actualizar', command=self.actualiza).grid(column=0,row=2,columnspan=2, pady=5)

        try:
            with Path("datos.json").open(encoding="UTF-8") as fuente:
                diccionario = json.load(fuente)
                fuente.close()
            datos = diccionario
            self.__horaact.set(datos['hora'])
            ainser = datos['dolares']
            for valores in ainser:
                self.insertar(valores)
        except:
            self.actualiza()


    def insertar(self, dato):
        self.lista.insert(tk.END, dato)

    def actualiza(self):
        self.lista.delete(0, tk.END)
        complete_url = 'https://www.dolarsi.com/api/api.php?type=valoresprincipales'
        r = requests.get(complete_url)
        v = r.json()
        for i in v:
            a = list(i['casa'].items())
            band = True
            j = 0
            valorventa = 0
            valorcompra = 0
            nombre = ''
            while j in range(len(a)) and band:
                if a[j][0] == 'nombre':
                    if a[j][1].find("Dolar") == -1:
                        band = False
                    else:
                        nombre = a[j][1]
                else:
                    if a[j][0] == 'venta':
                        valorventa, band = self.probar(a[j][1])
                    else:
                        if a[j][0] == 'compra':
                            valorcompra, band = self.probar(a[j][1])
                j += 1

            if band:
                text = "Nombre: {}, Valor compra: {}, Valor venta: {}".format(nombre, valorcompra, valorventa)
                self.insertar(text)

        self.__horaact.set(datetime.time(datetime.today()).isoformat(timespec='minutes'))
        d = self.toJSON()
        with Path("datos.json").open('w',encoding="UTF-8") as destino:
                json.dump(d, destino, indent=4)
                destino.close()

    def probar(self, valor):
        bandera = True
        valor = valor.replace('.','')
        valor = valor.replace(',','.')
        try:
            valorv = float(valor)
        except ValueError:
            bandera = False
            valorv = 0
        else:
            if valorv <= 0:
                bandera = False
        finally:
            return(valorv, bandera)


    def toJSON(self):
        d = dict(
            hora = self.__horaact.get(),
            dolares = self.lista.get(0, tk.END)
        )
        return d

if __name__ == '__main__':
    app = aplicacion()
    app.mainloop()
