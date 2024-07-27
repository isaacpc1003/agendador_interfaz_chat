import modulos.idActual as idActual
import modulos.dataBase.controller as controller
from modulos.dataBase.data_storage import data_storage_instance
from modulos.grafoChats.grafoChat import *

def extraerNombreCompleto(nombreCompleto):
    """Extrae el nombre completo y lo coloca en el formato json estandar"""
    datos_cliente = {"nombreCompleto": nombreCompleto}
    #data_storage_instance.clear_data()
    data_storage_instance.add_data('nombreCompleto', nombreCompleto)

    if controller.verificarExistencia(json.dumps(datos_cliente)):
        print("El usuario ya existe en la base de datos")
        idActual.global_id = 2
        pass
    else:
        print("No en la base de datos")
        if 'nombreCompleto' in data_storage_instance.get_data() and 'celular' in data_storage_instance.get_data() and 'correo' in data_storage_instance.get_data() and 'proyecto' in data_storage_instance.get_data() and 'presupuesto' in data_storage_instance.get_data() and 'tarjetaCredito' in data_storage_instance.get_data() and 'horario' in data_storage_instance.get_data():
            datos_cliente_completo = data_storage_instance.get_data()
            controller.registrarEntrada(json.dumps(datos_cliente_completo))
            print("Usuario registrado en la base de datos")
            data_storage_instance.clear_data()
            idActual.global_id = 2
        else:
            idActual.global_id = 2

    return json.dumps({"nombreCompleto": nombreCompleto})

def getGrafoChatID1():
    lista_de_tools = [
        {
            
            "type": "function",
            "function": {
                "name": "extraerNombreCompleto",
                "description": "Después de que al usuario se le pregunte cual es su nombre completo y que este responda, se pasa su nombre completo para que se lo reserve",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "nombreCompleto": {
                            "type": "string",
                            "description": "Nombre completo del usuario"
                        },
                    },
                    "required": ["nombreCompleto"]
                }
            }
        }
        ]

    available_functions = {
                "extraerNombreCompleto":extraerNombreCompleto
            }

    prompt = """Eres una experta en ventas llamada IrinA, extremadamente amable, feliz y comunicativa. 
    En tu presentación dirás quién eres y que eres la experta en inteligencia artificial que guiará al usuario en su proceso 
    de agendación de la cita. Ahora tu único trabajo es presentarte al usuario y preguntarle cual es su nombre, sin mencionar 
    que sea completo. Bajo ninguna otra condición harás cualquier otra acción, considera que puede que recibas una conversación 
    de antemano, evalúa esta conversación y únicamente enfócate en presentarte y obtener el nombre completo del usuario. 
    Además NO usarás emojis."""

    return grafoChat(1, available_functions, lista_de_tools, None, prompt)