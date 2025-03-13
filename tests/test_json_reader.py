import pytest
import json
from lif_reader.json_reader import JSONReader
from lif_reader.utils.exceptions import InvalidLIFFileError

def test_read_valid_json(tmp_path):
    # Create a valid JSON file
    json_data = {
        "metaInformation": {
            "projectIdentification": "TestProject",
            "creator": "TestCreator",
            "exportTimestamp": "2023-10-01T00:00:00Z",
            "lifVersion": "1.0.0"
        },
        "layouts": []
    }
    file_path = tmp_path / "test.lif"
    with open(file_path, "w") as f:
        json.dump(json_data, f)

    # Test reading the file
    reader = JSONReader(file_path)
    data = reader.read()
    assert data == json_data

def test_read_invalid_json(tmp_path):
    # Create an invalid JSON file
    file_path = tmp_path / "test.lif"
    with open(file_path, "w") as f:
        f.write("invalid json")

    # Test reading the file
    reader = JSONReader(file_path)
    with pytest.raises(InvalidLIFFileError):
        reader.read()

def test_read_missing_file():
    # Test reading a non-existent file
    reader = JSONReader("nonexistent.lif")
    with pytest.raises(FileNotFoundError):
        reader.read()