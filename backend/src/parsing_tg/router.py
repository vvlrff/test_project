import time
from fastapi.responses import JSONResponse
from fastapi import APIRouter
from .PG_parser import PG_parser
from fastapi import APIRouter,Depends
from sqlalchemy.ext.asyncio import AsyncSession

from ..datebase import get_async_session

router = APIRouter (
    prefix='/parsing',
    tags= ['parsing']
)

@router.get('/test')
async def test(session: AsyncSession = Depends(get_async_session)):
    while True:
        parser = PG_parser(session)
        await parser.parse_data()
        time.sleep(5)
        return 1  
