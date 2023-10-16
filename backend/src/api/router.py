from fastapi import APIRouter, Query
from fastapi.responses import JSONResponse
from .shemas import *
from .datebase import PG_DB
from ..elastic_search.main import IntellectualSearch
from fastapi import APIRouter,Depends
from sqlalchemy.ext.asyncio import AsyncSession
from ..datebase import get_async_session
from fastapi_pagination import Page, paginate


router = APIRouter (
    prefix='/api',
    tags= ['api']
)


@router.get('/test_{param}')
async def test(param: str, session: AsyncSession = Depends(get_async_session),
               page: int = Query(ge=0, default=0),
               size: int = Query(ge=1, default=100))-> Page[PaginateNews]:
    db = PG_DB(session)
    if (param == "old"):
        data = await db.get_all_info_true_old()
    elif (param == "new"):
        data = await db.get_all_info_true()
    return paginate(data)

@router.get('/test/{id}')
async def test_for_id(id:int, session: AsyncSession = Depends(get_async_session)):
    db = PG_DB(session)
    data = await db.test_for_id(id)
    return JSONResponse(data)
