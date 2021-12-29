from PyQt5.QtWidgets import QLabel, QLineEdit, QPushButton, QWidget
from PyQt5.QtGui import QFont, QPixmap, QIcon
from PyQt5.QtCore import Qt, pyqtSignal
import obtener_parametros as p


class VentanaInicio(QWidget):

    senal_enviar_usuario = pyqtSignal(dict)
    razon_signal = pyqtSignal(dict)

    def __init__(self):
        super().__init__()
        self.init_gui()

    def init_gui(self):
        self.setGeometry(300, 300, 500, 500)
        self.setWindowTitle("Ventana inicio")
        self.setWindowIcon(QIcon(p.ruta("RUTA_WONES")))

        self.titulo = QLabel(self)
        titulo = QPixmap(p.ruta("RUTA_LOGO_FONDO_NEGRO"))
        self.titulo.setPixmap(titulo)
        self.titulo.setGeometry(50, 100, 420, 110)
        self.titulo.setScaledContents(True)
        self.titulo.setStyleSheet("background: transparent;")

        self.logo = QLabel(self)
        logo = QPixmap(p.ruta("RUTA_TARJETA"))
        self.logo.setPixmap(logo)
        self.logo.setGeometry(170, 380, 150, 100)
        self.logo.setScaledContents(True)
        self.logo.setStyleSheet("background: transparent;")

        self.cuadrado = QLabel(self)
        self.cuadrado.setGeometry(0, 0, 500, 500)

        self.slogan = QLabel('¿Te atreves a jugar? ', self)
        self.slogan.setGeometry(180, 25, 300, 40)
        self.slogan.setFont(QFont("Times New Roman", 20, italic=True))
        self.slogan.setStyleSheet("color: white")

        self.nombre_label = QLabel('Escribe tu nombre de usuario (alfanumérico)', self)
        self.nombre_label.setGeometry(100, 230, 300, 35)
        self.nombre_label.setFont(QFont("Times New Roman", 16))
        self.nombre_label.setStyleSheet("color: white")

        self.nombre_form = QLineEdit("", self)
        self.nombre_form.setGeometry(100, 260, 300, 20)
        self.nombre_form.setFont(QFont("georgia", 16))

        self.fecha_label = QLabel('Fecha de nacimiento ', self)
        self.fecha_label.setGeometry(100, 290, 300, 30)
        self.fecha_label.setFont(QFont("Times New Roman", 16))
        self.fecha_label.setStyleSheet("color: white")

        self.fecha_form = QLineEdit("", self)
        self.fecha_form.setGeometry(100, 320, 300, 20)
        self.fecha_form.setFont(QFont("georgia", 16))

        self.firmar_button = QPushButton('Firmar', self)
        self.firmar_button.clicked.connect(self.firmar)
        self.firmar_button.setGeometry(180, 360, 130, 25)
        self.firmar_button.setFont(QFont("georgia", 18))

        self.label_razon = QLabel("", self)
        self.label_razon.setGeometry(130, 210, 200, 30)
        self.label_razon.setFont(QFont("Times New Roman", 16))
        self.label_razon.setStyleSheet("color: white")

        self.razon_signal.connect(self.razon_rechazo)

        self.agregar_estilo()

    def agregar_estilo(self):

        self.setStyleSheet("background-color: #000000")

        self.nombre_form.setStyleSheet("background-color: #ffffff;"
                                        "color: #131212")
        
        self.fecha_form.setStyleSheet("background-color: #ffffff;"
                                        "color: #131212")
        
        self.cuadrado.setStyleSheet("background-color: 7EBBAB;"
                                    "border: 10px solid #ed1b76")
        
        self.firmar_button.setStyleSheet("background-color: #ffffff;"
                                        "border-radius: 1px;"
                                        "color: #131212")

    def firmar(self):
        dict_user = {
            "comando": "ingreso",
            "info": (self.nombre_form.text(), self.fecha_form.text())
            }
        self.senal_enviar_usuario.emit(dict_user)

    def razon_rechazo(self, comentario):
        self.fecha_form.clear()
        self.nombre_form.clear()
        razon = comentario["comentario"]
        self.label_razon.setText(f"{razon}")
        self.label_razon.setStyleSheet("color: white")
        self.label_razon.show()

    def mostrar(self):
        self.fecha_form.clear()
        self.nombre_form.clear()
        self.label_razon.setText("")
        self.show()
    
    def ocultar(self):
        self.hide()