import threading
import obtener_parametro as p
from random import randint


class LogicaJuego:
  
    ingresar_cliente_lock = threading.Lock()
    clientes_activos_lock = threading.Lock()

    def __init__(self, log_activado=True):
        super().__init__()
        self.jugadores = {}
        self.clientes_activos = {}
        self.retos_activos = {}
        self.log_activado = log_activado
        self.id_reto = 0

    def nombre_fecha_usuario(self, nombre_usuario, fecha_cumpleaños):  
        with self.clientes_activos_lock:  
            if len(nombre_usuario) < p.parametro("MIN_CARACTERES"):
                self.log(f"El largo de nombre {nombre_usuario} no cumple con el minimo de caracteres")
                return False, "Nombre de usuario no válido"
            elif nombre_usuario in self.jugadores.values():
                self.log(f"Nombre {nombre_usuario} ya fue utilizado")
                return False, "Nombre de usuario ya utilizado"
            elif not self.fecha_usuario(fecha_cumpleaños):
                self.log("Formato de fecha incorrecto")
                return False, "Fecha de cumpleaños no válida"
            else:
                self.log(f"Nombre {nombre_usuario} es valido, bienvenido!")
                self.log(f"")
                return True, None

    def fecha_usuario(self, fecha_cumpleaños):
        devolver = True
        if not "/" in fecha_cumpleaños:
            devolver = False
        else:
            fecha = fecha_cumpleaños.split("/")
            if len(fecha) != 3:
                devolver = False
            else:
                if not fecha[0].isnumeric() or not fecha[1].isnumeric() or not fecha[2].isnumeric():
                    devolver = False
                elif len(fecha[0]) != 2 or len(fecha[1]) != 2 or len(fecha[2]) != 4:
                    devolver = False
        return devolver
 
    def comienza_turno(self, jugador1, jugador2):
        valor = randint(1, 2)
        if valor == 1:
            return jugador1
        else:
            return jugador2

    def eliminar_cliente(self, id_cliente):
        with self.clientes_activos_lock:
            try:
                del self.jugadores[id_cliente]
                self.log(f"Se ha eliminado al cliente {id_cliente} de la lista de usuarios")
            except KeyError:
                self.log(f"El cliente {id_cliente} no esta activo")

    def manejar_mensaje(self, mensaje, id_cliente):
        try:
            comando = mensaje["comando"]

        except KeyError:
            self.log(f"ERROR: el mensaje del cliente {id_cliente} no cumple el formato.")
            return dict()

        respuesta = dict()
        destinatarios = [id_cliente]
        destinatarios_todos = list()
        for id in self.jugadores.keys():
            destinatarios_todos.append(id)
     
        if comando == "ingreso":
            nombre_usuario = mensaje["info"][0]
            fecha_usuario = mensaje["info"][1]
            with self.ingresar_cliente_lock:
                resultado, comentario = self.nombre_fecha_usuario(nombre_usuario, fecha_usuario)
                if resultado:
                    self.log("El nombre es valido")
                    with self.clientes_activos_lock:
                        self.jugadores[id_cliente] = nombre_usuario
                        self.clientes_activos[id_cliente] = nombre_usuario
                    respuesta = {
                        "comando": "ingreso_aceptado",
                        "info": (nombre_usuario, id_cliente, fecha_usuario),
                    }
                    self.log(f"Cliente: {self.clientes_activos[id_cliente]} con" +
                             f"ID: {id_cliente} ha sido aceptado en el juego")
                else:
                    self.log("El nombre o la fecha no son validos")
                    respuesta = {
                        "comando": "ingreso_rechazado",
                        "comentario": comentario,
                    }
     
        elif comando == "actualizar_clientes_activos":
            with self.clientes_activos_lock:
                destinatarios = destinatarios_todos
                respuesta = {
                    "comando": "actualizar_nombres_activos",
                    "dict_nombres": self.clientes_activos
                }
        
        elif comando == "retar_jugador":
            with self.clientes_activos_lock:
                retado = mensaje["id_jugador"]
                del self.clientes_activos[id_cliente]
                del self.clientes_activos[retado]
                destinatarios = [retado]
            respuesta = {
                "comando": "retando_jugador",
                "retador": (id_cliente, self.jugadores[id_cliente]),
            }
            self.log(f"Jugador: {id_cliente} ha retado a jugador {retado}")

        elif comando == "aceptar_reto":
            jugadores = mensaje["id_jugadores"]
            destinatarios = jugadores
            info = []
            for k in jugadores:
                info.append(k)
                info.append(self.jugadores[k])
            respuesta = {
                "comando": "iniciar_partida",
                "jugadores": info,
            }
            self.retos_activos[self.id_reto] = jugadores
            self.log(f'Jugador {id_cliente} acepto el reto, reto: {self.id_reto}')
            self.id_reto += 1
        
        elif comando == "rechazar_reto":
            jugadores = mensaje["id_jugadores"]
            destinatarios = jugadores
            with self.clientes_activos_lock:
                for jugador in jugadores:
                    self.clientes_activos[int(jugador)] = self.jugadores[jugador]
            respuesta = {
                "comando": "volver_principal",
                "jugadores": jugadores,
            }
            self.log(f'Jugador {id_cliente} rechazo el reto')

        elif comando == "iniciar_partida":
            pass

        elif comando == "fin_partida":
            ganador_id = mensaje["ganador_perdedor"][0]
            perdedor_id = mensaje["ganador_perdedor"][1]
            destinatarios = [ganador_id, perdedor_id]
            reto = None
            for k in self.retos_activos.keys():
                if ganador_id in self.retos_activos[k]:
                    reto = k
            del self.retos_activos[reto]
            respuesta = {
                "comando": "fin_partida",
                "ganador_perdedor": (self.jugadores[ganador_id], self.jugadores[perdedor_id])
            }
            self.log(f'El reto {reto} ha terminado. El ganador fue {self.jugadores[ganador_id]}')

        elif comando == "nueva_partida":
            id_jugador = mensaje["jugador"]
            del self.jugadores[id_jugador]
            respuesta = {
                "comando": "reiniciar",
            }
        
        return respuesta, destinatarios

    def log(self, mensaje_consola):
        if self.log_activado:
            print(mensaje_consola)