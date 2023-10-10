from sqlalchemy import insert

from .models import NEWS_DATA
from .env_tg import *


from sqlalchemy.ext.asyncio import AsyncSession
from ..datebase import get_async_session
from fastapi import APIRouter, Depends
from .utils import PG_DB


router = APIRouter (
    prefix='/parsing',
    tags= ['parsing']
)


@router.get('/test')
async def test(session: AsyncSession = Depends(get_async_session)):
    print(2)
    # test = PG_parser()
    # test.parse_data()
    
    pass