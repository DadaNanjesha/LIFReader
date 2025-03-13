from typing import Dict, List, Optional
from pydantic import BaseModel

from .vehicle_properties import VehicleTypeNodeProperty


class Node(BaseModel):
    nodeId: str
    nodeName: Optional[str] = None
    nodeDescription: Optional[str] = None
    mapId: Optional[str] = None
    nodePosition: Optional[Dict[str, float]] = None  # {"x": number, "y": number}
    vehicleTypeNodeProperties: Optional[List[VehicleTypeNodeProperty]] = None
