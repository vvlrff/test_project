import json
from telethon.sync import TelegramClient
from datetime import timedelta
from datetime import datetime

from Preprocessing import Preprocessing

from params import tg_name, tg_api_id, tg_api_hash, RU_CHANNELS, UA_CHANNELS

from db_postgres import PG_DB


class PG_parser:

    def __init__(self, name=tg_name, api_id=tg_api_id, api_hash=tg_api_hash):
        self.name = name
        self.api_id = api_id
        self.api_hash = api_hash

        self.preprocessing = Preprocessing()
        self.db_writer = PG_DB()

        self.searching_period = datetime.now() - timedelta(days=5)

    def parse_ru(self):

        self.last_date_ru = self.db_writer.last_date_ru()

        with TelegramClient(self.name,
                            self.api_id,
                            self.api_hash,
                            device_model = "iPhone 13 Pro Max",
                            system_version = "14.8.1",
                            app_version = "8.4",
                            lang_code = "en",
                            system_lang_code = "en-US") as client:
            
            for index in range(len(RU_CHANNELS)):
                try:
                    for message in client.iter_messages(RU_CHANNELS[index]):
                        if message.date.timestamp() > self.last_date_ru:
                        # if message.date.timestamp() > self.searching_period.timestamp():

                            text = message.text

                            if text is None or message.text == '':
                                continue

                            if type(text) != float:
                                final_text = self.preprocessing.preprocess(text)

                                adv_text = json.dumps(final_text)

                                self.db_writer.insert_into_ru((message.id,
                                                            RU_CHANNELS[index],
                                                            message.chat.title,
                                                            int(message.date.timestamp()),
                                                            message.text,
                                                            adv_text))
                        else:
                            break
                except:
                    pass

    def parse_ua(self):

        self.last_date_ua = self.db_writer.last_date_ua()

        with TelegramClient(self.name,
                            self.api_id,
                            self.api_hash,
                            device_model = "iPhone 13 Pro Max",
                            system_version = "14.8.1",
                            app_version = "8.4",
                            lang_code = "en",
                            system_lang_code = "en-US") as client:
            
            for index in range(len(UA_CHANNELS)):
                try:
                    for message in client.iter_messages(UA_CHANNELS[index]):
                        if message.date.timestamp() > self.last_date_ua:
                        # if message.date.timestamp() > self.searching_period.timestamp():

                            text = message.text

                            if text is None or message.text == '':
                                continue

                            if type(text) != float:
                                final_text = self.preprocessing.preprocess(text)

                                adv_text = json.dumps(final_text)

                                self.db_writer.insert_into_ua((message.id,
                                                            UA_CHANNELS[index],
                                                            message.chat.title,
                                                            int(message.date.timestamp()),
                                                            message.text,
                                                            adv_text))
                        else:
                            break
                except:
                    pass

# if __name__ == '__main__':
#     test = PG_parser()
#     test.parse_ru()
#     test.parse_ua()