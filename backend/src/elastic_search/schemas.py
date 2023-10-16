from pydantic import BaseModel
from datetime import datetime


class InputUser(BaseModel):
    message: str
    start_date: datetime
    end_date: datetime

class InputUserMessage(BaseModel):
    message: str


class PaginateNewsElastic(BaseModel):
    id:int
    date:datetime
    relevant_score:float
    msg:str
    url:str
    photo:str