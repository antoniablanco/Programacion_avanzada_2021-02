from frontend.ventana_inicio import VentanaInicio
from frontend.sala_principal import SalaPrincipal
from frontend.ventana_reto import VentanaReto
from frontend.ventana_final import VentanaFinal
from frontend.sala_juego import SalaJuego
from backend.clases import Jugador
from PyQt5.QtCore import pyqtSignal, QObject
import obtener_parametros as p

class Manejo(QObject):

    mostrar_ventana_inicio_signal = pyqtSignal()
    mostrar_sala_principal_signal = pyqtSignal()
    mostrar_ventana_reto_signal = pyqtSignal(int, str)
    mostrar_sala_juego_signal = pyqtSignal(Jugador, Jugador)
    mostrar_ventana_final_signal = pyqtSignal(str, str)
    actualizar_clientes_signal = pyqtSignal()
    senal_servidor = pyqtSignal(dict)  

    def __init__(self, parent):
        super().__init__()
        self.ventana_inicio = VentanaInicio()
        self.sala_principal = SalaPrincipal()
        self.ventana_reto = VentanaReto()
        self.ventana_final = VentanaFinal()
        self.sala_juego = SalaJuego()

        self.jugador = None  # Clase Jugador
        self.retador = None  # Clase Jugador
        self.ruta_libre = None  # Se guarda el avatar no utilizado
        self.esperando = False  # Bool que indica si esta esperando una respuesta
        self.retando = None  # El nombre del jugador a quien reta
        # Se conectan las señales:

        # Señales de la clase manejo
        self.senal_servidor.connect(parent.send)
        self.mostrar_ventana_inicio_signal.connect(self.mostrar_ventana_inicio)
        self.mostrar_sala_principal_signal.connect(self.mostrar_sala_principal)
        self.mostrar_ventana_reto_signal.connect(self.mostrar_ventana_reto)
        self.mostrar_sala_juego_signal.connect(self.mostrar_sala_juego)
        self.mostrar_ventana_final_signal.connect(self.mostrar_ventana_final)
        self.actualizar_clientes_signal.connect(self.actualizar_jugadores)

        # Señales de las ventanas
        self.ventana_inicio.senal_enviar_usuario.connect(parent.send)
        self.sala_principal.boton_signal.connect(self.retar_jugador)
        self.ventana_reto.boton_aceptar_signal.connect(self.aceptar_reto)
        self.ventana_reto.boton_rechazar_signal.connect(self.rechazar_reto)
        self.sala_juego.boton_listo_signal.connect(self.fin_partida)
        self.ventana_final.boton_nueva_partida_signal.connect(self.nueva_partida)
        
    def mostrar_ventana_inicio(self):
        try:
            self.ventana_final.ocultar()
        finally:
            self.ventana_inicio.mostrar()

    def mostrar_sala_principal(self):
        try:
            self.ventana_inicio.ocultar()
            self.ventana_reto.ocultar()
        finally:
            self.sala_principal.mostrar()
    
    def mostrar_ventana_reto(self, id_retador, nombre_retador):
        self.esperando = False
        self.sala_principal.ocultar()
        self.ventana_reto.mostrar(id_retador, nombre_retador)
    
    def mostrar_sala_juego(self, jugador1, jugador2):
        self.esperando = False
        try:
            self.ventana_reto.ocultar()
            self.sala_principal.ocultar()
        finally:
            self.sala_juego.agregar_informacion(jugador1, jugador2)
            self.sala_juego.mostrar()
    
    def mostrar_ventana_final(self, ganador, perdedor):
        self.sala_juego.close()
        self.ventana_final.definir_info(ganador, perdedor)
        self.ventana_final.mostrar()

    def actualizar_jugadores(self):
        info_pedir = {"comando": "actualizar_clientes_activos"}
        self.senal_servidor.emit(info_pedir)

    def retar_jugador(self, id_jugador_retar): 
        info_pedir = {"comando": "retar_jugador",
                      "id_jugador": id_jugador_retar,
                    }
        self.senal_servidor.emit(info_pedir)
        self.esperando = True
        self.retando = id_jugador_retar
        self.actualizar_clientes_signal.emit()
    
    def aceptar_reto(self, id_retador):
        id_retado = self.jugador.identificador
        info_pedir = {"comando": "aceptar_reto",
                      "id_jugadores": (id_retador, id_retado),
                      }
        self.senal_servidor.emit(info_pedir)

    def rechazar_reto(self, id_retador):
        id_retado = self.jugador.identificador
        info_pedir = {"comando": "rechazar_reto",
                      "id_jugadores": (id_retador, id_retado)}
        self.senal_servidor.emit(info_pedir)

    def iniciar_partida(self):
        info_pedir = {"comando": "iniciar_partida"}
        self.senal_servidor.emit(info_pedir)

    def fin_partida(self):
        # Si esto funcionara correctamente se le entregaria el id del ganador
        # Y el del perdedor
        info_pedir = {"comando": "fin_partida",
                      "ganador_perdedor": (self.jugador.identificador, self.retador.identificador)}
        self.senal_servidor.emit(info_pedir)

    def nueva_partida(self):
        print("Llega a nueva partida")
        info_pedir = {"comando": "nueva_partida",
                      "jugador": self.jugador.identificador}
        self.senal_servidor.emit(info_pedir)

    def manejar_mensaje(self, mensaje):
        try:
            comando = mensaje["comando"]
        except KeyError:
            print("Falta de keyword comando")
            return []

        if comando == "ingreso_aceptado":
            datos_usuario = mensaje["info"]
            if datos_usuario[1] % 2 == 0:
                ruta = "RUTA_AVATAR_1"
                self.ruta_libre = "RUTA_AVATAR_2"
            else:
                ruta = "RUTA_AVATAR_2"
                self.ruta_libre = "RUTA_AVATAR_1"

            jugador = Jugador(datos_usuario[0], datos_usuario[2], ruta, datos_usuario[1])
            self.jugador = jugador
            self.actualizar_clientes_signal.emit()
            self.mostrar_sala_principal_signal.emit()

        elif comando == "ingreso_rechazado":
            self.ventana_inicio.razon_signal.emit(mensaje)

        elif comando == "actualizar_nombres_activos":
            for ky in mensaje["dict_nombres"].keys():
                if self.retando == int(ky):
                    self.esperando = False
                    self.retando = None
            nombres = mensaje["dict_nombres"]
            self.sala_principal.actualizar_nombres_signal.emit(nombres, 
                                    self.jugador.nombre, self.esperando)

        elif comando == "retando_jugador":
            id_retador = mensaje["retador"][0]
            nombre_retador = mensaje["retador"][1]
            self.mostrar_ventana_reto_signal.emit(id_retador, nombre_retador)
        
        elif comando == "volver_principal":
            self.actualizar_clientes_signal.emit()
            self.mostrar_sala_principal_signal.emit()

        elif comando == "iniciar_partida":
            info = mensaje["jugadores"]
            fecha = None

            if info[0] == self.jugador.identificador:
                self.retador = Jugador(info[3], fecha, self.ruta_libre, info[2])
            else:
                self.retador = Jugador(info[1], fecha, self.ruta_libre, info[0])
            self.ruta_libre = None
            self.mostrar_sala_juego_signal.emit(self.jugador, self.retador)

        elif comando == "fin_partida":
            ganador = mensaje["ganador_perdedor"][0]
            perdedor = mensaje["ganador_perdedor"][1]
            self.retador = None
            self.mostrar_ventana_final_signal.emit(ganador, perdedor)

        elif comando == "reiniciar":
            self.jugador = None
            self.mostrar_ventana_inicio_signal.emit()

        else:
            print(f"Error: no existe comando {comando} ")
