import datetime
import psycopg2
from psycopg2 import Error
from psycopg2.extensions import ISOLATION_LEVEL_AUTOCOMMIT
# 
class PG_DB:
    def __init__(self) -> None:
        try:
            self.connection = psycopg2.connect(user="postgres",
                                                password="4150",
                                                host="localhost",
                                                port="5432",
                                                dbname="AI_News")
            
            self.connection.set_isolation_level(ISOLATION_LEVEL_AUTOCOMMIT)

            self.cursor = self.connection.cursor()
            self.cursor.execute("""CREATE TABLE IF NOT EXISTS news_data
                                    (
                                    tg_data_id serial PRIMARY KEY,
                                    MESSAGE_ID INTEGER,
                                    SENDER TEXT,
                                    CHAT_TITLE TEXT,
                                    DATE timestamp,
                                    MESSAGE TEXT,
                                    PHOTO_ID bigint
                                    );""")
            
        except (Exception, Error) as error:
            print("Ошибка при работе с PostgreSQL", error)

    def last_date_ru(self):
        self.cursor.execute(
            "SELECT  news_data.date FROM news_data ORDER BY date DESC"
        )
        if self.cursor.fetchone() == None:
            return (datetime.datetime.now() - datetime.timedelta(seconds=3600)).timestamp() #seconds=0 days=1
        else:
            return self.cursor.fetchone()[0].timestamp()
        # return self.cursor.fetchone()
        
        ...

    def insert_into_db(self, new_line):
        self.cursor.execute('''INSERT INTO news_data 
                                (
                                MESSAGE_ID,
                                SENDER,
                                CHAT_TITLE,
                                DATE,
                                MESSAGE,
                                PHOTO_ID
                                )
                                VALUES(%s, %s, %s, %s, %s, %s);''', new_line)
        self.connection.commit()


    def get_last_id(self):
        self.cursor.execute('''SELECT tg_data_id FROM news_data ORDER BY tg_data_id DESC LIMIT 1;''')
        last_id = self.cursor.fetchone()
        return last_id[0]
    
    def last_date(self):
        self.cursor.execute("SELECT MAX(DATE) from news_data;")
        last_date = self.cursor.fetchone()
        return last_date[0]
    
    def is_post_in_time_range(self, id):
        self.cursor.execute("SELECT DATE from news_data WHERE tg_data_id = %s;", (id,))
        current_date = self.cursor.fetchone()
        return current_date[0]

    def get_all_info(self, id):

        try:
            self.cursor.execute("SELECT * from news_data WHERE tg_data_id = %s;", (id,))
            records = self.cursor.fetchone()
            answer = {
                    "TG_DATA_ID": records[0],
                    "MESSAGE_ID": records[1],
                    "SENDER": records[2],
                    "CHAT_TITLE": records[3],
                    "DATE": records[4],
                    "MESSAGE": records[5],
                    "PHOTO_ID": records[6]
                    }
            return answer

        except (Exception, Error) as error:
            print("Ошибка при работе с PostgreSQL", error)

# test = PG_DB()
# print(test.get_last_id())