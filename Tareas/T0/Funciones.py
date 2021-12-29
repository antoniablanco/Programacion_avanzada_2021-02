# En este se usaran funciones para modularisar el flujo
import parametros
import datetime 


def Leer_Archivo(archivo, division, inicio):
    principio = open(archivo, "r", encoding="utf-8")
    lectura = principio.readlines()
    principio.close()

    lista = []
    for linea in lectura[inicio:]:
        if len(linea) > 1:
            intermedio = linea.strip()
            final = intermedio.split(",", division)
            lista.append(final)

    return lista


def Verificar_usuario(nombre):

    lista_nombres = Leer_Archivo("usuarios.csv", parametros.MAXSPLIT_NOMBRES, 1)
    devolver = False
    for usuario in range(len(lista_nombres)):
        if nombre.lower() == lista_nombres[usuario][0].lower():
            devolver = lista_nombres[usuario][0].lower()

    return devolver


def Registrar_usuario():
    print("El nombre de usuario no debe contener ',' y debe tener un largo de 1 a 15 caracteres")
    nombre = input("Ingrese el nombre: ")
    largo = len(nombre)
    cumple = True
    if Verificar_usuario(nombre):
        cumple = False
        print("ESTE NOMBRE DE USUARIO YA FUE UTILIZADO")
    if "," in nombre:
        cumple = False
        print("EL NOMBRE DE USUARIO NO PUEDE CONTENER ',' ")
    largo = len(nombre)
    if largo <= parametros.MIN_CARACTERES or largo > parametros.MAX_CARACTERES:
        cumple = False
        print("EL NOMBRE DE USUARIO NO CUMPLE CON EL LARGO PERMITIDO")
        print("RECUERDE EL MINIMOS REQUERIDO ES 1 CARACTERES Y EL MAXIMO 15 CARACTERES")
    if nombre == "anonimo":
        cumple = False
        print("Ese es un nombre clave que no esta permitido")

    if cumple:
        archivo = open("usuarios.csv", "a", encoding="utf-8")    
        print(nombre, file=archivo)
        archivo.close()
        cumple = nombre
    
    return cumple


def Una_Publicacion(id, usuario):
    id = int(id)
    devolver = False
    Datos_Publicacion(id, usuario)
    Comentarios_Publicacion(id, usuario)
    print("")
    if usuario != "anonimo":
        print("[1] Agregar comentario")
        print("[2] Volver")
        eleccion = input("Indique su opción: ")
        if eleccion == "1":
            Agregar_Comentario(id, usuario)
            Una_Publicacion(id, usuario)
        elif eleccion == "2":
            devolver = True
        else:
            print("No es una opcion posible")
            Una_Publicacion(id, usuario)
            devolver = True
    else:
        print("[1] Volver")
        eleccion = input("Indique su opción: ")
        if eleccion != "1":
            print("No es una opcion posible")
            Una_Publicacion(id, usuario)
        else:
            devolver = True
    return devolver


def Datos_Publicacion(id, usuario):
    id = int(id)
    publicaciones = Leer_Archivo("publicaciones.csv", parametros.MAXSPLIT_PUBLICACIONES, 1)

    print("")
    print(f'*** {publicaciones[id-1][1]} ***')
    print("")
    print(f'Creado: {publicaciones[id-1][3]}')
    print(f'Vendedor: {publicaciones[id-1][2]}')
    print(f'Precio: ${publicaciones[id-1][4]}')
    print(f'Descripción: {publicaciones[id-1][5]}')
    print("")


def Comentarios_Publicacion(id, usuario):
    print("Comentarios de la publicación:")
    id = int(id)
    todos_comentarios = Leer_Archivo("comentarios.csv", parametros.MAXSPLIT_COMENTARIOS, 1)
    comentarios = []

    for k in range(len(todos_comentarios)):
        if id == int(todos_comentarios[k][0]):
            comentarios.append(todos_comentarios[k])

    if len(comentarios) > 0:
        comentarios = (Orden_Fecha(comentarios, parametros.POSICION_COMENTARIO))
        for r in range(len(comentarios)):
            print(f'{comentarios[r][2]} -- {comentarios[r][1]}: {comentarios[r][3]}')
    else:
        print("-Esta publicacion no posee comentarios")


