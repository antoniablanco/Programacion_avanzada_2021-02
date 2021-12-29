import socket
import threading
import codificacion as c
import json
from manejo import Manejo


class Client:
    lock_inicio = threading.Lock()
 
    def __init__(self, port, host):
        print("Inicializando cliente...")

        self.host = "localhost"
        self.port = 12341
        self.socket_client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.manejo = Manejo(self)

        try:
            self.connect_to_server()
            self.manejo.mostrar_ventana_inicio()
            self.listen()
            self.repl()
        except ConnectionError:
            print("Conexión terminada")
            self.socket_client.close()
            exit()

    def connect_to_server(self):
        self.socket_client.connect((self.host, self.port))

    def listen(self):
        thread = threading.Thread(target=self.listen_thread, daemon=True)
        thread.start()

    def send(self, msg):
        with self.lock_inicio:
            mensaje_codificado = self.codificar_mensaje(msg)
        try:
            self.socket_client.sendall(mensaje_codificado)
        except ConnectionError:
            self.socket_client.close()

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
                bytes_nuevos = c.encriptacion(bytes_nuevos) 
                while len(bytes_nuevos) < 80:
                    bytes_nuevos += b'\x00'
            else:
                bytes_nuevos = bytearray(bytes_mensaje[i: i + 80])
                bytes_nuevos = c.encriptacion(bytes_nuevos) 
            array_mensaje += numero_bloque + bytes_nuevos
        return (bytearray(largo_mensaje + array_mensaje))
        
    def listen_thread(self):
        try:
            while True:
                mensaje = self.recibir()
                if not mensaje:
                    raise ConnectionResetError
                else:
                    self.manejar_mensaje_recibido(mensaje)
        except ConnectionResetError:
            print("Hay un error de conexion con el servidor")
        finally:
            self.socket_client.close()

    def recibir(self):
        largo = self.socket_client.recv(4)  
        largo_mensaje = int.from_bytes(largo, byteorder="little")
        largo_total = largo_mensaje // (84 - 4)
        if largo_mensaje % (84 - 4) != 0:
            largo_total += 1
        largo_total *= 84
        array_mensaje = bytearray()
        while len(array_mensaje) < largo_total:
            bytes_nuevos = min(84, largo_total - len(array_mensaje))
            array_mensaje += self.socket_client.recv(bytes_nuevos)
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
            array_mensaje += bytes_nuevos
        try:
            mensaje_exacto = array_mensaje.strip(b'\x00')
            mensaje_decodificado = json.loads(mensaje_exacto)
            return mensaje_decodificado
        except json.JSONDecodeError:
            print("No se pudo decodificar el mensaje")
            return dict()
    
    def manejar_mensaje_recibido(self, mensaje):
        print(f'Acción asociada al mensaje: {mensaje}') 
        self.manejo.manejar_mensaje(mensaje)

    def repl(self):
        print("------ Consola ------\n>>> ", end='')
        while True:
            try:
                msg = input()
                print(f'Enviando mensaje: {msg}')
                self.send(msg)

            except KeyboardInterrupt:
                print("Se dio un KeyboardInterrupt, por cierre del socket cliente")
                self.socket_client.close()
                exit()
