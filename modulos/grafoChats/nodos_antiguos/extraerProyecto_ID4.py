import modulos.idActual as idActual
import modulos.dataBase.controller as controller
from modulos.dataBase.data_storage import data_storage_instance
from modulos.grafoChats.grafoChat import *

def extraerProyecto(proyecto):
    """Extrae el proyecto y lo coloca en el formato json estandar"""
    data_storage_instance.add_data('proyecto', proyecto)

    if 'nombreCompleto' in data_storage_instance.get_data() and 'celular' in data_storage_instance.get_data() and 'correo' in data_storage_instance.get_data() and 'proyecto' in data_storage_instance.get_data() and 'presupuesto' in data_storage_instance.get_data() and 'tarjetaCredito' in data_storage_instance.get_data() and 'horario' in data_storage_instance.get_data():
        datos_cliente_completo = data_storage_instance.get_data()
        controller.registrarEntrada(json.dumps(datos_cliente_completo))
        print("Usuario registrado en la base de datos")
        data_storage_instance.clear_data()
        idActual.global_id = 5
    else:
        idActual.global_id = 5
    

    return json.dumps({"proyecto": proyecto})

def getGrafoChatID4():
    lista_de_tools = [
        {
            
            "type": "function",
            "function": {
                "name": "extraerProyecto",
                "description": "Después de que al usuario se le pregunte cual es el proyecto con IA que tiene en mente y que este responda, se pasa su proyecto para que se lo registre",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "proyecto": {
                            "type": "string",
                            "description": "Proyecto con IA que el usuario tiene en mente"
                        },
                    },
                    "required": ["proyecto"]
                }
            }
        }
        ]

    available_functions = {
                "extraerProyecto":extraerProyecto
            }

    prompt = """Eres una experta en ventas llamada IrinA, extremadamente amable, feliz y comunicativa. 
    Ahora tu único trabajo es preguntarle al usuario por cual necesidad o proyecto de su empresa necesita implementar 
    soluciones con IA. Bajo ninguna otra condición harás cualquier otra acción, considera que puede que recibas una 
    conversación de antemano, evalúa esta conversación y únicamente enfócate en conocer el proyecto o necesidad 
    en el que el usuario quiere implementar IA al detalle."""

    return grafoChat(4, available_functions, lista_de_tools, None, prompt)