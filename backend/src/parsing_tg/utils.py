from ..datebase import get_async_session
from fastapi import Depends
from sqlalchemy import func, insert, select, delete, update, null, and_

from .models import NEWS_DATA


class PG_DB:
    def __init__(self):
        self.session = None


    async def get_session(self):
        return await get_async_session() 
    

    async def insert_into_db(self, new_line):
        if self.session is None:
            self.session = self.get_session()
        stmt = (
            insert(NEWS_DATA).values(
                message_id=new_line[0],
                sender=1,  # Замените на ваши значения
                chat_title=new_line[2],
                date=new_line[3],
                message=new_line[4],
                photo_id=new_line[5],
            )
        )
        async with self.session.begin():
            await self.session.execute(stmt)

    def get_last_id(self):
        last_id = self.session.query(NEWS_DATA.tg_data_id).order_by(NEWS_DATA.tg_data_id.desc()).first()
        return last_id[0] if last_id else None

    def last_date(self):
        last_date = self.session.query(func.max(NEWS_DATA.date)).first()
        return last_date[0] if last_date else None

    def is_post_in_time_range(self, id):
        current_date = self.session.query(NEWS_DATA.date).filter(NEWS_DATA.tg_data_id == id).first()
        return current_date[0] if current_date else None

    def get_all_info(self, id):
        record = self.session.query(NEWS_DATA).filter(NEWS_DATA.tg_data_id == id).first()
        if record:
            answer = {
                "TG_DATA_ID": record.tg_data_id,
                "MESSAGE_ID": record.message_id,
                "SENDER": record.sender,
                "CHAT_TITLE": record.chat_title,
                "DATE": record.date,
                "MESSAGE": record.message,
                "PHOTO_ID": record.photo_id
            }
            return answer
        return None





# class PG_DB:
#     async def __init__(self) -> None:
#         try:
#             self.connection = await Depends(get_async_session)
            
#         except (Exception, Error) as error:
#             print("Ошибка при работе с PostgreSQL", error)

#                                                         # (message.id,
#                                                         # CHANNELS[index],
#                                                         # message.chat.title,
#                                                         # message.date,
#                                                         # message.text,
#                                                         # photo_id)
#     async def insert_into_db(self, new_line):
#         # print(new_line)
#         stmt = (
#             insert(NEWS_DATA).values(
#                     message_id = new_line[0],
#                     sender = new_line[1] ,
#                     chat_title = new_line[2],
#                     date = new_line[3] ,
#                     message = new_line[4],
#                     photo_id = new_line[5],
#             )
#                 )
#         # print(stmt)
#         # await self.connection.execute(stmt)
#         # print(self.connection.execute(stmt))
#         # await self.connection.commit()

#     def get_last_id(self):
#         self.cursor.execute('''SELECT tg_data_id FROM news_data ORDER BY tg_data_id DESC LIMIT 1;''')
#         last_id = self.cursor.fetchone()
#         return last_id[0]
    
#     def last_date(self):
#         self.cursor.execute("SELECT MAX(DATE) from news_data;")
#         last_date = self.cursor.fetchone()
#         return last_date[0]
    
#     def is_post_in_time_range(self, id):
#         self.cursor.execute("SELECT DATE from news_data WHERE tg_data_id = %s;", (id,))
#         current_date = self.cursor.fetchone()
#         return current_date[0]

#     def get_all_info(self, id):

#         try:
#             self.cursor.execute("SELECT * from news_data WHERE tg_data_id = %s;", (id,))
#             records = self.cursor.fetchone()
#             answer = {
#                     "TG_DATA_ID": records[0],
#                     "MESSAGE_ID": records[1],
#                     "SENDER": records[2],
#                     "CHAT_TITLE": records[3],
#                     "DATE": records[4],
#                     "MESSAGE": records[5],
#                     "PHOTO_ID": records[6]
#                     }
#             return answer

#         except (Exception, Error) as error:
#             print("Ошибка при работе с PostgreSQL", error)

# test = PG_DB()
# print(test.get_last_id())
