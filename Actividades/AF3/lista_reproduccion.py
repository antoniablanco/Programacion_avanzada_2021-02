"""
En este archivo se encuentra la clase ListaReproduccion, la Iterable que
contiene los videos ordenados
"""


class ListaReproduccion:

    def __init__(self, conjunto_videos, usuario, nombre):
        self.conjunto_videos = conjunto_videos
        self.usuario = usuario
        self.nombre = nombre

    def __iter__(self):
        iterador = IterarLista(self.conjunto_videos.copy())
        return iterador

    def __str__(self):
        return f"Lista de Reproducción de {self.usuario}: {self.nombre}"


class IterarLista:

    def __init__(self, conjunto_videos):
        self.conjunto_videos = conjunto_videos

    def __iter__(self):
        return self

    def __next__(self):
        print("se llamo la funcion next")
        print("La lista es:", self.conjunto_videos)
        if self.conjunto_videos is None:
            raise StopIteration("No quedan más peliculas")
        else:           
            pelicula = max(self.conjunto_videos, key=lambda item: item[1])
            posicion = self.conjunto_videos.index(pelicula)
            devolver = self.conjunto_videos.pop(posicion)
            return pelicula[0]
