import modulos.idActual as idActual
import modulos.dataBase.controller as controller
from modulos.dataBase.data_storage import data_storage_instance
from modulos.grafoChats.grafoChat import *

def extraerTiempoContacto(tiempo_contacto):
    """Extrae el tiempo en el que el usuario desea ser contactado nuevamente"""
    data_storage_instance.add_data('tiempo_contacto', tiempo_contacto)

    if 'nombreCompleto' in data_storage_instance.get_data() and 'celular' in data_storage_instance.get_data() and 'correo' in data_storage_instance.get_data() and 'proyecto' in data_storage_instance.get_data() and 'presupuesto' in data_storage_instance.get_data() and 'tiempo_contacto' in data_storage_instance.get_data():
        datos_cliente_completo = data_storage_instance.get_data()
        controller.registrarEntrada(json.dumps(datos_cliente_completo))
        print("Usuario registrado en la base de datos")
        data_storage_instance.clear_data()
        idActual.global_id = 9     
    else:
        idActual.global_id = 9  
        pass

    return json.dumps({"tiempo_contacto": tiempo_contacto})


def getGrafoChatID9():
    lista_de_tools = [
        {
            "type": "function",
            "function": {
                "name": "extraerTiempoContacto",
                "description": "Después de que al usuario se le explique que se entiende su situación respecto al presupuesto, se le pregunta en cuánto tiempo desea ser contactado nuevamente. Luego se registra el tiempo de contacto.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "tiempo_contacto": {
                            "type": "string",
                            "description": "Tiempo en el que el usuario desea ser contactado nuevamente."
                        },
                    },
                    "required": ["tiempo_contacto"]
                }
            }
        }
    ]

    available_functions = {
        "extraerTiempoContacto": extraerTiempoContacto
    }

    prompt = """Eres una experta en ventas llamada IrinA, extremadamente amable, feliz y comunicativa. 
    Ahora tu único trabajo es EXPLICAR al usuario que se entiende su situación por la que no esta dispuesto a invertir por ahora, y 
    PREGUNTARLE al usuario en cuánto tiempo le gustaría que lo contactáramos nuevamente, si en 1, 2, 3 meses, o si ya no quiere ser contactado. 
    Bajo ninguna otra condición harás cualquier otra acción. Se clara y concisa en tu respuesta, y evita el uso de emojis."""

    return grafoChat(9, available_functions, lista_de_tools, None, prompt)
