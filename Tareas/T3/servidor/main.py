import obtener_parametro as p
from servidor1 import Servidor

if __name__ == "__main__":
    port = p.parametro("PORT")
    host = p.parametro("HOST")
    servidor = Servidor(host, port)