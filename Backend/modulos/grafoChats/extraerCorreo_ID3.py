import modulos.idActual as idActual
import modulos.dataBase.controller as controller
from modulos.dataBase.data_storage import data_storage_instance
from modulos.grafoChats.grafoChat import *

def extraerCorreo(correo):
    """Extrae el correo y lo coloca en el formato json estandar"""
    datos_cliente = {"correo": correo}
    data_storage_instance.add_data('correo', correo)


    if controller.verificarExistencia(json.dumps(datos_cliente)):
        print("El usuario ya existe en la base de datos")
        idActual.global_id = 4
    else:
        print("No en la base de datos")
        if 'nombreCompleto' in data_storage_instance.get_data() and 'celular' in data_storage_instance.get_data() and 'correo' in data_storage_instance.get_data() and 'proyecto' in data_storage_instance.get_data() and 'presupuesto' in data_storage_instance.get_data() and 'tarjetaCredito' in data_storage_instance.get_data() and 'horario' in data_storage_instance.get_data():
            datos_cliente_completo = data_storage_instance.get_data()
            controller.registrarEntrada(json.dumps(datos_cliente_completo))
            print("Usuario registrado en la base de datos")
            data_storage_instance.clear_data()
            idActual.global_id = 4
        else:
            idActual.global_id = 4
    

    return json.dumps({"correo": correo})

lista_de_tools = [
        {
            
            "type": "function",
            "function": {
                "name": "extraerCorreo",
                "description": "Después de que al usuario se le pregunte cual es su correo electrónico y que este responda, se pasa su correo electrónico para que se lo registre",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "correo": {
                            "type": "string",
                            "description": "Correo electrónico del usuario"
                        },
                    },
                    "required": ["correo"]
                }
            }
        }
        ]

available_functions = {
                "extraerCorreo":extraerCorreo
            }
    
def getGrafoChatID3():

    prompt = """Eres una experta en ventas llamada IrinA, extremadamente amable, feliz y comunicativa. 
    Ahora tu único trabajo es preguntarle al usuario cual es su correo electrónico. Bajo ninguna otra condición harás cualquier otra acción, 
    considera que puede que recibas una conversación de antemano, evalúa esta conversación y únicamente enfócate en obtener el correo electrónico del usuario. 
    No asumirás el correo del usuario por ningún motivo. Se clara y concisa en tu respuesta, y evita el uso de emojis."""

    return grafoChat(3, available_functions, lista_de_tools, None, prompt)