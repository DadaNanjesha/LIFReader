from typing import Dict, List, Any
from pathlib import Path
import json

def validate_json_file(file_path: Path) -> bool:
    """Validate that a file exists and is a valid JSON file."""
    if not file_path.exists():
        return False
    try:
        with open(file_path, "r") as f:
            json.load(f)
        return True
    except json.JSONDecodeError:
        return False

def find_duplicates(items: List[Any]) -> List[Any]:
    """Find duplicate items in a list."""
    seen = set()
    duplicates = set()
    for item in items:
        if item in seen:
            duplicates.add(item)
        else:
            seen.add(item)
    return list(duplicates)

def calculate_distance(node1: Dict[str, float], node2: Dict[str, float]) -> float:
    """Calculate the Euclidean distance between two nodes."""
    return ((node1["x"] - node2["x"]) ** 2 + (node1["y"] - node2["y"]) ** 2) ** 0.5

def load_json(file_path: Path) -> Dict:
    """Load a JSON file and return its contents as a dictionary."""
    if not file_path.exists():
        raise FileNotFoundError(f"File not found: {file_path}")
    with open(file_path, "r") as f:
        return json.load(f)

def save_json(data: Dict, file_path: Path):
    """Save a dictionary as a JSON file."""
    try:
        with open(file_path, "w") as f:
            json.dump(data, f, indent=4)
    except IOError as e:
        raise IOError(f"Failed to save JSON file: {e}")