from fastapi import APIRouter
from fastapi.responses import JSONResponse
from .schemas import *
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
    date_object = datetime.datetime.strptime(str(inputuser.end_date), "%Y-%m-%d %H:%M:%S.%f%z")
    end_date = date_object.strftime("%Y-%m-%d %H:%M:%S")
    search = IntellectualSearch()
    data = search.main(inputuser.message,start_date, end_date )
    return JSONResponse(content=data)

