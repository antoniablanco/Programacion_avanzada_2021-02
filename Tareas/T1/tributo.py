import parametros as p
from random import randint 


class Tributo:

    def __init__(self, nombre, distrito, edad, vida, energia,
                 agilidad, fuerza, ingenio, popularidad):
        self.nombre = nombre
        self.distrito = distrito
        self.agilidad = agilidad
        self.fuerza = fuerza
        self.ingenio = ingenio
        self.popularidad = popularidad
        self.esta_vivo = True
        self.mochila = []
        self.peso = 0
        self.edad = edad
        self._vida = vida
        self._energia = energia

    @property
    def vida(self):
        return self._vida
        
    @vida.setter
    def vida(self, p):
        if p > 100:
            self._vida = 100
        elif p < 0:
            self._vida = 0
        else:
            self._vida = p

    @property
    def energia(self):
        return self._energia
    
    @energia.setter
    def energia(self, p):
        if p > 100:
            self._energia = 100
        elif p < 0:
            self._energia = 0
        else:
            self._energia = p

    def atacar(self, tributo, arena):
        logrado = True
        if self.energia >= p.ENERGIA_ATACAR:
            self.energia -= p.ENERGIA_ATACAR
            arena.informacion_hora += "En la simluacion de hora se selecciono"
            arena.informacion_hora += " la opcion atacar tributo\n"
            print(f'{self.nombre} esta atacando a {tributo.nombre}')
            ponderacion = 60 * self.fuerza + 40 * self.agilidad + 40 * self.ingenio - 30 * self.peso
            dano = int(min(90, max(5, (ponderacion)/self.edad)))
            tributo.vida -= dano
            if tributo.vida <= 0: 
                print(f"Ha peleado con valentia y ha ganado")
                print(f"{tributo.nombre} del distrito {tributo.distrito} ha muerto")
                tributo.esta_vivo = False
                self.popularidad += p.POPULARIDAD_ATACAR
                arena.muertos.append(tributo)

                arena.informacion_hora += (self.nombre + " mato a " + tributo.nombre + "\n")
                arena.informacion_hora += ("ganando " + str(p.POPULARIDAD_ATACAR) +
                                            " de popularidad\n")
            else:
                print(f'{tributo.nombre} ha sufrido {dano} de daño')
                print(f"Le queda {tributo.vida} de vida")
                arena.informacion_hora += (self.nombre + " realizo " + str(dano) +
                                           " de daño a " + tributo.nombre + "\n") 
        else:
            logrado = False
            print("No tienes suficiente energia para atacar a otro tributo")

        return logrado
    
    def utilizar_objeto(self, arena):
        #Revisar
        print("")
        print("Has accedido a tu mochila")
        if len(self.mochila) > 0:
            print("Estos objetos posees")

            for objeto in range(len(self.mochila)):
                print(f'[{objeto}]. {self.mochila[objeto].nombre}')
                
            print(f"[{len(self.mochila)}]. Volver")
            numero_objeto = input("Número del objeto que quiere utilizar: ")
            if numero_objeto.isnumeric():
                if int(numero_objeto) >= 0 and int(numero_objeto) < len(self.mochila):
                    objeto = self.mochila.pop(int(numero_objeto))
                    objeto.entregar_beneficio(self, arena)
                elif int(numero_objeto) == len(self.mochila):
                    pass
                else:
                    self.utilizar_objeto()
                    print("Esa no es una opción valida")

            else:
                self.utilizar_objeto()
                print("Esa no es una opcion valida")

        else:
            print("No posees objetos")

    def pedir_objeto(self, lista_objetos, arena):
        logrado = False
        print("")
        if self.popularidad >= p .COSTO_OBJETO:
            arena.informacion_hora += "En la simluacion de hora se selecciono"
            arena.informacion_hora += " la opcion pedir objeto\n"
            logrado = True
            self.popularidad -= p.COSTO_OBJETO
            numero = randint(0, len(lista_objetos)-1)
            objeto = lista_objetos[numero]
            self.mochila.append(objeto)
            self.peso += objeto.peso

            print('Los patrocinadores te aman, y te han mandado un objeto')
            print(f'Has obtenido {objeto.nombre} de tipo {objeto.tipo}')
            print(f"Tristemente no todo es perfecto y te costo {p.COSTO_OBJETO} a tu popularidad")

            arena.informacion_hora += ("Adquiriendo el objeto " + objeto.nombre +
                                       " a un costo de " + str(p.COSTO_OBJETO) + "\n")
        
        else:
            print("No eres lo suficientemente popular para pedir un objeto")

        return logrado

    def accion_heroica(self, arena):
        print("")
        logrado = False
        if self.energia >= p.ENERGIA_ACCION_HEROICA:
            arena.informacion_hora +=  "En la simluacion de hora se selecciono la opcion accion heroica\n"
            logrado = True
            self.popularidad += p.POPULARIDAD_ACCION_HEROICA
            self.energia -= p.ENERGIA_ACCION_HEROICA
            print(f'Has realizado una accion heroica...')
            print(f'Ahora tienes una popularidad de {self.popularidad} ')
            print(f'Pero has gastado {p.ENERGIA_ACCION_HEROICA} puntos de energia para lograrlo')

            arena.informacion_hora += "Ganando " + str(p.POPULARIDAD_ACCION_HEROICA) + "\n"
        else:
            print("No tienes suficiente energia para realizar una accion heroica")

        return logrado

    def hacerse_bolita(self, arena):
        arena.informacion_hora +=  "En la simluacion de hora se selecciono la opcion accion heroica\n"
        arena.informacion_hora +=  "Ganando " + str(p.ENERGIA_BOLITA) + " de energia\n"

        print("")
        print("Para recuperar energia decides hacerte bolita y descansar")
        print("Pasan los minutos...")
        self.energia += p.ENERGIA_BOLITA
        print(f"Tu energía ahora es {self.energia}")

    def atacar_encuentros(self, tributo):
        vivo = True
        print("")
        print("Los tributos comienzan a pelear entre ellos")
        print(f'{self.nombre} esta atacando a {tributo.nombre}')
        ponderacion = 60 * self.fuerza + 40 * self.agilidad + 40 * self.ingenio - 30 * self.peso
        dano = int(min(90, max(5, (ponderacion)/self.edad)))
        tributo.vida -= dano
        print(f"Tras el duro enfrentamiento {self.nombre} ha ganado")
        if tributo.vida <= 0:
            tributo.vida = 0
            print(f"{tributo.nombre} del distrito {tributo.distrito} ha muerto")
            tributo.esta_vivo = False
            vivo = False
    
        else:
            print(f'{tributo.nombre} ha sufrido {dano} de daño')
            print(f"Le queda {tributo.vida} de vida")

        return vivo