def Agregar_Comentario(id, usuario): 
    fecha = Fecha_Emision()
    comentario = input("Escriba el comentario: ")
    with open("comentarios.csv", 'a', encoding="utf-8") as f:  
        print(f'\n{id},{usuario},{fecha},{comentario}', file=f)
  

def Publicaciones_Usuario(usuario):

    todas_publicaciones = Leer_Archivo("publicaciones.csv", parametros.MAXSPLIT_PUBLICACIONES, 1)
    publicaciones = []

    for k in range(len(todas_publicaciones)):
        if usuario.lower() == todas_publicaciones[k][2].lower():
            publicaciones.append(todas_publicaciones[k])
            print(f'- {todas_publicaciones[k][1]}')

    if len(publicaciones) == 0:
        print("-No posee publicaciones")


def Agregar_Publicacion(usuario):

    publicaciones = Leer_Archivo("publicaciones.csv", parametros.MAXSPLIT_PUBLICACIONES, 1)

    id = len(publicaciones) + 1
    nombre = input("Indique el nombre del producto: ")
    precio = input("Indique el precio del producto: ")
    descripcion = input("Indique la descripción del producto: ")
    fecha = Fecha_Emision()
    
    with open("publicaciones.csv", 'a', encoding="utf-8") as f:  
        print(f'\n{id},{nombre.lower()},{usuario},{fecha},{precio},{descripcion}', file=f)


def Eliminar_Publicacion(usuario): 

    devolver = False
    todas_publicaciones = Leer_Archivo("publicaciones.csv", parametros.MAXSPLIT_PUBLICACIONES, 0)
    
    print("")
    print("¿Cuál publicación deseas eliminar?:")
    todas = todas_publicaciones.copy()
    publicaciones = []
    for k in range(len(todas_publicaciones)):
        if usuario == todas_publicaciones[k][2]:
            publicaciones.append(todas_publicaciones[k])
            print(f'[{len(publicaciones)}] {todas_publicaciones[k][1]} -- Creado el {todas_publicaciones[k][3]}')

    if len(publicaciones) == 0:
        print("Usted no posee publicaciones")
        devolver = True
        return devolver

    print(f'[{len(publicaciones)+1}] Volver')
    id = ""
    opcion = int(input("Indique su opción: "))
    if opcion == len(publicaciones)+1:
        devolver = True
        return devolver

    elif opcion <= len(publicaciones)+1 and opcion > 0:
        for pub in range(len(todas)):
            if publicaciones[opcion-1][0] == todas[pub][0]:
                id = publicaciones[opcion-1][0]
                todas_publicaciones.pop(pub)
        
        r = open("publicaciones.csv", "w", encoding="utf-8")
        for k in range(len(todas_publicaciones)):
            print(f'{todas_publicaciones[k][0]},{todas_publicaciones[k][1]},{todas_publicaciones[k][2].lower()},{todas_publicaciones[k][3]},{todas_publicaciones[k][4]},{todas_publicaciones[k][4]}', file=r)
        r.close()
        Eliminar_Comentarios(usuario, id)
        devolver = True
        return devolver
    else:
        print("Esa respuesta no es una opción, vuelva a intentarlo")
        Eliminar_Publicacion(usuario)


def Eliminar_Comentarios(usuario, id):

    todas_comentarios = publicaciones = Leer_Archivo("comentarios.csv", parametros.MAXSPLIT_COMENTARIOS, 0)

    r = open("comentarios.csv", "w", encoding="utf-8")
    for k in range(len(todas_comentarios)):
        if id != todas_comentarios[k][0]:
            print(f'{todas_comentarios[k][0]},{todas_comentarios[k][1].lower()},{todas_comentarios[k][2]},{todas_comentarios[k][3]}\n', file=r)   
    r.close()


def Fecha_Emision():
    return datetime.datetime.now().strftime('%Y/%m/%d %H:%M:%S')


def Orden_Fecha(lista, posicion):
    fechas = []
    for linea in range(len(lista)):
        fechas.append(lista[linea][posicion])

    fechas.sort(key=lambda date: datetime.datetime.strptime(date, '%Y/%m/%d %H:%M:%S'))
    
    ordenada = []
    for k in range(len(fechas)):
        for n in range(len(lista)):
            if fechas[k] == lista[n][posicion]:
                ordenada.append(lista[n])
    return ordenada


