import json
from pathlib import Path
from lif_reader.utils.exceptions import InvalidLIFFileError

class JSONReader:
    def __init__(self, file_path):
        self.file_path = Path(file_path)

    def read(self):
        if not self.file_path.exists():
            raise FileNotFoundError(f"File not found: {self.file_path}")

        with open(self.file_path, "r") as f:
            try:
                data = json.load(f)
                self._validate(data)
                return data
            except json.JSONDecodeError:
                raise InvalidLIFFileError("Invalid JSON format")

    def _validate(self, data):
        if "metaInformation" not in data or "layouts" not in data:
            raise InvalidLIFFileError("Missing required fields in LIF file")