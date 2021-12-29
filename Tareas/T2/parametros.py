### Se guardan los parametros a utilizar en el programa
import os

#  Vidas al inicio de la partida
VIDAS_INICIO = 3

#  Tiempo en segundos entre autos
TIEMPO_AUTOS = 1

#  Tiempo en segundos entre los troncos
TIEMPO_TRONCOS = 1

#  Tiempo en segundos entre los objetos especiales
TIEMPO_OBJETO = 10

#  Monedas entregadas por el objeto Monedas
CANTIDAD_MONEDAS = 1

#  Tiempo de duracion de la ronda
DURACION_RONDA_INICIAL = 120

#  Velocidad en pixeles a la que se mueven los autos
VELOCIDAD_AUTOS = 30

#  Velocidad en pixeles a la que se mueven los troncos
VELOCIDAD_TRONCOS = 15

# Ponderador de dificultad para disminuir el tiempo de las rondas
PONDERADOR_DIFICULTAD = 0.8

# Minimo de caracteres en el nombre de usuario
MIN_CARACTERES = 1

#  Maximo de caracteres en el nombre de usuario
MAX_CARACTERES = 10

# Velocidad de movimiento en pixeles
VELOCIDAD_CAMINAR = 20

# Pixeles de movimiento al saltar
PIXELES_SALTO = 40

#  Cantidad de vidas aumentadas, al realizar cheatcode
VIDAS_TRAMPA = 1

# Cantidad de personas mostrar en el ranking
N_MOSTRAR = 5

TAMANO_VENTANA = 300, 300, 500, 500
TAMANO_VENTANA_JUEGO = 300, 300, 1000, 1000
MIN_X = 0
MAX_X = 950
MIN_Y = 170
MAX_Y = 740
Y_MAX_RIO = 500
Y_MIN_RIO = 360
POS_INICIO_AUTOS_Y = (680, 635, 585, 295, 255, 210, 680, 635, 585, 295, 255, 210)
POS_INICIO_AUTOS_X = (100, 400, 700, 200, 600, 800, 500, 800, 50, 600, 0, 100)
POS_INICIO_TRONCOS_Y = (400, 450, 4950, 400, 450, 495, 400, 450, 495)
POS_INICIO_TRONCOS_X = (100, 200, 300, 500, 600, 800, 900, 0, 100)
POS_INICIO_FROGG = 400, 740
POS_CHECK_POINT_1 = 400, 550
POS_CHECK_POINT_2 = 400, 340

# Tamaños de las imagenes de los objetos
WIDTH_FROGG = 40
HEIGHT_FROGG = 40
WIDTH_AUTO = 80
HEIGHT_AUTO = 50
WIDTH_TRONCO = 100
HEIGHT_TRONCO = 40
WIDTH_OBJETO = 30
HEIGHT_OBJETO = 30
FILAS_AUTOS = 6
FILAS_TRONCOS = 3

# Ruta archivo txt de puntajes
RUTA_PUNTAJES = os.path.join("puntajes.txt")

# Ruta archivo cancion
RUTA_CANCION = os.path.join("canciones", "musica.wav")

# Rutas imagenes de los objetos
RUTA_LOGO = os.path.join("frontend", "sprites", "Logo.png")
RUTA_MONEDA = os.path.join("frontend", "sprites", "Objetos", "Moneda.png")
RUTA_CORAZON = os.path.join("frontend", "sprites", "Objetos", "Corazon.png")
RUTA_RELOJ = os.path.join("frontend", "sprites", "Objetos", "Reloj.png")
RUTA_CALAVERA = os.path.join("frontend", "sprites", "Objetos", "Calavera.png")

# Rutas auto
RUTA_AUTO = os.path.join("frontend", "sprites", "Mapa", "autos", "plata_right.png")
RUTA_AUTO1_LEFT = os.path.join("frontend", "sprites", "Mapa", "autos", "amarillo_left.png")
RUTA_AUTO1_RIGHT = os.path.join("frontend", "sprites", "Mapa", "autos", "amarillo_right.png")
RUTA_AUTO2_LEFT = os.path.join("frontend", "sprites", "Mapa", "autos", "azul_left.png")
RUTA_AUTO2_RIGHT = os.path.join("frontend", "sprites", "Mapa", "autos", "azul_right.png")
RUTA_AUTO3_LEFT = os.path.join("frontend", "sprites", "Mapa", "autos", "blanco_left.png")
RUTA_AUTO3_RIGHT = os.path.join("frontend", "sprites", "Mapa", "autos", "blanco_right.png")
RUTA_AUTO4_LEFT = os.path.join("frontend", "sprites", "Mapa", "autos", "morado_left.png")
RUTA_AUTO4_RIGHT = os.path.join("frontend", "sprites", "Mapa", "autos", "morado_right.png")
RUTA_AUTO5_LEFT = os.path.join("frontend", "sprites", "Mapa", "autos", "negro_left.png")
RUTA_AUTO5_RIGHT = os.path.join("frontend", "sprites", "Mapa", "autos", "negro_right.png")
RUTA_AUTO6_LEFT = os.path.join("frontend", "sprites", "Mapa", "autos", "plata_left.png")
RUTA_AUTO6_RIGHT = os.path.join("frontend", "sprites", "Mapa", "autos", "plata_right.png")
RUTA_AUTO7_LEFT = os.path.join("frontend", "sprites", "Mapa", "autos", "rojo_left.png")
RUTA_AUTO7_RIGHT = os.path.join("frontend", "sprites", "Mapa", "autos", "rojo_right.png")

