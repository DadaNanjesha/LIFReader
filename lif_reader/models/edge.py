from dataclasses import dataclass
from typing import Dict, List

@dataclass
class Edge:
    edge_id: str
    edge_name: str
    edge_description: str
    start_node_id: str
    end_node_id: str
    vehicle_type_edge_properties: List[Dict]  # List of vehicle-specific properties