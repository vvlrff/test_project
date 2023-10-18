from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import  desc, insert,  select
from .models import news_data
import datetime




class PG_DB:

    def __init__(self, coonection):
        self.connect: AsyncSession = coonection

    async def last_date_ru(self):
        stmt = select(news_data.c.date).order_by((news_data.c.date.desc()))
        res = await self.connect.execute(stmt)
        data = res.fetchone()

        if data == None:
            return (datetime.datetime.now() - datetime.timedelta(days=30)).timestamp() #seconds=0 days=1
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
