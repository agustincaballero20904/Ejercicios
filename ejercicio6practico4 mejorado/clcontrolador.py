from app import Aplicacion, NewProvincia
from clmanejador import ManejadorProvincias



class ControladorProvincias(object):
    def __init__(self, repo, vista):
        self.repo = repo
        self.vista = vista
        self.seleccion = -1
        self.provincias = list(repo.obtenerListaProvincias())

    def crearProvincia(self):
        nuevaProvincia = NewProvincia(self.vista).show()
        if nuevaProvincia:
            provincia = self.repo.agregarProvincia(nuevaProvincia)
            self.provincias.append(provincia)
            self.vista.agregarProvincia(provincia)

    def seleccionarProvincia(self, index):
        self.seleccion = index
        provincia = self.provincias[index]
        self.vista.verProvinciaEnForm(provincia)

    def start(self):
        for c in self.provincias:
            self.vista.agregarProvincia(c)
        self.vista.mainloop()

    def salirGrabarDatos(self):
        self.repo.grabarDatos()


    def modificarProvincia(self):
        if self.seleccion == -1:
            return
        rowid = self.provincias[self.seleccion].rowid
        detallesPaciente = self.vista.obtenerDetalles()
        detallesPaciente.rowid = rowid
        provincia = self.repo.modificarProvincia(detallesPaciente)
        self.provincias[self.seleccion] = provincia
        self.vista.modificarProvincia(provincia, self.seleccion)
        self.seleccion = -1

    def borrarProvincia(self):
        if self.seleccion == -1:
            return
        provincia = self.provincias[self.seleccion]
        self.repo.borrarProvincia(provincia)
        self.provincias.pop(self.seleccion)
        self.vista.borrarProvincia(self.seleccion)
        self.seleccion = -1
