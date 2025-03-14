from typing import Dict, List, Optional
from pydantic import BaseModel

from .vehicle_properties import VehicleTypeNodeProperty


class NodePosition(BaseModel):
    x: float
    y: float
    z: Optional[float] = None


class Node(BaseModel):
    nodeId: str
    nodeName: Optional[str] = None
    nodeDescription: Optional[str] = None
    mapId: Optional[str] = None
    nodePosition: Optional[NodePosition] = None
    vehicleTypeNodeProperties: Optional[List[VehicleTypeNodeProperty]] = None
