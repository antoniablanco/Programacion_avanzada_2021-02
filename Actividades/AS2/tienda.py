from threading import Thread, Lock
from time import sleep
from random import randint


class Tienda(Thread):
    def __init__(self, nombre):
        # NO MODIFICAR
        super().__init__()
        self.nombre = nombre
        self.cola_pedidos = []
        self.abierta = True
        # COMPLETAR DESDE AQUI
        self.lock = Lock()
        self.daemon = True

    def ingresar_pedido(self, pedido, shopper):
        # Completar
        with self.lock:
            tupla = (pedido, shopper)
            self.cola_pedidos.append(tupla)

    def preparar_pedido(self, pedido):
        # Completar
        tiempo = randint(1, 10)
        print(f'El tiempo de espera para el pedido es de {tiempo}')
        sleep(tiempo)
        print(f"El pedido esta listo para ser recogido")

    def run(self):
        # Completar
        if self.abierta:
            if len(self.cola_pedidos) > 0:
                with self.lock:
                    pedido = self.cola_pedidos.pop(0)[0]
                    self.preparar_pedido(pedido)
                    pedido.evento_pedido_listo.set()
                    pedido.evento_llego_repartidor.wait()
                    print("El pedido ha sido retirado por el repartidor")
        else:
            print("Volvemos en {descanso} minutos")
            sleep(randint(1, 5))
