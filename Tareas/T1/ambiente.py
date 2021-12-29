import parametros as p
from abc import ABC, abstractmethod


class Ambiente(ABC):

    def __init__(self, nombre, eventos):
        self.nombre = nombre
        self.eventos = eventos  # Formato [nombre_evento, daño_evento]

    @abstractmethod
    def calcular_dano(self):
        pass


class Playa(Ambiente):

    def calcular_dano(self, n_evento, arena):
        dano_evento = int(self.eventos[n_evento][1])
        dano = max(5, (int(0.4 * p.HUMEDAD_PLAYA +
                       0.2 * p.VELOCIDAD_VIENTOS_PLAYA) + dano_evento)/5)
        print(f'Se acerca un@ {self.eventos[n_evento][0]}')
        print("La hora a pasado y un nuevo evento a ocurrido")
        arena.informacion_hora += (self.eventos[n_evento][0] + " produjo " +  str(dano) +
                                  " de daño a los tributos\n")
        return int(dano)


class Bosque(Ambiente):

    def calcular_dano(self, n_evento, arena):
        dano_evento = int(self.eventos[n_evento][1])
        dano = max(5, (int(0.2 * p.VELOCIDAD_VIENTOS_BOSQUE +
                       0.1 * p.PRECIPITACIONES_BOSQUE) + dano_evento)/5)
        print(f'Se acerca un@ {self.eventos[n_evento][0]}')
        print("La hora a pasado y un nuevo evento a ocurrido")
        arena.informacion_hora += (self.eventos[n_evento][0] + " produjo " +  str(dano) +
                                  " de daño a los tributos\n")
        return int(dano)


class Montana(Ambiente):

    def calcular_dano(self, n_evento, arena):
        dano_evento = int(self.eventos[n_evento][1])
        dano = max(5, (int(0.1 * p.PRECIPITACIONES_MONTANA +
                   0.3 * p.NUBOSIDAD_MONTANA) + dano_evento)/5)
        print(f'Se acerca un@ {self.eventos[n_evento][0]}')
        print("La hora a pasado y un nuevo evento a ocurrido")
        arena.informacion_hora += (self.eventos[n_evento][0] + " produjo " +  str(dano) +
                                  " de daño a los tributos\n")
        return int(dano)