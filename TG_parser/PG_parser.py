from telethon.sync import TelegramClient
from datetime import timedelta
from datetime import datetime

from elasticsearch import Elasticsearch

from params import tg_name, tg_api_id, tg_api_hash, CHANNELS

from db_postgres import PG_DB


class PG_parser:

    def __init__(self, name=tg_name, api_id=tg_api_id, api_hash=tg_api_hash):

        self.name = name
        self.api_id = api_id
        self.api_hash = api_hash

        self.es = Elasticsearch('http://localhost:9200')

        self.db_writer = PG_DB()
        self.searching_period = datetime.now() - timedelta(days=1)

    def parse_data(self):

        # self.last_date_ru = self.db_writer.last_date()

        with TelegramClient(self.name,
                            self.api_id,
                            self.api_hash,
                            device_model = "iPhone 13 Pro Max",
                            system_version = "14.8.1",
                            app_version = "8.4",
                            lang_code = "en",
                            system_lang_code = "en-US") as client:
            
            for index in range(len(CHANNELS)):
                try:
                    for message in client.iter_messages(CHANNELS[index]):
                        # if message.date.timestamp() > self.last_date_ru:
                        if message.date.timestamp() > self.searching_period.timestamp():

                            text = message.text

                            if text is None or message.text == '' or len(message.text) < 100:
                                continue

                            try:
                                photo = message.photo
                                photo_id = photo.id
                                client.download_media(photo, file=f'Photos\image{photo_id}.jpg')
                            except:
                                photo_id = None

                            self.db_writer.insert_into_db((message.id,
                                                        CHANNELS[index],
                                                        message.chat.title,
                                                        message.date,
                                                        message.text,
                                                        photo_id))
                            
                            self.es.index(index='news_index', document={'id': self.db_writer.get_last_id(),
                                                                        'date': message.date.strftime('%Y-%m-%d %H:%M:%S'),
                                                                        'content': message.text,
                                                                        'link': CHANNELS[index] + '/' + str(message.id),
                                                                        'photo': str(photo_id)})

                        else:
                            break
                except:
                    pass

if __name__ == '__main__':
    test = PG_parser()
    test.parse_data()