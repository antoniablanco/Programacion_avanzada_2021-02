import sys
from PyQt5.QtWidgets import QApplication
from backend.cliente1 import Client
import obtener_parametros as p

from frontend.ventana_inicio import VentanaInicio
from frontend.sala_principal import SalaPrincipal
from frontend.ventana_reto import VentanaReto
from frontend.ventana_final import VentanaFinal
from frontend.sala_juego import SalaJuego
from backend.clases import Jugador

if __name__ == "__main__":
    def hook(type, traceback):
        print(type)
        print(traceback)
    
    sys.__excepthook__ = hook
    app = QApplication([])
    
    #ventana_inicio = VentanaInicio()
    #sala_principal = SalaPrincipal()
    #ventana_reto = VentanaReto()
    #ventana_final = VentanaFinal()
    #sala_juego = SalaJuego()

    #jugador1 = Jugador("Maxy I5", "01/04/2001", "RUTA_AVATAR_1")
    #jugador2 = Jugador("EmiliaPinto", "05/03/2011", "RUTA_AVATAR_2")
    #sala_juego.agregar_informacion(jugador1, jugador2)

    #ventana_inicio.mostrar()
    #ventana_reto.mostrar("Jo")
    #sala_principal.mostrar()
    #ventana_final.mostrar("MaxI5", "EmiliaPinto")
    #sala_juego.actualizar("2","Par", False)
    #sala_juego.mostrar()

    port = p.parametro("PORT")
    host = p.parametro("HOST")

    servidor = Client(port, host)

    fin = app.exec_()

    sys.exit(fin)

    