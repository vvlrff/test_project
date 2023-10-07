import json
import os
import random as rnd
import re
import sys

from fastapi import APIRouter, Body, Depends, File, Query, UploadFile
from fastapi.responses import JSONResponse
from sqlalchemy.ext.asyncio import AsyncSession
# from src.api.occurrencesCounter import OccurrencesCounter
from .shemas import *
from ..datebase import get_async_session

router = APIRouter (
    prefix='/api',
    tags= ['api']
)

@router.get('/test')
async def test():
    return JSONResponse([
        {'id':1,
        "photo":"https://www.wikihow.com/images/thumb/f/fc/Get-the-URL-for-Pictures-Step-1-Version-6.jpg/v4-728px-Get-the-URL-for-Pictures-Step-1-Version-6.jpg",
        "date": "20:49 05.10.2023",
        "msg":"Откройте страницу поиска изображений Google. Перейдите на страницу https://images.google.com/ в веб-браузере на компьютере. Откроется страница поиска изображений Google.",
        "url": "https://ru.wikihow.com/узнать-адрес-(URL)-изображения",
    },
    {   'id':2,
        "photo":"https://www.wikihow.com/images/thumb/f/fc/Get-the-URL-for-Pictures-Step-1-Version-6.jpg/v4-728px-Get-the-URL-for-Pictures-Step-1-Version-6.jpg",
        "date": "20:49 05.10.2023",
        "msg":"Откройте страницу поиска изображений Google. Перейдите на страницу https://images.google.com/ в веб-браузере на компьютере. Откроется страница поиска изображений Google.",
        "url": "https://ru.wikihow.com/узнать-адрес-(URL)-изображения",
    },
    {   'id':3,
        "photo":"https://www.wikihow.com/images/thumb/f/fc/Get-the-URL-for-Pictures-Step-1-Version-6.jpg/v4-728px-Get-the-URL-for-Pictures-Step-1-Version-6.jpg",
        "date": "20:49 05.10.2023",
        "msg":"Откройте страницу поиска изображений Google. Перейдите на страницу https://images.google.com/ в веб-браузере на компьютере. Откроется страница поиска изображений Google.",
        "url": "https://ru.wikihow.com/узнать-адрес-(URL)-изображения",
    },
    {   'id':4,
        "photo":"https://www.wikihow.com/images/thumb/f/fc/Get-the-URL-for-Pictures-Step-1-Version-6.jpg/v4-728px-Get-the-URL-for-Pictures-Step-1-Version-6.jpg",
        "date": "20:49 05.10.2023",
        "msg":"Откройте страницу поиска изображений Google. Перейдите на страницу https://images.google.com/ в веб-браузере на компьютере. Откроется страница поиска изображений Google.",
        "url": "https://ru.wikihow.com/узнать-адрес-(URL)-изображения",
    },
    {   'id':5,
        "photo":"https://www.wikihow.com/images/thumb/f/fc/Get-the-URL-for-Pictures-Step-1-Version-6.jpg/v4-728px-Get-the-URL-for-Pictures-Step-1-Version-6.jpg",
        "date": "20:49 05.10.2023",
        "msg":"Откройте страницу поиска изображений Google. Перейдите на страницу https://images.google.com/ в веб-браузере на компьютере. Откроется страница поиска изображений Google.",
        "url": "https://ru.wikihow.com/узнать-адрес-(URL)-изображения",
    },
    {   'id':6,
        "photo":"https://www.wikihow.com/images/thumb/f/fc/Get-the-URL-for-Pictures-Step-1-Version-6.jpg/v4-728px-Get-the-URL-for-Pictures-Step-1-Version-6.jpg",
        "date": "20:49 05.10.2023",
        "msg":"Откройте страницу поиска изображений Google. Перейдите на страницу https://images.google.com/ в веб-браузере на компьютере. Откроется страница поиска изображений Google.",
        "url": "https://ru.wikihow.com/узнать-адрес-(URL)-изображения",
    },
    {   'id':7,
        "photo":"https://www.wikihow.com/images/thumb/f/fc/Get-the-URL-for-Pictures-Step-1-Version-6.jpg/v4-728px-Get-the-URL-for-Pictures-Step-1-Version-6.jpg",
        "date": "20:49 05.10.2023",
        "msg":"Откройте страницу поиска изображений Google. Перейдите на страницу https://images.google.com/ в веб-браузере на компьютере. Откроется страница поиска изображений Google.",
        "url": "https://ru.wikihow.com/узнать-адрес-(URL)-изображения",
    },
    {   'id':8,
        "photo":"https://www.wikihow.com/images/thumb/f/fc/Get-the-URL-for-Pictures-Step-1-Version-6.jpg/v4-728px-Get-the-URL-for-Pictures-Step-1-Version-6.jpg",
        "date": "20:49 05.10.2023",
        "msg":"Откройте страницу поиска изображений Google. Перейдите на страницу https://images.google.com/ в веб-браузере на компьютере. Откроется страница поиска изображений Google.",
        "url": "https://ru.wikihow.com/узнать-адрес-(URL)-изображения",
    },
    {
        'id':9,
        "photo":"https://www.wikihow.com/images/thumb/f/fc/Get-the-URL-for-Pictures-Step-1-Version-6.jpg/v4-728px-Get-the-URL-for-Pictures-Step-1-Version-6.jpg",
        "date": "20:49 05.10.2023",
        "msg":"Откройте страницу поиска изображений Google. Перейдите на страницу https://images.google.com/ в веб-браузере на компьютере. Откроется страница поиска изображений Google.",
        "url": "https://ru.wikihow.com/узнать-адрес-(URL)-изображения",
    },
    {   'id':10,
        "photo":"https://www.wikihow.com/images/thumb/f/fc/Get-the-URL-for-Pictures-Step-1-Version-6.jpg/v4-728px-Get-the-URL-for-Pictures-Step-1-Version-6.jpg",
        "date": "20:49 05.10.2023",
        "msg":"Откройте страницу поиска изображений Google. Перейдите на страницу https://images.google.com/ в веб-браузере на компьютере. Откроется страница поиска изображений Google.",
        "url": "https://ru.wikihow.com/узнать-адрес-(URL)-изображения",
    },
    {   'id':11,
        "photo":"https://www.wikihow.com/images/thumb/f/fc/Get-the-URL-for-Pictures-Step-1-Version-6.jpg/v4-728px-Get-the-URL-for-Pictures-Step-1-Version-6.jpg",
        "date": "20:49 05.10.2023",
        "msg":"Откройте страницу поиска изображений Google. Перейдите на страницу https://images.google.com/ в веб-браузере на компьютере. Откроется страница поиска изображений Google.",
        "url": "https://ru.wikihow.com/узнать-адрес-(URL)-изображения",
    },
    {
        'id':12,
        "photo":"https://www.wikihow.com/images/thumb/f/fc/Get-the-URL-for-Pictures-Step-1-Version-6.jpg/v4-728px-Get-the-URL-for-Pictures-Step-1-Version-6.jpg",
        "date": "20:49 05.10.2023",
        "msg":"Откройте страницу поиска изображений Google. Перейдите на страницу https://images.google.com/ в веб-браузере на компьютере. Откроется страница поиска изображений Google.",
        "url": "https://ru.wikihow.com/узнать-адрес-(URL)-изображения",
    },
   ])



@router.post('/test_time')
async def test(data: InputUser):
    print(data)
    res = []
    result = {
        "message": data.message,
        "start_date": data.start_date.isoformat(),
        "end_date": data.end_date.isoformat(),
    }
    for i in range(10):
        res.append(result)

    return JSONResponse(content=res)
