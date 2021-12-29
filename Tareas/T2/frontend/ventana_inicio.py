from PyQt5.QtCore import pyqtSignal, Qt, QRect
from PyQt5.QtGui import QIcon, QPixmap, QFont
from PyQt5.QtWidgets import (
    QWidget, QLabel,  QMessageBox, QLineEdit, QPushButton, QHBoxLayout, QVBoxLayout
)
import parametros as p


class VentanaInicio(QWidget):
    senal_verificar_nombre = pyqtSignal(str)
    senal_abrir_ranking = pyqtSignal()
    senal_resetear = pyqtSignal()
    senal_fin_musica = pyqtSignal()
    senal_inicio_musica = pyqtSignal()

    def __init__(self, tamano_ventana):
        super().__init__()
        self.init_gui(tamano_ventana)

    def init_gui(self, tamano_ventana):
        self.setGeometry(tamano_ventana)
        self.setWindowTitle("Ventana inicio")
        self.setWindowIcon(QIcon(p.RUTA_LOGO))

        self.logo = QLabel(self)
        logo = QPixmap(p.RUTA_LOGO)
        self.logo.setPixmap(logo)
        self.logo.setGeometry(130, 50, 250, 250)
        self.logo.setScaledContents(True)
        self.logo.setStyleSheet("background: transparent;")

        self.cuadrado = QLabel(self)
        self.cuadrado.setGeometry(20, 20, 460, 460)

        self.label1 = QLabel('Escribe tu nombre de usuario: ', self)
        self.label1.move(100, 300)
        self.label1.setFont(QFont("georgia", 16))

        self.usuario_form = QLineEdit("", self)
        self.usuario_form.setGeometry(100, 320, 300, 20)
        self.usuario_form.setFont(QFont("georgia", 16))

        self.ingresar_button = QPushButton('Iniciar Partida', self)
        self.ingresar_button.clicked.connect(self.verificar_nombre)
        self.ingresar_button.setGeometry(180, 350, 150, 30)
        self.ingresar_button.setFont(QFont("georgia", 16))

        self.ranking_button = QPushButton('Ver Ranking', self)
        self.ranking_button.clicked.connect(self.ver_ranking)
        self.ranking_button.setGeometry(180, 390, 150, 30)
        self.ranking_button.setFont(QFont("georgia", 16))

        self.agregar_estilo()

    def verificar_nombre(self):
        self.senal_verificar_nombre.emit(self.usuario_form.text())

    def ver_ranking(self):
        self.senal_abrir_ranking.emit()
        self.ocultar()

    def agregar_estilo(self):
        self.usuario_form.returnPressed.connect(
            lambda: self.ingresar_button.click()
        )

        self.setStyleSheet("background-color: #247E29")
        self.usuario_form.setStyleSheet("background-color: #ffffff;"
                                        "color: black")
        self.cuadrado.setStyleSheet("background-color: 7EBBAB;"
                                    "border: 10px solid rgb(176,224,230)")
        self.ingresar_button.setStyleSheet("background-color: #ffffff;"
                                        "border-radius: 5px;"
                                        "color: black")
        self.ranking_button.setStyleSheet("background-color: #ffffff;"
                                        "border-radius: 5px;"
                                        "color: black")

    def recibir_validacion(self, tupla_respuesta):
        if tupla_respuesta[1]:
            self.ocultar()
        else:
            self.pop_up_error()

    def pop_up_error(self):
        QMessageBox.about(self, "ERROR", f"Su nombre no cumple con el largo entre " +
        f"{p.MIN_CARACTERES} y {p.MAX_CARACTERES}, o con ser alfanumerico.\nVuelva a intentarlo")

    def mostrar(self):
        self.senal_inicio_musica.emit()
        self.show()

    def ocultar(self):
        self.senal_fin_musica.emit()
        self.hide()

    def resetear(self):
        self.usuario_form.setText("")
        self.senal_resetear.emit()
        self.mostrar()
        self.usuario_form.setText("")
        self.senal_resetear.emit()
        self.mostrar()