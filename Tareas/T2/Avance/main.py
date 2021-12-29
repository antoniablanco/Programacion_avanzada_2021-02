import sys

from PyQt5.QtCore import QRect
from PyQt5.QtWidgets import QApplication

import parametros as p
from frontend.ventana_inicio import VentanaInicio
import backend.back_avance 


if __name__ == '__main__':
    def hook(type, traceback):
        print(type)
        print(traceback)
    sys.__excepthook__ = hook
    app = QApplication([])

    # Instanciación de ventana
    tamano_ventana = QRect(*p.TAMANO_VENTANA)
    ventana_inicio = VentanaInicio(tamano_ventana)

    # Instanciacion de logica
    frogg = backend.back_avance.Frogg()
    juego = backend.back_avance.Juego(frogg)

    # Conexiones
    ventana_inicio.senal_tecla.connect(frogg.cambiar_direccion)
    ventana_inicio.senal_tecla.connect(frogg.avanzar)
    ventana_inicio.senal_iniciar_juego.connect(juego.iniciar_juego)

    frogg.senal_mover.connect(ventana_inicio.avanzar)
    juego.senal_recolectado.connect(ventana_inicio.ocultar_objeto)
    juego.senal_fin.connect(ventana_inicio.ocultar)
    juego.senal_mover_auto.connect(ventana_inicio.mover_autos)

    ventana_inicio.mostrar()
    app.exec()


