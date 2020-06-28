import tkinter as tk
from tkinter import ttk
from functools import partial
from clfraccion import Fraccion


class aplicacion(tk.Tk):
    __operador = None
    __primero = None
    __segundo = None
    __texto = None

    def __init__(self):
        super().__init__()
        self.title('Calculadora')
        self.resizable(0, 0)
        self.__operador = tk.StringVar(value='')
        self.__segundo = tk.StringVar(value='')
        self.__primero = tk.StringVar(value='')
        self.__texto = tk.StringVar()

        mainframe = ttk.Frame(self, borderwidth=2, relief='sunken', padding=5).grid(column=0, row=0)

        resultados = ttk.Entry(mainframe, textvariable=self.__texto, justify='right', state='disabled').grid(column=1, row=0, columnspan=3, sticky='W E')
        ttk.Button(mainframe, text='C', command=self.limpiar).grid(column=0,row=0)

        ttk.Button(mainframe, text='1', command=partial(self.ponernum, '1')).grid(column=0,row=1)
        ttk.Button(mainframe, text='2', command=partial(self.ponernum, '2')).grid(column=1,row=1)
        ttk.Button(mainframe, text='3', command=partial(self.ponernum, '3')).grid(column=2,row=1)
        ttk.Button(mainframe, text='4', command=partial(self.ponernum, '4')).grid(column=0,row=2)
        ttk.Button(mainframe, text='5', command=partial(self.ponernum, '5')).grid(column=1,row=2)
        ttk.Button(mainframe, text='6', command=partial(self.ponernum, '6')).grid(column=2,row=2)
        ttk.Button(mainframe, text='7', command=partial(self.ponernum, '7')).grid(column=0,row=3)
        ttk.Button(mainframe, text='8', command=partial(self.ponernum, '8')).grid(column=1,row=3)
        ttk.Button(mainframe, text='9', command=partial(self.ponernum, '9')).grid(column=2,row=3)
        ttk.Button(mainframe, text='0', command=partial(self.ponernum, '0')).grid(column=0,row=4)
        ttk.Button(mainframe, text='+', command=partial(self.ponerop, '+')).grid(column=3,row=1)
        ttk.Button(mainframe, text='-', command=partial(self.ponerop, '-')).grid(column=3,row=2)
        ttk.Button(mainframe, text='*', command=partial(self.ponerop, '*')).grid(column=3,row=3)
        ttk.Button(mainframe, text='%', command=partial(self.ponerop, '%')).grid(column=3,row=4)
        ttk.Button(mainframe, text='=', command=self.calcular).grid(column=2,row=4)
        ttk.Button(mainframe, text='⬚/⬚', command=partial(self.ponernum, '/')).grid(column=1,row=4)

        self.__texto.set('0')

    def limpiar(self):
        self.__texto.set('0')
        self.__primero.set('')
        self.__segundo.set('')
        self.__operador.set('')


    def fraccion(self, num):
        if num == '' or num == '0':
            val1 = '0'
            val2 = ''
        else:
            if num.find('/') == -1:
                val1 = num + '/'
                val2 = val1
            else:
                val1 = num
                val2 = val1
        return (val1, val2)

    def ponernum(self, num):
        if self.__operador.get() == '':
            if num == '/':
                val1, val2 = self.fraccion(self.__primero.get())
            else:
                val1 = self.__primero.get() + num
                val2 = val1
            self.__texto.set(val1)
            self.__primero.set(val2)
        else:
            if num == '/':
                val1, val2 = self.fraccion(self.__segundo.get())
            else:
                val1 = self.__segundo.get() + num
                val2 = val1
            self.__texto.set(self.__primero.get()+self.__operador.get()+val1)
            self.__segundo.set(val2)


    def ponerop(self, op):
        if self.__operador.get() == '':
            if self.__primero.get() == '':
                self.__primero.set(self.__texto.get())
        else:
            self.calcular()
            self.ponernum(self.__texto.get())
        self.__operador.set(op)
        self.__texto.set(self.__texto.get()+op)


    def calcular(self):
        prim = self.__primero.get()
        seg = self.__segundo.get()
        operad = self.__operador.get()
        if seg == '':
            self.__segundo.set('0')
        if prim.find('/') == -1 and seg.find('/') == -1:
            resultado = self.obtres(int(prim), int(seg), operad)
        else:
            op1 = prim.split('/')
            op2 = seg.split('/')
            try:
                op1 = Fraccion(int(op1[0]), int(op1[1]))
            except:
                op1 = Fraccion(int(op1[0]))
            try:
                op2 = Fraccion(int(op2[0]), int(op2[1]))
            except:
                op2 = Fraccion(int(op2[0]))
            resultado = self.obtres(op1, op2, operad)

        self.limpiar()
        self.__texto.set(resultado)

    def obtres(self, op1, op2, operad):
        if operad == '+':
            resultado = op1 + op2
        else:
            if operad == '-':
                resultado = op1 - op2
            else:
                if operad == '*':
                    resultado = op1 * op2
                else:
                    if operad == '%':
                        if op2 != 0:
                            resultado = op1 / op2
                        else:
                            resultado = 'Error X/0'
        return resultado


if __name__ == '__main__':
    app = aplicacion()
    app.mainloop()
