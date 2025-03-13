import json
import logging

logger = logging.getLogger(__name__)


class ConfigLoader:

    def __init__(self, config_path="config.json"):
        self.config_path = config_path
        self.config = self._load_config()

    def _load_config(self):
        """Loads the configuration from the config.json file."""
        try:
            with open(self.config_path, "r") as f:
                config = json.load(f)
            logger.info(f"Configuration loaded from {self.config_path}")
            return config
        except FileNotFoundError:
            logger.error(f"Configuration file not found at {self.config_path}")
            raise
        except json.JSONDecodeError:
            logger.error(f"Error decoding JSON from {self.config_path}")
            raise
        except Exception as e:
            logger.error(f"Error loading configuration: {e}")
            raise

    def get_file_path(self, key):
        """Gets a file path from the configuration."""
        try:
            return self.config["file_paths"][key]
        except KeyError:
            logger.warning(f"File path not found for key: {key}")
            return None

    def get_graph_setting(self, key):
        """Gets a graph setting from the configuration."""
        try:
            return self.config["graph_settings"][key]
        except KeyError:
            logger.warning(f"Graph setting not found for key: {key}")
            return None

    def get_logging_setting(self, key):
        """Gets a logging setting from the configuration."""
        try:
            return self.config["logging"][key]
        except KeyError:
            logger.warning(f"Logging setting not found for key: {key}")
            return None
