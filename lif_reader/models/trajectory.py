from typing import List, Optional
from pydantic import BaseModel

class ControlPoint(BaseModel):
    x: Optional[float] = None
    y: Optional[float] = None
    weight: Optional[float] = None

class Trajectory(BaseModel):
    degree: Optional[float] = None  # Changed to float
    knotVector: Optional[List[float]] = None
    controlPoints: Optional[List[ControlPoint]] = None
