from dataclasses import dataclass
from typing import Dict, List, Any

@dataclass
class VehicleTypeNodeProperty:
    vehicle_type_id: str
    theta: float
    actions: List[Dict]  # List of actions

@dataclass
class VehicleTypeEdgeProperty:
    vehicle_type_id: str
    vehicle_orientation: float
    orientation_type: str
    rotation_allowed: bool
    rotation_at_start_node_allowed: str
    rotation_at_end_node_allowed: str
    max_speed: float
    max_rotation_speed: float
    min_height: float
    max_height: float
    load_restriction: Dict[str, Any]  # {"unloaded": bool, "loaded": bool, "loadSetNames": List[str]}
    actions: List[Dict]  # List of actions
    trajectory: Dict[str, Any]  # {"degree": int, "knotVector": List[float], "controlPoints": List[Dict]}
    reentry_allowed: bool