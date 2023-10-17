import time
from fastapi import APIRouter, BackgroundTasks
from .PG_parser import PG_parser
from fastapi import APIRouter,Depends
from sqlalchemy.ext.asyncio import AsyncSession

from ..datebase import get_async_session
# 
router = APIRouter (
    prefix='/parsing',
    tags= ['parsing']
)

@router.get('/test')
async def test(background_tasks: BackgroundTasks, session: AsyncSession = Depends(get_async_session)):
    background_tasks.add_task(parse_data_in_background, session)
    return {"message": "Parsing started in the background"}


async def parse_data_in_background(session: AsyncSession):
    parser = PG_parser(session)
    while True:
        await parser.parse_data()
        time.sleep(60*60)