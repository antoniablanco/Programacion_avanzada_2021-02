import json
import os


def parametro(nombre):
    with open(os.path.join("parametros.json"), "r", encoding="utf-8") as archivo:
        parametros = json.load(archivo)
    return parametros[nombre]


def ruta(nombre):
    ruta_json = parametro(nombre)
    ruta_lista = ruta_json.split(",")
    return os.path.join(*ruta_lista)