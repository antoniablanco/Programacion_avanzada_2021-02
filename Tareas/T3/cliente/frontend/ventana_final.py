from PyQt5.QtWidgets import QLabel, QLineEdit, QPushButton, QWidget, QHBoxLayout, QVBoxLayout
from PyQt5.QtGui import QFont, QPixmap, QIcon
from PyQt5.QtCore import Qt, pyqtSignal
import obtener_parametros as p


class VentanaFinal(QWidget):
    boton_nueva_partida_signal = pyqtSignal()

    def __init__(self):
        super().__init__()
        self.init_gui()

    def init_gui(self):
    
        self.setGeometry(300, 300, 500, 500)
        self.setWindowTitle("Ventana Final")
        self.setWindowIcon(QIcon(p.ruta("RUTA_WONES")))

        self.cuadrado = QLabel(self)
        self.cuadrado.setGeometry(0, 0, 500, 500)

        self.logo = QLabel(self)
        logo = QPixmap(p.ruta("RUTA_TARJETA"))
        self.logo.setPixmap(logo)
        self.logo.setGeometry(170, 380, 150, 100)
        self.logo.setScaledContents(True)
        self.logo.setStyleSheet("background: transparent;")

        self.slogan = QLabel('¡Fin del juego! ', self)
        self.slogan.move(100, 50)
        self.slogan.setFont(QFont("Times New Roman", 46, italic=True))

        self.ganador_label = QLabel(" ", self)
        self.ganador_label.setGeometry(100, 150, 100, 30)
        self.ganador_label.setFont(QFont("Times New Roman", 24))

        self.perdedor_label = QLabel("aqui", self)
        self.perdedor_label.setGeometry(100, 250, 100, 30)
        self.perdedor_label.setFont(QFont("Times New Roman", 24))

        self.ganador_imagen = QLabel(self)
        ganador_imagen = QPixmap(p.ruta("RUTA_WONES"))
        self.ganador_imagen.setPixmap(ganador_imagen)
        self.ganador_imagen.setGeometry(300, 120, 120, 100)
        self.ganador_imagen.setScaledContents(True)
        self.ganador_imagen.setStyleSheet("background: transparent;")

        self.perdedor_imagen = QLabel(self)
        perdedor_imagen = QPixmap(p.ruta("RUTA_CALAVERA_GRIS"))
        self.perdedor_imagen.setPixmap(perdedor_imagen)
        self.perdedor_imagen.setGeometry(300, 220, 120, 100)
        self.perdedor_imagen.setScaledContents(True)
        self.perdedor_imagen.setStyleSheet("background: transparent;")

        self.button = QPushButton('Jugar otra vez', self)
        self.button.clicked.connect(self.jugar)
        self.button.setGeometry(180, 350, 130, 25)
        self.button.setFont(QFont("georgia", 18))

        self.agregar_estilo()

    def agregar_estilo(self):

        self.setStyleSheet("background-color: #000000")

        self.cuadrado.setStyleSheet("background-color: 7EBBAB;"
                                    "border: 10px solid #ed1b76")
        
        self.button.setStyleSheet("background-color: #ffffff;"
                                  "border-radius: 3px;"
                                  "color: #131212")

        self.ganador_label.setStyleSheet("background-color: #000000;"
                                         "color: #ed1b76")

    def definir_info(self, ganador, perdedor):
        self.ganador_label.setText(f"{ganador}")
        self.perdedor_label.setText(f"{perdedor}")
        self.perdedor_label.setStyleSheet("color: white")

    def jugar(self):
        self.boton_nueva_partida_signal.emit()

    def mostrar(self):
        self.show()

    def ocultar(self):
        self.hide()