# Rutas imagenes de la rana verde
RUTA_FROGG_STILL = os.path.join("frontend", "sprites", "Personajes", "Verde", "still.png")      
RUTA_FROGG_DOWN_1 = os.path.join("frontend", "sprites", "Personajes", "Verde", "down_1.png")
RUTA_FROGG_DOWN_2 = os.path.join("frontend", "sprites", "Personajes", "Verde", "down_2.png")
RUTA_FROGG_DOWN_3 = os.path.join("frontend", "sprites", "Personajes", "Verde", "down_3.png")
RUTA_FROGG_JUMP_1 = os.path.join("frontend", "sprites", "Personajes", "Verde", "jump_1.png")
RUTA_FROGG_JUMP_2 = os.path.join("frontend", "sprites", "Personajes", "Verde", "jump_2.png")
RUTA_FROGG_JUMP_3 = os.path.join("frontend", "sprites", "Personajes", "Verde", "jump_3.png")
RUTA_FROGG_LEFT_1 = os.path.join("frontend", "sprites", "Personajes", "Verde", "left_1.png")
RUTA_FROGG_LEFT_2 = os.path.join("frontend", "sprites", "Personajes", "Verde", "left_2.png")
RUTA_FROGG_LEFT_3 = os.path.join("frontend", "sprites", "Personajes", "Verde", "left_3.png")
RUTA_FROGG_RIGHT_1 = os.path.join("frontend", "sprites", "Personajes", "Verde", "right_1.png")
RUTA_FROGG_RIGHT_2 = os.path.join("frontend", "sprites", "Personajes", "Verde", "right_2.png")
RUTA_FROGG_RIGHT_3 = os.path.join("frontend", "sprites", "Personajes", "Verde", "right_3.png")
RUTA_FROGG_UP_1 = os.path.join("frontend", "sprites", "Personajes", "Verde", "up_1.png")
RUTA_FROGG_UP_2 = os.path.join("frontend", "sprites", "Personajes", "Verde", "up_2.png")
RUTA_FROGG_UP_3 = os.path.join("frontend", "sprites", "Personajes", "Verde", "up_3.png")

# Rutas areas
RUTA_CARRETERA = os.path.join("frontend", "sprites", "Mapa", "areas", "carretera")
RUTA_RIO = os.path.join("frontend", "sprites", "Mapa", "areas", "rio")
RUTA_PASTO = os.path.join("frontend", "sprites", "Mapa", "areas", "pasto.png")

# Rutas de los elementos
RUTA_ARBOL_1 = os.path.join("frontend", "sprites", "Mapa", "elementos", "arbol_1.png")
RUTA_ARBOL_2 = os.path.join("frontend", "sprites", "Mapa", "elementos", "arbol_2.png")
RUTA_ARBOL_3 = os.path.join("frontend", "sprites", "Mapa", "elementos", "arbol_3.png")
RUTA_ARBOL_4 = os.path.join("frontend", "sprites", "Mapa", "elementos", "arbol_4.png")
RUTA_ARBUSTO_1 = os.path.join("frontend", "sprites", "Mapa", "elementos", "arbusto_1.png")
RUTA_ARBUSTO_3 = os.path.join("frontend", "sprites", "Mapa", "elementos", "arbusto_2.png")
RUTA_ARBUSTO_1 = os.path.join("frontend", "sprites", "Mapa", "elementos", "arbusto_3.png")
RUTA_CACTUS = os.path.join("frontend", "sprites", "Mapa", "elementos", "cactus.png")
RUTA_CROC_1 = os.path.join("frontend", "sprites", "Mapa", "elementos", "croc_1.png")
RUTA_CROC_2 = os.path.join("frontend", "sprites", "Mapa", "elementos", "croc_2.png")
RUTA_CROC_3 = os.path.join("frontend", "sprites", "Mapa", "elementos", "croc_3.png")
RUTA_CROC_4 = os.path.join("frontend", "sprites", "Mapa", "elementos", "croc_4.png")
RUTA_CROC_5 = os.path.join("frontend", "sprites", "Mapa", "elementos", "croc_5.png")
RUTA_FAROL_1 = os.path.join("frontend", "sprites", "Mapa", "elementos", "farol_1.png")
RUTA_FAROL_2 = os.path.join("frontend", "sprites", "Mapa", "elementos", "farol_2.png")
RUTA_TRONCO = os.path.join("frontend", "sprites", "Mapa", "elementos", "tronco.png")


