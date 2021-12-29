from PyQt5.QtCore import pyqtSignal, Qt, QRect
from PyQt5.QtGui import QIcon, QPixmap, QFont
from PyQt5.QtWidgets import (
    QWidget, QLabel,  QMessageBox
)
import parametros as p
from time import sleep


class VentanaInicio(QWidget):

    senal_tecla = pyqtSignal(str)
    senal_iniciar_juego = pyqtSignal()

    def __init__(self, tamano_ventana):
        super().__init__()
        self.init_gui(tamano_ventana)
        self.identificador_autos = 0
        self.identificador_objetos = 0
        self.autos = {}
        self.objetos = {}
        self.__movfrog = 0
    
    @property
    def movfrog(self):
        return self.__movfrog
    
    @movfrog.setter
    def movfrog(self, k):
        if k > 2:
            self.__movfrog = 0
        elif k <= 0:
            self.movfrog = 0
        else:
            self.__movfrog = k

    def init_gui(self, tamano_ventana):
        self.setWindowIcon(QIcon(p.RUTA_ICONO))
        self.setWindowTitle("Frogger")
        self.setGeometry(tamano_ventana)

        self.background = QLabel(self)
        pixmap = QPixmap(p.RUTA_PASTO)
        self.background.setPixmap(pixmap)
        
        self.imagenes_frogg = {
            "S": [p.RUTA_FROGG_STILL],
            "D": [p.RUTA_FROGG_DOWN_1, p.RUTA_FROGG_DOWN_2, p.RUTA_FROGG_DOWN_3],
            "J": [p.RUTA_FROGG_JUMP_1, p.RUTA_FROGG_JUMP_2, p.RUTA_FROGG_JUMP_3],
            "L": [p.RUTA_FROGG_LEFT_1, p.RUTA_FROGG_LEFT_2, p.RUTA_FROGG_LEFT_3],
            "R": [p.RUTA_FROGG_RIGHT_1, p.RUTA_FROGG_RIGHT_2, p.RUTA_FROGG_RIGHT_3],
            "U": [p.RUTA_FROGG_UP_1, p.RUTA_FROGG_UP_2, p.RUTA_FROGG_UP_3]
            }

        self.frogg_label = QLabel("", self)
        self.pixeles_frogg = QPixmap(self.imagenes_frogg["S"][0])
        self.frogg_label.setPixmap(self.pixeles_frogg)
        self.frogg_label.setScaledContents(True)
        self.frogg_label.resize(p.WIDTH_FROGG, p.HEIGHT_FROGG)
        self.frogg_label.move(p.POS_INICIO_FROGG[0], p.POS_INICIO_FROGG[1])

        
    def keyPressEvent(self, event):
        if event.key() == Qt.Key_D:
            self.senal_tecla.emit("R")
        if event.key() == Qt.Key_W:
            self.senal_tecla.emit("U")
        if event.key() == Qt.Key_A:
            self.senal_tecla.emit("L")
        if event.key() == Qt.Key_S:
            self.senal_tecla.emit("D")
    
    def avanzar(self, direccion, posicion):
        print("imagen numero:", self.movfrog)
        print("Ruta:", self.imagenes_frogg[direccion][self.movfrog])
        self.pixeles_frogg = QPixmap(self.imagenes_frogg[direccion][self.movfrog])
        self.frogg_label.setPixmap(self.pixeles_frogg)
        self.frogg_label.setScaledContents(True)
        self.frogg_label.resize(p.WIDTH_FROGG, p.HEIGHT_FROGG)
        self.frogg_label.move(posicion[0], posicion[1])
        self.movfrog += 1
    
    def mover_autos(self, id, direccion):
        self.autos[id].move(direccion[0], direccion[1])

    def mostrar(self):
        self.senal_iniciar_juego.emit()
        self.crear_auto() #Como es solo un auto se crea aqui
        self.crear_objeto() #Como es solo un objeto se crea aqui
        self.show()

    def ocultar_objeto(self):  # Falta cambiarlo a que esconda el objeto segun su id
        self.objetos[0].hide()

    def ocultar(self):  # Acaba con la simulación
    
        self.mensaje_fin = QMessageBox()
        label = QLabel()
        label.setText("SE ACABO EL JUEGO")
        label.setFont(QFont('Times', 30))
        self.mensaje_fin.layout().addWidget(label)
        self.mensaje_fin.layout().setGeometry(QRect(80, 320, 300, 100))
        self.mensaje_fin.setWindowTitle("Has ganado la moneda magica")
        
        self.close()
    
    def crear_auto(self):
        imagen_item = QPixmap(p.RUTA_AUTO)
        auto1 = QLabel("", self)
        auto1.setPixmap(imagen_item)
        auto1.setScaledContents(True)
        auto1.resize(p.WIDTH_FROGG, p.HEIGHT_FROGG)
        auto1.move(p.POS_INICIO_AUTO[0], p.POS_INICIO_AUTO[1])

        self.autos[self.identificador_autos] = auto1
        self.identificador_autos += 1

    def crear_objeto(self):
        self.imagen_item = QPixmap(p.RUTA_MONEDA)
        moneda = QLabel("", self)
        moneda.setPixmap(self.imagen_item)
        moneda.setScaledContents(True)
        moneda.resize(p.WIDTH_FROGG, p.HEIGHT_FROGG)
        moneda.move(p.POS_INICIO_MONEDA[0], p.POS_INICIO_MONEDA[1])

        self.objetos[self.identificador_objetos] = moneda
        self.identificador_objetos += 1
