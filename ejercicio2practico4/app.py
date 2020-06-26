from tkinter import *
from tkinter import ttk, messagebox
import requests


class aplicacion():
    __ventana = None
    __peso = None
    __dolar = None

    def __init__(self):
        self.__ventana = Tk()
        self.__ventana.geometry('290x115')
        self.__ventana.title('Conversor de moneda')
        self.__peso = StringVar()
        self.__dolar = StringVar()
        self.__dolar.trace('w', self.calcular)

        mainframe = ttk.Frame(self.__ventana, padding='5 5 12 7', borderwidth=2, relief='sunken')
        mainframe.grid(column=0, row=0, sticky=(N,W,E,S))
        mainframe.columnconfigure(0, weight=1)
        mainframe.rowconfigure(0, weight=1)

        self.dolarentry = ttk.Entry(mainframe,width=7, textvariable=self.__dolar)
        self.dolarentry.grid(column=2, row=1, sticky=(W,E))
        ttk.Label(mainframe, textvariable=self.__peso).grid(column=2, row=2, sticky=(W,E))

        ttk.Button(mainframe, text="Salir", command=self.__ventana.destroy).grid(column=3, row=3, sticky=W)
        ttk.Label(mainframe, text="pesos").grid(column=3, row=2, sticky=W)
        ttk.Label(mainframe, text="es equivalente a").grid(column=1, row=2, sticky=E)
        ttk.Label(mainframe, text="dolares").grid(column=3, row=1, sticky=W)

        for child in mainframe.winfo_children():
            child.grid_configure(padx=5, pady=5)
        self.dolarentry.focus()
        self.__ventana.mainloop()

    def calcular(self, *args):
        complete_url = 'https://www.dolarsi.com/api/api.php?type=dolar'
        r = requests.get(complete_url)
        v = r.json()
        band = True
        i=0
        valventa = 0
        while i in range(len(v)) and band:
            a = v[i]
            b = list(a['casa'].items())
            if b[0][1] == 'Oficial':
                j=1
                while j in range(len(b)) and band:
                    if b[j][0] == 'venta':
                        valventa = b[j][1]
                        valventa = valventa.replace(',','.')
                        band = False
                    j += 1
            i += 1

        if self.dolarentry.get() != '':
            try:
                valor = self.dolarentry.get()
                valor = float(valor.replace(',','.'))
                self.__peso.set(round(valor * float(valventa),2))
            except ValueError:
                messagebox.showerror(title='Error de tipo', message='Debe ingresar un valor numerico')
                self.__dolar.set('')
                self.__dolarentry.focus()
        else:
            self.__peso.set('')


if __name__ == '__main__':
    app = aplicacion()
