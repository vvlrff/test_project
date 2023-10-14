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
    print(12)
    background_tasks.add_task(parse_data_in_background, session)
    return {"message": "Parsing started in the background"}


async def parse_data_in_background(session: AsyncSession):
    # print()
    parser = PG_parser(session)
    await parser.parse_data()
    time.sleep(2*2)