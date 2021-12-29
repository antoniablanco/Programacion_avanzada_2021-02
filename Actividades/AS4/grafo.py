from collections import deque


class NodoGrafo:
    def __init__(self, usuario):
        # No modificar
        self.usuario = usuario
        self.amistades = None

    def formar_amistad(self, nueva_amistad):
        # Completar
        esta = False
        
        if self.amistades is not None:
            for persona in self.amistades:
                if nueva_amistad.usuario.nombre == persona.usuario.nombre:
                    esta = True
        
        if not esta:
            self.amistades.append(nueva_amistad)
        
        # Para la nueva amistad
        esta2 = False
        
        if nueva_amistad.amistades is not None:
            for persona in nueva_amistad.amistades:
                if self.usuario.nombre == persona.usuario.nombre:
                    esta2 = True
        
        if not esta2:
            nueva_amistad.amistades.append(nueva_amistad)
        

    def eliminar_amistad(self, ex_amistad):
        # Completar
        ctd = None
        if self.amistades is not None:
            for persona in range(len(self.amistades)):
                if self.amistades[persona].usuario.nombre == ex_amistad.usuario.nombre:
                    ctd = persona
        if ctd is not None:
            self.amistades.pop(ctd)
        
        #Para la ex amistad
        ctd2 = None
        if ex_amistad.amistades is not None:
            for persona in range(len(ex_amistad.amistades)):
                if ex_amistad.amistades[persona].usuario.nombre == self.usuario.nombre:
                    ctd2 = persona
        if ctd2 is not None:
            ex_amistad.amistades.pop(ctd)
        
        

def recomendar_amistades(nodo_inicial, profundidad, distancia=int("0"), recomendados=None, visitados=None, vecino=None):
    """
    Recibe un NodoGrafo inicial y una profundidad de busqueda, retorna una
    lista de nodos NodoGrafo recomendados como amistad a esa profundidad.
    """
    recomendados = recomendados or set()
    visitados = visitados or set()
    vecino = vecino or nodo_inicial

    if distancia <= profundidad:

        for n in vecino.amistades:
            #print("n:",n.usuario.nombre)
            # Se revisa no haberlo revisado antes
            if n not in visitados:
                visitados.add(n)

                # Se revisa si esta en los amigos
                esta = False
                if nodo_inicial.amistades is not None:
                    for persona in nodo_inicial.amistades:
                        #print(n.usuario.nombre, "revisando:",persona.usuario.nombre)
                        if n.usuario.nombre == persona.usuario.nombre:
                            esta = True
                        #print(esta)
                # Se agrega a la lista
                if n not in recomendados and not esta:
                    #print("se agrego:", n.usuario.nombre)
                    recomendados.add(n)
                
                return recomendar_amistades(nodo_inicial, profundidad, distancia + 1, recomendados, visitados, n)

    else:
        return list(recomendados)


def busqueda_famosos(nodo_inicial, visitados=None, distancia_min=80):
    """
    [BONUS]
    Recibe un NodoGrafo y busca en la red social al famoso mas
    cercano, retorna la distancia y el nodo del grafo que contiene
    a el usuario famoso cercano al que se encuentra.
    """
    # Completar para el bonus
