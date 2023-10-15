import os
from fastapi import APIRouter
from fastapi.responses import JSONResponse
from .shemas import *
from .datebase import PG_DB
from fastapi import APIRouter,Depends
from sqlalchemy.ext.asyncio import AsyncSession
from ..datebase import get_async_session


router = APIRouter (
    prefix='/api',
    tags= ['api']
)


@router.get('/test')
async def test(session: AsyncSession = Depends(get_async_session)):
    print(os.getcwd())
    db = PG_DB(session)
    data = await db.get_all_info_true()
    return data

@router.get('/test/{id}')
async def test_for_id(id:int, session: AsyncSession = Depends(get_async_session)):
    db = PG_DB(session)
    data = await db.test_for_id(id)
    return JSONResponse(data)
