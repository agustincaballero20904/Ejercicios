from clpaciente import Paciente
from repopacientes import RepositorioPacientes
from clObjectEncoder import ObjectEncoder
from clcontrolador import ControladorPacientes
from app import aplicacion


if __name__=='__main__':
    conn = ObjectEncoder('pacientes.json')
    repo = RepositorioPacientes(conn)
    apli = aplicacion()
    ctrl = ControladorPacientes(repo, apli)
    apli.setControlador(ctrl)
    ctrl.start()
    ctrl.salirGrabarDatos()
