from typing import List, Dict, Optional
from pydantic import BaseModel


class Station(BaseModel):
    stationId: str
    interactionNodeIds: List[str]
    stationName: Optional[str] = None
    stationDescription: Optional[str] = None
    stationHeight: Optional[float] = None
    stationPosition: Optional[Dict[str, float]] = None
