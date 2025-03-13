from typing import Optional
from pydantic import BaseModel

class ActionParameter(BaseModel):
    key: Optional[str] = None
    value: Optional[str] = None
