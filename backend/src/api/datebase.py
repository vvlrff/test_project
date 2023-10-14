from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import and_, desc, insert, or_,  select,  func, update 
# from .models import news_data
from ..elastic_search.models import news_data


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


    async def get_all_info_true(self):
        stmt = select(news_data)
        res = await self.connect.execute(stmt)
        res = res.fetchall()
        data = []
        for row in res:
            answer = {
                    "id": row[0],
                    "MESSAGE_ID": row[1],
                    "url": row[2],
                    "CHAT_TITLE": row[3],
                    "date": row[4],
                    "msg": row[5],
                    "photo": f"http://localhost:8001/Photos/image{row[6]}.jpg"
                    }
            if row[6] == None:
                answer['photo'] = f"http://localhost:8001/Photos/image5253752555547251902.jpg"
            data.append(answer)
        return data

    async def test_for_id(self, id:int):
        stmt = select(news_data).where(news_data.c.tg_data_id == id)
        print(stmt)
        res = await self.connect.execute(stmt)
        data = res.fetchone()
        # print(data)
        answer = {
                    "id": data[0],
                    "MESSAGE_ID": data[1],
                    "url": data[2],
                    "CHAT_TITLE": data[3],
                    "date": data[4].strftime("%Y-%m-%d %H:%M:%S"),
                    "msg": data[5],
                    "photo": f"http://localhost:8001/Photos/image{data[6]}.jpg"
                    }
        print(answer)
        return answer 
    # def get_all_info_true(self):

    #     try:
    #         self.cursor.execute("SELECT * from news_data")
    #         records = self.cursor.fetchall()
    #         data = []
    #         for row in records:
    #             answer = {
    #                     "id": row[0],
    #                     "MESSAGE_ID": row[1],
    #                     "url": row[2],
    #                     "CHAT_TITLE": row[3],
    #                     "date": row[4],
    #                     "msg": row[5],
    #                     "photo": f"http://localhost:8001/Photos/image{row[6]}.jpg"
    #                     }
    #             if row[6] == None:
    #                 answer['photo'] = f"http://localhost:8001/Photos/image5253752555547251902.jpg"
    #             data.append(answer)
    #         return data

    #     except (Exception, Error) as error:
    #         print("Ошибка при работе с PostgreSQL", error)
