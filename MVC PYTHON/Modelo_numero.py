
class Numero:
    def __init__(self):
        self.numero= " "

    def get_numero(self):
        return self.numero
    def set_numero(self, nuevo_numero):
        self.numero= nuevo_numero

    def validar_par(self):
        if self.numero % 2 ==0:
            mensaje = "Numero es par"
        else: 
            mensaje = "numero es impar"
        return mensaje
