from typing import List, Optional
from pydantic import BaseModel

from .metaInformation import MetaInformation  # Import MetaInformation
from .layout import Layout  # Import Layout

class LIF(BaseModel):
    metaInformation: Optional[MetaInformation] = None
    layouts: Optional[List[Layout]] = None
