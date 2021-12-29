from random import randint, choice
from comida import Comida
import parametros as p


class Hotel:

    def __init__(self):
        self.__energia = 100
        self.__dias = 0
        self.max_energia = p.MAXIMO_ENERGIA_HOTEL
        self.mascotas = list()
        self.funcionando = True
        self.comidas = [
        Comida('Carne con legumbres', 18, 0.3),
        Comida('Pescado con Castañas', 22, 0.2),
        Comida('Pollo y Arroz', 20, 0.1)
        ]

    @property
    def energia(self):
        return self.__energia
    
    @energia.setter
    def energia(self, nuevo_valor):
        if 0 < nuevo_valor < self.max_energia:
            self.__energia = nuevo_valor
        elif nuevo_valor >= self.max_energia:
            self.__energia = self.max_energia
        else:
            self.__energia = 0

    @property
    def dias(self):
        return self.__dias
    
    @dias.setter
    def dias(self, mas):
        self.__dias += mas

    def hotel_en_buen_estado(self):
        """
        Esta función verifica las condiciones de término
        del programa. Si se pierden más de dos mascotas
        en un mismo día o el Hotel se queda con menos de
        tres mascotas, el programa termina.
        """
        mascotas_perdidas = 0
        for mascota in self.mascotas:
            if mascota.satisfaccion < p.MASCOTA_SATISFACCION_MINIMO:
                self.despedir_mascota(mascota)
                mascotas_perdidas += 1
        if mascotas_perdidas > 2 or len(self.mascotas) < 3:
            return False

        return True

    def imprimir_estado(self):
        print(f'Dias: {self.__dias}')
        print(f'Energía cuidador: {self.__energia}')
        print(f'Mascotas hospedadas: {len(self.mascotas)}')

    def recibir_mascota(self, mascotas):
        self.mascotas += (mascotas)
        for mascota in mascotas:
            mascota.saludar()
            print(f"""
            Ha aparecido un {mascota.especie} en la recepción,
            su nombre es {mascota.nombre}. {mascota.dueno}, su dueño
            te pide que lo cuides hasta que regrese.
            """)

    def despedir_mascota(self, mascota):
        self.mascotas.remove(mascota)

        print(f"""
        Oh no!
        {mascota.dueno}, el dueño de {mascota.nombre} se lo ha llevado.
        Huéspedes en el Hotel: {len(self.mascotas)}
        """)

    def imprimir_mascotas(self):
        for mascota in self.mascotas:
            print(mascota)

    def nuevo_dia(self):
        if self.hotel_en_buen_estado:
            print("A comenzado un nuevo día")
            self.__dias += 1
            self.__energia = self.max_energia
            for mascota in self.mascotas:
                mascota._entretencion -= randint(7,21)
                mascota._saciedad -= randint(8,14)
        
        else:
            self.funcionando = False
            print("Oh no, has perdido!!!")
            print(f'Dias activos: {self.dias}')

    def revisar_energia(self):
        if self.energia >= min(p.COSTO_ENERGIA_ALIMENTAR, 
                               p.COSTO_ENERGIA_PASEAR):
            return True
        return False

    def pasear_mascota(self, mascota):
        self.energia -= p.COSTO_ENERGIA_PASEAR
        mascota.pasear()
        print(f'{mascota.nombre} salió a pasear feliz!')

    def alimentar_mascota(self, mascota):
        mascota.comer(choice(self.comidas))
        print(f'{mascota.nombre} ahora tiene la pancita llena')
        self.__energia -= p.COSTO_ENERGIA_ALIMENTAR
