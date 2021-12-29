import socket
import threading
import json
from logica_juego import LogicaJuego
import codificacion as c
import obtener_parametro as p
 
class Servidor:
    cliente_id = 0
    lock_clientes = threading.Lock()

    def __init__(self, host, port):
        self.host = "localhost"
        self.port = 12341
        self.socket_servidor = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.log("Se creo el Servidor")

        self.clientes_conectados = {}
        self.logica = LogicaJuego()

        self.unir_y_escuchar()

    def unir_y_escuchar(self):
        self.socket_servidor.bind((self.host, self.port))
        self.socket_servidor.listen()
        self.log(f'Servidor escuchando en {self.host}:{self.port}')
        self.aceptar_conexiones()
    
    def aceptar_conexiones(self):
        self.log("Se creo el thread para aceptar conexiones")
        thread = threading.Thread(target=self.aceptar_clientes)
        thread.start()

    def aceptar_clientes(self):
        self.log("Aceptando las conexiones...")
        while True:
            socket_cliente, address = self.socket_servidor.accept()
            self.clientes_conectados[self.cliente_id] = socket_cliente
            self.log(f'Cliente con dirección {address} se ha conectado al servidor')
            thread_cliente = threading.Thread(target=self.escuchar_cliente, args=(socket_cliente, self.cliente_id))
            self.cliente_id += 1
            thread_cliente.start()

    def escuchar_cliente(self, socket_cliente, id_cliente):
        self.log(f"Escuchando al cliente. ID: {id_cliente}")
        try:
            while True:
                mensaje = self.recibir(socket_cliente, id_cliente)
                if not mensaje:
                    raise ConnectionResetError
                elif mensaje != {}:
                    self.log(f'Acción asociada al mensaje: {mensaje}') 
                    respuesta, destinatarios = self.logica.manejar_mensaje(mensaje, id_cliente) #Falta crear en logica
                    self.enviar(respuesta, destinatarios)

        except ConnectionResetError:
            self.log('Error de conexión con el cliente')
            self.eliminar_cliente(id_cliente)

    def recibir(self, socket_cliente, id_usuario):
        largo = socket_cliente.recv(4)  
        largo_mensaje = int.from_bytes(largo, byteorder="little")
        largo_total = largo_mensaje // (84 - 4)
        if largo_mensaje % (84 - 4) != 0:
            largo_total += 1
        largo_total *= 84
        array_mensaje = bytearray()
        while len(array_mensaje) < largo_total:
            bytes_nuevos = min(84, largo_total - len(array_mensaje))
            array_mensaje += socket_cliente.recv(bytes_nuevos)
        mensaje_decodificado = self.decodificar_mensaje(largo + array_mensaje)
        return mensaje_decodificado
        
    def decodificar_mensaje(self, mensaje):
        tamano_chunk = 84  
        largo = mensaje[0: 4]
        largo_mensaje = int.from_bytes(largo, byteorder="little")
        largo_total = largo_mensaje // 80
        if largo_mensaje % 80 != 0:
            largo_total += 1
        largo_total *= tamano_chunk
        array_mensaje = bytearray()
        for i in range(4, largo_total, tamano_chunk):  
            bloque = mensaje[i: i + 4]
            numero_bloque = int.from_bytes(bloque, byteorder="big")
            bytes_nuevos = mensaje[i + 4: i + tamano_chunk]
            bytes_nuevos = bytes_nuevos.strip(b'\x00')
            bytes_nuevos = c.desincriptar(bytes_nuevos)
            array_mensaje += bytes_nuevos
        try:
            mensaje_decodificado = json.loads(array_mensaje)
            return mensaje_decodificado
        except json.JSONDecodeError:
            print("No se pudo decodificar el mensaje")
            return dict()

    def enviar(self, respuesta, socket_client):
        mensaje_codificado = self.codificar_mensaje(respuesta)
        try:
            for id in socket_client:
                self.clientes_conectados[id].sendall(mensaje_codificado)
        except ConnectionError:
            socket_client.close()
    
    def codificar_mensaje(self, mensaje):
        json_mensaje = json.dumps(mensaje)
        bytes_mensaje = json_mensaje.encode("UTF-8")
        largo_mensaje = len(bytes_mensaje).to_bytes(4, byteorder="little")
        contador = 0
        array_mensaje = bytearray()
        for i in range(0, len(bytes_mensaje), 80):
            numero_bloque = contador.to_bytes(4, byteorder="big")
            contador += 1
            if i + 80 > len(bytes_mensaje):
                bytes_nuevos = bytearray(bytes_mensaje[i:])
                while len(bytes_nuevos) < 80:
                    bytes_nuevos += b'\x00'
            else:
                bytes_nuevos = bytearray(bytes_mensaje[i: i + 80])
            array_mensaje += numero_bloque + bytes_nuevos
        return (bytearray(largo_mensaje + array_mensaje))

    def log(self, mensaje_consola):
            print(mensaje_consola)
    
    def eliminar_cliente(self, id):
        with self.lock_clientes:
            self.log(f"Borrando socket del cliente {id}.")
            socket_client = self.clientes_conectados[id]
            socket_client.close()
            del self.clientes_conectados[id]
            self.logica.eliminar_cliente(id)

    def cierre_servidor(self):
        self.log("Realizando el cierre del servidor...")
        for id in self.clientes_conectados.keys():
            self.eliminar_cliente(id)
        self.socket_servidor.close()