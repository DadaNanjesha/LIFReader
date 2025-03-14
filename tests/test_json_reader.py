import pytest
from lif_reader.lif_reader import LIFReader
from lif_reader.graph.lif_graph import LIFGraph
from lif_reader.models.lif import LIF  # Import the LIF model
import json


def test_read_valid_json():
    lif_graph = LIFGraph()
    reader = LIFReader(lif_graph)
    file_path = "files/example2.json"  # Ensure this path is correct for testing
    try:
        reader.parse_lif_file(file_path)  # Call the parse_lif_file method
        assert True  # If parsing succeeds, the test passes
    except Exception as e:
        assert False, f"Parsing failed: {e}"


def test_read_invalid_json():
    lif_graph = LIFGraph()
    reader = LIFReader(lif_graph)
    file_path = "files/invalid.json"
    with pytest.raises(Exception):
        reader.parse_lif_file(file_path)


def test_read_missing_file():
    lif_graph = LIFGraph()
    reader = LIFReader(lif_graph)
    file_path = "missing.json"
    with pytest.raises(FileNotFoundError):
        reader.parse_lif_file(file_path)
