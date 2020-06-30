import tkinter as tk


class imc(tk.Toplevel):
    compo = ("Peso inferior al normal", "Peso Normal", "Peso superior al normal", "Obesidad")
    __composicionentry = None
    __imcentry = None

    def __init__(self, parent, altura, peso):
        super().__init__(parent)
        self.title('IMC')
        self.altura = int(altura)
        self.peso = int(peso)
        self.__composicionentry = tk.StringVar()
        self.__imcentry = tk.StringVar()
        tk.Label(self, text='IMC').grid(column=0, row=0, pady=5)
        self.imcentry = tk.Entry(self, textvariable=self.__imcentry, state='disabled')
        tk.Label(self, text='Composicion corporal').grid(column=0, row=1, pady=5)
        self.composicionentry = tk.Entry(self, textvariable=self.__composicionentry, state='disabled')
        self.btn_volver = tk.Button(self, text="Volver", command=self.destroy)
        self.imcentry.grid(column=1, row=0, pady=5)
        self.composicionentry.grid(column=1, row=1, pady=5)
        self.btn_volver.grid(column=0, row=2, columnspan=2, pady=(25, 10))
        self.calcular()

    def calcular(self):
        elcuadrado = self.altura * self.altura / 10000
        imcal = round(self.peso / elcuadrado, 2)
        self.__imcentry.set(str(imcal))
        if imcal < 18.5:
            i = 0
        else:
            if imcal < 25:
                i = 1
            else:
                if imcal < 30:
                    i = 2
                else:
                    i = 3
        self.__composicionentry.set(self.compo[i])

    def show(self):
        self.grab_set()
        self.wait_window()
