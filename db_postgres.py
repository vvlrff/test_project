import psycopg2
from psycopg2 import Error
from psycopg2.extensions import ISOLATION_LEVEL_AUTOCOMMIT

class PG_DB:
    def __init__(self) -> None:
        try:
            self.connection = psycopg2.connect(user="postgres",
                                                password="0013jqfqA",
                                                host="localhost",
                                                port="5432",
                                                dbname="ukraine")
            
            self.connection.set_isolation_level(ISOLATION_LEVEL_AUTOCOMMIT)

            self.cursor = self.connection.cursor()
            self.cursor.execute("""CREATE TABLE IF NOT EXISTS ru
                                    (
                                    tg_data_id serial PRIMARY KEY,
                                    MESSAGE_ID INTEGER,
                                    SENDER TEXT,
                                    CHAT_TITLE TEXT,
                                    DATE INTEGER,
                                    MESSAGE TEXT,
                                    ADV_MESSAGE TEXT
                                    );""")
            
            self.cursor.execute("""CREATE TABLE IF NOT EXISTS ua
                                    (
                                    tg_data_id serial PRIMARY KEY,
                                    MESSAGE_ID INTEGER,
                                    SENDER TEXT,
                                    CHAT_TITLE TEXT,
                                    DATE INTEGER,
                                    MESSAGE TEXT,
                                    ADV_MESSAGE TEXT
                                    );""")
            
            self.cursor.execute("""CREATE TABLE IF NOT EXISTS user_actions
                                    (
                                    EVENT_ID serial PRIMARY KEY,
                                    EVENT_DATA TIMESTAMP DEFAULT NOW(),
                                    USER_ID BIGINT,
                                    USER_NAME TEXT,
                                    ACTION TEXT
                                    );""")
            
            self.cursor.execute("""CREATE TABLE IF NOT EXISTS db_updates
                                    (
                                    UPDATE_ID serial PRIMARY KEY,
                                    UPDATE_DATA TIMESTAMP DEFAULT NOW(),
                                    UPDATE_TEXT TEXT
                                    );""")
            
        except (Exception, Error) as error:
            print("Ошибка при работе с PostgreSQL", error)

    def update_database(self, update_data):
        self.cursor.execute('''INSERT INTO db_updates 
                                (
                                UPDATE_TEXT
                                ) 
                                VALUES(%s);''', [update_data])
        self.connection.commit()

    def insert_into_ru(self, new_line):
        self.cursor.execute('''INSERT INTO ru 
                                (
                                MESSAGE_ID,
                                SENDER,
                                CHAT_TITLE,
                                DATE,
                                MESSAGE,
                                ADV_MESSAGE
                                ) 
                                VALUES(%s, %s, %s, %s, %s, %s);''', new_line)
        self.connection.commit()

    def insert_into_ua(self, new_line):
        self.cursor.execute('''INSERT INTO ua 
                                (
                                MESSAGE_ID,
                                SENDER,
                                CHAT_TITLE,
                                DATE,
                                MESSAGE,
                                ADV_MESSAGE
                                ) 
                                VALUES(%s, %s, %s, %s, %s, %s);''', new_line)
        self.connection.commit()
    
    def last_date_ru(self):
        self.cursor.execute("SELECT MAX(DATE) from ru;")
        last_date = self.cursor.fetchone()
        return last_date[0]
    
    def last_date_ua(self):
        self.cursor.execute("SELECT MAX(DATE) from ua;")
        last_date = self.cursor.fetchone()
        return last_date[0]

    def read_db_ru(self, begin, end):
        result = []

        try:
            self.cursor.execute("SELECT * from ru WHERE DATE BETWEEN %s AND %s", (begin, end))
            records = self.cursor.fetchall()
            for row in records:
                result.append(
                    {
                    "MESSAGE_ID": row[1],
                     "SENDER": row[2],
                     "CHAT_TITLE": row[3],
                     "DATE": row[4],
                     "MESSAGE": row[5],
                     "ADV_MESSAGE": row[6]
                     })
            return result

        except (Exception, Error) as error:
            print("Ошибка при работе с PostgreSQL", error)

    def read_db_ua(self, begin, end):
        result = []

        try:
            self.cursor.execute("SELECT * from ua WHERE DATE BETWEEN %s AND %s", (begin, end))
            records = self.cursor.fetchall()
            for row in records:
                result.append(
                    {
                    "MESSAGE_ID": row[1],
                     "SENDER": row[2],
                     "CHAT_TITLE": row[3],
                     "DATE": row[4],
                     "MESSAGE": row[5],
                     "ADV_MESSAGE": row[6]
                     })
            return result

        except (Exception, Error) as error:
            print("Ошибка при работе с PostgreSQL", error)

# test = PG_DB()
# test.update_database("Database was updated...")
