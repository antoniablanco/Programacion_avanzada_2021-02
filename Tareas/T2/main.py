import sys

from PyQt5.QtCore import QRect
from PyQt5.QtWidgets import QApplication

from frontend.ventana_inicio import VentanaInicio
from frontend.ventana_juego import VentanaJuego
from frontend.ventana_post import VentanaPost
from frontend.ventana_ranking import VentanaRanking

import backend.logica_inicio
import backend.logica_ranking
import backend.logica_juego
import backend.logica_post
import backend.clases_objetos

import parametros as p

if __name__ == '__main__':
    def hook(type, traceback):
        print(type)
        print(traceback)
    sys.__excepthook__ = hook
    app = QApplication([])

    # Instanciación de ventana
    tamano_ventana = QRect(*p.TAMANO_VENTANA)
    tamano_ventana_juego = QRect(*p.TAMANO_VENTANA_JUEGO)
    ventana_inicio = VentanaInicio(tamano_ventana)
    ventana_juego = VentanaJuego(tamano_ventana_juego)
    ventana_post = VentanaPost(tamano_ventana)
    ventana_ranking = VentanaRanking(tamano_ventana)

    # Instanciación de lógica
    logica_inicio = backend.logica_inicio.Logica()
    logica_ranking = backend.logica_ranking.Logica()
    logica_post = backend.logica_post.Logica()
    frogg = backend.clases_objetos.Frogg()
    juego = backend.logica_juego.Juego(frogg)

    # Conexiones ventana inicio
    ventana_inicio.senal_verificar_nombre.connect(logica_inicio.comprobar_nombre)
    ventana_inicio.senal_abrir_ranking.connect(logica_inicio.abrir_ranking)
    ventana_inicio.senal_fin_musica.connect(logica_inicio.stop_musica)
    ventana_inicio.senal_resetear.connect(juego.resetear)
    ventana_inicio.senal_inicio_musica.connect(logica_inicio.comenzar_musica)

    # Conexion logica inicio
    logica_inicio.senal_respuesta_validacion.connect(ventana_inicio.recibir_validacion)
    logica_inicio.senal_ventana_ranking.connect(ventana_ranking.mostrar)
    logica_inicio.senal_ventana_juego.connect(ventana_juego.mostrar)
    logica_inicio.senal_ventana_juego.connect(juego.definir_nombre)

    # Conexiones ventana ranking
    ventana_ranking.senal_volver_inicio.connect(logica_ranking.volver_inicio)
    ventana_ranking.senal_obtener_orden.connect(logica_ranking.ordenar)
    ventana_ranking.senal_fin_musica.connect(logica_ranking.stop_musica)
    ventana_ranking.senal_inicio_musica.connect(logica_ranking.comenzar_musica)

    # Conexion logica ventana ranking
    logica_ranking.senal_ventana_inicio.connect(ventana_inicio.mostrar)
    logica_ranking.senal_mostrar_ranking.connect(ventana_ranking.mostrar_ranking)

    # Conexiones ventana juego
    ventana_juego.senal_tecla.connect(frogg.cambiar_direccion)
    ventana_juego.senal_tecla.connect(frogg.avanzar)
    ventana_juego.senal_salto.connect(juego.union_rio)
    ventana_juego.senal_iniciar_juego.connect(juego.iniciar_juego)
    ventana_juego.senal_iniciar_juego.connect(juego.instanciar_autos)
    ventana_juego.senal_iniciar_juego.connect(juego.instanciar_troncos)
    ventana_juego.senal_abrir_post.connect(juego.abrir_post)
    ventana_juego.senal_pausa.connect(juego.pausar)
    ventana_juego.senal_continuar.connect(juego.continuar)
    ventana_juego.senal_cheat_vidas.connect(juego.cheat_vida)
    ventana_juego.senal_resetear.connect(ventana_inicio.resetear)
    ventana_juego.senal_fin_musica.connect(juego.stop_musica)
    ventana_juego.senal_inicio_musica.connect(juego.comenzar_musica)
    ventana_juego.senal_cerrar.connect(juego.vaciar)

    # Conexiones logica juego
    frogg.senal_mover.connect(ventana_juego.avanzar)
    juego.senal_recolectado.connect(ventana_juego.ocultar_objeto)
    juego.senal_mover_auto.connect(ventana_juego.mover_autos)
    juego.senal_mover_tronco.connect(ventana_juego.mover_troncos)
    juego.senal_ventana_post.connect(ventana_post.mostrar)
    juego.senal_ventana_post.connect(ventana_juego.ocultar)
    juego.senal_actualizar.connect(ventana_juego.actualizar_informacion)
    juego.senal_crear_auto.connect(ventana_juego.crear_autos)
    juego.senal_crear_tronco.connect(ventana_juego.crear_troncos)
    juego.senal_siguiente.connect(ventana_juego.siguiente_nivel)
    juego.senal_ocultar_objeto.connect(ventana_juego.ocultar_objeto)
    juego.senal_crear_objeto.connect(ventana_juego.crear_objeto)

    # Conexiones ventana post-nivel
    ventana_post.senal_siguiente_nivel.connect(logica_post.siguiente_nivel)
    ventana_post.senal_guardar_puntaje.connect(logica_post.guardar_puntajes)
    ventana_post.senal_ventana_inicio.connect(ventana_inicio.resetear)
    ventana_post.senal_fin_musica.connect(logica_post.stop_musica)
    ventana_post.senal_inicio_musica.connect(logica_post.comenzar_musica)

    # Conexiones logica post
    logica_post.senal_nuevo_nivel.connect(juego.siguiente_nivel)

    ventana_inicio.mostrar()
    app.exec()
