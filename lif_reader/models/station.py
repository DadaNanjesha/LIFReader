from dataclasses import dataclass
from typing import List, Dict

@dataclass
class Station:
    station_id: str
    station_name: str
    interaction_node_ids: List[str]
    station_description: str
    station_height: float
    station_position: Dict[str, float]  # {"x": float, "y": float, "theta": float}
    station_type: str = "default"  # property: "parking", "drop", or "station"