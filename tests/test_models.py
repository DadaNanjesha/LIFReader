import pytest
from lif_reader.models.node import Node
from lif_reader.models.edge import Edge
from lif_reader.models.station import Station
from lif_reader.models.layout import Layout


def test_node_creation():
    node = Node(nodeId="N1", nodeName="Node 1")  # Updated to use 'nodeName'
    assert node.nodeId == "N1"
    assert node.nodeName == "Node 1"


def test_edge_creation():
    edge = Edge(
        edgeId="E1", edgeName="Edge 1", startNodeId="N1", endNodeId="N2"
    )  # Updated to use 'edgeName'
    assert edge.edgeId == "E1"
    assert edge.edgeName == "Edge 1"
    assert edge.startNodeId == "N1"
    assert edge.endNodeId == "N2"


def test_station_creation():
    station = Station(
        stationId="S1",
        stationName="Station 1",
        interactionNodeIds=[],
    )
    assert station.stationId == "S1"
    assert station.stationName == "Station 1"
    assert station.interactionNodeIds == []


def test_layout_creation():
    # Creating a layout requires at least an ID
    layout = Layout(layoutId="Layout1")  # Updated to include 'layoutId'
    assert layout.layoutId == "Layout1"
