from invitades import Invitade


def verificar_edad(invitade):
    edad = invitade.edad
    if edad <= 0:
        print(f"TypeError: la edad de {invitade.nombre} es negativa")
        raise TypeError


def corregir_edad(invitade):
    try:
        verificar_edad(invitade)
    except TypeError as error:
        invitade.edad = -invitade.edad
        print(f"El error en la edad de {invitade.nombre} ha sido corregido")


def verificar_pase_movilidad(invitade):
    pase = invitade.pase_movilidad
    if not isinstance(pase, bool):
        print(f"ValueError: el pase de movilidad de {invitade.nombre} no es un bool")
        raise ValueError


def corregir_pase_movilidad(invitade):
    try:
        verificar_pase_movilidad(invitade)
    except ValueError as error:
        invitade.pase_de_movilidad = True
        print(f"El error en el pase de movilidad de {invitade.nombre} ha sido corregido")


def verificar_mail(invitade):
    lista = invitade.mail.split("@")
    if lista[1] != "uc.cl":
        print(f"ValueError: El mail de {invitade.nombre} no está en el formato correcto")
        raise ValueError(f"Error: El mail de {invitade.nombre} no está en el formato correcto")


def corregir_mail(invitade):
    try:
        verificar_mail(invitade)
    except ValueError as error:
        lista = invitade.mail.split("@")
        nuevo = lista[1]+"@"+lista[0]
        invitade.mail = nuevo
        print(f"El error en el mail de {invitade.nombre} ha sido corregido")


def dar_alerta_colado(nombre_asistente, diccionario_invitades):
    try:
        keys = diccionario_invitades.keys()
        esta = False
        for k in keys:
            if k==nombre_asistente:
                esta = True
        if esta == False:
            raise KeyError
    except KeyError as error:
        print(f"KeyError: {nombre_asistente} se está intentando colar al carrete")
    else:
        asistente = diccionario_invitades[nombre_asistente]
        print(f"{asistente.nombre} esta en la lista y tiene edad {asistente.edad}")

