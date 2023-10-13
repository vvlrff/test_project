from fastapi import APIRouter
from fastapi.responses import JSONResponse
from .schemas import *
from .main import IntellectualSearch


router = APIRouter(
    prefix='/search',
    tags=['search']
)


@router.post('/test')
async def test_search(inputuser: InputUser):
    start_date = inputuser.start_date
    start_date_str = start_date.strftime("%Y-%m-%d %H:%M:%S")

    end_date = inputuser.end_date
    end_date_str = end_date.strftime("%Y-%m-%d %H:%M:%S")

    search = IntellectualSearch()
    data = search.main(inputuser.message, start_date_str, end_date_str)

    return JSONResponse(content=data)
