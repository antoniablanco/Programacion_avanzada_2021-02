import obtener_parametros as p

class Jugador:

    def __init__(self, nombre, fecha, ruta, identificador):
        self.nombre = nombre
        self.fecha = fecha
        self.imagen = p.ruta(ruta)
        self.canicas = 10
        self.identificador = identificador