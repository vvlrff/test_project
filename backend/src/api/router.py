import json
import os
import random as rnd
import re
import sys

from fastapi import APIRouter, Body, Depends, File, Query, UploadFile
from fastapi.responses import JSONResponse
from sqlalchemy.ext.asyncio import AsyncSession
# from src.api.occurrencesCounter import OccurrencesCounter

from ..datebase import get_async_session

router = APIRouter (
    prefix='/api',
    tags= ['api']
)

@router.get('/test')
async def test():
    return JSONResponse([{
        "photo":"https://www.wikihow.com/images/thumb/f/fc/Get-the-URL-for-Pictures-Step-1-Version-6.jpg/v4-728px-Get-the-URL-for-Pictures-Step-1-Version-6.jpg",
        "date": "20:49 05.10.2023",
        "msg":"Откройте страницу поиска изображений Google. Перейдите на страницу https://images.google.com/ в веб-браузере на компьютере. Откроется страница поиска изображений Google.",
        "url": "https://ru.wikihow.com/узнать-адрес-(URL)-изображения",
    },
    {
        "photo":"https://www.wikihow.com/images/thumb/f/fc/Get-the-URL-for-Pictures-Step-1-Version-6.jpg/v4-728px-Get-the-URL-for-Pictures-Step-1-Version-6.jpg",
        "date": "20:49 05.10.2023",
        "msg":"Откройте страницу поиска изображений Google. Перейдите на страницу https://images.google.com/ в веб-браузере на компьютере. Откроется страница поиска изображений Google.",
        "url": "https://ru.wikihow.com/узнать-адрес-(URL)-изображения",
    },
    {
        "photo":"https://www.wikihow.com/images/thumb/f/fc/Get-the-URL-for-Pictures-Step-1-Version-6.jpg/v4-728px-Get-the-URL-for-Pictures-Step-1-Version-6.jpg",
        "date": "20:49 05.10.2023",
        "msg":"Откройте страницу поиска изображений Google. Перейдите на страницу https://images.google.com/ в веб-браузере на компьютере. Откроется страница поиска изображений Google.",
        "url": "https://ru.wikihow.com/узнать-адрес-(URL)-изображения",
    },
    {
        "photo":"https://www.wikihow.com/images/thumb/f/fc/Get-the-URL-for-Pictures-Step-1-Version-6.jpg/v4-728px-Get-the-URL-for-Pictures-Step-1-Version-6.jpg",
        "date": "20:49 05.10.2023",
        "msg":"Откройте страницу поиска изображений Google. Перейдите на страницу https://images.google.com/ в веб-браузере на компьютере. Откроется страница поиска изображений Google.",
        "url": "https://ru.wikihow.com/узнать-адрес-(URL)-изображения",
    },
    {
        "photo":"https://www.wikihow.com/images/thumb/f/fc/Get-the-URL-for-Pictures-Step-1-Version-6.jpg/v4-728px-Get-the-URL-for-Pictures-Step-1-Version-6.jpg",
        "date": "20:49 05.10.2023",
        "msg":"Откройте страницу поиска изображений Google. Перейдите на страницу https://images.google.com/ в веб-браузере на компьютере. Откроется страница поиска изображений Google.",
        "url": "https://ru.wikihow.com/узнать-адрес-(URL)-изображения",
    },
    {
        "photo":"https://www.wikihow.com/images/thumb/f/fc/Get-the-URL-for-Pictures-Step-1-Version-6.jpg/v4-728px-Get-the-URL-for-Pictures-Step-1-Version-6.jpg",
        "date": "20:49 05.10.2023",
        "msg":"Откройте страницу поиска изображений Google. Перейдите на страницу https://images.google.com/ в веб-браузере на компьютере. Откроется страница поиска изображений Google.",
        "url": "https://ru.wikihow.com/узнать-адрес-(URL)-изображения",
    },
    {
        "photo":"https://www.wikihow.com/images/thumb/f/fc/Get-the-URL-for-Pictures-Step-1-Version-6.jpg/v4-728px-Get-the-URL-for-Pictures-Step-1-Version-6.jpg",
        "date": "20:49 05.10.2023",
        "msg":"Откройте страницу поиска изображений Google. Перейдите на страницу https://images.google.com/ в веб-браузере на компьютере. Откроется страница поиска изображений Google.",
        "url": "https://ru.wikihow.com/узнать-адрес-(URL)-изображения",
    },
    {
        "photo":"https://www.wikihow.com/images/thumb/f/fc/Get-the-URL-for-Pictures-Step-1-Version-6.jpg/v4-728px-Get-the-URL-for-Pictures-Step-1-Version-6.jpg",
        "date": "20:49 05.10.2023",
        "msg":"Откройте страницу поиска изображений Google. Перейдите на страницу https://images.google.com/ в веб-браузере на компьютере. Откроется страница поиска изображений Google.",
        "url": "https://ru.wikihow.com/узнать-адрес-(URL)-изображения",
    },
    {
        "photo":"https://www.wikihow.com/images/thumb/f/fc/Get-the-URL-for-Pictures-Step-1-Version-6.jpg/v4-728px-Get-the-URL-for-Pictures-Step-1-Version-6.jpg",
        "date": "20:49 05.10.2023",
        "msg":"Откройте страницу поиска изображений Google. Перейдите на страницу https://images.google.com/ в веб-браузере на компьютере. Откроется страница поиска изображений Google.",
        "url": "https://ru.wikihow.com/узнать-адрес-(URL)-изображения",
    },
    {
        "photo":"https://www.wikihow.com/images/thumb/f/fc/Get-the-URL-for-Pictures-Step-1-Version-6.jpg/v4-728px-Get-the-URL-for-Pictures-Step-1-Version-6.jpg",
        "date": "20:49 05.10.2023",
        "msg":"Откройте страницу поиска изображений Google. Перейдите на страницу https://images.google.com/ в веб-браузере на компьютере. Откроется страница поиска изображений Google.",
        "url": "https://ru.wikihow.com/узнать-адрес-(URL)-изображения",
    },
    {
        "photo":"https://www.wikihow.com/images/thumb/f/fc/Get-the-URL-for-Pictures-Step-1-Version-6.jpg/v4-728px-Get-the-URL-for-Pictures-Step-1-Version-6.jpg",
        "date": "20:49 05.10.2023",
        "msg":"Откройте страницу поиска изображений Google. Перейдите на страницу https://images.google.com/ в веб-браузере на компьютере. Откроется страница поиска изображений Google.",
        "url": "https://ru.wikihow.com/узнать-адрес-(URL)-изображения",
    },
    {
        "photo":"https://www.wikihow.com/images/thumb/f/fc/Get-the-URL-for-Pictures-Step-1-Version-6.jpg/v4-728px-Get-the-URL-for-Pictures-Step-1-Version-6.jpg",
        "date": "20:49 05.10.2023",
        "msg":"Откройте страницу поиска изображений Google. Перейдите на страницу https://images.google.com/ в веб-браузере на компьютере. Откроется страница поиска изображений Google.",
        "url": "https://ru.wikihow.com/узнать-адрес-(URL)-изображения",
    },
    {
        "photo":"https://www.wikihow.com/images/thumb/f/fc/Get-the-URL-for-Pictures-Step-1-Version-6.jpg/v4-728px-Get-the-URL-for-Pictures-Step-1-Version-6.jpg",
        "date": "20:49 05.10.2023",
        "msg":"Откройте страницу поиска изображений Google. Перейдите на страницу https://images.google.com/ в веб-браузере на компьютере. Откроется страница поиска изображений Google.",
        "url": "https://ru.wikihow.com/узнать-адрес-(URL)-изображения",
    },
    {
        "photo":"https://www.wikihow.com/images/thumb/f/fc/Get-the-URL-for-Pictures-Step-1-Version-6.jpg/v4-728px-Get-the-URL-for-Pictures-Step-1-Version-6.jpg",
        "date": "20:49 05.10.2023",
        "msg":"Откройте страницу поиска изображений Google. Перейдите на страницу https://images.google.com/ в веб-браузере на компьютере. Откроется страница поиска изображений Google.",
        "url": "https://ru.wikihow.com/узнать-адрес-(URL)-изображения",
    },
    {
        "photo":"https://www.wikihow.com/images/thumb/f/fc/Get-the-URL-for-Pictures-Step-1-Version-6.jpg/v4-728px-Get-the-URL-for-Pictures-Step-1-Version-6.jpg",
        "date": "20:49 05.10.2023",
        "msg":"Откройте страницу поиска изображений Google. Перейдите на страницу https://images.google.com/ в веб-браузере на компьютере. Откроется страница поиска изображений Google.",
        "url": "https://ru.wikihow.com/узнать-адрес-(URL)-изображения",
    },
    {
        "photo":"https://www.wikihow.com/images/thumb/f/fc/Get-the-URL-for-Pictures-Step-1-Version-6.jpg/v4-728px-Get-the-URL-for-Pictures-Step-1-Version-6.jpg",
        "date": "20:49 05.10.2023",
        "msg":"Откройте страницу поиска изображений Google. Перейдите на страницу https://images.google.com/ в веб-браузере на компьютере. Откроется страница поиска изображений Google.",
        "url": "https://ru.wikihow.com/узнать-адрес-(URL)-изображения",
    },
    {
        "photo":"https://www.wikihow.com/images/thumb/f/fc/Get-the-URL-for-Pictures-Step-1-Version-6.jpg/v4-728px-Get-the-URL-for-Pictures-Step-1-Version-6.jpg",
        "date": "20:49 05.10.2023",
        "msg":"Откройте страницу поиска изображений Google. Перейдите на страницу https://images.google.com/ в веб-браузере на компьютере. Откроется страница поиска изображений Google.",
        "url": "https://ru.wikihow.com/узнать-адрес-(URL)-изображения",
    },
    {
        "photo":"https://www.wikihow.com/images/thumb/f/fc/Get-the-URL-for-Pictures-Step-1-Version-6.jpg/v4-728px-Get-the-URL-for-Pictures-Step-1-Version-6.jpg",
        "date": "20:49 05.10.2023",
        "msg":"Откройте страницу поиска изображений Google. Перейдите на страницу https://images.google.com/ в веб-браузере на компьютере. Откроется страница поиска изображений Google.",
        "url": "https://ru.wikihow.com/узнать-адрес-(URL)-изображения",
    },
    {
        "photo":"https://www.wikihow.com/images/thumb/f/fc/Get-the-URL-for-Pictures-Step-1-Version-6.jpg/v4-728px-Get-the-URL-for-Pictures-Step-1-Version-6.jpg",
        "date": "20:49 05.10.2023",
        "msg":"Откройте страницу поиска изображений Google. Перейдите на страницу https://images.google.com/ в веб-браузере на компьютере. Откроется страница поиска изображений Google.",
        "url": "https://ru.wikihow.com/узнать-адрес-(URL)-изображения",
    },
    {
        "photo":"https://www.wikihow.com/images/thumb/f/fc/Get-the-URL-for-Pictures-Step-1-Version-6.jpg/v4-728px-Get-the-URL-for-Pictures-Step-1-Version-6.jpg",
        "date": "20:49 05.10.2023",
        "msg":"Откройте страницу поиска изображений Google. Перейдите на страницу https://images.google.com/ в веб-браузере на компьютере. Откроется страница поиска изображений Google.",
        "url": "https://ru.wikihow.com/узнать-адрес-(URL)-изображения",
    },
    {
        "photo":"https://www.wikihow.com/images/thumb/f/fc/Get-the-URL-for-Pictures-Step-1-Version-6.jpg/v4-728px-Get-the-URL-for-Pictures-Step-1-Version-6.jpg",
        "date": "20:49 05.10.2023",
        "msg":"Откройте страницу поиска изображений Google. Перейдите на страницу https://images.google.com/ в веб-браузере на компьютере. Откроется страница поиска изображений Google.",
        "url": "https://ru.wikihow.com/узнать-адрес-(URL)-изображения",
    },
    {
        "photo":"https://www.wikihow.com/images/thumb/f/fc/Get-the-URL-for-Pictures-Step-1-Version-6.jpg/v4-728px-Get-the-URL-for-Pictures-Step-1-Version-6.jpg",
        "date": "20:49 05.10.2023",
        "msg":"Откройте страницу поиска изображений Google. Перейдите на страницу https://images.google.com/ в веб-браузере на компьютере. Откроется страница поиска изображений Google.",
        "url": "https://ru.wikihow.com/узнать-адрес-(URL)-изображения",
    },
    {
        "photo":"https://www.wikihow.com/images/thumb/f/fc/Get-the-URL-for-Pictures-Step-1-Version-6.jpg/v4-728px-Get-the-URL-for-Pictures-Step-1-Version-6.jpg",
        "date": "20:49 05.10.2023",
        "msg":"Откройте страницу поиска изображений Google. Перейдите на страницу https://images.google.com/ в веб-браузере на компьютере. Откроется страница поиска изображений Google.",
        "url": "https://ru.wikihow.com/узнать-адрес-(URL)-изображения",
    },
    {
        "photo":"https://www.wikihow.com/images/thumb/f/fc/Get-the-URL-for-Pictures-Step-1-Version-6.jpg/v4-728px-Get-the-URL-for-Pictures-Step-1-Version-6.jpg",
        "date": "20:49 05.10.2023",
        "msg":"Откройте страницу поиска изображений Google. Перейдите на страницу https://images.google.com/ в веб-браузере на компьютере. Откроется страница поиска изображений Google.",
        "url": "https://ru.wikihow.com/узнать-адрес-(URL)-изображения",
    },
    {
        "photo":"https://www.wikihow.com/images/thumb/f/fc/Get-the-URL-for-Pictures-Step-1-Version-6.jpg/v4-728px-Get-the-URL-for-Pictures-Step-1-Version-6.jpg",
        "date": "20:49 05.10.2023",
        "msg":"Откройте страницу поиска изображений Google. Перейдите на страницу https://images.google.com/ в веб-браузере на компьютере. Откроется страница поиска изображений Google.",
        "url": "https://ru.wikihow.com/узнать-адрес-(URL)-изображения",
    },
    {
        "photo":"https://www.wikihow.com/images/thumb/f/fc/Get-the-URL-for-Pictures-Step-1-Version-6.jpg/v4-728px-Get-the-URL-for-Pictures-Step-1-Version-6.jpg",
        "date": "20:49 05.10.2023",
        "msg":"Откройте страницу поиска изображений Google. Перейдите на страницу https://images.google.com/ в веб-браузере на компьютере. Откроется страница поиска изображений Google.",
        "url": "https://ru.wikihow.com/узнать-адрес-(URL)-изображения",
    },
    {
        "photo":"https://www.wikihow.com/images/thumb/f/fc/Get-the-URL-for-Pictures-Step-1-Version-6.jpg/v4-728px-Get-the-URL-for-Pictures-Step-1-Version-6.jpg",
        "date": "20:49 05.10.2023",
        "msg":"Откройте страницу поиска изображений Google. Перейдите на страницу https://images.google.com/ в веб-браузере на компьютере. Откроется страница поиска изображений Google.",
        "url": "https://ru.wikihow.com/узнать-адрес-(URL)-изображения",
    },
    {
        "photo":"https://www.wikihow.com/images/thumb/f/fc/Get-the-URL-for-Pictures-Step-1-Version-6.jpg/v4-728px-Get-the-URL-for-Pictures-Step-1-Version-6.jpg",
        "date": "20:49 05.10.2023",
        "msg":"Откройте страницу поиска изображений Google. Перейдите на страницу https://images.google.com/ в веб-браузере на компьютере. Откроется страница поиска изображений Google.",
        "url": "https://ru.wikihow.com/узнать-адрес-(URL)-изображения",
    },
    {
        "photo":"https://www.wikihow.com/images/thumb/f/fc/Get-the-URL-for-Pictures-Step-1-Version-6.jpg/v4-728px-Get-the-URL-for-Pictures-Step-1-Version-6.jpg",
        "date": "20:49 05.10.2023",
        "msg":"Откройте страницу поиска изображений Google. Перейдите на страницу https://images.google.com/ в веб-браузере на компьютере. Откроется страница поиска изображений Google.",
        "url": "https://ru.wikihow.com/узнать-адрес-(URL)-изображения",
    },
    {
        "photo":"https://www.wikihow.com/images/thumb/f/fc/Get-the-URL-for-Pictures-Step-1-Version-6.jpg/v4-728px-Get-the-URL-for-Pictures-Step-1-Version-6.jpg",
        "date": "20:49 05.10.2023",
        "msg":"Откройте страницу поиска изображений Google. Перейдите на страницу https://images.google.com/ в веб-браузере на компьютере. Откроется страница поиска изображений Google.",
        "url": "https://ru.wikihow.com/узнать-адрес-(URL)-изображения",
    },
    {
        "photo":"https://www.wikihow.com/images/thumb/f/fc/Get-the-URL-for-Pictures-Step-1-Version-6.jpg/v4-728px-Get-the-URL-for-Pictures-Step-1-Version-6.jpg",
        "date": "20:49 05.10.2023",
        "msg":"Откройте страницу поиска изображений Google. Перейдите на страницу https://images.google.com/ в веб-браузере на компьютере. Откроется страница поиска изображений Google.",
        "url": "https://ru.wikihow.com/узнать-адрес-(URL)-изображения",
    },
    {
        "photo":"https://www.wikihow.com/images/thumb/f/fc/Get-the-URL-for-Pictures-Step-1-Version-6.jpg/v4-728px-Get-the-URL-for-Pictures-Step-1-Version-6.jpg",
        "date": "20:49 05.10.2023",
        "msg":"Откройте страницу поиска изображений Google. Перейдите на страницу https://images.google.com/ в веб-браузере на компьютере. Откроется страница поиска изображений Google.",
        "url": "https://ru.wikihow.com/узнать-адрес-(URL)-изображения",
    },
    {
        "photo":"https://www.wikihow.com/images/thumb/f/fc/Get-the-URL-for-Pictures-Step-1-Version-6.jpg/v4-728px-Get-the-URL-for-Pictures-Step-1-Version-6.jpg",
        "date": "20:49 05.10.2023",
        "msg":"Откройте страницу поиска изображений Google. Перейдите на страницу https://images.google.com/ в веб-браузере на компьютере. Откроется страница поиска изображений Google.",
        "url": "https://ru.wikihow.com/узнать-адрес-(URL)-изображения",
    },
    {
        "photo":"https://www.wikihow.com/images/thumb/f/fc/Get-the-URL-for-Pictures-Step-1-Version-6.jpg/v4-728px-Get-the-URL-for-Pictures-Step-1-Version-6.jpg",
        "date": "20:49 05.10.2023",
        "msg":"Откройте страницу поиска изображений Google. Перейдите на страницу https://images.google.com/ в веб-браузере на компьютере. Откроется страница поиска изображений Google.",
        "url": "https://ru.wikihow.com/узнать-адрес-(URL)-изображения",
    },
    {
        "photo":"https://www.wikihow.com/images/thumb/f/fc/Get-the-URL-for-Pictures-Step-1-Version-6.jpg/v4-728px-Get-the-URL-for-Pictures-Step-1-Version-6.jpg",
        "date": "20:49 05.10.2023",
        "msg":"Откройте страницу поиска изображений Google. Перейдите на страницу https://images.google.com/ в веб-браузере на компьютере. Откроется страница поиска изображений Google.",
        "url": "https://ru.wikihow.com/узнать-адрес-(URL)-изображения",
    },
    {
        "photo":"https://www.wikihow.com/images/thumb/f/fc/Get-the-URL-for-Pictures-Step-1-Version-6.jpg/v4-728px-Get-the-URL-for-Pictures-Step-1-Version-6.jpg",
        "date": "20:49 05.10.2023",
        "msg":"Откройте страницу поиска изображений Google. Перейдите на страницу https://images.google.com/ в веб-браузере на компьютере. Откроется страница поиска изображений Google.",
        "url": "https://ru.wikihow.com/узнать-адрес-(URL)-изображения",
    },
    {
        "photo":"https://www.wikihow.com/images/thumb/f/fc/Get-the-URL-for-Pictures-Step-1-Version-6.jpg/v4-728px-Get-the-URL-for-Pictures-Step-1-Version-6.jpg",
        "date": "20:49 05.10.2023",
        "msg":"Откройте страницу поиска изображений Google. Перейдите на страницу https://images.google.com/ в веб-браузере на компьютере. Откроется страница поиска изображений Google.",
        "url": "https://ru.wikihow.com/узнать-адрес-(URL)-изображения",
    },
    {
        "photo":"https://www.wikihow.com/images/thumb/f/fc/Get-the-URL-for-Pictures-Step-1-Version-6.jpg/v4-728px-Get-the-URL-for-Pictures-Step-1-Version-6.jpg",
        "date": "20:49 05.10.2023",
        "msg":"Откройте страницу поиска изображений Google. Перейдите на страницу https://images.google.com/ в веб-браузере на компьютере. Откроется страница поиска изображений Google.",
        "url": "https://ru.wikihow.com/узнать-адрес-(URL)-изображения",
    },
    {
        "photo":"https://www.wikihow.com/images/thumb/f/fc/Get-the-URL-for-Pictures-Step-1-Version-6.jpg/v4-728px-Get-the-URL-for-Pictures-Step-1-Version-6.jpg",
        "date": "20:49 05.10.2023",
        "msg":"Откройте страницу поиска изображений Google. Перейдите на страницу https://images.google.com/ в веб-браузере на компьютере. Откроется страница поиска изображений Google.",
        "url": "https://ru.wikihow.com/узнать-адрес-(URL)-изображения",
    },
    {
        "photo":"https://www.wikihow.com/images/thumb/f/fc/Get-the-URL-for-Pictures-Step-1-Version-6.jpg/v4-728px-Get-the-URL-for-Pictures-Step-1-Version-6.jpg",
        "date": "20:49 05.10.2023",
        "msg":"Откройте страницу поиска изображений Google. Перейдите на страницу https://images.google.com/ в веб-браузере на компьютере. Откроется страница поиска изображений Google.",
        "url": "https://ru.wikihow.com/узнать-адрес-(URL)-изображения",
    },
    {
        "photo":"https://www.wikihow.com/images/thumb/f/fc/Get-the-URL-for-Pictures-Step-1-Version-6.jpg/v4-728px-Get-the-URL-for-Pictures-Step-1-Version-6.jpg",
        "date": "20:49 05.10.2023",
        "msg":"Откройте страницу поиска изображений Google. Перейдите на страницу https://images.google.com/ в веб-браузере на компьютере. Откроется страница поиска изображений Google.",
        "url": "https://ru.wikihow.com/узнать-адрес-(URL)-изображения",
    },
    {
        "photo":"https://www.wikihow.com/images/thumb/f/fc/Get-the-URL-for-Pictures-Step-1-Version-6.jpg/v4-728px-Get-the-URL-for-Pictures-Step-1-Version-6.jpg",
        "date": "20:49 05.10.2023",
        "msg":"Откройте страницу поиска изображений Google. Перейдите на страницу https://images.google.com/ в веб-браузере на компьютере. Откроется страница поиска изображений Google.",
        "url": "https://ru.wikihow.com/узнать-адрес-(URL)-изображения",
    },
    {
        "photo":"https://www.wikihow.com/images/thumb/f/fc/Get-the-URL-for-Pictures-Step-1-Version-6.jpg/v4-728px-Get-the-URL-for-Pictures-Step-1-Version-6.jpg",
        "date": "20:49 05.10.2023",
        "msg":"Откройте страницу поиска изображений Google. Перейдите на страницу https://images.google.com/ в веб-браузере на компьютере. Откроется страница поиска изображений Google.",
        "url": "https://ru.wikihow.com/узнать-адрес-(URL)-изображения",
    },])
