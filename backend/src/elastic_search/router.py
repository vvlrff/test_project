from fastapi import APIRouter
from fastapi.responses import JSONResponse
from .schemas import *
from .main import IntellectualSearch


router = APIRouter(
    prefix='/search',
    tags=['search']
)


@router.post('/test_message_date_{param}')
async def elastic_test(param: str, inputuser: InputUser):
    start_date = inputuser.start_date
    start_date_str = start_date.strftime("%Y-%m-%d %H:%M:%S")

    end_date = inputuser.end_date
    end_date_str = end_date.strftime("%Y-%m-%d %H:%M:%S")

    elastic = IntellectualSearch()
    data = elastic.sort_answer(inputuser.message, start_date_str, end_date_str, param)

    return JSONResponse(content=data)

@router.post('/test_message_{param}')
async def test_search(param: str, inputuser: InputUserMessage):
    search = IntellectualSearch()
    data = search.sort_answer_without_date(inputuser.message, param)

    return JSONResponse(content=data)
