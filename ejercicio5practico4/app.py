import tkinter as tk
from tkinter import ttk
from listapaciente import PacienList
from botpacform import BotonesPacienForm
from clpaciente import Paciente


class aplicacion(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Lista de Pacientes")
        self.list = PacienList(self, height=15)
        self.form = BotonesPacienForm(self)
        self.btn_new = tk.Button(self, text="Agregar Paciente")
        self.list.pack(side=tk.LEFT, padx=10, pady=10)
        self.form.pack(padx=10, pady=10)
        self.btn_new.pack(side=tk.BOTTOM, pady=5)

    def setControlador(self, ctrl):
        self.btn_new.config(command=ctrl.crearPaciente)
        self.list.bind_doble_click(ctrl.seleccionarPaciente)
        self.form.bind_save(ctrl.modificarPaciente)
        self.form.bind_delete(ctrl.borrarPaciente)
        self.form.bind_IMC(ctrl.mostrarIMC)

    def agregarPaciente(self, paciente):
        self.list.insertar(paciente)

    def modificarPaciente(self, paciente, index):
        self.list.modificar(paciente, index)

    def borrarPaciente(self, index):
        self.form.limpiar()
        self.list.borrar(index)

    def obtenerDetalles(self):
        return self.form.crearPacienteDesdeFormulario()

    def verPacienteEnForm(self, paciente):
        self.form.mostrarEstadoPacienteEnFormulario(paciente)
