from zope.interface import Interface


class IGerente (Interface):

    def modificarBasicoEPlanta(dni, nuevoBasico):
        pass

    def modificarViaticoEExterno(dni, nuevoViatico):
        pass

    def modificarValorEPorHora(nuevoValorHora):
        pass