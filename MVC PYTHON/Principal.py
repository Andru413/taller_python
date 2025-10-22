from Modelo_numero import Numero
from Vista import Vista_formulario
from controlador import Controlador

#Zona de codigo principal
# paso 5
obj_modelo = Numero()
obj_vista = Vista_formulario()
obj_controlador = Controlador(obj_vista, obj_modelo)