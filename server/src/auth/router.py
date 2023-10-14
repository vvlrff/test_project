import json
from fastapi import APIRouter, Depends
import fastapi_users
from sqlalchemy.ext.asyncio import AsyncSession
from ..auth.models import user
from ..datebase import get_async_session
from .schemas import UserRead, UserCreate
from .base_config import auth_backend, fastapi_users
from sqlalchemy import select
from fastapi.responses import JSONResponse
router = APIRouter(
    prefix = '/auth',
    tags = ['auth']
)


router.include_router(
    fastapi_users.get_auth_router(auth_backend),
    
)

router.include_router(
    fastapi_users.get_register_router(UserRead, UserCreate),
)

current_user = fastapi_users.current_user()

@router.get('/user')
async def protected_lk(user_pol: user = Depends(current_user), session: AsyncSession = Depends(get_async_session)):
    return JSONResponse(content={
        'name' : user_pol.name,
    })
