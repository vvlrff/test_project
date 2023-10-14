from pydantic import BaseModel
from datetime import datetime


class InputUser(BaseModel):
    message: str
    start_date: datetime
    end_date: datetime

class InputUserMessage(BaseModel):
    message: str