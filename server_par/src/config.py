from dotenv import load_dotenv
import os 

load_dotenv()

DB_HOST = os.environ.get('DB_HOST')
DB_PORT = os.environ.get('DB_PORT')
DB_NAME = os.environ.get('DB_NAME')
DB_USER = os.environ.get('DB_USER')
DB_PASS = os.environ.get('DB_PASS')
SECRET = os.environ.get('SECRET')
TG_NAME = os.environ.get('TG_NAME')
TG_API_ID = os.environ.get('TG_API_ID')
TG_API_HASH = os.environ.get('TG_API_HASH')
ELASTIC_URL =  os.environ.get('ELASTICSEARCH_HOSTS')