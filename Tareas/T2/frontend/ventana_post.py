from os import _wrap_close
from PyQt5.QtCore import pyqtSignal
from PyQt5.QtGui import QIcon, QFont
from PyQt5.QtWidgets import (
    QWidget, QLabel, QPushButton
)
import parametros as p


class VentanaPost(QWidget):
    senal_siguiente_nivel = pyqtSignal(int)
    senal_guardar_puntaje = pyqtSignal(str, int)
    senal_ventana_inicio = pyqtSignal()
    senal_inicio_musica = pyqtSignal()
    senal_fin_musica = pyqtSignal()

    def __init__(self, tamano_ventana):
        super().__init__()
        self.init_gui(tamano_ventana)
        self.tiempo = p.DURACION_RONDA_INICIAL
        self.vida = None
        self.nivel1 = None
        self.puntaje_turno = None
        self.puntaje_total = None
        self.moneda = None
        self.nombre = None

    def init_gui(self, tamano_ventana):
        self.setGeometry(tamano_ventana)
        self.setWindowTitle("Ventana post nivel")
        self.setWindowIcon(QIcon(p.RUTA_LOGO))

        self.cuadrado = QLabel(self)
        self.cuadrado.setGeometry(20, 20, 460, 460)

        self.label1 = QLabel('RESUMEN DE PERSONAJES', self)
        self.label1.setFont(QFont("Rockwell", 28))
        self.label1.setGeometry(60, 40, 400, 50)

        self.label_nivel = QLabel(f'Nivel actual: ', self)
        self.label_nivel.move(90, 100)
        self.label_nivel.setFont(QFont("georgia", 16))

        self.label_puntaje_total = QLabel(f'Puntaje total: ', self)
        self.label_puntaje_total.move(90, 150)
        self.label_puntaje_total.setFont(QFont("georgia", 16))

        self.label_puntaje = QLabel(f'Puntaje obtenido en el nivel: ', self)
        self.label_puntaje.move(90, 200)
        self.label_puntaje.setFont(QFont("georgia", 16))

        self.label_vida = QLabel(f'Vidas restantes: ', self)
        self.label_vida.move(90, 250)
        self.label_vida.setFont(QFont("georgia", 16))

        self.label_monedas = QLabel(f'Total de monedas: ', self)
        self.label_monedas.move(90, 300)
        self.label_monedas.setFont(QFont("georgia", 16))

        self.label_semaforo = QLabel('      Puedes seguir con el siguiente nivel', self)
        self.label_semaforo.setGeometry(110, 340, 300, 40)
        self.label_semaforo.setFont(QFont("georgia", 16))

        self.tienda_button = QPushButton('Ir a la Tienda', self)
        self.tienda_button.setGeometry(50, 400, 120, 30)
        self.tienda_button.setFont(QFont("georgia", 16))
        self.tienda_button.clicked.connect(self.tienda)

        self.nivel_button = QPushButton('Siguiente nivel', self)
        self.nivel_button.setGeometry(190, 400, 120, 30)
        self.nivel_button.clicked.connect(self.nivel)
        self.nivel_button.setFont(QFont("georgia", 16))

        self.salir_button = QPushButton('Salir', self)
        self.salir_button.clicked.connect(self.salir)
        self.salir_button.setGeometry(330, 400, 120, 30)
        self.salir_button.setFont(QFont("georgia", 16))

        self.agregar_estilo()

    def agregar_estilo(self):
        self.setStyleSheet("background-color: #247E29")
        self.cuadrado.setStyleSheet("background-color: 7EBBAB;"
                                    "border: 10px solid rgb(176,224,230)")
        self.label_semaforo.setStyleSheet("background-color: #20D639;"
                                          "color: black;"
                                          "border: 1px solid rgb(0,0,0)")
        self.tienda_button.setStyleSheet("background-color: #ffffff;"
                                        "border-radius: 5px;"
                                        "color: black")
        self.nivel_button.setStyleSheet("background-color: #ffffff;"
                                        "border-radius: 5px;"
                                        "color: black")
        self.salir_button.setStyleSheet("background-color: #ffffff;"
                                        "border-radius: 5px;"
                                        "color: black")

    def mostrar(self, informacion):
        self.senal_inicio_musica.emit()

        self.vida = informacion[0]
        self.nivel1 = informacion[1]
        self.tiempo = informacion[2]
        self.puntaje_turno = informacion[3]
        self.puntaje_total = informacion[4]
        self.moneda = informacion[5]
        self.nombre = informacion[6]

        self.label_nivel.setText(f'Nivel actual: {self.nivel1} ')
        self.label_puntaje_total.setText(f'Tiempo restante: {int(self.tiempo)} sgds')
        self.label_puntaje.setText(f'Puntaje obtenido en el nivel: {int(self.puntaje_turno)} ')
        self.label_vida.setText(f'Vidas restantes: {self.vida} ')
        self.label_monedas.setText(f'Total de monedas: {self.moneda} ')

        if int(self.vida) <= 0 or self.tiempo <= 0:
            self.ventana_parar()

        self.show()

    def ventana_seguir(self):
        self.label_semaforo.setGeometry(110, 340, 300, 40)
        self.label_semaforo.setFont(QFont("georgia", 16))
        self.label_semaforo.setStyleSheet("background-color: #20D639;"
                                          "color: black;"
                                          "border: 1px solid rgb(0,0,0)")
        self.tienda_button.clicked.connect(self.tienda)
        self.tienda_button.setStyleSheet("background-color: #ffffff;"
                                        "border-radius: 5px;"
                                        "color: black")

    def ventana_parar(self):
        self.label_semaforo.setText("      No puedes seguir con el siguiente nivel ")
        self.label_semaforo.setGeometry(70, 340, 350, 40)
        self.label_semaforo.setFont(QFont("georgia", 16))
        self.label_semaforo.setStyleSheet("background-color: #C8321E;"
                                          "color: black;"
                                          "border: 1px solid rgb(0,0,0)")
        self.tienda_button.setStyleSheet("background-color: #D9D8D8;"
                                        "border-radius: 5px;"
                                        "color: #A7A4A4")
        self.tienda_button.clicked.disconnect()
        self.nivel_button.setStyleSheet("background-color: #D9D8D8;"
                                        "border-radius: 5px;"
                                        "color: #A7A4A4")
        self.nivel_button.clicked.disconnect()

    def tienda(self):
        pass

    def nivel(self):
        self.senal_siguiente_nivel.emit(self.tiempo)
        self.ocultar()

    def ocultar(self):
        self.senal_fin_musica.emit()
        self.hide()

    def salir(self):
        self.senal_guardar_puntaje.emit(self.nombre, self.puntaje_total)
        self.senal_ventana_inicio.emit()
        self.ocultar()

    def rojo():
        pass