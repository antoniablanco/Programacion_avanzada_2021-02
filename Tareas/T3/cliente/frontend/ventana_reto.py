from PyQt5.QtWidgets import QLabel, QLineEdit, QPushButton, QWidget
from PyQt5.QtGui import QFont, QPixmap, QIcon
from PyQt5.QtCore import Qt, pyqtSignal
import obtener_parametros as p

class VentanaReto(QWidget):
    boton_aceptar_signal = pyqtSignal(int)
    boton_rechazar_signal = pyqtSignal(int)

    def __init__(self):
        super().__init__()
        self.init_gui()
        self.id_retador = None
    
    def init_gui(self):
        self.setGeometry(300, 300, 500, 500)
        self.setWindowTitle("Ventana Reto")
        self.setWindowIcon(QIcon(p.ruta("RUTA_WONES")))

        self.cuadrado = QLabel(self)
        self.cuadrado.setGeometry(0, 0, 500, 500)
        
        self.atacante_label = QLabel('te ha invitado a jugar ', self)
        self.atacante_label.setGeometry(90, 50, 400, 40)
        self.atacante_label.setFont(QFont("Times New Roman", 28, italic=True))
        self.atacante_label.setStyleSheet("color: white")

        self.titulo = QLabel(self)
        titulo = QPixmap(p.ruta("RUTA_LOGO_FONDO_NEGRO"))
        self.titulo.setPixmap(titulo)
        self.titulo.setGeometry(50, 100, 420, 110)
        self.titulo.setScaledContents(True)
        self.titulo.setStyleSheet("background: transparent;")

        self.label1 = QLabel('¿Aceptas el reto?', self)
        self.label1.setGeometry(125, 250, 300, 40)
        self.label1.setFont(QFont("Times New Roman", 36, italic=False))
        self.label1.setStyleSheet("color: white")

        self.aceptar_button = QPushButton('Aceptar', self)
        self.aceptar_button.clicked.connect(self.aceptar)
        self.aceptar_button.setGeometry(110, 320, 130, 25)
        self.aceptar_button.setFont(QFont("georgia", 18))

        self.rechazar_button = QPushButton('Rechazar', self)
        self.rechazar_button.clicked.connect(self.rechazar)
        self.rechazar_button.setGeometry(260, 320, 130, 25)
        self.rechazar_button.setFont(QFont("georgia", 18))

        self.logo = QLabel(self)
        logo = QPixmap(p.ruta("RUTA_TARJETA"))
        self.logo.setPixmap(logo)
        self.logo.setGeometry(180, 380, 150, 100)
        self.logo.setScaledContents(True)
        self.logo.setStyleSheet("background: transparent;")

        self.agregar_estilo()
    
    def agregar_estilo(self):

        self.setStyleSheet("background-color: #000000")

        self.cuadrado.setStyleSheet("background-color: 7EBBAB;"
                                    "border: 10px solid #ed1b76")
        
        self.aceptar_button.setStyleSheet("background-color: #ffffff;"
                                        "border-radius: 1px;"
                                        "color: #000000")
        
        self.rechazar_button.setStyleSheet("background-color: #ffffff;"
                                        "border-radius: 1px;"
                                        "color: #000000")
    
    def definir_atacante(self, jugador):
        self.atacante_label.setText(f'{jugador} te ha invitado a jugar')

    def aceptar(self):
        self.boton_aceptar_signal.emit(self.id_retador)

    def rechazar(self):
        self.boton_rechazar_signal.emit(self.id_retador)
    
    def mostrar(self, id, jugador):
        self.id_retador = id
        self.definir_atacante(jugador)
        self.show()
    
    def ocultar(self):
        self.hide()
    