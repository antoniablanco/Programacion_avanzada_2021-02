class RiesgoCovid(Exception):

    def __init__(self, sintoma, nombre_invitade):
        self.sintoma = sintoma
        self.nombre = nombre_invitade
        
    def alerta_de_covid(self):
        print(f'El invitade tiene {self.sintoma} y tiene prohibida la entrada al DCCarrete')
