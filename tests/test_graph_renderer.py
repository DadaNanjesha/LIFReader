import pytest
from lif_reader.graph.graph_renderer import GraphRenderer
from lif_reader.graph.lif_graph import LIFGraph
from lif_reader.utils.config_loader import ConfigLoader

def test_graph_renderer():
    lif_graph = LIFGraph()
    config_loader = ConfigLoader()  # Create a ConfigLoader instance
    renderer = GraphRenderer(lif_graph, config_loader)  # Pass config_loader instance
    # This is a basic test. Add more assertions to validate the visualization.
    try:
        renderer.visualize_graph()
        assert True  # If visualization runs without error, consider the test passed
    except Exception as e:
        assert False, f"Visualization failed: {e}"
