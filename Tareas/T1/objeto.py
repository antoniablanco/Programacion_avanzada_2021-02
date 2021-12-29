import parametros as p
from abc import ABC, abstractmethod


class Objeto(ABC):

    def __init__(self, nombre, tipo, peso):
        self.nombre = nombre
        self.tipo = tipo
        self.peso = peso
    
    @abstractmethod
    def entregar_beneficio(self, tributo, arena):
        pass

    
class Consumible(Objeto):

    def entregar_beneficio(self, tributo, arena):
        tributo.energia += p.AUMENTAR_ENERGIA
        print(f"Tu energia ha aumentado, ahora posees: {tributo.energia}")


class Arma(Objeto):

    def entregar_beneficio(self, tributo, arena):
        aumento_fuerza = int(tributo.fuerza * (p.PONDERADOR_AUMENTAR_FUERZA * arena.riesgo + 1))
        tributo.fuerza += aumento_fuerza
        print(f"Tu fuerza ha aumentado, ahora posees: {tributo.fuerza}")


class Especial(Objeto):

    def entregar_beneficio(self, tributo, arena):
        aumento_fuerza = int(tributo.fuerza * (p.PONDERADOR_AUMENTAR_FUERZA * arena.riesgo + 1))
        tributo.fuerza += aumento_fuerza
        tributo.energia += p.AUMENTAR_ENERGIA
        tributo.agilidad += p.AUMENTAR_AGILIDAD
        tributo.ingenio += p.AUMENTAR_INGENIO
        print(f"Tu energia ha aumentado, ahora posees: {tributo.energia}")
        print(f"Tu fuerza ha aumentado, ahora posees: {tributo.fuerza}")
        print(f"Tu agilidad ha aumentado, ahora posees: {tributo.agilidad}")
        print(f"Tu ingenio ha aumentado, ahora posees: {tributo.ingenio}")