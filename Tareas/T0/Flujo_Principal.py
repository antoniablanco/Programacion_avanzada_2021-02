import parametros
import Funciones


def Menu_inicio():
    usuario = ""
    print("")
    print("*** Menu Inicio ***")
    print("")
    print("Selecciona una opción")
    print("[1] Ingresar sesión")
    print("[2] Registrar usuario")
    print("[3] Ingresar como usuario anónimo")
    print("[4] Salir")

    opcion = input("Indique su opcion: ")
    if opcion == "1":
        nombre = input("Indique el nombre de usuario: ")
        ret = Funciones.Verificar_usuario(nombre)
        if ret == False:
            print("")
            print("El nombre de usuario no se encuentra registrado")
            Menu_inicio()
        else:
            print("Se ha encontrado al usuario")
            usuario = ret
            Menu_Principal(usuario)

    elif opcion == "2":
        ret = Funciones.Registrar_usuario()
        if ret == False:
            Menu_inicio()
        else:
            usuario = ret
            Menu_Principal(usuario)

    elif opcion == "3":
        print("Usted a ingresado como usuario anonimo")
        usuario = "anonimo"
        Menu_Principal(usuario)

    elif opcion == "4":
        print("Gracias por utilizar DCComercio")
        usuario = "Salir"
    else:
        print("")
        print("Ese numero no es valido, intentelo de nuevo")
        Menu_inicio()
    
    return usuario


def Menu_Principal(usuario):
    print("")
    print("*** Menu Principal ***")
    print("")
    print("Selecciona una opción")
    print("[1] Menu Publicaciones")
    if usuario != "anonimo":
        print("[2] Menu Publicaciones Realizada")
        print("[3] Volver")
    else:
        print("[2] Volver")
    
    accion = input("Indique su opcion: ")
    if accion == "1":
        Menu_Publicaciones(usuario)
    elif accion == "2" and usuario != "anonimo":
        Menu_PublicacionesRealizadas(usuario)
    elif (accion == "3" and usuario != "anonimo") or (accion == "2" and usuario == "anonimo"):
        Menu_inicio()
    else:
        print("")
        print("Esa no es una opcion valida")
        Menu_Principal(usuario)


def Menu_Publicaciones(usuario):
    print("")
    print("*** Menú de Publicaciones ***")
    print("")

    publicaciones = Funciones.Leer_Archivo("publicaciones.csv", parametros.MAXSPLIT_PUBLICACIONES, 1)
    publicaciones = Funciones.Orden_Fecha(publicaciones, parametros.POSICION_PUBLICACION)
    alreves_publicaciones = []
    for k in reversed(range(len(publicaciones))):
        print(f'[{len(publicaciones)-k}] {publicaciones[k][1]}')
        alreves_publicaciones.append(publicaciones[k])

    print(f'[{len(publicaciones)+1}] Volver')
    
    publicacion = input("Indique su opción: ")

    if not publicacion.isnumeric():
        print("")
        print("Esa no es una opcione valida, intentelo de nuevo")
        Menu_Publicaciones(usuario)
    elif int((publicacion)) == len(publicaciones)+1:
        Menu_Principal(usuario)
    elif int(publicacion) <= (len(publicaciones)+1) and int(publicacion) >= 1:
        id = alreves_publicaciones[(int(publicacion)-1)][0]
        print(f'el id es: {id}')
        devolver = Funciones.Una_Publicacion(id, usuario)
        Menu_Publicaciones(usuario)
    else:
        print("")
        print("Esa no es una opcione valida, intentelo de nuevo")
        Menu_Publicaciones(usuario)


def Menu_PublicacionesRealizadas(usuario):
    print("")
    print("*** Menú de Publicaciones Realizadas ***")
    print("")
    print("Mis publicaciones:")
    Funciones.Publicaciones_Usuario(usuario) 
    print("")
    print("[1] Crear nueva publicación")
    print("[2] Eliminar publicación")
    print("[3] Volver")

    eleccion = input("Indique su opción: ")
    if eleccion == "1":
        Funciones.Agregar_Publicacion(usuario)
        Menu_PublicacionesRealizadas(usuario)
    elif eleccion == "2":
        devolver = Funciones.Eliminar_Publicacion(usuario)
        if devolver:
            Menu_PublicacionesRealizadas(usuario)
        Menu_PublicacionesRealizadas(usuario)
    elif eleccion == "3":
        Menu_Principal(usuario)
    else:
        print("Esa no es una opción valida")
        Menu_PublicacionesRealizadas(usuario)

print("")
print("--- ¡Bienvenid@s a DCCommerce! ---")
Menu_inicio()