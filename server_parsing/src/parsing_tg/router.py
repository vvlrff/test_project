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
        print(1)
        parser = PG_parser()
        print(2)
        await parser.parse_data()
        time.sleep(3600)    
