from excepciones_covid import RiesgoCovid


# NO DEBES MODIFICAR ESTA FUNCIÓN
def verificar_sintomas(invitade):
    if invitade.temperatura > 37.5:
        raise RiesgoCovid("fiebre", invitade.nombre)
    elif invitade.tos:
        raise RiesgoCovid("tos", invitade.nombre)
    elif invitade.dolor_cabeza:
        raise RiesgoCovid("dolor_cabeza", invitade.nombre)


def entregar_invitados(diccionario_invitades):
    lista = []
    for invitade in diccionario_invitades.values():
        try: 
            verificar_sintomas(invitade)
        except RiesgoCovid as error:
            error.alerta_de_covid()
        else:
            lista.append(invitade.nombre)
    return lista


