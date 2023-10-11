from fastapi.responses import JSONResponse
from sqlalchemy import insert


from sqlalchemy.ext.asyncio import AsyncSession
from ..datebase import get_async_session
from fastapi import APIRouter, Depends
from .PG_parser import PG_parser

parser = PG_parser()

router = APIRouter (
    prefix='/parsing',
    tags= ['parsing']
)

@router.get('/test')
async def test(session: AsyncSession = Depends(get_async_session)):
    parser = PG_parser()
    data = []
    print(parser)
    data = await parser.parse_data()    
    return JSONResponse(content=data)
