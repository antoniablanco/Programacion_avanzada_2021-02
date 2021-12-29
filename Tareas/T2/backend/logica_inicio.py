from PyQt5.QtCore import QObject, pyqtSignal

import parametros as p
from backend.clases_objetos import Musica


class Logica(QObject):

    senal_respuesta_validacion = pyqtSignal(tuple)
    senal_ventana_juego = pyqtSignal(str)
    senal_ventana_ranking = pyqtSignal()

    def __init__(self):
        super().__init__()
        self.musica = Musica(p.RUTA_CANCION)
        self.musica.comenzar()

    def comprobar_nombre(self, nombre):
        if nombre.isalnum() and len(nombre) <= p.MAX_CARACTERES and len(nombre) >= p.MIN_CARACTERES:
            self.senal_ventana_juego.emit(nombre)
            self.senal_respuesta_validacion.emit((nombre, True))
        else:
            self.senal_respuesta_validacion.emit((nombre, False))

    def abrir_ranking(self):
        self.senal_ventana_ranking.emit()

    def stop_musica(self):
        self.musica.pausar()

    def comenzar_musica(self):
        self.musica.comenzar()