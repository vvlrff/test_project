import time
from fastapi.responses import JSONResponse
from fastapi import APIRouter
from .PG_parser import PG_parser

router = APIRouter (
    prefix='/parsing',
    tags= ['parsing']
)

@router.get('/test')
async def test():
    while True:
        parser = PG_parser()
        print('Я работаю')
        await parser.parse_data()
        print('Я сделал')    
        time.sleep(5)
        print('Я поспал')    
