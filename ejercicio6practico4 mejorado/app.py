import tkinter as tk
from tkinter import messagebox
from clprovincia import Provincia



class ProvinciaList(tk.Frame):
    def __init__(self, master, **kwargs):
        super().__init__(master)
        self.lb = tk.Listbox(self, **kwargs)
        scroll = tk.Scrollbar(self, command=self.lb.yview)
        self.lb.config(yscrollcommand=scroll.set)
        scroll.pack(side=tk.RIGHT, fill=tk.Y)
        self.lb.pack(side=tk.LEFT, fill=tk.BOTH, expand=1)

    def insertar(self, provincia, index=tk.END):
        text = "{}".format(provincia.getNombre())
        self.lb.insert(index, text)
        
    def borrar(self, index):
        self.lb.delete(index, index)
        
    def modificar(self, provincia, index):
        self.borrar(index)
        self.insertar(provincia, index)

    def bind_doble_click(self, callback):
        handler = lambda _: callback(self.lb.curselection()[0])
        self.lb.bind("<Double-Button-1>", handler)



class ProvinciaForm(tk.LabelFrame):
    def __init__(self, master, fields, **kwargs):
        super().__init__(master, text="Provincia", padx=10, pady=10, **kwargs)
        self.frame = tk.Frame(self)
        self.entries = list(map(self.crearCampo, enumerate(fields)))
        self.frame.pack()

    def crearCampo(self, field):
        position, text = field
        label = tk.Label(self.frame, text=text)
        entry = tk.Entry(self.frame, width=25)
        label.grid(row=position, column=0, pady=5)
        entry.grid(row=position, column=1, pady=5)
        if text == "Temperatura" or text == "Sensacion termica" or text == "Humedad":
            entry.config(state=tk.DISABLED)
        return entry

    def mostrarEstadoProvinciaEnFormulario(self, provincia, fields):
        values = (provincia.getNombre(), provincia.getCapital(),
                  provincia.getHabitantes(), provincia.getDepartamentos(),
                  provincia.getTemperatura(), provincia.getSensacion(),
                  provincia.getHumedad())
        i = 0
        for entry, value in zip(self.entries, values):
            text = fields[i]
            i += 1
            entry.config(state=tk.NORMAL)
            entry.delete(0, tk.END)
            entry.insert(0, value)
            if text == "Temperatura" or text == "Sensacion termica" or text == "Humedad":
                entry.config(state=tk.DISABLED)

    def crearProvinciaDesdeFormulario(self):
        values = [e.get() for e in self.entries]
        if len(values) > 4:
            for i in range(3):
                values.pop()
        provincia = None
        try:
            provincia = Provincia(*values)
        except ValueError as e:
            messagebox.showerror("Error de Validación", str(e), parent=self)
        return provincia

    def limpiar(self):
        fields = ("Nombre", "Capital", "Cantidad de habitantes", "Cantidad de departamentos/partidos", "Temperatura", "Sensacion termica", "Humedad")
        i = 0
        for entry in self.entries:
            text = fields[i]
            i += 1
            entry.config(state=tk.NORMAL)
            entry.delete(0, tk.END)
            if text == "Temperatura" or text == "Sensacion termica" or text == "Humedad":
                entry.config(state=tk.DISABLED)


class BotonesProvForm(ProvinciaForm):
    def __init__(self, master, fields, **kwargs):
        super().__init__(master, fields, **kwargs)
        self.btn_save = tk.Button(self, text="Guardar")
        self.btn_delete = tk.Button(self, text="Borrar")
        self.btn_save.pack(side=tk.RIGHT, ipadx=5, padx=5, pady=5)
        self.btn_delete.pack(side=tk.RIGHT, ipadx=5, padx=5, pady=5)

    def bind_save(self, callback):
        self.btn_save.config(command=callback)

    def bind_delete(self, callback):
        self.btn_delete.config(command=callback)




class NewProvincia(tk.Toplevel):
    fields = ("Nombre", "Capital", "Cantidad de habitantes", "Cantidad de departamentos/partidos")
    def __init__(self, parent):
        super().__init__(parent)
        self.provincia = None
        self.form = ProvinciaForm(self, self.fields)
        self.btn_add = tk.Button(self, text="Confirmar", command=self.confirmar)
        self.form.pack(padx=10, pady=10)
        self.btn_add.pack(pady=10)

    def confirmar(self):
        self.provincia = self.form.crearProvinciaDesdeFormulario()
        if self.provincia:
            self.destroy()

    def show(self):
        self.grab_set()
        self.wait_window()
        return self.provincia



class Aplicacion(tk.Tk):
    fields = ("Nombre", "Capital", "Cantidad de habitantes", "Cantidad de departamentos/partidos", "Temperatura", "Sensacion termica", "Humedad")
    def __init__(self):
        super().__init__()
        self.title("Lista de Provincias")
        self.list = ProvinciaList(self, height=15)
        self.form = BotonesProvForm(self, self.fields)
        self.btn_new = tk.Button(self, text="Agregar Provincia")
        self.list.pack(side=tk.LEFT, padx=10, pady=10)
        self.form.pack(padx=10, pady=10)
        self.btn_new.pack(side=tk.BOTTOM, pady=5)

    def setControlador(self, ctrl):
        self.btn_new.config(command=ctrl.crearProvincia)
        self.list.bind_doble_click(ctrl.seleccionarProvincia)
        self.form.bind_save(ctrl.modificarProvincia)
        self.form.bind_delete(ctrl.borrarProvincia)
        
    def borrarProvincia(self, index):
        self.form.limpiar()
        self.list.borrar(index)
        
    def modificarProvincia(self, provincia, index):
        self.list.modificar(provincia, index)

    def obtenerDetalles(self):
        return self.form.crearProvinciaDesdeFormulario()

    def agregarProvincia(self, provincia):
        self.list.insertar(provincia)

    def verProvinciaEnForm(self, provincia):
        self.form.mostrarEstadoProvinciaEnFormulario(provincia, self.fields)