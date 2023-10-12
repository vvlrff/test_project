import select

from fastapi import APIRouter
from .shemas import *
from .datebase import PG_DB


router = APIRouter (
    prefix='/api',
    tags= ['api']
)


@router.get('/test')
async def test():
    db = PG_DB()
    data = db.get_all_info_true()
    return data