from mascota import Perro, Gato, Conejo


def cargar_mascotas(archivo_mascotas):
    with open(archivo_mascotas, "r", encoding="utf-8") as archivo:
        lineas = archivo.readlines()

    lista_mascotas = []
    for k in lineas[1:]:
        (nombre, especie, raza, dueno, saciedad, entretencion) = k.split(",")
 
        if especie == "perro":
            mascota = Perro(nombre, raza, dueno, int(saciedad), int(entretencion))
        
        elif especie == "gato":
            mascota = Gato(nombre, raza, dueno, int(saciedad), int(entretencion))

        elif especie == "conejo":
            mascota = Conejo(nombre, raza, dueno, int(saciedad), int(entretencion))

        else:
            print("No es una especie permitida")

        lista_mascotas.append(mascota)

    return lista_mascotas
