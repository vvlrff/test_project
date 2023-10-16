from pydantic import BaseModel
from datetime import datetime


class InputUser(BaseModel):
    message: str
    start_date: datetime
    end_date: datetime

class PaginateNews(BaseModel):
    id:int
    url:str
    CHAT_TITLE:str
    date:datetime
    msg:str
    photo:str