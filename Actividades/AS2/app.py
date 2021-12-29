from random import randint
from time import sleep
from pedido import Pedido
from shopper import Shopper
from threading import Thread


class DCComidApp(Thread):

    def __init__(self, shoppers, tiendas, pedidos):
        # NO MODIFICAR
        super().__init__()
        self.shoppers = shoppers
        self.pedidos = pedidos
        self.tiendas = tiendas

    def obtener_shopper(self):
        # Completar
        libre = False
        for shop in range(len(self.shoppers)):
            if self.shoppers[shop].pedido_actual is None:
                libre = True
                print(f"Su shopper sera: {self.shoppers[shop].nombre}")
                return self.shoppers[shop]
        if libre is False:
            print("En este minuto no hay shoppers disponibles")
            Shopper.evento_disponible.wait()
            print("Se ha encontrado un shopper disponible")
            Shopper.evento_disponible.clear()
            self.obtener_shopper()

    def run(self):
        # Completar
        while self.pedidos:
            pedido = self.pedidos.pop(0)
            for k in self.tiendas.keys():
                if pedido[1] == k:
                    nuevo_pedido = Pedido(pedido[0], pedido[1], pedido[2])
                    shopper = self.obtener_shopper()
                    shopper.asignar_pedido(nuevo_pedido)
                    self.tiendas[k].ingresar_pedido(nuevo_pedido, shopper)
                    sleep(randint(1, 5))


if __name__ == '__main__':
    pass
