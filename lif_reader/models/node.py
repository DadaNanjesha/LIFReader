from dataclasses import dataclass
from typing import Dict, List

@dataclass
class Node:
    node_id: str
    node_name: str
    node_description: str
    map_id: str
    node_position: Dict[str, float]  # {"x": float, "y": float}
    vehicle_type_node_properties: List[Dict]  # List of vehicle-specific properties
    actions: List[Dict]
    node_type: str # property: "parking", "drop", or "station"