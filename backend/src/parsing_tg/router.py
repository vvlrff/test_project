from sqlalchemy import insert

from .models import NEWS_DATA
from .env_tg import *
from .channels import CHANNELS

from telethon.sync import TelegramClient

from datetime import datetime, timedelta
from sqlalchemy.ext.asyncio import AsyncSession
from ..datebase import get_async_session
from elasticsearch import Elasticsearch
from fastapi import APIRouter, Depends
from .utils import PG_DB
import asyncio


router = APIRouter (
    prefix='/parsing',
    tags= ['parsing']
)
session: AsyncSession = Depends(get_async_session)
@router.get('/test')
async def test(session: AsyncSession = Depends(get_async_session)):
    print(2)
    # test = PG_parser()
    # test.parse_data()
    
    pass

class PG_parser:

    def __init__(self, name=TG_NAME, api_id=TG_API_ID, api_hash=TG_API_HASH):
        self.name = name
        self.api_id = api_id
        self.api_hash = api_hash
        self.es = Elasticsearch('http://localhost:9200')
        self.db_writer = PG_DB()  # Create an instance of PG_DB
        self.searching_period = datetime.now() - timedelta(days=1)

    async def parse_data(self):
        async with TelegramClient(self.name,
                                  self.api_id,
                                  self.api_hash,
                                  device_model="iPhone 13 Pro Max",
                                  system_version="14.8.1",
                                  app_version="8.4",
                                  lang_code="en",
                                  system_lang_code="en-US") as client:
            for index in range(len(CHANNELS)):
                try:
                    async for message in client.iter_messages(CHANNELS[index]):
                        if message.date.timestamp() > self.searching_period.timestamp():
                            text = message.text
                            if text is None or message.text == '' or len(message.text) < 100:
                                continue
                            try:
                                photo = message.photo
                                if photo:
                                    photo_id = photo.id
                                    client.download_media(photo, file=f'Photos\image{photo_id}.jpg')
                                else:
                                    photo_id = None
                            except Exception as e:
                                print(e)
                                photo_id = None

                            # Access the session attribute from db_writer
                            await self.db_writer.insert_into_db((message.id,
                                                        CHANNELS[index],
                                                        message.chat.title,
                                                        message.date,
                                                        message.text,
                                                        photo_id))
                            # The rest of your code...

                        else:
                            break
                except Exception as e:
                    print(e)
                    pass

async def get_parser():
    return PG_parser()

@router.get("/parse")
async def parse_data(parser: PG_parser = Depends(get_parser)):
    await parser.parse_data()
    return {"status": "success"}