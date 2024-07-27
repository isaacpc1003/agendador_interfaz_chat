import modulos.idActual as idActual
import modulos.dataBase.controller as controller
from modulos.dataBase.data_storage import data_storage_instance
from modulos.grafoChats.grafoChat import *

def extraerPresupuesto(presupuesto):
    """Extrae el presupuesto y lo coloca en el formato json estandar"""
    if int(presupuesto) < 2000:
        data_storage_instance.add_data('presupuesto', presupuesto)
        if 'nombreCompleto' in data_storage_instance.get_data() and 'celular' in data_storage_instance.get_data() and 'correo' in data_storage_instance.get_data() and 'proyecto' in data_storage_instance.get_data() and 'presupuesto' in data_storage_instance.get_data() and 'tarjetaCredito' in data_storage_instance.get_data() and 'horario' in data_storage_instance.get_data():
            datos_cliente_completo = data_storage_instance.get_data()
            controller.registrarEntrada(json.dumps(datos_cliente_completo))
            print("Usuario registrado en la base de datos")
            data_storage_instance.clear_data()
            idActual.global_id = 6
        else: 
            idActual.global_id = 6
    else:
        data_storage_instance.add_data('presupuesto', presupuesto)
        if 'nombreCompleto' in data_storage_instance.get_data() and 'celular' in data_storage_instance.get_data() and 'correo' in data_storage_instance.get_data() and 'proyecto' in data_storage_instance.get_data() and 'presupuesto' in data_storage_instance.get_data() and 'tarjetaCredito' in data_storage_instance.get_data() and 'horario' in data_storage_instance.get_data():
            datos_cliente_completo = data_storage_instance.get_data()
            controller.registrarEntrada(json.dumps(datos_cliente_completo))
            print("Usuario registrado en la base de datos")
            data_storage_instance.clear_data()
            idActual.global_id = 7
        else: 
            idActual.global_id = 7

    return json.dumps({"presupuesto": presupuesto})



def getGrafoChatID5():
    lista_de_tools = [
        {
            
            "type": "function",
            "function": {
                "name": "extraerPresupuesto",
                "description": "Después de que al usuario se le pregunte si cuenta con un presupuesto significativo para invertir en el proyecto y cual es la cantidad, y que este responda, se pasa su presupuesto para que se lo registre.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "presupuesto": {
                            "type": "integer",
                            "description": "Presupuesto que el usuario tiene para invertir en el proyecto."
                        },
                    },
                    "required": ["presupuesto"]
                }
            }
        }
        ]

    available_functions = {
                "extraerPresupuesto":extraerPresupuesto
            }

    prompt = """Eres una experta en ventas llamada IrinA, extremadamente amable, feliz y comunicativa. 
    Ahora tu único trabajo es decirle al usuario que efectivamente hemos realizado proyectos similares al que tiene pensado realizar y darle 
    detalles de estos pasados proyectos, los resultados y siempre mennciona el beneficio económico que percibieron los clientes. 
    Luego preguntarle si posee un presupuesto significativo para este proyecto y cuanto sería la cantidad del presupuesto. 
    Bajo ninguna otra condición harás cualquier otra acción, considera que puede que recibas una conversación de antemano, 
    evalúa esta conversación y únicamente enfócate en contarle las experiencias pasadas de los productos desarrollados, su beneficio económico, 
    y preguntarle su presupuesto. Además NO usarás emojis."""

    return grafoChat(5, available_functions, lista_de_tools, None, prompt)