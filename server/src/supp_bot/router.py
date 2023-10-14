from fastapi import APIRouter
from fastapi.responses import JSONResponse
from .schemas import InputUserForGPT
from .gpt import GPT
router = APIRouter (
    prefix='/bot',
    tags= ['bot']
)
gpt = GPT()
@router.post("/send_bot")
async def send_bot(data:InputUserForGPT):
    data = await process_message(data.message)
    return JSONResponse(content=data)

async def process_message(message):
    data = await gpt.chat_complete(message)
    return data