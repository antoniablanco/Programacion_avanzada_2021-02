from PyQt5.QtCore import pyqtSignal
from PyQt5.QtGui import QFont
from PyQt5.QtWidgets import (
    QWidget, QLabel,  QMessageBox, QPushButton
)
import parametros as p


class VentanaRanking(QWidget):
    senal_volver_inicio = pyqtSignal()
    senal_obtener_orden = pyqtSignal()
    senal_fin_musica = pyqtSignal()
    senal_inicio_musica = pyqtSignal()

    def __init__(self, tamano_ventana):
        super().__init__()
        self.init_gui(tamano_ventana)
        self.rankings = []
        self.id_ranking = 0

        for n in range(p.N_MOSTRAR):
            self.label = QLabel(f"{n+1}.", self)
            self.label.setFont(QFont("Rockwell", 20))
            self.label.setGeometry(70, 80 + 60*n, 300, 30)
            self.label.setStyleSheet("background-color: #247E29;"
                                     "color: black")
            self.rankings.append(self.label)

    def init_gui(self, tamano_ventana):
        self.setGeometry(tamano_ventana)

        self.label1 = QLabel('RANKING DE PUNTAJES: ', self)
        self.label1.setFont(QFont("Rockwell", 28))
        self.label1.setGeometry(80, 30, 350, 50)

        self.cuadrado = QLabel(self)
        self.cuadrado.setGeometry(20, 20, 460, 460)

        self.volver_button = QPushButton('Volver', self)
        self.volver_button.clicked.connect(self.volver)
        self.volver_button.setGeometry(180, 390, 150, 30)
        self.volver_button.setFont(QFont("georgia", 16))

        self.agregar_estilo()

    def agregar_estilo(self):
        self.setStyleSheet("background-color: #247E29")
        self.label1.setStyleSheet("background-color: #247E29;"
                                  " color: black")
        self.cuadrado.setStyleSheet("background-color: 7EBBAB;"
                                    "border: 10px solid rgb(176,224,230)")
        self.volver_button.setStyleSheet("background-color: #ffffff;"
                                        "border-radius: 5px;"
                                        "color: black")

    def volver(self):
        self.senal_volver_inicio.emit()
        self.ocultar()

    def mostrar_ranking(self, informacion):
        for persona in range(len(informacion)):
            nombre = informacion[persona][0]
            if len(nombre) < 10:
                nombre += (10-len(nombre))*" "
            parte1 = f"{persona+1}. {nombre}"
            parte2 = f"            {informacion[persona][1]} ptos"
            new = parte1 + parte2
            self.rankings[persona].setText(new)

    def mostrar(self):
        self.senal_inicio_musica.emit()
        self.senal_obtener_orden.emit()
        self.show()

    def ocultar(self):
        self.senal_fin_musica.emit()
        self.hide()

    def closeEvent(self, event):
        reply = QMessageBox.question(self, "Window Close", "¿Estas seguro que " +
        "quieres cerrar la ventana?", QMessageBox.Yes | QMessageBox.No)

        if reply == QMessageBox.Yes:
            self.volver()
            event.accept()
        else:
            event.ignore()