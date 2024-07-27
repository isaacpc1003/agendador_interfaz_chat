import modulos.idActual as idActual
import modulos.dataBase.controller as controller
from modulos.dataBase.data_storage import data_storage_instance
from modulos.grafoChats.grafoChat import *

def extraerTarjetaCredito(tarjetaCredito):
    """Extrae la respuesta si el usuario tiene tarjeta de crédito y lo coloca en el formato json estandar"""
    data_storage_instance.add_data('tarjetaCredito', tarjetaCredito)

    if 'nombreCompleto' in data_storage_instance.get_data() and 'celular' in data_storage_instance.get_data() and 'correo' in data_storage_instance.get_data() and 'proyecto' in data_storage_instance.get_data() and 'presupuesto' in data_storage_instance.get_data() and 'tarjetaCredito' in data_storage_instance.get_data() and 'horario' in data_storage_instance.get_data():
        datos_cliente_completo = data_storage_instance.get_data()
        controller.registrarEntrada(json.dumps(datos_cliente_completo))
        print("Usuario registrado en la base de datos")
        data_storage_instance.clear_data()
        idActual.global_id = 8
    else:
        idActual.global_id = 8
    

    return json.dumps({"tarjetaCredito": tarjetaCredito})

def getGrafoChatID7():
    lista_de_tools = [
        {
            
            "type": "function",
            "function": {
                "name": "extraerTarjetaCredito",
                "description": "Después de que al usuario se le pregunte si posee una tarjeta de crédito Visa o Mastercard y que este responda, se pasa la respuesta del usuario para que se registre",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "tarjetaCredito": {
                            "type": "string",
                            "description": "Respuesta del usuario si posee una tarjeta de crédito Visa o Mastercard."
                        },
                    },
                    "required": ["tarjetaCredito"]
                }
            }
        }
        ]

    available_functions = {
                "extraerTarjetaCredito":extraerTarjetaCredito
            }

    prompt = """Eres una experta en ventas llamada IrinA, extremadamente amable, feliz y comunicativa. 
    Ahora tu único trabajo es informarle al usuario que ofrecemos un descuento para personas que tienen una tarjeta de crédito Visa o Mastercard. 
    Luego, PREGUNTALE al usuario tal cual la frase: '¿Este es tu caso?' y, de ser así, que tipo de tarjeta tiene (Visa o Mastercard).
    No asumirás su decision por ningún motivo. Además NO usarás emojis."""

    return grafoChat(7, available_functions, lista_de_tools, None, prompt)