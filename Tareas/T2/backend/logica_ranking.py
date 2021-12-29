from PyQt5.QtCore import QObject, pyqtSignal
import parametros as p
from backend.clases_objetos import Musica


class Logica(QObject):

    senal_ventana_inicio = pyqtSignal()
    senal_mostrar_ranking = pyqtSignal(list)

    def __init__(self):
        super().__init__()
        self.musica = Musica(p.RUTA_CANCION)

    def ordenar(self):
        try:
            archivo = open(p.RUTA_PUNTAJES, "r")
            lectura = archivo.readlines()
            archivo.close()
        except FileNotFoundError as error:
            print("El archivo todavia no ha sido creado")
            lectura = []

        puntajes = []
        for linea in lectura:
            sin_strip = linea.strip("\n")
            puntos = sin_strip.split(",")
            puntajes.append(puntos)

        puntajes.sort(key=self.k_orden)
        if len(puntajes) >= p.N_MOSTRAR:
            puntajes = puntajes[0:p.N_MOSTRAR]
        self.senal_mostrar_ranking.emit(puntajes)

    def k_orden(self, elemento):
        try:
            return -1 * int(elemento[1])

        except IndexError as error:
            print("La lista esta vacia")
            return 0

    def volver_inicio(self):
        self.senal_ventana_inicio.emit()

    def stop_musica(self):
        self.musica.pausar()

    def comenzar_musica(self):
        self.musica.comenzar()

