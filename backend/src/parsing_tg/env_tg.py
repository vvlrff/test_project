from dotenv import load_dotenv
import os 

load_dotenv()
TG_NAME = os.environ.get('TG_NAME')
TG_API_ID = os.environ.get('TG_API_ID')
TG_API_HASH = os.environ.get('TG_API_HASH')