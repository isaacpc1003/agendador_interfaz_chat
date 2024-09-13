import modulos.idActual as idActual
import modulos.dataBase.controller as controller
from modulos.dataBase.data_storage import data_storage_instance
from modulos.grafoChats.grafoChat import *

def terminarConversacion(nuevoMensaje):
    """Termina la conversación con el usuario y espera si vuelve a recibir un mensaje"""

    if nuevoMensaje:
        idActual.global_id = 1
    else:
        idActual.global_id = 10
        pass

    return json.dumps({"nuevoMensaje": nuevoMensaje}) 

lista_de_tools = [
        {
            
            "type": "function",
            "function": {
                "name": "terminarConversacion",
                "description": "Termina la conversación con el usuario y espera si vuelve a recibir un mensaje.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "nuevoMensaje": {
                            "type": "string",
                            "description": "Mensaje que se recibe de un nuevo usuario."
                        },
                    },
                    "required": ["nuevoMensaje"]
                }
            }
        }
        ]

available_functions = {
                "terminarConversacion":terminarConversacion
            }
    
def getGrafoChatID10():

    prompt = """Eres una experta en ventas llamada IrinA, extremadamente amable, feliz, comunicativa y que responde de manera clara y precisa.
    Ahora debes seguir estas instrucciones al pie de la letra:

    1. Ahora tu único trabajo es agradecer al usuario por su tiempo y por haberse comunicado contigo, dependiendo del camino que haya 
    tomado en la conversación. Y luego, terminarás la conversación amablemente sin preguntarle nada más al usuario y sin mencionar 
    más detalles.
    
    2. Luego, tu único trabajo es olvidarte de la conversiación y esperar si vuelves a recibir un mensaje. Si vuelves a recibir un mensaje, 
    vas a llamar la función terminarConversacion, y empezarás una nueva conversación con otro usuario que debes atender desde el principio.
    
    Bajo ninguna otra condición harás cualquier otra acción. Se clara y concisa en tu respuesta, y evita el uso de emojis."""

    return grafoChat(10, available_functions, lista_de_tools, None, prompt)