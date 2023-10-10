from pydantic import BaseModel
from datetime import datetime
from typing import Any, Dict, List


class InputUser(BaseModel):
    message: str
    start_date: datetime
    end_date: datetime