class Controlador:
    def __init__(self, obj_vista, obj_modelo):
        #composicion es en el constructor
        self.obj_formulario = obj_vista
        self.obj_numero = obj_modelo
    
    def hacer_pregunta(self):
        numero = self.obj_formulario.hacer_campo()
        self.obj_formulario.hacer_campo()
        self.obj_numero.set_numero(numero)
        aux_mensaje = self.obj_numero.validar_par()

        self.obj_formulario.imprimir_resultado(aux_mensaje)