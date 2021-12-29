class NodoFama:

    def __init__(self, usuario, padre=None):
        # No modificar
        self.usuario = usuario
        self.padre = padre
        self.hijo_izquierdo = None
        self.hijo_derecho = None


class ArbolBinario:

    def __init__(self):
        # No modificar
        self.raiz = None

    def crear_arbol(self, nodos_fama):
        # No modificar
        for nodo in nodos_fama:
            self.insertar_nodo(nodo, self.raiz)

    def insertar_nodo(self, nuevo_nodo, padre=None):
        # Completar
        if self.raiz is None:
            self.raiz = nuevo_nodo
            return
        
        if nuevo_nodo.usuario.fama <= padre.usuario.fama:

            if padre.hijo_izquierdo:
                self.insertar_nodo(nuevo_nodo, padre.hijo_izquierdo)
            
            else:
                padre.hijo_izquierdo = nuevo_nodo
                nuevo_nodo.padre = padre
        
        elif nuevo_nodo.usuario.fama > padre.usuario.fama:

            if padre.hijo_derecho:
                self.insertar_nodo(nuevo_nodo, padre.hijo_derecho)
            
            else:
                padre.hijo_derecho = nuevo_nodo
                nuevo_nodo.padre = padre


    def buscar_nodo(self, fama, nodo=None):
        # Completar

        ### Se cambio el nombre de padre or nodo, para no confundir dado que
        ### No se utiliza como el padre dle nodo, si no como el nodo actual
        if nodo is None:
            nodo = self.raiz
        
        if nodo.usuario.fama == fama:
            return nodo
        
        if nodo.hijo_izquierdo or nodo.hijo_derecho:
            for hijo in [nodo.hijo_izquierdo, nodo.hijo_derecho]:
                nodo_obtenido = self.buscar_nodo(fama, hijo)
                if nodo_obtenido is not None:
                    return nodo_obtenido
        else:
            return None


    def print_arbol(self, nodo=None, nivel_indentacion=0):
        # No modificar
        indentacion = "|   " * nivel_indentacion
        if nodo is None:
            print("** DCCelebrity Arbol Binario**")
            self.print_arbol(self.raiz)
        else:
            print(f"{indentacion}{nodo.usuario.nombre}: "
                  f"{nodo.usuario.correo}")
            if nodo.hijo_izquierdo:
                self.print_arbol(nodo.hijo_izquierdo,
                                 nivel_indentacion + 1)
            if nodo.hijo_derecho:
                self.print_arbol(nodo.hijo_derecho,
                                 nivel_indentacion + 1)
