
from os import set_inheritable
from PyQt5.QtCore import pyqtSignal, Qt, QRect
from PyQt5.QtGui import QIcon, QPixmap, QFont
from PyQt5.QtWidgets import (
    QWidget, QLabel,  QMessageBox, QLineEdit, QPushButton, QHBoxLayout, QVBoxLayout
)
import parametros as p
from random import randint


class VentanaJuego(QWidget):
    senal_tecla = pyqtSignal(str)
    senal_salto = pyqtSignal(str)
    senal_iniciar_juego = pyqtSignal()
    senal_abrir_post = pyqtSignal()
    senal_pausa = pyqtSignal()
    senal_continuar = pyqtSignal()
    senal_cheat_vidas = pyqtSignal()
    senal_resetear = pyqtSignal()
    senal_inicio_musica = pyqtSignal()
    senal_fin_musica = pyqtSignal()
    senal_cerrar = pyqtSignal()

    def __init__(self, tamano_ventana):
        super().__init__()
        self.init_gui(tamano_ventana)
        self.identificador_autos = 0
        self.identificador_objetos = 0
        self.identificador_troncos = 0
        self.autos = {}
        self.objetos = {}
        self.troncos = {}
        self.__movfrog = 0
        self.pausa = False
        self.v = False
        self.i = False
        self.d = False
        self.n = False

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
        self.setGeometry(tamano_ventana)
        self.setWindowTitle("Ventana juego")
        self.setWindowIcon(QIcon(p.RUTA_LOGO))

        self.imagenes_frogg = {"S": [p.RUTA_FROGG_STILL, p.RUTA_FROGG_STILL, p.RUTA_FROGG_STILL],
            "D": [p.RUTA_FROGG_DOWN_1, p.RUTA_FROGG_DOWN_2, p.RUTA_FROGG_DOWN_3],
            "J": [p.RUTA_FROGG_JUMP_1, p.RUTA_FROGG_JUMP_2, p.RUTA_FROGG_JUMP_3],
            "L": [p.RUTA_FROGG_LEFT_1, p.RUTA_FROGG_LEFT_2, p.RUTA_FROGG_LEFT_3],
            "R": [p.RUTA_FROGG_RIGHT_1, p.RUTA_FROGG_RIGHT_2, p.RUTA_FROGG_RIGHT_3],
            "U": [p.RUTA_FROGG_UP_1, p.RUTA_FROGG_UP_2, p.RUTA_FROGG_UP_3]}

        self.imagenes_autos = {1: [p.RUTA_AUTO1_LEFT, p.RUTA_AUTO1_RIGHT],
            2: [p.RUTA_AUTO2_LEFT, p.RUTA_AUTO2_RIGHT],
            3: [p.RUTA_AUTO3_LEFT, p.RUTA_AUTO3_RIGHT],
            4: [p.RUTA_AUTO4_LEFT, p.RUTA_AUTO4_RIGHT],
            5: [p.RUTA_AUTO5_LEFT, p.RUTA_AUTO5_RIGHT],
            6: [p.RUTA_AUTO6_LEFT, p.RUTA_AUTO6_RIGHT],
            7: [p.RUTA_AUTO7_LEFT, p.RUTA_AUTO7_RIGHT]}

        self.imagenes_objetos = {"moneda": p.RUTA_MONEDA,
            "corazon": p.RUTA_CORAZON,
            "reloj": p.RUTA_RELOJ,
            "calavera": p.RUTA_CALAVERA}

        # Informacion
        self.logo = QLabel(self)
        logo = QPixmap(p.RUTA_LOGO)
        self.logo.setPixmap(logo)
        self.logo.setGeometry(430, 30, 150, 150)
        self.logo.setScaledContents(True)
        self.logo.setStyleSheet("background: transparent;")

        self.cuadrado1 = QLabel(self)
        self.cuadrado1.setGeometry(20, 20, 350, 150)

        self.cuadrado2 = QLabel(self)
        self.cuadrado2.setGeometry(630, 20, 350, 150)

        self.pausar_button = QPushButton('Pausar', self)
        self.pausar_button.clicked.connect(self.pausar)
        self.pausar_button.setGeometry(810, 60, 150, 30)
        self.pausar_button.setFont(QFont("georgia", 16))

        self.salir_button = QPushButton('Salir', self)
        self.salir_button.clicked.connect(self.resetear)
        self.salir_button.setGeometry(810, 100, 150, 30)
        self.salir_button.setFont(QFont("georgia", 16))

        self.label_vida = QLabel('VIDAS: ', self)
        self.label_vida.move(70, 50)
        self.label_vida.setFont(QFont("georgia", 16))

        self.label_tiempo = QLabel('TIEMPO: ', self)
        self.label_tiempo.move(70, 80)
        self.label_tiempo.setFont(QFont("georgia", 16))

        self.label_monedas = QLabel('MONEDAS: ', self)
        self.label_monedas.move(70, 110)
        self.label_monedas.setFont(QFont("georgia", 16))

        self.label_nivel = QLabel('NIVEL: ', self)
        self.label_nivel.move(670, 60)
        self.label_nivel.setFont(QFont("georgia", 16))

        self.label_puntaje = QLabel('PUNTAJE: ', self)
        self.label_puntaje.move(670, 100)
        self.label_puntaje.setFont(QFont("georgia", 16))

        # Areas de fondo
        self.pasto = QLabel(self)
        pasto = QPixmap(p.RUTA_PASTO)
        self.pasto.setPixmap(pasto)
        self.pasto.setGeometry(10, 190, 980, 800)
        self.pasto.setScaledContents(True)
        self.pasto.setStyleSheet("background: transparent;")

        self.carretera1 = QLabel(self)
        carretera1 = QPixmap(p.RUTA_CARRETERA)
        self.carretera1.setPixmap(carretera1)
        self.carretera1.setGeometry(10, 220, 980, 130)
        self.carretera1.setScaledContents(True)
        self.carretera1.setStyleSheet("background: transparent;")

        self.carretera2 = QLabel(self)
        carretera2 = QPixmap(p.RUTA_CARRETERA)
        self.carretera2.setPixmap(carretera2)
        self.carretera2.setGeometry(10, 600, 980, 130)
        self.carretera2.setScaledContents(True)
        self.carretera2.setStyleSheet("background: transparent;")

        self.rio = QLabel(self)
        rio = QPixmap(p.RUTA_RIO)
        self.rio.setPixmap(rio)
        self.rio.setGeometry(10, 410, 980, 130)
        self.rio.setScaledContents(True)
        self.rio.setStyleSheet("background: transparent;")

        self.agregar_estilo()

    def agregar_estilo(self):
        self.setStyleSheet("background-color: #247E29")
        self.cuadrado1.setStyleSheet("background-color: 7EBBAB;"
                                    "border: 10px solid rgb(176,224,230)")
        self.cuadrado2.setStyleSheet("background-color: 7EBBAB;"
                                    "border: 10px solid rgb(176,224,230)")
        self.pausar_button.setStyleSheet("background-color: #ffffff;"
                                        "border-radius: 5px;"
                                        "color: black")
        self.salir_button.setStyleSheet("background-color: #ffffff;"
                                        "border-radius: 5px;"
                                        "color: black")

    def keyPressEvent(self, event):
        if event.key() == Qt.Key_V and not self.i:
            self.v = True
        elif event.key() == Qt.Key_I and self.v:
            self.i = True
        elif event.key() == Qt.Key_D and self.i:
            self.senal_cheat_vidas.emit()
            self.v, self.i, self.d, self.n = False, False, False, False
        elif event.key() == Qt.Key_N:
            self.n = True
        elif event.key() == Qt.Key_I and self.n:
            self.i = True
        elif event.key() == Qt.Key_V and self.i:
            self.ventana_post()
            self.v, self.i, self.d, self.n = False, False, False, False
        elif event.key() == Qt.Key_D and not self.i:
            self.senal_tecla.emit("R")
            self.v, self.i, self.d, self.n = False, False, False, False
        elif event.key() == Qt.Key_W:
            self.senal_tecla.emit("U")
            self.v, self.i, self.d, self.n = False, False, False, False
        elif event.key() == Qt.Key_A:
            self.senal_tecla.emit("L")
            self.v, self.i, self.d, self.n = False, False, False, False
        elif event.key() == Qt.Key_S:
            self.senal_tecla.emit("D")
            self.v, self.i, self.d, self.n = False, False, False, False
        elif event.key() == Qt.Key_J:
            self.senal_salto.emit("J")
            self.v, self.i, self.d, self.n = False, False, False, False
        elif event.key() == Qt.Key_P and self.pausa:
            # Falta que funcione
            self.senal_continuar.emit()
            self.v, self.i, self.d, self.n = False, False, False, False
        elif event.key() == Qt.Key_P and not self.pausa:
            self.pausar()
            self.v, self.i, self.d, self.n = False, False, False, False
        else:
            self.v, self.i, self.d, self.n = False, False, False, False

    def avanzar(self, direccion, posicion):
        self.pixeles_frogg = QPixmap(self.imagenes_frogg[direccion][self.movfrog])
        self.frogg_label.setPixmap(self.pixeles_frogg)
        self.frogg_label.setScaledContents(True)
        self.frogg_label.resize(p.WIDTH_FROGG, p.HEIGHT_FROGG)
        self.frogg_label.move(posicion[0], posicion[1])
        self.movfrog += 1

    def mover_autos(self, id, posicion):
        try:
            self.autos[id].move(posicion[0], posicion[1])

        except KeyError:
            print(f"No existe key {id} dentro del diccionario de autos ")

    def mover_troncos(self, id, posicion):
        try:
            self.troncos[id].move(posicion[0], posicion[1])

        except KeyError:
            print(f"No existe key {id} dentro del diccionario de troncos ")

    def ocultar_objeto(self, id):
        self.objetos[id].hide()

    def crear_autos(self, direccion, posicion):
        num_imagen = randint(0, 6)
        imagen_item = QPixmap(self.imagenes_autos[num_imagen+1][direccion])
        auto1 = QLabel("", self)
        auto1.setPixmap(imagen_item)
        auto1.setScaledContents(True)
        auto1.resize(p.WIDTH_AUTO, p.HEIGHT_AUTO)
        auto1.setStyleSheet("background: transparent;")
        auto1.move(posicion[0], posicion[1])

        self.autos[self.identificador_autos] = auto1
        self.identificador_autos += 1

    def crear_objeto(self, tipo, posicion):
        self.imagen_item = QPixmap(self.imagenes_objetos[tipo])
        item = QLabel("", self)
        item.setPixmap(self.imagen_item)
        item.setScaledContents(True)
        item.resize(p.WIDTH_OBJETO, p.HEIGHT_OBJETO)
        item.setStyleSheet("background: transparent;")
        item.move(posicion[0], posicion[1])

        self.objetos[self.identificador_objetos] = item
        self.objetos[self.identificador_objetos].show()
        self.identificador_objetos += 1

    def crear_troncos(self, posicion):
        imagen_item = QPixmap(p.RUTA_TRONCO)
        tronco = QLabel("", self)
        tronco.setPixmap(imagen_item)
        tronco.setScaledContents(True)
        tronco.resize(p.WIDTH_TRONCO, p.HEIGHT_TRONCO)
        tronco.setStyleSheet("background: transparent;")
        tronco.move(posicion[0], posicion[1])

        self.troncos[self.identificador_troncos] = tronco
        self.identificador_troncos += 1

    def crear_frogg(self):
        self.frogg_label = QLabel("", self)
        self.pixeles_frogg = QPixmap(self.imagenes_frogg["S"][0])
        self.frogg_label.setPixmap(self.pixeles_frogg)
        self.frogg_label.setScaledContents(True)
        self.frogg_label.resize(p.WIDTH_FROGG, p.HEIGHT_FROGG)
        self.frogg_label.move(p.POS_INICIO_FROGG[0], p.POS_INICIO_FROGG[1])
        self.frogg_label.setStyleSheet("background: transparent;")

    def actualizar_informacion(self, informacion):

        self.label_vida.hide()
        self.label_vida = QLabel(f'VIDAS:  {informacion[0]}', self)
        self.label_vida.move(70, 50)
        self.label_vida.setFont(QFont("georgia", 16))
        self.label_vida.show()

        self.label_tiempo.hide()
        self.label_tiempo = QLabel(f'TIEMPO: {int(informacion[1])} sgds', self)
        self.label_tiempo.move(70, 80)
        self.label_tiempo.setFont(QFont("georgia", 16))
        self.label_tiempo.show()

        self.label_monedas.hide()
        self.label_monedas = QLabel(f'MONEDAS: {informacion[2]}', self)
        self.label_monedas.move(70, 110)
        self.label_monedas.setFont(QFont("georgia", 16))
        self.label_monedas.show()

        self.label_nivel.hide()
        self.label_nivel = QLabel(f'NIVEL: {informacion[4]}', self)
        self.label_nivel.move(670, 60)
        self.label_nivel.setFont(QFont("georgia", 16))
        self.label_nivel.show()

        self.label_puntaje.hide()
        self.label_puntaje = QLabel(f'PUNTAJE: {int(informacion[3])}  ', self)
        self.label_puntaje.move(670, 100)
        self.label_puntaje.setFont(QFont("georgia", 16))
        self.label_puntaje.show()

    def pausar(self):
        self.senal_pausa.emit()
        self.senal_fin_musica.emit()
        reply = QMessageBox.question(self, "Ventana pausa", "¿Quieres continuar el juego?",
        QMessageBox.Yes | QMessageBox.No)
        self.pausa = True

        if reply == QMessageBox.Yes:
            self.senal_continuar.emit()
            self.senal_inicio_musica.emit()
            self.pausar = False
        else:
            self.pausar = False
            self.resetear()

    def mostrar(self):
        self.senal_iniciar_juego.emit()
        self.crear_frogg()
        self.senal_inicio_musica.emit()
        self.show()

    def ventana_post(self):
        self.senal_abrir_post.emit()
        self.ocultar()

    def ocultar(self):
        self.senal_fin_musica.emit()
        for n in self.autos.keys():
            self.autos[n].hide()
        for n in self.troncos.keys():
            self.troncos[n].hide()
        for n in self.objetos.keys():
            self.objetos[n].hide()
        self.frogg_label.hide()
        self.identificador_autos = 0
        self.identificador_objetos = 0
        self.identificador_troncos = 0
        self.autos.clear()
        self.objetos.clear()
        self.troncos.clear()
        self.__movfrog = 0
        self.senal_cerrar.emit()
        self.hide()

    def siguiente_nivel(self):
        self.mostrar()

    def resetear(self):
        self.ocultar()
        self.senal_resetear.emit()