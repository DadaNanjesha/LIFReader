from typing import Optional
from pydantic import BaseModel

class MetaInformation(BaseModel):
    projectIdentification: Optional[str] = None
    creator: Optional[str] = None
    exportTimestamp: Optional[str] = None
    lifVersion: Optional[str] = None
