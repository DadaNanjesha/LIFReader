import json
from pathlib import Path
from typing import Dict, Any

class ConfigLoader:
    def __init__(self, config_file: str = "config.json"):
        self.config_file = Path(config_file)
        self.config = self._load_config()

    def _load_config(self) -> Dict[str, Any]:
        """Load the configuration from the JSON file."""
        if not self.config_file.exists():
            raise FileNotFoundError(f"Configuration file not found: {self.config_file}")

        with open(self.config_file, "r") as f:
            return json.load(f)

    def get_file_path(self, key: str) -> str:
        """Get a file path from the configuration."""
        return self.config["file_paths"].get(key)

    def get_graph_setting(self, key: str) -> Any:
        """Get a graph setting from the configuration."""
        return self.config["graph_settings"].get(key)

    def get_logging_setting(self, key: str) -> Any:
        """Get a logging setting from the configuration."""
        return self.config["logging"].get(key)