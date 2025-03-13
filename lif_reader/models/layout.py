from dataclasses import dataclass
from typing import List
from .node import Node
from .edge import Edge
from .station import Station

@dataclass
class Layout:
    layout_id: str
    layout_name: str
    layout_version: str
    layout_level_id: str
    layout_description: str
    nodes: List[Node]
    edges: List[Edge]
    stations: List[Station]