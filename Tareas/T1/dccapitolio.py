from lectura_archivos import cargar_ambientes, cargar_arenas
from lectura_archivos import cargar_objetos, cargar_tributos
from random import randint


class DCCapitolio:

    def __init__(self):
        print("")
        print("Cargando DCCapitolio...")
        print("")
        # Falta dar contexto del juego
        self.lista_tributos = cargar_tributos()
        self.lista_ambientes = cargar_ambientes()
        self.lista_objetos = cargar_objetos()
        self.lista_arenas = cargar_arenas()
        self.tributo_seleccionado = ""
        self.arena_seleccionada = ""
    
    def run(self):
        self.menu_inicio()

    def menu_inicio(self):
        print("")
        self.__acciones_menu_inicio()
        opcion = input("Indique numericamente la opcion: ")
        if opcion == "1":
            self.elegir_tributo()
        elif opcion == "2":
            print("Esta partida se ha cerrado, pero siempre se puede volver a intentar")
        else:
            print("Esa no es una opcion valida ")
            self.menu_inicio()
    
    def menu_principal(self):
        self.lista_tributos = cargar_tributos()
        seguir = True
        while seguir:
            print("")
            self.__acciones_menu_prinicipal()
            opcion = input("Indique numericamente la opcion: ")

            if opcion == "1":

                seguir = self.simulacion_hora()
                vivos = []
                tributos = self.arena_seleccionada.tributos
                for tributo in range(len(tributos)):
                    if tributos[tributo].esta_vivo:
                        vivos.append(tributos[tributo])

                if self.tributo_seleccionado.vida == 0:
                    seguir = False
                    print("No has logrado sobrevivir, y te han matado")
                    if len(vivos) > 0 :
                        numero = randint(0, len(vivos)-1)
                        ganador = vivos[numero]
                        print(f'El ganador del DCCapitolio fue {ganador.nombre} del distrito {ganador.distrito}')
                    else:
                        print("Fue una batalla sangrienta donde todos los tributos murieron")
                        print("No hubo ganador")
                    print("Vuelve a jugar y practica para ganar")
                    self.menu_inicio()

                if len(vivos) == 0:
                    print("Eres el último sobreviviente has ganado DCCapitolio")
                    print(f"Con el premio podras ayudar a tu distrito")
                    print("Vuelve a jugar en otro nivel")
                    seguir = False
                    self.menu_inicio()

            elif opcion == "2":
                self.estado_tributo()

            elif opcion == "3":
                self.tributo_seleccionado.utilizar_objeto(self.arena_seleccionada)

            elif opcion == "4":
                self.resumen_dccapitolio()

            elif opcion == "5":
                print("Al volver atras la partida se reinicia")
                seguir = False
                self.menu_inicio()

            elif opcion == "6":
                seguir = False
                print("Esta partida se ha cerrado, pero siempre se puede volver a intentar")
                #break
            else:
                print("Esa no es una opcion valida ")

    def simulacion_hora(self):
        self.__acciones_simular_hora()
        opcion = input("Seleccione numericamente una de las opciones: ")
        self.arena_seleccionada.muertos = []
        self.arena_seleccionada.informacion_hora = ""

        seguir = True
        logrado = True
        salir = False
        if opcion == "1":
            logrado = self.tributo_seleccionado.accion_heroica(self.arena_seleccionada)
        elif opcion == "2":
            logrado = self.atacar_tributo(self.arena_seleccionada)
        elif opcion == "3":
            logrado = self.tributo_seleccionado.pedir_objeto(self.lista_objetos,
                                                             self.arena_seleccionada)
        elif opcion == "4":
            self.tributo_seleccionado.hacerse_bolita(self.arena_seleccionada)
        elif opcion == "5":
            self.menu_principal()
        elif opcion == "6":
            seguir = False
            salir = True
            print("Esta partida se ha cerrado, pero siempre se puede volver a intentar")
        else:
            print("No es una opcion valida, vuelve a intentarlo")
            logrado = False

        if not logrado:
            self.simulacion_hora()
        elif not salir:
            print("")
            print("Se acerca el fin de la hora...")
            self.arena_seleccionada.eventos_fin_hora()

        return seguir
    
    def elegir_tributo(self):
        print("")
        print("Es hora de escoger a su tributo")
        print("")
        for numero in range(len(self.lista_tributos)):
            tributo = self.lista_tributos[numero]
            print(f'[{numero}]. {tributo.nombre} representa al distrito {tributo.distrito}')
        print(f'[{numero+1}]. Volver')
        print(f'[{numero+2}]. Salir')

        jugador = input("Seleccione numericamente: ")
        if jugador.isnumeric():
            jugador = int(jugador)
            if jugador < (len(self.lista_tributos)) and jugador >= 0:
                self.tributo_seleccionado = self.lista_tributos[jugador]
                self.tributo_seleccionado.mochila = []
                self.tributo_seleccionado.peso = 0
                self.elegir_arena()
            elif jugador == len(self.lista_tributos):
                self.menu_inicio()
            elif jugador == len(self.lista_tributos) + 1:
                print("Esta partida se ha cerrado, pero siempre se puede volver a intentar")
            else:
                print("Esa no es una opción valida, vuelva a intentarlo")
                self.elegir_tributo()
        else:
            print("Esa no es una opción valida, vuelva a intentarlo")
            self.elegir_tributo()

    def elegir_arena(self):
        print("")
        print("El último paso antes de iniciar es escoger la arena en la que competiras")
        for numero in range(len(self.lista_arenas)):
            arena = self.lista_arenas[numero]
            print(f'[{numero}]. {arena.nombre} nivel {arena.dificultad}')
        print(f'[{numero+1}]. Volver')
        print(f'[{numero+2}]. Salir')

        numero_arena = input("Seleccione numericamente: ")
        if numero_arena.isnumeric():
            numero_arena = int(numero_arena)
            if numero_arena < (len(self.lista_arenas)) and numero_arena >= 0 :
                seleccionado = self.lista_arenas[numero_arena]
                self.arena_seleccionada = seleccionado
                seleccionado.entregar_jugador(self.tributo_seleccionado, self.lista_tributos)
                seleccionado.entregar_ambientes(self.lista_ambientes)
                self.menu_principal()
            elif numero_arena == len(self.lista_arenas):
                self.elegir_tributo()
            elif numero_arena == len(self.lista_arenas) + 1:
                print("Esta partida se ha cerrado, pero siempre se puede volver a intentar")
            else:
                print("Esa no es una opción valida, vuelva a intentarlo")
                self.elegir_arena()
        else:
            print("Esa no es una opción valida, vuelva a intentarlo")
            self.elegir_arena()

    def atacar_tributo(self, arena):
        print("")
        print("Elige a que tributo quieres atacar: ")
        logrado = False
        tributos = self.arena_seleccionada.tributos
        vivos = []
        for tributo in range(len(tributos)):
            if tributos[tributo].esta_vivo and tributos[tributo].nombre != self.tributo_seleccionado.nombre:
                vivos.append(tributos[tributo])
                print(f"[{len(vivos)}] {tributos[tributo].nombre}")
        print(f'[{len(vivos)+1}] Volver')
        opcion = input("Seleccione numericamente: ")
        if opcion.isnumeric():
            opcion = int(opcion)-1
            if opcion < len(vivos) and opcion >= 0:
                logrado = self.tributo_seleccionado.atacar(vivos[opcion], arena)
            elif opcion == len(vivos):
                self.simulacion_hora()
            else:
                print("Esa no es una opción valida, vuelva a intentarlo")
                self.atacar_tributo()
        else:
            print("Esa no es una opción valida, vuelva a intentarlo")
            self.atacar_tributo()
        return logrado

    def resumen_dccapitolio(self):
        print("")
        print("                 *** Estado DCCapitolio ***")
        print("--------------------------------------------------------------")
        print(f"Dificultad : {self.arena_seleccionada.dificultad}")
        print("Tributos vivos:") 
        tributos = self.arena_seleccionada.tributos
        for tributo in range(len(tributos)):
            if tributos[tributo].esta_vivo:
                print(f"     {tributos[tributo].nombre}: {tributos[tributo].vida}")
        numero = self.arena_seleccionada.ambiente_turno
        print(f"Proximo ambiente: {self.arena_seleccionada.ambientes[numero].nombre}") 

    def estado_tributo(self):
        tributo = self.tributo_seleccionado
        print("")
        print("                        Estado tributo                         ")
        print("---------------------------------------------------------------")
        print(f'Nombre: {tributo.nombre}')
        print(f'Distrito: {tributo.distrito}')
        print(f'Edad: {tributo.edad}')
        print(f'Vida: {tributo.vida}')
        print(f'Energía: {tributo.energia}')
        print(f'Agilidad: {tributo.agilidad}')
        print(f'Fuerza: {tributo.fuerza}')
        print(f'Ingenio: {tributo.ingenio}')
        print(f'Popularidad: {tributo.popularidad}')
        objetos = ""
        ctd = 0
        for objeto in tributo.mochila:
            if ctd == 0:
                objetos = objeto.nombre
            else:
                objetos = objetos + ", " + objeto.nombre
            ctd += 1
        print(f'Objetos: {objetos}')
        print(f'Peso: {tributo.peso}')

    @staticmethod
    def __acciones_menu_prinicipal():
        print("      *** Menú Principal ***\n"
              "----------------------------------\n"
              "[1] Simulación hora\n"
              "[2] Mostrar estado del tributo\n"
              "[3] Utilizar objeto\n"
              "[4] Resumen DCCapitolio\n"
              "[5] Volver\n"
              "[6] Salir")
    
    @staticmethod
    def __acciones_menu_inicio():
        print("    *** Menú Principal ****\n"
              "--------------------------------\n"
              "[1] Iniciar partida\n"
              "[2] Salir")
    
    @staticmethod
    def __acciones_simular_hora():
        print("")
        print("    *** Simular hora ****\n"
              "--------------------------------\n"
              "[1] Acción heroica\n"
              "[2] Atacar tributo\n"
              "[3] Pedir objeto a patrocinadores\n"
              "[4] Hacerse bolita\n"
              "[5] Volver\n"
              "[6] Salir") 
