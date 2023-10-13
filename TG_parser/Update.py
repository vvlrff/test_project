import time
from PG_parser import PG_parser
from db_postgres import PG_DB


pg_parser = PG_parser()
database = PG_DB()

while True:
    print('Start...')
    pg_parser.parse_data()
    print('Finish...')
    time.sleep(6000)
