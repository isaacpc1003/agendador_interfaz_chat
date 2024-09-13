import modulos.idActual as idActual

from modulos.grafoChats.extraerNombreCompleto_ID1 import getGrafoChatID1
from modulos.grafoChats.extraerCelular_ID2 import getGrafoChatID2
from modulos.grafoChats.extraerCorreo_ID3 import getGrafoChatID3
from modulos.grafoChats.extraerProyecto_ID4 import getGrafoChatID4
from modulos.grafoChats.extraerPresupuesto_ID5 import getGrafoChatID5
from modulos.grafoChats.extraerDecision_ID6 import getGrafoChatID6
from modulos.grafoChats.extraerTarjetaCredito_ID7 import getGrafoChatID7
from modulos.grafoChats.extraerHorario_ID8 import getGrafoChatID8
from modulos.grafoChats.extraerTiempoContacto_ID9 import getGrafoChatID9
from modulos.grafoChats.terminarConversacion_ID10 import getGrafoChatID10


import os
from fastapi import FastAPI, HTTPException, Depends, Body
from pydantic import BaseModel
from openai import OpenAI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.security import APIKeyHeader
from typing import List
import json

# Get the API key from the environment variable
GOOGLE_CLOUD_API_KEY = os.getenv('GOOGLE_CLOUD_API_KEY')
if not GOOGLE_CLOUD_API_KEY:
    raise ValueError("No Google Cloud API key found in environment variables")

grafoChats = {1:getGrafoChatID1(), 2:getGrafoChatID2(), 3:getGrafoChatID3(), 4:getGrafoChatID4(), 5:getGrafoChatID5(), 6:getGrafoChatID6(), 7:getGrafoChatID7(), 8:getGrafoChatID8(), 9:getGrafoChatID9(), 10:getGrafoChatID10()}
chatActual = grafoChats[1]
idActual.global_id = 1

def traspaso():
    
    print(f"Paso a {idActual.global_id}")
    chatActual = grafoChats[idActual.global_id]
    chatActual.update_lista_de_mensajes()
    #print(lista_de_mensajes)
    #print(f"Traspaso a chat {idActual.global_id}")

app = FastAPI()

#origins = ["http://127.0.0.1:5500"]  # Adjust as per your CORS needs

origins = [
    "http://localhost",
    "http://localhost:8000",
    "http://127.0.0.1",
    "http://127.0.0.1:8000",
    "http://127.0.0.1:5501",
    "http://127.0.0.1:5500",
    "http://chat-agendador2.s3-website-us-east-1.amazonaws.com",
    "https://d17tzfbhnhm1ae.cloudfront.net",
    "https://irina.relatividadia.com"
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_methods=["*"],
    allow_headers=["*"],
    allow_credentials=True,
)

api_keys = [
    "c5435fd0-hrry-4617-krpn-9ffb829e7513",
    "ec9bcba1-tfwk-9799-rslv-378aae060441",
    "94705224-bhvg-4745-mac7-f15c455858f4"
]

api_key_header = APIKeyHeader(name='Psico-API-Key')

def get_api_key(api_key: str = Depends(api_key_header)) -> str:
    if api_key in api_keys:
        return api_key
    else:
        raise HTTPException(
            status_code=HTTPException.HTTP_401_UNAUTHORIZED,
            detail="Invalid API Key"
        )

client = OpenAI()  # Use your OpenAI API key

@app.get('/')
async def index():
    return {'message': 'API is Up and Running!'}

@app.get('/api-key')
async def get_google_cloud_api_key(api_key: str = Depends(get_api_key)):
    return {'GOOGLE_CLOUD_API_KEY': GOOGLE_CLOUD_API_KEY}

class ChatMessage(BaseModel):
    role: str
    content: str

class ChatInput(BaseModel):
    messages: List[ChatMessage]

@app.post("/chatgpt")
async def chat_with_gpt_extract_name(input_data: ChatInput, api_key: str = Depends(get_api_key)):
    global chatActual
    
    formatted_messages = [{"role": msg.role, "content": msg.content} for msg in input_data.messages]
    idActual.global_msgs = formatted_messages
    #print(formatted_messages)
    traspaso()
    return {"response": chatActual.run_conversation()}

@app.post("/chatgpt/reset-chat")
async def reset_chat(api_key: str = Depends(get_api_key)):
    global chatActual
    idActual.global_id = 1  # Restablecer el ID global al inicio
    chatActual = grafoChats[idActual.global_id]  # Restablecer el chatActual
    return {"message": "Chat reset successfully"}