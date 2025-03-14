import pytest
from lif_reader.graph.lif_graph import LIFGraph
from lif_reader.models.node import Node
from lif_reader.models.edge import Edge
from lif_reader.models.metaInformation import MetaInformation
from lif_reader.models.layout import Layout

def test_lif_graph_add_node():
    lif_graph = LIFGraph()
    lif_graph.add_layout("1")  # Add layout with ID "1"

    node = Node(nodeId="N1")
    lif_graph.add_node(node, layout_id="1")
    assert "N1" in lif_graph.layouts["1"].nodes()


def test_lif_graph_add_edge():
    lif_graph = LIFGraph()
    lif_graph.add_layout("Layout1")  # Add layout with ID "Layout1"

    # Providing the fields to pass the validation check of Edge model
    edge = Edge(edgeId="E1", edgeName="Edge 1", startNodeId="N1", endNodeId="N2")
    lif_graph.add_edge(edge, layout_id="Layout1")
    assert ("N1", "N2") in lif_graph.layouts["Layout1"].edges()
