import json
import socket
import threading
from os.path import join

import parametros as p
from manejo_archivos import (
    leer_unidad, guardar_archivo, almacenamiento_utilizado, iniciar_sistema,
)


class Servidor:
    _id_cliente = 1

    def __init__(self, host, port):
        print("Inicializando servidor...")

        self.host = host
        self.port = port
        self.socket_servidor = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

        # Clientes actualmente conectados al servidor
        self.clientes_conectados = {}
        iniciar_sistema()
        self.lock_archivos = threading.Lock()

        self.unir_y_escuchar()

    def unir_y_escuchar(self):
        # Completar
        self.socket_servidor.bind((self.host, self.port))
        self.socket_servidor.listen()
        print(f"Este es el host: {self.host} y se esta escuchando desde el puerto {self.port}")
        self.aceptar_conexiones()

    def aceptar_conexiones(self):
        # Completar
        thread = threading.Thread(target=self.thread_aceptar_conexiones)
        thread.start()

    def thread_aceptar_conexiones(self):
        # Completar
        while True:
            try:
                client_socket, _ = self.socket_servidor.accept()
                self.clientes_conectados[self._id_cliente] = client_socket
                thread_escuchando_cliente = threading.Thread(target=self.thread_escuchar_cliente,
                    args=(client_socket, self._id_cliente), daemon=False)
                thread_escuchando_cliente.start()
                self._id_cliente += 1

            except ConnectionError as error:
                print("La conexion fallo")
                thread_escuchando_cliente.close()
        
    def thread_escuchar_cliente(self, socket_cliente, id_cliente):
        # Completar
        try:
            while True:
                recibido = self.recibir_mensaje(socket_cliente)

                if recibido != {}:
                    procesado = self.manejar_comando(recibido, socket_cliente)
                    if procesado != "":
                        self.enviar(procesado, socket_cliente)
                    else:
                        print("Error de conexion")
                        self.clientes_conectados[id_cliente].close()
                else:
                    print("Error de conexion, mensaje vacio")
                    self.clientes_conectados[id_cliente].close()
        except ConnectionResetError:
            print('Error de conexión con el cliente')
            self.clientes_conectados[id_cliente].close()

    def recibir_mensaje(self, socket_cliente):
        # Completar
        print("Se recibio el mensaje")
        largo_respuesta = socket_cliente.recv(4)
        response_length = int.from_bytes(largo_respuesta, byteorder='big')
        response = bytearray()

        while len(response) < response_length:
            read_length = min(4096, response_length - len(response))
            response.extend(socket_cliente.recv(read_length))

        print("codificado:", response)
        decodificado = self.decodificar_mensaje(response)
        print("El mensaje decodificado es:", decodificado)

        return decodificado

    def enviar(self, mensaje, sock_cliente):
        # Completar
        string = str(mensaje)
        codificado = self.codificar_mensaje(string)
        largo = len(codificado).to_bytes(4, byteorder='big')
        sock_cliente.send(largo + codificado)

    def manejar_comando(self, recibido, socket_cliente):
        comando = recibido["comando"]
        print("Comando recibido:", comando)
        respuesta = {}

        if comando == "explorar":
            respuesta["comando"] = "explorar"
            respuesta["argumentos"] = {"contenido": leer_unidad()}

        elif comando == "explorar_descargar":
            respuesta["comando"] = "explorar_descargar"
            respuesta["argumentos"] = {"contenido": leer_unidad()}

        elif comando == "almacenamiento":
            data_unidad = leer_unidad()
            uso = almacenamiento_utilizado(data_unidad)
            respuesta["comando"] = "almacenamiento"
            respuesta["argumentos"] = {"contenido": uso}

        elif comando == "subir":
            bytes_archivo = recibido["argumentos"]["contenido"]
            archivo = bytes.fromhex(bytes_archivo)
            tipo = recibido["argumentos"]["tipo"]
            nombre = recibido["argumentos"]["nombre"]
            with self.lock_archivos:
                exito = guardar_archivo(archivo, tipo, nombre)
            if exito:
                respuesta["comando"] = "exito"
            else:
                respuesta["comando"] = "error"
                respuesta["argumentos"] = {"mensaje": "El archivo ya existe"}

        elif comando == "descargar":
            tipo = recibido["argumentos"]["tipo"]
            nombre = recibido["argumentos"]["nombre"]
            ruta = join(p.RUTA_DATOS[tipo], nombre)
            msg = {
                "comando": "archivo",
                "argumentos": {
                    "ruta": ruta
                }
            }
            self.enviar(msg, socket_cliente)
            self.enviar_archivo(socket_cliente, ruta)
        return respuesta

    def enviar_archivo(self, socket_cliente, ruta):
        """
        Recibe una ruta a un archivo a enviar y los separa en chunks de 8 kb
        """
        with open(ruta, 'rb') as archivo:
            chunk = archivo.read(8000)
            largo = len(chunk)
            while largo > 0:
                chunk = chunk.ljust(8000, b'\0')    # Padding
                msg = {
                    "comando": "chunk",
                    "argumentos": {
                        "largo": largo,
                        "contenido": chunk.hex()
                    }
                }
                self.enviar(msg, socket_cliente)
                chunk = archivo.read(8000)
                largo = len(chunk)

    @staticmethod
    def codificar_mensaje(mensaje):
        try:
            mensaje_json = json.dumps(mensaje)
            mensaje_bytes = mensaje_json.encode()
            return mensaje_bytes
        except json.JSONDecodeError:
            print('No se pudo codificar el mensaje.')

    @staticmethod
    def decodificar_mensaje(msg_bytes):
        try:
            mensaje = json.loads(msg_bytes)
            return mensaje
        except json.JSONDecodeError:
            print('No se pudo decodificar el mensaje.')
            return dict()
