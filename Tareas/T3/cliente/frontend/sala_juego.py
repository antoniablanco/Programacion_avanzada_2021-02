from PyQt5.QtWidgets import QLabel, QLineEdit, QWidget
from PyQt5.QtWidgets import (QPushButton, QRadioButton, QSpinBox)
from PyQt5.QtGui import QFont, QPixmap, QIcon
from PyQt5.QtCore import Qt, pyqtSignal
import obtener_parametros as p


class SalaJuego(QWidget):
    boton_listo_signal = pyqtSignal()

    def __init__(self):
        super().__init__()
        self.init_gui() 
        self.jugador1 = None
        self.jugador2 = None
    
    def init_gui(self):
    
        self.setGeometry(300, 300, 800, 600)
        self.setWindowTitle("Sala Juego")
        self.setWindowIcon(QIcon(p.ruta("RUTA_WONES")))

        self.cuadrado1 = QLabel(self)
        self.cuadrado1.setGeometry(0, 0, 800, 300)

        self.cuadrado = QLabel(self)
        self.cuadrado.setGeometry(0, 300, 800, 300)

        self.nombre1_label = QLabel('Jugador 1:  ', self)
        self.nombre1_label.setGeometry(170, 40, 400, 30)
        self.nombre1_label.setFont(QFont("Times New Roman", 24))

        self.nombre2_label = QLabel('Jugador 2:  ', self)
        self.nombre2_label.setGeometry(170, 340, 400, 30)
        self.nombre2_label.setFont(QFont("Times New Roman", 24))

        self.imagen_jugador1 = QLabel(self)
        imagen_jugador1 = QPixmap(p.ruta("RUTA_AVATAR_1"))
        self.imagen_jugador1.setPixmap(imagen_jugador1)
        self.imagen_jugador1.setGeometry(20, 30, 130, 150)
        self.imagen_jugador1.setScaledContents(True)
        self.imagen_jugador1.setStyleSheet("background: transparent;")

        self.label4 = QLabel('¿Cuantás canicas apuesta?', self)
        self.label4.setGeometry(170, 80, 200, 30)
        self.label4.setFont(QFont("Times New Roman", 16))
        self.label4.setStyleSheet("background-color: #000000;"
                                  "color: #ffffff")
        
        self.canicas_propias = QLabel('La apuesta de tu oponente es  ', self)
        self.canicas_propias.setGeometry(420, 80, 200, 30)
        self.canicas_propias.setFont(QFont("Times New Roman", 16))
        self.canicas_propias.setStyleSheet("background-color: #000000;"
                                           "color: white")
        
        self.firmar_button = QPushButton('Listo!', self)
        self.firmar_button.clicked.connect(self.boton_listo)
        self.firmar_button.setGeometry(650, 120, 100, 30)
        self.firmar_button.setFont(QFont("georgia", 18))

        self.imagen_jugador2 = QLabel(self)
        imagen_jugador2 = QPixmap(p.ruta("RUTA_AVATAR_2"))
        self.imagen_jugador2.setPixmap(imagen_jugador2)
        self.imagen_jugador2.setGeometry(20, 330, 130, 150)
        self.imagen_jugador2.setScaledContents(True)
        self.imagen_jugador2.setStyleSheet("background: transparent;")

        self.label2 = QLabel('¿Cuál es su apuesta?  ', self)
        self.label2.setGeometry(170, 400, 200, 30)
        self.label2.setFont(QFont("Times New Roman", 16))
        self.label2.setStyleSheet("color: white")

        self.canicas_contrario = QLabel('Esperando...  ', self)
        self.canicas_contrario.move(200, 430)
        self.canicas_contrario.setFont(QFont("Times New Roman", 16))
        self.canicas_contrario.setStyleSheet("background-color: #000000;"
                                             "color: #72A082")

        self.label3 = QLabel('El valor de tu apuesta es  ', self)
        self.label3.setGeometry(370, 400, 200, 30)
        self.label3.setFont(QFont("Times New Roman", 16))
        self.label3.setStyleSheet("color: white")

        self.par_contrario = QLabel('Esperando...  ', self)
        self.par_contrario.move(420, 430)
        self.par_contrario.setFont(QFont("Times New Roman", 16))
        self.par_contrario.setStyleSheet("background-color: #000000;"
                                         "color: #72A082")
        
        self.cuadrado_gris = QLabel(self)
        self.cuadrado_gris.setGeometry(600, 340, 170, 140)
        self.cuadrado_gris.setStyleSheet("background-color: #232121")

        self.label5 = QLabel('Esperando a ..  ', self)
        self.label5.setGeometry(605, 350, 160, 30)
        self.label5.setFont(QFont("Times New Roman", 16))
        self.label5.setStyleSheet("background-color: #232121;"
                                  "color: white")
        
        self.label6 = QLabel("", self)
        self.label6.setGeometry(630, 380, 140, 30)
        self.label6.setFont(QFont("Times New Roman", 16))
        self.label6.setStyleSheet("background-color: #232121;"
                                  "color: white")

        self.imagen_gris = QLabel(self)
        imagen_gris = QPixmap(p.ruta("RUTA_RELOJ"))
        self.imagen_gris.setPixmap(imagen_gris)
        self.imagen_gris.setGeometry(650, 410, 70, 70)
        self.imagen_gris.setScaledContents(True)
        self.imagen_gris.setStyleSheet("background: transparent;")

        self.rbtn1 = QRadioButton('Impar', self)
        self.rbtn1.setGeometry(450, 120, 100, 30)
        self.rbtn1.setStyleSheet("color: white")
        self.rbtn2 = QRadioButton('Par', self)
        self.rbtn2.setStyleSheet("color: white")
        self.rbtn2.setGeometry(530, 120, 100, 30)

        self.sp = QSpinBox(self)
        self.sp.setGeometry(220, 120, 80, 35)
        self.sp.setStyleSheet("color: white")

        self.agregar_estilo()
    
    def agregar_informacion(self, jugador1, jugador2):
        self.jugador1 = jugador1
        self.jugador2 = jugador2
        self.nombre1_label.setText(f"Jugador 1: {jugador1.nombre}")
        self.nombre2_label.setText(f"Jugador 2: {jugador2.nombre}")
        self.imagen_jugador1.setPixmap(QPixmap(jugador1.imagen))
        self.imagen_jugador2.setPixmap(QPixmap(jugador2.imagen))
        self.label5.setText(f"Esperando a {jugador2.nombre}")
        self.sp.setRange(1, jugador1.canicas)

        for n in range(jugador1.canicas):
            self.canica = QLabel(self)
            self.canica.setPixmap(QPixmap(p.ruta("RUTA_CANICA_1")))
            self.canica.setGeometry(60*n+25, 220, 50, 50)
            self.canica.setScaledContents(True)
            self.canica.setStyleSheet("background: transparent;")
        
        for n in range(jugador2.canicas):
            self.canica = QLabel(self)
            self.canica.setPixmap(QPixmap(p.ruta("RUTA_CANICA_2")))
            self.canica.setGeometry(60*n+25, 520, 50, 50)
            self.canica.setScaledContents(True)
            self.canica.setStyleSheet("background: transparent;")
    
    def actualizar(self, apuesta, valor, ganar):
        self.canicas_contrario.setText(f"{apuesta} canicas")
        self.par_contrario.setText(f"{valor}")
        if ganar:
            self.label5.setText(f"{self.jugador2.nombre} ha perdido")
            self.label6.setText(f"Ganas {apuesta} canicas")
            imagen_gris = QPixmap(p.ruta("RUTA_CALAVERA_BLANCA"))
            self.imagen_gris.setPixmap(imagen_gris)
        else:
            self.label5.setText(f"{self.jugador2.nombre} ha ganado")
            self.label6.setText(f"Pierdes {apuesta} canicas")
            imagen_gris = QPixmap(p.ruta("RUTA_WONES"))
            self.imagen_gris.setPixmap(imagen_gris)

    def boton_listo(self):
        valor = self.sp.value()
        marcado = None
        if self.rbtn1.isChecked():
            marcado = "Impar"
        elif self.rbtn2.isChecked():
            marcado = "Par"
        self.boton_listo_signal.emit()
        # Faltaria que se envie la informacion de las asignaciones

    def agregar_estilo(self):

        self.setStyleSheet("background-color: #000000")

        self.cuadrado.setStyleSheet("background-color: 7EBBAB;"
                                    "border: 10px solid #ed1b76")
        
        self.cuadrado1.setStyleSheet("background-color: 7EBBAB;"
                                     "border: 10px solid #ed1b76")

        self.nombre1_label.setStyleSheet("background-color: #000000;"
                                         "color: #ffffff")
        
        self.nombre2_label.setStyleSheet("background-color: #000000;"
                                         "color: #ffffff")
        
        self.firmar_button.setStyleSheet("background-color: #ffffff;"
                                         "border-radius: 1px;"
                                         "color: #131212")
 
    def mostrar(self):
        self.show()
 
    def ocultar(self):
        self.hide()