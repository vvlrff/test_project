from pydantic import BaseModel
from datetime import datetime
from typing import Any, Dict, List


class InputUserForGPT(BaseModel):
    message: str
