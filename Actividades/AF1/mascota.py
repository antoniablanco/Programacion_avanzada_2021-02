import random
import parametros as p


class Mascota:
    def __init__(self, nombre, raza, dueno,
                 saciedad, entretencion):
        self.nombre = nombre
        self.raza = raza
        self.dueno = dueno
        
        # Los siguientes valores están en %.
        self._saciedad = saciedad
        self._entretencion = entretencion

    @property
    def saciedad(self):
        return self._saciedad
    
    @saciedad.setter
    def saciedad(self, nuevo_valor):
        if 0 < nuevo_valor < 100:
            self._saciedad = nuevo_valor
        elif nuevo_valor >= 100:
            self._saciedad = 100
        else:
            self._saciedad = 0

    @property
    def entretencion(self):
        return self._entretencion
    
    @entretencion.setter
    def entretencion(self, nuevo_valor):
        if 0 < nuevo_valor < 100:
            self._entretncion = nuevo_valor
        elif nuevo_valor >= 100:
            self._entretencion = 100
        else:
            self._entretencion = 0
    
    @property
    def satisfaccion(self):
        return (self.saciedad//2 + self.entretencion//2)
    
    def comer(self, comida):
        valor_random = random.random()
        valor_comida = comida.probabilidad_vencer
        if valor_random <= valor_comida:
            print(f"La comida estaba vencida! A {self.nombre} le duele la pancita :(")
            self.saciedad-=comida.calorias
        else:
            print(f"{self.nombre} está comiendo {comida.nombre}, que rico!")
            self.saciedad+=comida.calorias

    def pasear(self):
        self.entretencion += p.ENTRETENCION_PASEAR
        self.saciedad += p.SACIEDAD_PASEAR
    
    def __str__(self):
        print(f'Nombre: {self.nombre}')
        print(f'Saciedad: {self._saciedad}')
        print(f'Entretencion: {self._entretencion}')
        linea = f'Satisfaccion: {self.satisfaccion}'
        return linea


class Perro(Mascota):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.especie = "PERRO"
    
    def saludar(self):
        print("guau guau")
        

class Gato(Mascota):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.especie = "Gato"

    def saludar(self):
        print("miau miau")

    
class Conejo(Mascota):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.especie = "Conejo"

    def saludar(self):
        print("chillido")