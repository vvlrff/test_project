from fastapi import APIRouter, Body, Depends, File, Query, UploadFile
from fastapi.responses import JSONResponse
from sqlalchemy.ext.asyncio import AsyncSession
# from src.api.occurrencesCounter import OccurrencesCounter
from .schemas import *
from ..datebase import get_async_session
from .main import IntellectualSearch
import datetime

router = APIRouter (
    prefix='/search',
    tags= ['search']
)

@router.post('/test')
async def test_search(inputuser:InputUser):
    date_object = datetime.datetime.strptime(str(inputuser.start_date), "%Y-%m-%d %H:%M:%S.%f%z")
    start_date = date_object.strftime("%Y-%m-%d %H:%M:%S")
    print(start_date)
    date_object = datetime.datetime.strptime(str(inputuser.end_date), "%Y-%m-%d %H:%M:%S.%f%z")
    end_date = date_object.strftime("%Y-%m-%d %H:%M:%S")
    print(end_date)
    search = IntellectualSearch()
    print(inputuser.message)

    data = search.main(inputuser.message,start_date, end_date )
    return JSONResponse(content=data)

