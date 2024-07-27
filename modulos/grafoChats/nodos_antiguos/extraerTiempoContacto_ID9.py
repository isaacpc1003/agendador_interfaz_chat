import modulos.idActual as idActual
import modulos.dataBase.controller as controller
from modulos.dataBase.data_storage import data_storage_instance
from modulos.grafoChats.grafoChat import *

def extraerTiempoContacto(tiempoContacto):
    """Extrae el tiempo en el que el usuario desea ser contactado y lo coloca en el formato json estandar"""
    data_storage_instance.add_data('tiempoContacto', tiempoContacto)

    if 'nombreCompleto' in data_storage_instance.get_data() and 'celular' in data_storage_instance.get_data() and 'correo' in data_storage_instance.get_data() and 'proyecto' in data_storage_instance.get_data() and 'presupuesto' in data_storage_instance.get_data() and 'decision' in data_storage_instance.get_data() and 'tiempo_contacto' in data_storage_instance.get_data():
        datos_cliente_completo = data_storage_instance.get_data()
        controller.registrarEntrada(json.dumps(datos_cliente_completo))
        print("Usuario registrado en la base de datos")
        data_storage_instance.clear_data()
        #idActual.global_id = 1     
    else:
        #idActual.global_id = 1  
        pass

    return json.dumps({"tiempoContacto": tiempoContacto})


def getGrafoChatID9():
    lista_de_tools = [
        {
            "type": "function",
            "function": {
                "name": "extraerTiempoContacto",
                "description": "Después de que al usuario se le explique que se entiende su situación, se le pregunte en cuánto tiempo desea ser contactado nuevamente, y que este RESPONDA, se pasa el tiempo para que se lo registre.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "tiempoContacto": {
                            "type": "string",
                            "description": "Tiempo en el que el usuario desea ser contactado nuevamente."
                        },
                    },
                    "required": ["tiempoContacto"]
                }
            }
        }
        ]

    available_functions = {
        "extraerTiempoContacto": extraerTiempoContacto
    }

    prompt = """Eres una experta en ventas llamada IrinA, extremadamente amable, feliz y comunicativa. 
    Ahora tu único trabajo es EXPLICALE al usuario que se entiende su situación. Luego PREGUNTALE al usuario en 
    cuánto tiempo le gustaría ser contactado nuevamente, si en 1, 2, 3 meses, o si ya no quiere ser contactado. 
    No asumirás su decision por ningún motivo. Además NO usarás emojis."""

    return grafoChat(9, available_functions, lista_de_tools, None, prompt)
