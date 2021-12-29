from PyQt5.QtCore import QObject, pyqtSignal
from PyQt5 import QtMultimedia
import parametros as p


class Troncos(QObject):

    def __init__(self, identificador, direccion, posicionX, posicionY):
        super().__init__()
        self.identificador = identificador
        self.__posicionX = posicionX
        self.__posicionY = posicionY
        self.direccion = direccion  # Si es 1 se mueve a la izq, si es -1 se mueve a la derecha

    @property
    def posicionX(self):
        return self.__posicionX

    @posicionX.setter
    def posicionX(self, k):
        if k > p.MAX_X + p.WIDTH_FROGG:
            self.__posicionX = p.MIN_X - p.WIDTH_FROGG
        elif k < p.MIN_X - p.WIDTH_FROGG:
            self.__posicionX = p.MAX_X + p.WIDTH_FROGG
        else:
            self.__posicionX = k

    @property
    def posicionY(self):
        return self.__posicionY

    @posicionY.setter
    def posicionY(self, k):
        if k > p.MAX_Y:
            self.__posicionY = p.MAX_Y
        elif k < p.MIN_Y:
            self.__posicionY = p.MIN_Y
        else:
            self.__posicionY = k

    def movimiento(self, velocidad):
        self.posicionX += velocidad*self.direccion
        return (self.posicionX, self.posicionY)


class Autos(QObject):

    def __init__(self, identificador, direccion, posicionX, posicionY):
        super().__init__()
        self.identificador = identificador
        self.__posicionX = posicionX
        self.__posicionY = posicionY
        self.direccion = direccion  # Si es 1 se mueve a la izq, si es -1 se mueve a la derecha

    @property
    def posicionX(self):
        return self.__posicionX

    @posicionX.setter
    def posicionX(self, k):
        if k > p.MAX_X + p.WIDTH_FROGG:
            self.__posicionX = p.MIN_X - p.WIDTH_FROGG
        elif k < p.MIN_X - p.WIDTH_FROGG:
            self.__posicionX = p.MAX_X + p.WIDTH_FROGG
        else:
            self.__posicionX = k

    @property
    def posicionY(self):
        return self.__posicionY

    @posicionY.setter
    def posicionY(self, k):
        if k > p.MAX_Y:
            self.__posicionY = p.MAX_Y
        elif k < p.MIN_Y:
            self.__posicionY = p.MIN_Y
        else:
            self.__posicionY = k

    def movimiento(self, velocidad):
        self.posicionX += velocidad*self.direccion
        return (self.posicionX, self.posicionY)


class Objeto(QObject):

    def __init__(self, tipo, posicionX, posicionY):
        super().__init__()
        self.tipo = tipo
        self.posicionX = posicionX
        self.posicionY = posicionY
        self.activo = True


class Frogg(QObject):
    senal_mover = pyqtSignal(str, tuple)

    def __init__(self):
        super().__init__()
        self.direccion = "R"
        self.salto = False
        self.__posicionX = p.POS_INICIO_FROGG[0]
        self.__posicionY = p.POS_INICIO_FROGG[1]

    @property
    def posicionX(self):
        return self.__posicionX

    @posicionX.setter
    def posicionX(self, k):
        if k > p.MAX_X:
            self.__posicionX = p.MAX_X
        elif k < p.MIN_X:
            self.__posicionX = p.MIN_X
        else:
            self.__posicionX = k

    @property
    def posicionY(self):
        return self.__posicionY

    @posicionY.setter
    def posicionY(self, k):
        if k > p.MAX_Y:
            self.__posicionY = p.MAX_Y
        elif k < p.MIN_Y:
            self.__posicionY = p.MIN_Y
        else:
            self.__posicionY = k

    def cambiar_direccion(self, nueva_direccion):
        # Cambia la direccion segun la letra
        if nueva_direccion.upper() in "URDL":
            self.direccion = nueva_direccion
            self.salto = False
        elif nueva_direccion.upper() in "J":
            self.salto = True

    def avanzar(self):  # Genera el movimiento
        minimo = self.posicionY - p.VELOCIDAD_CAMINAR >= p.Y_MAX_RIO
        maximo = self.posicionY <= p.Y_MIN_RIO
        if maximo or minimo or self.salto:
            if self.direccion == "R":
                if self.salto:
                    self.posicionX += p.PIXELES_SALTO
                else:
                    self.posicionX += p.VELOCIDAD_CAMINAR
            elif self.direccion == "L":
                if self.salto:
                    self.posicionX -= p.PIXELES_SALTO
                else:
                    self.posicionX -= p.VELOCIDAD_CAMINAR
            elif self.direccion == "U":
                if self.salto:
                    self.posicionY -= p.PIXELES_SALTO
                else:
                    self.posicionY -= p.VELOCIDAD_CAMINAR
            elif self.direccion == "D":
                if self.salto:
                    self.posicionY += p.PIXELES_SALTO
                else:
                    self.posicionY += p.VELOCIDAD_CAMINAR
        if not self.salto:
            self.senal_mover.emit(self.direccion, (self.posicionX, self.posicionY))
        else:
            self.senal_mover.emit("J", (self.posicionX, self.posicionY))

    def reinicio(self):

        if self.posicionY <= p.Y_MIN_RIO:
            self.posicionX = p.POS_CHECK_POINT_2[0]
            self.posicionY = p.POS_CHECK_POINT_2[1]

        elif self.posicionY <= p.Y_MAX_RIO:
            self.posicionX = p.POS_CHECK_POINT_1[0]
            self.posicionY = p.POS_CHECK_POINT_1[1]

        else:
            self.posicionX = p.POS_INICIO_FROGG[0]
            self.posicionY = p.POS_INICIO_FROGG[1]
        self.direccion = "S"
        self.senal_mover.emit("S", (self.posicionX, self.posicionY))

    def volver_inicio(self):
        self.posicionX = p.POS_INICIO_FROGG[0]
        self.posicionY = p.POS_INICIO_FROGG[1]
        self.direccion = "S"
        self.senal_mover.emit("S", (self.posicionX, self.posicionY))

    def avanzar_tronco(self, posicion):
        self.posicionX = posicion[0]
        self.posicionY = posicion[1]
        self.senal_mover.emit(self.direccion, (self.posicionX, self.posicionY))


class Musica(QObject):

    def __init__(self, ruta_cancion):
        super().__init__()
        self.ruta_cancion = ruta_cancion

    def comenzar(self):
        self.cancion = QtMultimedia.QSound(self.ruta_cancion)
        self.cancion.Loop()
        self.cancion.play()

    def pausar(self):
        self.cancion.stop()
