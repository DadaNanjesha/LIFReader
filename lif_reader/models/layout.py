from typing import List, Optional
from pydantic import BaseModel

from .node import Node  # Import Node
from .edge import Edge  # Import Edge
from .station import Station  # Import Station


class Layout(BaseModel):
    layoutId: str
    layoutName: Optional[str] = None
    layoutVersion: Optional[str] = None
    layoutLevelId: Optional[str] = None
    layoutDescription: Optional[str] = None
    nodes: Optional[List[Node]] = None
    edges: Optional[List[Edge]] = None
    stations: Optional[List[Station]] = None
