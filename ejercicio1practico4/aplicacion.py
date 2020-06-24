from tkinter import *
from tkinter import ttk, font, messagebox
import tkinter as tk

class aplicacion():
    __ventana = None
    __altura = None
    __peso = None
    __imc = None
    __resultado = None
    __comp = None

    def __init__(self):
        self.__ventana = Tk()
        self.__ventana.title("Calculadora de IMC")
        self.__altura = IntVar()
        self.__peso = DoubleVar()
        self.__resultado = DoubleVar(value=0)
        self.__comp = StringVar(value='--Peso--')


        s1 = ttk.Style()
        s1.configure('new1.TLabel',background='#7EFAC3')
        fr1 = ttk.Style()
        fr1.configure('new2.TFrame',background='#FAF7EF')
        s2 = ttk.Style()
        s2.configure('new2.TLabel',background='#FAF7EF')
        s = ttk.Style()
        s.configure('new.TLabel', background='lightgray')
        fr = ttk.Style()
        fr.configure('new.TFrame', background='lightgray')
        titul = font.Font(weight="bold", size=10)

        self.marco = ttk.Frame(self.__ventana, borderwidth=2, relief='groove', style='new2.TFrame')
        self.titu = ttk.Frame(self.marco, style='new.TFrame')
        self.titulo = ttk.Label(self.titu, text="Calculadora de IMC", font=titul, style='new.TLabel')
        self.separ0 = ttk.Separator(self.marco, orient=HORIZONTAL)

        self.contenedor = ttk.Frame(self.marco, padding=(5,5), style='new2.TFrame')
        self.separ1 = ttk.Separator(self.contenedor, orient=HORIZONTAL)
        self.alturalbl = ttk.Label(self.contenedor, text="Altura:", style='new2.TLabel')
        self.altura = ttk.Entry(self.contenedor, textvariable=self.__altura)
        self.altura.bind('<ButtonRelease-1>', self.sacar)
        self.altura.bind('<FocusOut>', self.nosacar)
        self.altura.bind('<Return>', self.botonsito)
        self.cmcont = ttk.Frame(self.contenedor,borderwidth=1, relief='sunken')
        self.cm = ttk.Label(self.cmcont, text="cm", width=3)

        self.separ2 = ttk.Separator(self.contenedor, orient=HORIZONTAL)
        self.pesolbl = ttk.Label(self.contenedor, text="Peso:", style='new2.TLabel')
        self.peso = ttk.Entry(self.contenedor, textvariable=self.__peso)
        self.peso.bind('<ButtonRelease-1>', self.sacar2)
        self.peso.bind('<FocusOut>', self.nosacar2)
        self.peso.bind('<Return>', self.botonsito)
        self.kgcont = ttk.Frame(self.contenedor,borderwidth=1, relief='sunken')
        self.kg = ttk.Label(self.kgcont, text="kg", width=3)

        self.separ3 = ttk.Separator(self.contenedor, orient=HORIZONTAL)
        self.boton1 = tk.Button(self.contenedor, fg='white', bg='green', text="Calcular", command=self.calculo, width=10)
        self.boton2 = tk.Button(self.contenedor, fg='white', bg='green', text="Limpiar", command=self.limpieza, width=10)

        self.contresul = ttk.Button(self.marco, style='new.TFrame')
        self.indmas = ttk.Label(self.contresul, text="Tu Indice de Masa Corporal (IMC) es:", font=font.Font(size=8), style='new1.TLabel')
        self.resul = ttk.Label(self.contresul, textvariable=self.__resultado, font=font.Font(weight="bold", size=8), style='new1.TLabel')
        self.kgms = ttk.Label(self.contresul, text="Kg/m2", font=font.Font(weight="bold", size=8), style='new1.TLabel')

        self.contcomp = ttk.Button(self.marco, style='new.TFrame')
        self.composicion = ttk.Label(self.contcomp, textvariable=self.__comp, font=font.Font(size=10), style='new1.TLabel')


        self.marco.grid(column=0, row=0)
        self.titu.grid(column=0, row=0, sticky=W+E)
        self.titulo.grid(column=0, row=0, padx=(50,0))
        self.separ0.grid(column=0, row=1, sticky=W+E+N)

        self.contenedor.grid(column=0, row=2)
        self.separ1.grid(column=0, row=0, columnspan=4, pady=(10,5),sticky=W+E)
        self.alturalbl.grid(column=0, row=1, sticky='N')
        self.altura.grid(column=1, row=1, columnspan=2, sticky=W+E)
        self.cmcont.grid(column=3, row=1, sticky='W')
        self.cm.grid(column=0, row=0)

        self.separ2.grid(column=0, row=2, columnspan=4, pady=(20,5),sticky=W+E)
        self.pesolbl.grid(column=0, row=3, sticky='N')
        self.peso.grid(column=1, row=3, columnspan=2, sticky=W+E)
        self.kgcont.grid(column=3, row=3, sticky='W')
        self.kg.grid(column=0, row=0)

        self.separ3.grid(column=0, row=4, columnspan=4, pady=(20,5),sticky=W+E)
        self.boton1.grid(column=1, row=5)
        self.boton2.grid(column=2, row=5, padx=(20,0))

        self.contresul.grid(column=0, row=3, pady=(5,0), padx=5)
        self.indmas.grid(column=0, row=0)
        self.resul.grid(column=1, row=0)
        self.kgms.grid(column=2, row=0)

        self.contcomp.grid(column=0, row=4, pady=(0,5))
        self.composicion.grid(column=0, row=0)

        self.__ventana.mainloop()


    def calculo(self):
        
        compo = ["Peso inferior al normal", "Peso Normal", "Peso superior al normal", "Obesidad"]
        
        try:
            alt = self.__altura.get()
            pes = self.__peso.get()
        except:
            messagebox.showerror(title="Error de tipo", message="Debe ingresar un valor numerico de peso y altura")
            self.limpieza()
        else:
            if pes != 0 and alt !=0:
                elcuadrado = alt * alt / 10000
                self.__resultado.set(round(pes / elcuadrado, 2))
                imc = self.__resultado.get()
                if imc < 18.5:
                    i = 0
                else:
                    if imc < 25:
                        i = 1
                    else:
                        if imc < 30:
                            i = 2
                        else:
                            i = 3
                self.__comp.set(compo[i])
            else:
                messagebox.showerror(title="Error de tipo", message="Debe ingresar un valor de peso y altura")

    def limpieza(self):
        self.__altura.set(0)
        self.__peso.set(0.0)
        self.__resultado.set(0)
        self.__comp.set('--Peso--')

    def sacar(self, event):
        if self.__altura.get() == 0:
            self.altura.delete(0,1)

    def sacar2(self, event):
        if self.__peso.get() == 0:
            self.peso.delete(0,3)

    def nosacar(self, event):
        if self.altura.get() == '':
            self.__altura.set(0)

    def nosacar2(self, event):
        if self.peso.get() == '':
            self.__peso.set(0.0)

    def botonsito(self, event):
        self.calculo()


if __name__ == '__main__':
    app = aplicacion()
