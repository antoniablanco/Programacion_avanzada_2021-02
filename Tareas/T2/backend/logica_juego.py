from PyQt5.QtCore import QObject, pyqtSignal, QTimer, QRect
import parametros as p
from backend.clases_objetos import Autos, Troncos, Objeto, Musica
from random import randint, choice


class Juego(QObject):
    senal_recolectado = pyqtSignal()
    senal_mover_auto = pyqtSignal(int, tuple)
    senal_mover_tronco = pyqtSignal(int, tuple)
    senal_ventana_post = pyqtSignal(tuple)
    senal_actualizar = pyqtSignal(tuple)
    senal_crear_auto = pyqtSignal(int, tuple)
    senal_crear_tronco = pyqtSignal(tuple)
    senal_crear_objeto = pyqtSignal(str, tuple)
    senal_siguiente = pyqtSignal()
    senal_ocultar_objeto = pyqtSignal(int)

    def __init__(self, frogg):
        super().__init__()

        self.frogg = frogg
        self.instanciar_timer()
        self.musica = Musica(p.RUTA_CANCION)

        self.contador_monedas = 0
        self.identificador_autos = 0
        self.identificador_troncos = 0
        self.identificador_objetos = 0
        self.ctd_objeto = 0
        self.autos = {}
        self.troncos = {}
        self.objetos = {}

        # Datos de la logica
        self.velocidad_autos = p.VELOCIDAD_AUTOS
        self.velocidad_troncos = p.VELOCIDAD_TRONCOS
        self.nombre = None
        self.unido = False
        self.id_union = None

        # Datos del juego visibles
        self.vida = p.VIDAS_INICIO
        self.nivel = 1
        self.puntaje_turno = 0
        self.puntaje_total = 0
        self.monedas = 0
        self.tiempo_restante = p.DURACION_RONDA_INICIAL
        self.tiempo_total = p.DURACION_RONDA_INICIAL

    def instanciar_timer(self):
        self.timer = QTimer()
        self.timer.timeout.connect(self.timer_tick)
        self.timer.setInterval(int(0.5 * 1000))
        self.subtick = 0

    def instanciar_autos(self):
        k = randint(0, 1)
        for n in range(p.FILAS_AUTOS):
            nuevo_auto = Autos(self.identificador_autos, (-1)**(k+n),
            posicionX=p.POS_INICIO_AUTOS_X[n], posicionY=p.POS_INICIO_AUTOS_Y[n])
            self.autos[self.identificador_autos] = nuevo_auto
            if nuevo_auto.direccion == -1:
                self.senal_crear_auto.emit(0, (nuevo_auto.posicionX, nuevo_auto.posicionY))
            else:
                self.senal_crear_auto.emit(1, (nuevo_auto.posicionX, nuevo_auto.posicionY))
            self.identificador_autos += 1

        for n in range(p.FILAS_AUTOS):
            n = int(n + p.FILAS_AUTOS)
            nuevo_auto = Autos(self.identificador_autos, (-1)**(k+n),
            posicionX=p.POS_INICIO_AUTOS_X[n], posicionY=p.POS_INICIO_AUTOS_Y[n])
            self.autos[self.identificador_autos] = nuevo_auto
            if nuevo_auto.direccion == -1:
                self.senal_crear_auto.emit(0, (nuevo_auto.posicionX, nuevo_auto.posicionY))
            else:
                self.senal_crear_auto.emit(1, (nuevo_auto.posicionX, nuevo_auto.posicionY))
            self.identificador_autos += 1

    def instanciar_troncos(self):
        k = randint(0, 1)
        for n in range(int(p.FILAS_TRONCOS)):
            nuevo_tronco = Troncos(self.identificador_troncos, (-1)**(k+n),
            posicionX=p.POS_INICIO_TRONCOS_X[n], posicionY=p.POS_INICIO_TRONCOS_Y[n])
            self.troncos[self.identificador_troncos] = nuevo_tronco
            self.senal_crear_tronco.emit((nuevo_tronco.posicionX, nuevo_tronco.posicionY))
            self.identificador_troncos += 1

        for n in range(int(p.FILAS_TRONCOS)):
            n = int(n + p.FILAS_TRONCOS)
            nuevo_tronco = Troncos(self.identificador_troncos, (-1)**(k+1+n), 
            posicionX=p.POS_INICIO_TRONCOS_X[n], posicionY=p.POS_INICIO_TRONCOS_Y[n])
            self.troncos[self.identificador_troncos] = nuevo_tronco
            self.senal_crear_tronco.emit((nuevo_tronco.posicionX, nuevo_tronco.posicionY))
            self.identificador_troncos += 1

        for n in range(int(p.FILAS_TRONCOS)):
            n = int(n + p.FILAS_TRONCOS*2)
            nuevo_tronco = Troncos(self.identificador_troncos, (-1)**(k+n), 
            posicionX=p.POS_INICIO_TRONCOS_X[n], posicionY=p.POS_INICIO_TRONCOS_Y[n])
            self.troncos[self.identificador_troncos] = nuevo_tronco
            self.senal_crear_tronco.emit((nuevo_tronco.posicionX, nuevo_tronco.posicionY))
            self.identificador_troncos += 1

    def instanciar_objeto(self):
        posicionx = randint(p.MIN_X, p.MAX_X)
        posiciony = randint(p.MIN_Y, p.MAX_Y)
        while ((p.Y_MIN_RIO <= posiciony <= p.Y_MAX_RIO + p.WIDTH_OBJETO) or 
                posiciony == self.frogg.posicionY):
            posiciony = randint(p.MIN_Y, p.MAX_Y)

        opciones = ["corazon", "reloj", "moneda", "calavera"]
        tipo = choice(opciones)
        objeto = Objeto(tipo, posicionx, posiciony)

        self.objetos[self.identificador_objetos] = objeto
        self.senal_crear_objeto.emit(tipo, (posicionx, posiciony))
        self.identificador_objetos += 1

    def iniciar_juego(self):
        self.timer.start()

    def detener_juego(self):
        self.timer.stop()

    def timer_tick(self):
        self.subtick += 1
        self.tiempo_restante -= 0.5
        self.ctd_objeto += 1

        if self.ctd_objeto == p.TIEMPO_OBJETO:
            self.ctd_objeto = 0
            self.instanciar_objeto()

        if not self.verificar_seguir():
            self.abrir_post()

        for auto in range(len(self.autos)):  # Genera el movimiento de los autos
            posicion = self.autos[auto].movimiento(self.velocidad_autos)
            self.senal_mover_auto.emit(auto, posicion)

        for tronco in range(len(self.troncos)):  # Genera el movimiento de los troncos
            posicion = self.troncos[tronco].movimiento(self.velocidad_troncos)
            self.senal_mover_tronco.emit(tronco, posicion)
            if self.unido and tronco == self.id_union:
                self.frogg.avanzar_tronco(posicion)

        if self.colision_auto() and self.frogg.direccion != "S":  # Verifica si choco con el auto
            self.frogg.reinicio()
            self.vida -= 1

        if self.frogg.posicionY < p.Y_MAX_RIO and self.frogg.posicionY > p.Y_MIN_RIO:
            if self.frogg.posicionX+1 >= p.MAX_X or self.frogg.posicionX-1 <= p.MIN_X:
                self.unido = False
                self.id_union = None
                self.frogg.reinicio()
                self.vida -= 1
        else:
            self.unido = False
            self.id_union = None

        self.recolecta_item()
        self.senal_actualizar.emit((self.vida, self.tiempo_restante, 
        self.monedas, self.puntaje_total, self.nivel))

    def verificar_seguir(self):
        devolver = True
        if self.vida <= 0:
            devolver = False
        elif self.tiempo_restante <= 0:
            devolver = False
        elif self.frogg.posicionY <= 180:
            devolver = False
        return devolver

    def recolecta_item(self):
        devolver = False
        for objeto in range(len(self.objetos)):
            posicionx = self.objetos[objeto].posicionX
            posiciony = self.objetos[objeto].posicionY

            if posicionx - p.WIDTH_FROGG <= self.frogg.posicionX <= posicionx + p.WIDTH_FROGG:
                if posiciony - p.WIDTH_FROGG <= self.frogg.posicionY <= posiciony + p.HEIGHT_FROGG:
                    if self.objetos[objeto].activo:
                        devolver = True
                        self.poder_objeto(objeto)
                        self.senal_ocultar_objeto.emit(objeto)
                        self.objetos[objeto].activo = False

        return devolver

    def colision_auto(self):
        devolver = False
        for auto in range(len(self.autos)):
            posicionx = self.autos[auto].posicionX
            posiciony = self.autos[auto].posicionY

            if posicionx <= self.frogg.posicionX <= posicionx + p.WIDTH_AUTO/2:
                if posiciony  <= self.frogg.posicionY <= posiciony + p.HEIGHT_AUTO/2:
                    devolver = True
        return devolver

    def abrir_post(self):
        self.detener_juego()
        self.puntaje_turno = (self.vida + self.tiempo_restante*50)*(self.nivel)
        self.puntaje_total += self.puntaje_turno
        informacion = (self.vida, self.nivel, self.tiempo_restante,
                       self.puntaje_turno, self.puntaje_total, self.monedas, self.nombre)
        self.senal_ventana_post.emit(informacion)

    def siguiente_nivel(self, tiempo):
        self.senal_siguiente.emit()

        nvelocidad_auto = self.velocidad_autos * (2/(1+p.PONDERADOR_DIFICULTAD))
        nvelocidad_tronco = self.velocidad_troncos * (2/(1+p.PONDERADOR_DIFICULTAD))

        self.instanciar_autos()
        self.instanciar_troncos()
        self.frogg.volver_inicio()

        self.tiempo_restante = tiempo
        self.tiempo_total = tiempo
        self.velocidad_autos = nvelocidad_auto
        self.velocidad_troncos = nvelocidad_tronco
        self.puntaje_turno = 0
        self.nivel += 1

        self.senal_actualizar.emit((self.vida, self.tiempo_restante, self.monedas,
                                    self.puntaje_turno, self.nivel))

    def pausar(self):
        self.detener_juego()

    def continuar(self):
        self.iniciar_juego()

    def cheat_vida(self):
        self.vida += p.VIDAS_TRAMPA

    def definir_nombre(self, nombre):
        self.nombre = nombre

    def union_rio(self):
        self.unido = False
        self.id_union = None
        if self.frogg.direccion == "U":
            if (self.frogg.posicionY - p.PIXELES_SALTO <= p.Y_MAX_RIO
                and self.frogg.posicionY - p.PIXELES_SALTO > p.Y_MIN_RIO):
                for tronco in range(len(self.troncos)):
                    posicionx = self.troncos[tronco].posicionX
                    posiciony = self.troncos[tronco].posicionY
                    minimox = posicionx - int(p.WIDTH_TRONCO/2)
                    maximox = posicionx + int(p.WIDTH_TRONCO)
                    minimoy = posiciony - int(p.HEIGHT_TRONCO/2)
                    maximoy = posiciony + int(p.HEIGHT_TRONCO/2)

                    if minimoy <= self.frogg.posicionY - p.PIXELES_SALTO <= maximoy:
                        if minimox <= self.frogg.posicionX <= maximox:
                            self.unido = True
                            self.id_union = tronco
                            self.frogg.cambiar_direccion("J")
                            self.frogg.avanzar()
            else:
                self.frogg.cambiar_direccion("J")
                self.frogg.avanzar()

        elif self.frogg.direccion == "D":
            if (self.frogg.posicionY + p.PIXELES_SALTO <= p.Y_MAX_RIO
                and self.frogg.posicionY - p.PIXELES_SALTO > p.Y_MIN_RIO):
                for tronco in range(len(self.troncos)):
                    posicionx = self.troncos[tronco].posicionX
                    posiciony = self.troncos[tronco].posicionY
                    minimox = posicionx
                    maximox = posicionx + int(p.WIDTH_TRONCO)
                    minimoy = posiciony - int(p.HEIGHT_TRONCO/2)
                    maximoy = posiciony + int(p.HEIGHT_TRONCO/2)

                    if minimoy <= self.frogg.posicionY + p.PIXELES_SALTO <= maximoy:
                        if minimox <= self.frogg.posicionX <= maximox:
                            self.unido = True
                            self.id_union = tronco
                            self.frogg.cambiar_direccion("J")
                            self.frogg.avanzar()
            else:
                self.frogg.cambiar_direccion("J")
                self.frogg.avanzar()
        else:
            minimo = self.frogg.posicionY - p.VELOCIDAD_CAMINAR >= p.Y_MAX_RIO
            maximo = self.frogg.posicionY <= p.Y_MIN_RIO
            if maximo or minimo:
                self.frogg.cambiar_direccion("J")
                self.frogg.avanzar()
        if not self.unido and self.frogg.posicionY > p.Y_MIN_RIO:
            self.frogg.reinicio()
            self.vida -= 1

    def resetear(self):
        self.instanciar_timer()
        self.contador_monedas = 0

        '''
        self.identificador_autos = 0
        self.identificador_troncos = 0
        self.identificador_objetos = 0
        self.autos.clear()
        self.troncos.clear()
        self.objetos.clear()
        '''

        # Datos de la logica
        self.velocidad_autos = p.VELOCIDAD_AUTOS
        self.velocidad_troncos = p.VELOCIDAD_TRONCOS
        self.nombre = None
        self.unido = False
        self.id_union = None

        # Datos del juego visibles
        self.vida = p.VIDAS_INICIO
        self.nivel = 1
        self.puntaje_turno = 0
        self.puntaje_total = 0
        self.monedas = 0
        self.tiempo_restante = p.DURACION_RONDA_INICIAL

        self.frogg.volver_inicio()

    def poder_objeto(self, id):
        objeto = self.objetos[id]
        if objeto.tipo == "corazon":
            self.vida += 1
        elif objeto.tipo == "moneda":
            self.monedas += 1
        elif objeto.tipo == "calavera":
            self.velocidad_troncos = self.velocidad_troncos*1.05
        elif objeto.tipo == "reloj":
            try:
                self.tiempo_restante += (self.tiempo_restante/self.tiempo_total)*10
            except ZeroDivisionError as error:
                print("Se dividio por eso")
                self.tiempo_restante = 0

    def stop_musica(self):
        self.musica.pausar()

    def comenzar_musica(self):
        self.musica.comenzar()

    def vaciar(self):
        self.identificador_autos = 0
        self.identificador_troncos = 0
        self.identificador_objetos = 0
        self.autos.clear()
        self.troncos.clear()
        self.objetos.clear()