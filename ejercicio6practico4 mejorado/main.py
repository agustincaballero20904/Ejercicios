from clrepositorio import RespositorioProvincias
from app import Aplicacion
from clcontrolador import ControladorProvincias
from clobjectencoder import ObjectEncoder


def main():
    conn = ObjectEncoder('provincias.json')
    repo = RespositorioProvincias(conn)
    vista = Aplicacion()
    ctrl = ControladorProvincias(repo, vista)
    vista.setControlador(ctrl)
    ctrl.start()
    ctrl.salirGrabarDatos()

if __name__ == '__main__':
    main()
