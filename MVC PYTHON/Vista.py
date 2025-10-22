
class Vista_formulario:
    def __init__(self): 
        self.nombre_modulo= "Validar numeros"
        self.texto_pregunta = "Digite el numero"
        self.campo_numero= ""

    def hacer_campo(self):
        print(self.nombre_modulo)
        print(self.texto_pregunta)
        self.campo_numero= int (input())
        return self.campo_numero
    
    def imprimir_resultados(self, dato_mensaje):
        print(dato_mensaje)
    
