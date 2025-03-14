from typing import List, Optional
from pydantic import BaseModel

class LoadRestriction(BaseModel):
    unloaded: Optional[bool] = None
    loaded: Optional[bool] = None
    loadSetNames: Optional[List[str]] = None
