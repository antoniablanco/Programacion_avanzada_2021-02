from random import randint
import parametros as p


class Arena:

    def __init__(self, nombre, dificultad, riesgo):
        self.nombre = nombre
        self.riesgo = riesgo
        self.dificultad = dificultad
        self.jugador = ""
        self.tributos = ""
        self.ambientes = ""
        self.muertos = []
        self.informacion_hora = ""
        self.ambiente_turno = 0

    def ejecutar_evento(self, ambiente):
        self.informacion_hora += "No tuviste suerte y en el evento de la arena ocurrio:\n"
        evento = randint(0, 2)
        print(f"")
        dano = ambiente.calcular_dano(evento, self)
        print(f'Todos los tributos han sufrido {dano} de daño')
        self.jugador.vida -= dano
        for tributo in self.tributos:
            if tributo.esta_vivo:
                tributo.vida -= dano
                if tributo.vida == 0:
                    tributo.esta_vivo = False
                    self.muertos.append(tributo)

    def encuentros(self):
        self.informacion_hora += "Los encuentros ocurrido fueron:\n"
        n_encuentros = int(self.riesgo * (len(self.tributos) // 2))
        for batalla in range(n_encuentros):
            seguir = True
            while seguir:
                atacante = randint(0, len(self.tributos)-1)
                if self.tributos[atacante].nombre == self.jugador.nombre:
                    atacante = randint(0, len(self.tributos)-1)
                atacado = randint(0, len(self.tributos)-1)
                if atacante == atacado:
                    atacado = randint(0, len(self.tributos)-1)
                vivo1 = self.tributos[atacante].esta_vivo
                vivo2 = self.tributos[atacado].esta_vivo
                if (atacante != atacado) and vivo1 and vivo2:
                    seguir = False
            atacante = self.tributos[atacante]
            atacado = self.tributos[atacado]
            self.informacion_hora += " " + atacante.nombre + " ataco a " + atacado.nombre + "\n"
            print("Al parecer se acerca una nueva batalla ")
            vivo = atacante.atacar_encuentros(atacado)
            if not vivo:
                self.muertos.append(atacado)
                pass

    def entregar_jugador(self, jugador, tributos):
        self.jugador = jugador
        self.tributos = tributos

    def entregar_ambientes(self, ambientes):
        self.ambientes = ambientes

    def eventos_fin_hora(self):
        print("Las horas pasan y los animos ya estan revueltos")
        
        self.encuentros()
        
        probabilidad = randint(0, 1)
        ocurrio_evento = False
        if probabilidad == p.PROBABILIDAD_EVENTO:
            self.ejecutar_evento(self.ambientes[self.ambiente_turno])
            ocurrio_evento = True
        self.siguiente_ambiente()

        if not ocurrio_evento:
            self.informacion_hora += "Tuviste suerte y el evento de la arena no ocurrio\n"
        
        self.informacion_hora += "Los tributos vivos son:\n"
        for tributo in self.tributos:
            if tributo.esta_vivo:
                self.informacion_hora += "        - " + tributo.nombre + "\n"

        self.informacion_hora += "Los  tributos que murieron en esta hora son:\n"
        for tributo in set(self.muertos):
            self.informacion_hora += "        - " + tributo.nombre + "\n"

        print("")
        print("  *** Resumen simulacion de hora ***")
        print(self.informacion_hora)

    def siguiente_ambiente(self):
        self.ambiente_turno += 1
        if self.ambiente_turno == len(self.ambientes):
            self.ambiente_turno = 0
