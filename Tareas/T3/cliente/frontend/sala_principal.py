from PyQt5.QtWidgets import QLabel, QLineEdit, QPushButton, QWidget, QHBoxLayout, QVBoxLayout
from PyQt5.QtGui import QFont, QPixmap, QIcon
from PyQt5.QtCore import Qt, pyqtSignal
from backend.clases import Jugador
import obtener_parametros as p


class SalaPrincipal(QWidget):
    actualizar_nombres_signal = pyqtSignal(dict,  str, bool)
    boton_signal = pyqtSignal(int)

    def __init__(self):
        super().__init__()
        self.init_gui()
        self.actualizar_nombres_signal.connect(self.print_jugadores)

    def init_gui(self):
        self.botones = []
        self.jugadores = []
        self.botones_conectados = []
    
        self.setGeometry(300, 300, 500, 500)
        self.setWindowTitle("Sala Principal")
        self.setWindowIcon(QIcon(p.ruta("RUTA_WONES")))

        self.cuadrado = QLabel(self)
        self.cuadrado.setGeometry(0, 0, 500, 500)

        self.logo = QLabel(self)
        logo = QPixmap(p.ruta("RUTA_TARJETA"))
        self.logo.setPixmap(logo)
        self.logo.setGeometry(170, 380, 150, 100)
        self.logo.setScaledContents(True)
        self.logo.setStyleSheet("background: transparent;")

        self.slogan = QLabel('Jugadores que han aceptado el reto ', self)
        self.slogan.move(90, 25)
        self.slogan.setFont(QFont("Times New Roman", 22, italic=True))

        self.slogan2 = QLabel('¿Quién ganará el premio mayor? ', self)
        self.slogan2.move(80, 300)
        self.slogan2.setFont(QFont("Times New Roman", 26, italic=False))

        self.slogan3 = QLabel(' ₩ 45.600.000.000', self)
        self.slogan3.move(40, 330)
        self.slogan3.setFont(QFont("Times New Roman", 54, italic=False))

        self.jugador1 = QLabel('             0.', self)
        self.jugador1.setGeometry(40, 100, 150, 30)
        self.jugador1.setFont(QFont("Times New Roman", 18, italic=False))
        self.jugadores.append(self.jugador1)

        self.jugador2 = QLabel('             1.', self)
        self.jugador2.setGeometry(40, 140, 150, 30)
        self.jugador2.setFont(QFont("Times New Roman", 18, italic=False))
        self.jugadores.append(self.jugador2)

        self.jugador3 = QLabel('             2.', self)
        self.jugador3.setGeometry(40, 180, 150, 30)
        self.jugador3.setFont(QFont("Times New Roman", 18, italic=False))
        self.jugadores.append(self.jugador3)

        self.jugador4 = QLabel('             3.', self)
        self.jugador4.setGeometry(40, 220, 150, 30)
        self.jugador4.setFont(QFont("Times New Roman", 18, italic=False))
        self.jugadores.append(self.jugador4)

        self.boton1 = QPushButton('Retar', self)
        self.boton1.setFont(QFont("georgia", 18))
        self.boton1.setGeometry(300, 100, 90, 20)
        self.boton1.setStyleSheet("background-color: #000000;"
                                  "border-radius: 1px;"
                                  "color: black")
        self.botones.append(self.boton1)

        self.boton2 = QPushButton('Retar', self)
        self.boton2.setFont(QFont("georgia", 18))
        self.boton2.setGeometry(300, 140, 90, 20)
        self.boton2.setStyleSheet("background-color: #000000;"
                                  "border-radius: 1px;"
                                  "color: black")
        self.botones.append(self.boton2)

        self.boton3 = QPushButton('Retar', self)
        self.boton3.setFont(QFont("georgia", 18))
        self.boton3.setGeometry(300, 180, 90, 20)
        self.boton3.setStyleSheet("background-color: #000000;"
                                  "border-radius: 1px;"
                                  "color: black")
        self.botones.append(self.boton3)

        self.boton4 = QPushButton('Retar', self)
        self.boton4.setFont(QFont("georgia", 18))
        self.boton4.setGeometry(300, 220, 90, 20)
        self.boton4.setStyleSheet("background-color: #000000;"
                                  "border-radius: 1px;"
                                  "color: black")
        self.botones.append(self.boton4)

        self.frase = QLabel('             Esperando jugador... ', self)
        self.frase.setGeometry(40, 250, 400, 30)
        self.frase.setFont(QFont("Times New Roman", 18, italic=False))
        self.frase.setStyleSheet("background-color: trasparent;"
                                 "color: red")

        self.agregar_estilo()

    def agregar_estilo(self):

        self.setStyleSheet("background-color: #000000")

        self.cuadrado.setStyleSheet("background-color: 7EBBAB;"
                                    "border: 10px solid #ed1b76")
    
        self.slogan.setStyleSheet("background-color: trasparent;"
                                  "color: #ffffff")
        
        self.slogan2.setStyleSheet("background-color: trasparent;"
                                   "color: #ffffff")
        
        self.slogan3.setStyleSheet("background-color: trasparent;"
                                   "color: #ffffff")

    def print_jugadores(self, jugadores, main, esperando):
        nombres = []
        for nombre in jugadores.values():
            nombres.append(nombre)
 
        diccionario_alrevez = {v: k for k, v in jugadores.items()}

        for m in self.botones_conectados:
            m[0].clicked.disconnect() 
            m[0].setStyleSheet("background-color: black;"
                               "border-radius: 1px;"
                               "color: black")
        self.botones_conectados.clear()
        for m in range(4):
            self.jugadores[m].setText(f'             {m + 1}.')
            self.jugadores[m].setStyleSheet("color: black")

        if nombres:
            ctd = -1
            for jugador in nombres[:4]:

                ctd += 1
                self.jugadores[ctd].setText(f'             {ctd + 1}. {jugador}')
                self.jugadores[ctd].setStyleSheet("color: white")
                if not esperando:
                    self.frase.setText('             Esperando jugador... ')
                    if jugador != main:
                        self.botones[ctd].clicked.connect(self.retar)
                        self.botones[ctd].setStyleSheet("background-color: #ffffff;"
                                                        "border-radius: 1px;"
                                                        "color: black")
                        self.botones_conectados.append([self.botones[ctd], diccionario_alrevez[jugador]])
                else:
                    self.frase.setText('             Esperando respuesta jugador... ')
                            
    def retar(self):
        id_boton = self.sender()
        jugador = None
        for id in range(len(self.botones_conectados)):
            if id_boton == self.botones_conectados[id][0]:
                jugador = int(self.botones_conectados[id][1])
        self.boton_signal.emit(jugador)

    def mostrar(self):
        self.show()

    def ocultar(self):
        self.hide()