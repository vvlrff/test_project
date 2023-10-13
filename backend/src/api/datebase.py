from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import and_, desc, insert, or_,  select,  func, update 
from .models import news_data
import datetime




class PG_DB:

    def __init__(self, coonection):
        self.connect: AsyncSession = coonection

    async def last_date_ru(self):
        stmt = select(news_data.c.date).order_by(desc(news_data.c.date))
        res = await self.connect.execute(stmt)
        data = res.fetchone()
        if res == None:
            return (datetime.datetime.now() - datetime.timedelta(seconds=1200)).timestamp() #seconds=0 days=1
        else:
            return data[0].timestamp()
        
    async def insert_into_db(self, row):
        print(row)
        stmt = insert(news_data).values()
        data = await self.connect.execute(stmt)

        return data


      

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
