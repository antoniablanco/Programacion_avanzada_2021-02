""" En este archivo se escribiran los parametros a utilizar en la tarea 1"""

### Parametros para leer los archivos ###

# Lectura del archivo tributos
RUTA_TRIBUTOS = "tributos.csv"

# Lectura del archivo ambientes
RUTA_AMBIENTES = "ambientes.csv"

# Lectura del archivo objetos
RUTA_OBJETOS = "objetos.csv"

# Lectura del archivo arenas
RUTA_ARENAS = "arenas.csv"

### Parametros de la simulación de la hora ###

# Gasto de energía al realizar la acción heroica
ENERGIA_ACCION_HEROICA = 15

# Popularidad ganada al realizar la accion heroica
POPULARIDAD_ACCION_HEROICA = 3

# Gasto de energía al atacar a un tributo
ENERGIA_ATACAR = 20

# Popularidad ganada al matar a otro tributo
POPULARIDAD_ATACAR = 5

# Popularidad gastada para obtener un objeto aleatorio
POPULARIDAD_PEDIR = 3

# Energía ganada al hacerse bolita
ENERGIA_BOLITA = 10


### Parametros entidad Tributo ###

# Costo de popularidad al pedir un objeto aleatorio
COSTO_OBJETO = 3

### Parametros entidad Ambiente ###

# Daño que realiza el viento en el ambiente Playa
VELOCIDAD_VIENTOS_PLAYA = 20.0

# Daño que realiza la humedad en el ambiente Playa
HUMEDAD_PLAYA = 18.0

# Daño que realiza la nubosidad en el ambiente Montaña
NUBOSIDAD_MONTANA = 9.0

# Daño que realiza las precipitaciones en el ambiente Montaña
PRECIPITACIONES_MONTANA = 21.0

# Daño que realizan las precipitaciones en el ambiente Bosque
PRECIPITACIONES_BOSQUE = 17.0

# Daño que realizan los vientos en el ambiente Bosque
VELOCIDAD_VIENTOS_BOSQUE = 4.0


### Parametros entidad Objeto###

# Cantidad de energía que puede aumentar un objeto consumible
AUMENTAR_ENERGIA = 15

# Ponderador para aumentar la fuerza de un tributo a traves de un objeto Arma
PONDERADOR_AUMENTAR_FUERZA = 3

# Aumento de agilidad que puede realizar un objeto especial
AUMENTAR_AGILIDAD = 4

# Aumento de ingenio que puede realizar un objeto especial
AUMENTAR_INGENIO = 4


### Parametros entidad Arena###

# Probabilidad de evento
PROBABILIDAD_EVENTO = 1