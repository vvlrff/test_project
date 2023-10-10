from fastapi import WebSocket
from fastapi import APIRouter, Body, Depends, File, Query, UploadFile
from .gpt import GPT
router = APIRouter (
    prefix='/bot',
    tags= ['bot']
)
gpt = GPT()
@router.websocket("/send_bot")
async def websocket_endpoint(websocket: WebSocket):
    await print(process_message('Какой сегодня день ?'))
    # await websocket.accept()
    # while True:
    #     data = await websocket.receive_text()
    #     # Обработка сообщения от клиента, например, отправка его на ChatGPT
    #     response = process_message(data)
    #     print(process_message(data))
    #     if response:
    #         await websocket.send_text(response)

async def process_message(message):
    data = await gpt.chat_complete(message)
    return data