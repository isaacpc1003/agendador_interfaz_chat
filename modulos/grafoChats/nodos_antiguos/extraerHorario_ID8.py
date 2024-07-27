import modulos.idActual as idActual
import modulos.dataBase.controller as controller
from modulos.dataBase.data_storage import data_storage_instance
from modulos.grafoChats.grafoChat import *

def extraerHorario(horario):
    """Extrae el horario y lo coloca en el formato json estandar"""
    data_storage_instance.add_data('horario', horario)

    if 'nombreCompleto' in data_storage_instance.get_data() and 'celular' in data_storage_instance.get_data() and 'correo' in data_storage_instance.get_data() and 'proyecto' in data_storage_instance.get_data() and 'presupuesto' in data_storage_instance.get_data() and 'tarjetaCredito' in data_storage_instance.get_data() and 'horario' in data_storage_instance.get_data():
        datos_cliente_completo = data_storage_instance.get_data()
        controller.registrarEntrada(json.dumps(datos_cliente_completo))
        print("Usuario registrado en la base de datos")
        data_storage_instance.clear_data()
        #idActual.global_id = 1
    else:
        #idActual.global_id = 1
        pass
    

    return json.dumps({"horario": horario}) 

def getGrafoChatID8():
    lista_de_tools = [
        {
            
            "type": "function",
            "function": {
                "name": "extraerHorario",
                "description": "Después de que al usuario se le pregunte cuál es el horario más conveniente para ser contactado por nuestro IA Project Manager, y que este responda, se pasa el horario para que se lo registre",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "horario": {
                            "type": "string",
                            "description": "Horario más conveniente para que el usuario sea contactado por nuestro IA Project Manager"
                        },
                    },
                    "required": ["horario"]
                }
            }
        }
        ]

    available_functions = {
                "extraerHorario":extraerHorario
            }

    prompt = """Eres una experta en ventas llamada IrinA, extremadamente amable, feliz y comunicativa. 
    Ahora tu único trabajo es preguntarle al usuario cuál es el horario más conveniente para que nuestro IA Project 
    Manager lo contacte. Luego decirle al usuario que nuestro IA Project Manager lo contactará pronto. 
    Bajo ninguna otra condición harás cualquier otra acción, considera que puede que recibas una conversación de antemano, 
    evalúa esta conversación y únicamente enfócate en preguntar el horario más conveniente para que el usuario sea contactado 
    por nuestro IA Project Manager. Además NO usarás emojis."""

    return grafoChat(8, available_functions, lista_de_tools, None, prompt)