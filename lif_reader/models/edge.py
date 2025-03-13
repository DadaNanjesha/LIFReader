from typing import List, Optional
from pydantic import BaseModel, Field
from .vehicle_properties import VehicleTypeEdgeProperty


class Edge(BaseModel):
    edgeId: str
    edgeName: Optional[str] = None
    edgeDescription: Optional[str] = None
    startNodeId: str
    endNodeId: str
    vehicleTypeEdgeProperties: Optional[List[VehicleTypeEdgeProperty]] = None
