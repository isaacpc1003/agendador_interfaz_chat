import modulos.idActual as idActual
import modulos.dataBase.controller as controller
from modulos.dataBase.data_storage import data_storage_instance
from modulos.grafoChats.grafoChat import *

def extraerDecision(decision):
    """Extrae la decision si el usuario esta dispuesto a extender su presupuesto y lo coloca en el formato json estandar"""
    data_storage_instance.add_data('decision', decision)
    
    if decision == True:
        if 'nombreCompleto' in data_storage_instance.get_data() and 'celular' in data_storage_instance.get_data() and 'correo' in data_storage_instance.get_data() and 'proyecto' in data_storage_instance.get_data() and 'presupuesto' in data_storage_instance.get_data() and 'tarjetaCredito' in data_storage_instance.get_data() and 'horario' in data_storage_instance.get_data() and 'decision' in data_storage_instance.get_data():
            datos_cliente_completo = data_storage_instance.get_data()
            controller.registrarEntrada(json.dumps(datos_cliente_completo))
            print("Usuario registrado en la base de datos")
            data_storage_instance.clear_data()
            idActual.global_id = 7
        else:
            idActual.global_id = 7
    else:
        if 'nombreCompleto' in data_storage_instance.get_data() and 'celular' in data_storage_instance.get_data() and 'correo' in data_storage_instance.get_data() and 'proyecto' in data_storage_instance.get_data() and 'presupuesto' in data_storage_instance.get_data() and 'tarjetaCredito' in data_storage_instance.get_data() and 'horario' in data_storage_instance.get_data() and 'decision' in data_storage_instance.get_data():
            datos_cliente_completo = data_storage_instance.get_data()
            controller.registrarEntrada(json.dumps(datos_cliente_completo))
            print("Usuario registrado en la base de datos")
            data_storage_instance.clear_data()
            idActual.global_id = 9
        else:
            idActual.global_id = 9

    return json.dumps({"decision": decision})

lista_de_tools = [
        {

            "type": "function",
            "function": {
                "name": "extraerDecision",
                "description": "Después de que al usuario se le pregunte si esta dispuesto a extender su presupuesto, y que este RESPONDA, se pasa la respuesta del usuario para que se registre.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "decision": {
                            "type": "boolean",
                            "enum": [True, False],
                            "description": "Respuesta del usuario si esta dispuesto a extender su presupuesto al mínimo requerido para el proyecto."
                        },
                    },
                    "required": ["decision"]
                }
            }
        }
    ]

available_functions = {
    "extraerDecision": extraerDecision
    }
    
def getGrafoChatID6():
    prompt = """Eres una experta en ventas llamada IrinA, extremadamente amable, feliz, comunicativa y que responde de manera clara y precisa.
    Ahora tu único trabajo es explicar al usuario que el presupuesto mínimo para realizar su proyecto es de 2000 dólares. Luego 
    PREGUNTALE al usuario si esta dispuesto a extender su presupuesto al menos a 2000 dólares para realizar
    su proyecto exitosamente y continuar con el registro de los datos faltantes. No asumirás su decision por ningún motivo.
    Se clara y concisa en tu respuesta, y evita el uso de emojis."""

    return grafoChat(6, available_functions, lista_de_tools, None, prompt)
