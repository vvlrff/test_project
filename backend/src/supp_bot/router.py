from fastapi import WebSocket
from fastapi import APIRouter, Body, Depends, File, Query, UploadFile

router = APIRouter (
    prefix='/bot',
    tags= ['bot']
)

@router.websocket("/send_bot")
async def websocket_endpoint(websocket: WebSocket):
    await websocket.accept()
    while True:
        data = await websocket.receive_text()
        # Обработка сообщения от клиента, например, отправка его на ChatGPT
        response = process_message(data)
        await websocket.send_text(response)

def process_message(message):
    # Отправить запрос к ChatGPT API и получить ответ
    # response = openai.Completion.create(
    #     engine="text-davinci-002",
    #     prompt=message,
    #     max_tokens=150,
    #     n=1,
    #     stop=None
    # )

    return f'Привет СемЕн: {message}'