from threading import Thread, Event
from time import sleep
from random import randint


class Shopper(Thread):

    evento_disponible = Event()

    def __init__(self, nombre, velocidad):
        # No Modificar
        super().__init__()
        self.posicion = 0
        self.distancia_tienda = 0
        self.distancia_destino = 0
        self.pedido_actual = None
        self.termino_jornada = False
        # COMPLETAR DESDE AQUI
        self.nombre = nombre
        self.velocidad = velocidad

    @property
    def ocupado(self):
        # No Modificar
        if self.pedido_actual:
            return True
        return False

    def asignar_pedido(self, pedido):
        # No Modificar
        print(f"Asignando pedido {pedido.id_} a {self.nombre}...")
        self.distancia_tienda = randint(1, 10)
        self.distancia_destino = self.distancia_tienda +\
            pedido.distancia_destino
        self.pedido_actual = pedido
        self.posicion = 0
        print(f"El pedido {pedido.id_} fue asignado a {self.nombre}")

    def avanzar(self):
        espera = 1/self.velocidad
        sleep(espera)
        self.posicion += 1
        print(f"Soy el Shopper {self.nombre} y estoy en la posicion {self.posicion}")

    def run(self):
        # Completar
        if not self.termino_jornada or self.ocupado:
            if self.ocupado:
                self.avanzar()

            if self.posicion == self.distancia_tienda:
                print("El shopper ha llegado a recoger el pedido")
                self.pedido_actual.evento_llego_repartidor.set()
                self.pedido_actual.evento_pedido_listo.wait()

            if self.posicion == self.distancia_destino:
                print("El shopper ha llegado al destino, y el pedido ha sido entregado")
                self.pedido_actual.entregado = True
                self.evento_disponible.set()
                self.posicion = 0
                self.pedido_actual = None


if __name__ == "__main__":
    pass
