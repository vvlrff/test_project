from datetime import timezone
from telethon.sync import TelegramClient
from elasticsearch import Elasticsearch
import re
from .params import tg_name, tg_api_id, tg_api_hash, CHANNELS
from .db_postgres import PG_DB

class PG_parser:

    def __init__(self, connection, name=tg_name, api_id=tg_api_id, api_hash=tg_api_hash):

        self.name = name
        self.api_id = api_id
        self.api_hash = api_hash

        self.es = Elasticsearch('http://localhost:9200')
        self.db_writer = PG_DB(connection)
        self.searching_period = self.db_writer.last_date_ru()

    def clean_text(self, text):
        text = re.sub(r'\(*http\S+\)*', '', text)
        text = re.sub(r'[^a-zA-Zа-яА-ЯёЁ0-9.,:;!?\'"()-]', ' ', text)
        text = re.sub(r'\s+', ' ', text)
        return text.strip()

    async def parse_data(self):
        searching_period = await self.db_writer.last_date_ru()
        async with TelegramClient(self.name,
                            self.api_id,
                            self.api_hash,
                            device_model = "iPhone 13 Pro Max",
                            system_version = "14.8.1",
                            app_version = "8.4",
                            lang_code = "en",
                            system_lang_code = "en-US") as client:
            
            for index in range(len(CHANNELS)):
                try:
                    async for message in client.iter_messages(CHANNELS[index]):
                        if message.date.timestamp() > searching_period + 10800: # временной сдвиг на 3 часа из-за таймзоны (UTC + 3)

                            text = self.clean_text(message.text)

                            if text is None or message.text == '' or len(message.text) < 100:
                                continue

                            try:
                                photo = message.photo
                                photo_id = photo.id
                                await client.download_media(photo, file=f'src\Photos\image{photo_id}.jpg')

                            except Exception as e:
                                photo_id = None
                                
                            await self.db_writer.insert_into_db([message.id,
                                                                CHANNELS[index],
                                                                message.chat.title,
                                                                message.date.astimezone(timezone.utc).replace(tzinfo=None),
                                                                text,
                                                                photo_id])
                                    
                            id = await self.db_writer.get_last_id()
                            self.es.index(index='news_index', document={'id': id,
                                                                        'date': message.date.strftime('%Y-%m-%d %H:%M:%S'),
                                                                        'content': text,
                                                                        'link': CHANNELS[index] + '/' + str(message.id),
                                                                        'photo': str(photo_id)})

                        else:
                            break
                except Exception as e:
                    print(e)
                    pass