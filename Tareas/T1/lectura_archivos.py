from parametros import RUTA_TRIBUTOS, RUTA_ARENAS, RUTA_OBJETOS, RUTA_AMBIENTES
from tributo import Tributo
from ambiente import Bosque, Playa, Montana
from arena import Arena
from objeto import Consumible, Arma, Especial


def cargar_tributos():
    lista_tributos = []
    with open(RUTA_TRIBUTOS, "r", encoding="utf-8") as archivo:
        archivo = archivo.readlines()
        for linea in archivo[1:]:
            nombre, distrito, edad, vida, energia, agilidad, \
                fuerza, ingenio, popularidad = linea.strip().split(",")
            distrito = str(distrito)
            edad = int(edad)
            vida = int(vida)
            energia = int(energia)
            agilidad = int(agilidad)
            fuerza = int(fuerza)
            ingenio = int(ingenio)
            popularidad = int(popularidad)

            lista_tributos.append(Tributo(nombre, distrito, edad, vida, energia,
                                          agilidad, fuerza, ingenio, popularidad))
    return lista_tributos


def cargar_arenas():
    lista_arenas = []
    with open(RUTA_ARENAS, "r", encoding="utf-8") as archivo:
        archivo = archivo.readlines()
        for arena in archivo[1:]:
            nombre, dificultad, riesgo = arena.strip().split(",")
            dificultad = str(dificultad)
            riesgo = float(riesgo)
            lista_arenas.append(Arena(nombre, dificultad, riesgo))

    return lista_arenas


def cargar_objetos():
    lista_objetos = []

    with open(RUTA_OBJETOS, "r", encoding="utf-8") as archivo:
        archivo = archivo.readlines()
        for objeto in archivo[1:]:
            nombre, tipo, peso = objeto.strip().split(",")
            tipo = str(tipo)
            peso = int(peso)
            if tipo == "consumible":
                lista_objetos.append(Consumible(nombre, tipo, int(peso)))

            elif tipo == "arma":
                lista_objetos.append(Arma(nombre, tipo, int(peso)))

            elif tipo == "especial":
                lista_objetos.append(Especial(nombre, tipo, int(peso)))

    return lista_objetos


def cargar_ambientes():
    lista_ambientes = []
    with open(RUTA_AMBIENTES, "r", encoding="utf-8") as archivo:
        archivo = archivo.readlines()
        for ambiente in archivo[1:]:
            nombre, evento_1, evento_2, evento_3 = ambiente.strip().split(",")
            evento_1 = evento_1.split(";")
            evento_2 = evento_2.split(";")
            evento_3 = evento_3.split(";")
            eventos = [evento_1, evento_2, evento_3]
            if nombre == "bosque":
                lista_ambientes.append(Bosque(nombre, eventos))

            elif nombre == "playa":
                lista_ambientes.append(Playa(nombre, eventos))
                
            elif nombre == "montaña":
                lista_ambientes.append(Montana(nombre, eventos))
    return lista_ambientes