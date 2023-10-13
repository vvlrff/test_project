from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import and_, desc, insert, or_,  select,  func, update 
from .models import news_data
import datetime




class PG_DB:

    def __init__(self, coonection):
        self.connect: AsyncSession = coonection

    async def last_date_ru(self):
        stmt = select(news_data.c.date).order_by((news_data.c.date))
        res = await self.connect.execute(stmt)
        data = res.fetchone()
        print(data, 'date_start')
        if data == None:
            return (datetime.datetime.now() - datetime.timedelta(seconds=1000000)).timestamp() #seconds=0 days=1
        else:
            return data[0].timestamp()

    async def insert_into_db(self, row:list):

        add_post = insert(news_data).values(message_id = row[0],
                                            sender=row[1],
                                            chat_title=row[2],
                                            date=row[3],
                                            message=row[4],
                                            photo_id=row[5])

        await self.connect.execute(add_post)
        await self.connect.commit()

    async def get_last_id(self):
        stmt  = select(news_data.c.tg_data_id).order_by(desc(news_data.c.tg_data_id))
        res = await self.connect.execute(stmt)
        data = res.fetchone()
        return data[0]

#     def get_last_id(self):
#         self.cursor.execute('''SELECT tg_data_id FROM news_data ORDER BY tg_data_id DESC LIMIT 1;''')
#         last_id = self.cursor.fetchone()
#         return last_id[0]
# tg_data_id
# message_id
# sender
# chat_title
# date
# message
# photo_id
      

#     def insert_into_db(self, new_line):
#         self.cursor.execute('''INSERT INTO news_data 
#                                 (
#                                 MESSAGE_ID,
#                                 SENDER,
#                                 CHAT_TITLE,
#                                 DATE,
#                                 MESSAGE,
#                                 PHOTO_ID
#                                 )
#                                 VALUES(%s, %s, %s, %s, %s, %s);''', new_line)
#         self.connection.commit()


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

#     def get_all_info_true(self):

#         try:
#             self.cursor.execute("SELECT * from news_data")
#             records = self.cursor.fetchall()
#             data = []
#             for row in records:
#                 answer = {
#                         "id": row[0],
#                         "MESSAGE_ID": row[1],
#                         "url": row[2],
#                         "CHAT_TITLE": row[3],
#                         "date": row[4],
#                         "msg": row[5],
#                         "photo": f"http://localhost:8001/Photos/image{row[6]}.jpg"
#                         }
#                 if row[6] == None:
#                     answer['photo'] = f"http://localhost:8001/Photos/image5253752555547251902.jpg"
#                 data.append(answer)
#             return data

#         except (Exception, Error) as error:
#             print("Ошибка при работе с PostgreSQL", error)














# import datetime
# import psycopg2
# from psycopg2 import Error
# from psycopg2.extensions import ISOLATION_LEVEL_AUTOCOMMIT
# from ..config import DB_HOST, DB_NAME, DB_PASS, DB_PORT, DB_USER
# # 
# class PG_DB:
#     def __init__(self) -> None:
#         try:
#             self.connection = psycopg2.connect(user=DB_USER,
#                                                 password=DB_PASS,
#                                                 host=DB_HOST,
#                                                 port=DB_PORT,
#                                                 dbname=DB_NAME)
            
#             self.connection.set_isolation_level(ISOLATION_LEVEL_AUTOCOMMIT)

#             self.cursor = self.connection.cursor()
#             self.cursor.execute("""CREATE TABLE IF NOT EXISTS news_data
#                                     (
#                                     tg_data_id serial PRIMARY KEY,
#                                     MESSAGE_ID INTEGER,
#                                     SENDER TEXT,
#                                     CHAT_TITLE TEXT,
#                                     DATE timestamp,
#                                     MESSAGE TEXT,
#                                     PHOTO_ID bigint
#                                     );""")
            
#         except (Exception, Error) as error:
#             print("Ошибка при работе с PostgreSQL", error)

#     def last_date_ru(self):
#         self.cursor.execute(
#             "SELECT  news_data.date FROM news_data ORDER BY date DESC"
#         )
#         if self.cursor.fetchone() == None:
#             return (datetime.datetime.now() - datetime.timedelta(days=1)).timestamp() #seconds=0 days=1
#         else:
#             return self.cursor.fetchone()[0].timestamp()        

#     def insert_into_db(self, new_line):
#         self.cursor.execute('''INSERT INTO news_data 
#                                 (
#                                 MESSAGE_ID,
#                                 SENDER,
#                                 CHAT_TITLE,
#                                 DATE,
#                                 MESSAGE,
#                                 PHOTO_ID
#                                 )
#                                 VALUES(%s, %s, %s, %s, %s, %s);''', new_line)
#         self.connection.commit()


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
# # 'photo': f"http://localhost:8000/Photos/image{el['_source']['photo']}.jpg"

#     def get_all_info_true(self):

#         try:
#             self.cursor.execute("SELECT * from news_data")
#             records = self.cursor.fetchall()
#             data = []
#             for row in records:
#         #                 id
#         #                   date
#         #                   relevant_score
#         #                   msg
#         #                   url
#         #                   photo
#                 answer = {
#                         "id": row[0],
#                         "MESSAGE_ID": row[1],
#                         "url": row[2],
#                         "CHAT_TITLE": row[3],
#                         "date": row[4],
#                         "msg": row[5],
#                         "photo": f"http://localhost:8001/Photos/image{row[6]}.jpg"
#                         }
#                 if row[6] == None:
#                     answer['photo'] = f"http://localhost:8001/Photos/image5253752555547251902.jpg"
#                 data.append(answer)
#             return data

#         except (Exception, Error) as error:
#             print("Ошибка при работе с PostgreSQL", error)

# # test = PG_DB()
# # print(test.get_last_id())
