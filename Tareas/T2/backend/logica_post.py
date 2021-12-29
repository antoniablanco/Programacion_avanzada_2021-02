from PyQt5.QtCore import QObject, pyqtSignal
import parametros as p
from backend.clases_objetos import Musica


class Logica(QObject):
    senal_nuevo_nivel = pyqtSignal(int)

    def __init__(self):
        super().__init__()
        self.musica = Musica(p.RUTA_CANCION)

    def tienda(self):
        pass

    def siguiente_nivel(self, tiempo_ronda):
        duracion_ronda = p.PONDERADOR_DIFICULTAD * tiempo_ronda
        self.senal_nuevo_nivel.emit(duracion_ronda)

    def guardar_puntajes(self, nombre, puntaje):
        with open(p.RUTA_PUNTAJES, "a", encoding="utf-8") as puntajes:
            puntajes.write(f"{nombre},{int(puntaje)}\n")

    def stop_musica(self):
        self.musica.pausar()

    def comenzar_musica(self):
        self.musica.comenzar()
