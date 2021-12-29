# Debes completar esta función para que retorne la información de los ayudantes
def cargar_datos(path):
    archivo = open(path, "r")
    medio = archivo.readlines()
    archivo.close()

    lista = []
    for k in medio:
        lin = k.strip("\n")
        linea = lin.split(",")
        lista.append(linea)
    return lista


# Completa esta función para encontrar la información del ayudante entregado
def buscar_info_ayudante(nombre_ayudante, lista_ayudantes):
  info = False
  for k in lista_ayudantes:
    if nombre_ayudante.upper() in k[0].upper():
      info = True
      return k
  if info == False :
    return None  


# Completa esta función para que los ayudnates puedan saludar
def saludar_ayudante(info_ayudante):
  lista = info_ayudante
  frase = "Bienvenido "+lista[0]+", tu rol como ayudante es"+lista[1]+". Confirmemos que los siguientes datos esten correcto: Github -> "+lista[2]+", Discord -> "+lista[3]
  return frase


if __name__ == '__main__':
    pass
    # El código que aquí escribas se ejecutará solo al llamar a este módulo.
    # Aquí puedes probar tu código llamando a las funciones definidas.

    # Puede llamar a cargar_datos con el path del archivo 'ayudantes.csv'
    # para probar si obtiene bien los datos.

    # Puedes intentar buscar la lista de unos de los nombres
    # que se encuentran en el archivo con la función buscar_info_ayudante.
    # Además puedes utilizar la lista obtenida para generar su saludo.

    # Hint: la función print puede se útil para revisar
    #       lo que se está retornando.


informacion=cargar_datos("/Users/antoniablanco/Desktop/Progra Avanzada/antoniablanco-iic2233-2021-2/Actividades/AP0/ayudantes.csv")
