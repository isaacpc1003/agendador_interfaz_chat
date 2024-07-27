import modulos.idActual as idActual
import modulos.dataBase.controller as controller
from modulos.dataBase.data_storage import data_storage_instance
from modulos.grafoChats.grafoChat import *

def extraerCelular(celular):
    """Extrae el número celular y lo coloca en el formato json estandar"""
    celular = celular.replace(" ", "")
    datos_cliente = {"celular": celular}
    data_storage_instance.add_data('celular', celular)


    if controller.verificarExistencia(json.dumps(datos_cliente)):
        print("El usuario ya existe en la base de datos")
        pass
    else:
        print("No en la base de datos")
        if 'nombreCompleto' in data_storage_instance.get_data() and 'celular' in data_storage_instance.get_data() and 'correo' in data_storage_instance.get_data() and 'proyecto' in data_storage_instance.get_data() and 'presupuesto' in data_storage_instance.get_data() and 'tarjetaCredito' in data_storage_instance.get_data() and 'horario' in data_storage_instance.get_data():
            datos_cliente_completo = data_storage_instance.get_data()
            controller.registrarEntrada(json.dumps(datos_cliente_completo))
            print("Usuario registrado en la base de datos")
            data_storage_instance.clear_data()
            idActual.global_id = 3
        else:
            idActual.global_id = 3
    

    return json.dumps({"celular": celular})

def getGrafoChatID2():
    lista_de_tools = [
        {
            
            "type": "function",
            "function": {
                "name": "extraerCelular",
                "description": "Después de que al usuario se le pregunte cual es su número celular y que este responda, se pasa su número celular para que se lo reserve",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "celular": {
                            "type": "string",
                            "description": "Número celular del usuario"
                        },
                    },
                    "required": ["celular"]
                }
            }
        }
        ]

    available_functions = {
                "extraerCelular":extraerCelular
            }

    prompt = """Eres una experta en ventas llamada IrinA, extremadamente amable, feliz y comunicativa. 
    Ahora tu único trabajo es preguntarle al usuario cual es su número celular. Bajo ninguna otra condición harás cualquier 
    otra acción, considera que puede que recibas una conversación de antemano, evalúa esta conversación y únicamente enfócate 
    en obtener el número de celular del usuario. Además NO usarás emojis."""

    return grafoChat(2, available_functions, lista_de_tools, None, prompt)