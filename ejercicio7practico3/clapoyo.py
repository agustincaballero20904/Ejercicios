from clpersonal import Personal


class PersonaldeApoyo(Personal):
    __categoria = 0

    def __init__(self, cuil, apellido, nombre, sueldobase, antig, categoria):
        super().__init__(cuil, apellido, nombre, sueldobase, antig)
        self.__categoria = int(categoria)

    def mostrar(self):
        super().mostrar()
        print("Datos Personal de apoyo")
        print("Categoria: {}".format(self.__categoria))

    def Sueldo(self):
        base = super().getSueldobase()
        antig = super().getAntig()
        uno = base / 100
        sueldo = base + uno*antig
        if self.__categoria in range(1, 11):
            sueldo += uno*10
        else:
            if self.__categoria in range(11,21):
                sueldo += uno*20
            else:
                if self.__categoria == 21 or self.__categoria == 22:
                    sueldo += uno*30
        return sueldo

    def toJSON(self):
        d = dict(
            __class__=self.__class__.__name__,
            atributos=dict(
                cuil = super().getCuil(),
                apellido = super().getApellido(),
                nombre = super().getNombre(),
                sueldobase = super().getSueldobase(),
                antig = super().getAntig(),
                categoria = self.__categoria
            )
        )
        return d
