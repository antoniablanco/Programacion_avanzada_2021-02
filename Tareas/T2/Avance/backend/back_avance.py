
from PyQt5.QtCore import QObject, pyqtSignal, QTimer, QRect
import parametros as p


class Autos(QObject):

    def __init__(self, identificador, direccion):
        super().__init__()
        self.identificador = identificador
        self.__posicionX = p.POS_INICIO_AUTO[0]
        self.__posicionY = p.POS_INICIO_AUTO[1]
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

    def movimiento(self):
        self.posicionX += p.VELOCIDAD_AUTOS*self.direccion
        #print("La nueva posicion es:", self.posicionX, self.posicionY)
        return (self.posicionX, self.posicionY)


class Frogg(QObject):
    senal_mover = pyqtSignal(str, tuple)
    
    def __init__(self):
        super().__init__()
        self.direccion = "R"
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

    def cambiar_direccion(self, nueva_direccion):  # Cambia la direccion segun la letra
        if nueva_direccion.upper() in "URDLJ":
            self.direccion = nueva_direccion
    
    def avanzar(self):  # Genera el movimiento 
        # print(self.posicionX, self.posicionY)
        if self.direccion == "R":
            self.posicionX += p.MOVIMIENTO
        elif self.direccion == "L":
            self.posicionX -= p.MOVIMIENTO
        elif self.direccion == "U":
            self.posicionY -= p.MOVIMIENTO
        else:
            self.posicionY += p.MOVIMIENTO

        self.senal_mover.emit(self.direccion, (self.posicionX, self.posicionY))
    
    def reinicio(self):
        self.posicionX = p.POS_INICIO_FROGG[0]
        self.posicionY = p.POS_INICIO_FROGG[1]
        self.senal_mover.emit("S", (self.posicionX, self.posicionY))


class Juego(QObject):
    senal_recolectado = pyqtSignal()
    senal_fin = pyqtSignal()
    senal_mover_auto = pyqtSignal(int, tuple)

    def __init__(self, frogg):
        super().__init__()
        self.frogg = frogg
        self.instanciar_timer()
        self.contador_monedas = 0
        self.pos_moneda = p.POS_INICIO_MONEDA
        self.identificador_autos = 0
        self.autos = {}
    
    def instanciar_timer(self):
        self.timer = QTimer()
        self.timer.timeout.connect(self.timer_tick)
        self.timer.setInterval(int(0.5 * 1000))
    
    def instanciar_autos(self):
        nuevo_auto = Autos(self.identificador_autos, 1)
        self.autos[self.identificador_autos] = nuevo_auto
        self.identificador_autos += 1
    
    def iniciar_juego(self):
        self.instanciar_autos()
        self.timer.start()
    
    def detener_juego(self):
        self.timer.stop()
        self.senal_fin.emit()

    def timer_tick(self):
        for auto in range(len(self.autos)):  # Genera el movimiento de los autos
            posicion = self.autos[auto].movimiento()
            self.senal_mover_auto.emit(auto, posicion)

        if self.colision_auto():  # Verifica si choco con el auto
            self.frogg.reinicio()
        elif self.recolecta_item():  # Verifica si agarro el objeto
            self.senal_recolectado.emit()
            self.detener_juego()

    def recolecta_item(self):
        devolver = False
        if self.pos_moneda[0] - p.WIDTH_FROGG <= self.frogg.posicionX <= self.pos_moneda[0] + p.WIDTH_FROGG:
            if self.pos_moneda[1] - p.WIDTH_FROGG <= self.frogg.posicionY <= self.pos_moneda[1] + p.WIDTH_FROGG:
                self.contador_monedas += 1
                devolver = True
        return devolver
    
    def colision_auto(self):
        devolver = False
        for auto in range(len(self.autos)):
            posicionx = self.autos[auto].posicionX
            posiciony = self.autos[auto].posicionY
            if posicionx - p.WIDTH_FROGG <= self.frogg.posicionX <= posicionx + p.WIDTH_FROGG:
                if posiciony - p.WIDTH_FROGG <= self.frogg.posicionY <= posiciony + p.WIDTH_FROGG:
                    devolver = True
        return devolver
