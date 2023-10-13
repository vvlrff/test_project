from fastapi.responses import JSONResponse
from sqlalchemy.ext.asyncio import AsyncSession
from ..datebase import get_async_session
from fastapi import APIRouter, Depends
from .shemas import *
from .datebase import PG_DB


router = APIRouter (
    prefix='/api',
    tags= ['api']
)


@router.get('/test')
async def test(session: AsyncSession = Depends(get_async_session)):
    db = PG_DB(session)
    # res = await db.last_date_ru()
    res = await db.insert_into_db()
    return JSONResponse(content=res)