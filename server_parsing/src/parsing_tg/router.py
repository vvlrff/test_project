from fastapi.responses import JSONResponse
from sqlalchemy import insert


from sqlalchemy.ext.asyncio import AsyncSession
from fastapi import APIRouter
from .PG_parser import PG_parser

router = APIRouter (
    prefix='/parsing',
    tags= ['parsing']
)

@router.get('/test')
async def test():
    parser = PG_parser()
    data = await parser.parse_data()    
    return JSONResponse(content=data)
