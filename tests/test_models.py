from lif_reader.models.node import Node
from lif_reader.models.edge import Edge
from lif_reader.models.station import Station
from lif_reader.models.layout import Layout

def test_node_creation():
    node = Node(
        node_id="N1",
        node_name="Node 1",
        node_description="Test Node",
        map_id="Map1",
        node_position={"x": 0.0, "y": 0.0},
        vehicle_type_node_properties=[]
    )
    assert node.node_id == "N1"
    assert node.node_name == "Node 1"
    assert node.node_position == {"x": 0.0, "y": 0.0}

def test_edge_creation():
    edge = Edge(
        edge_id="E1",
        edge_name="Edge 1",
        edge_description="Test Edge",
        start_node_id="N1",
        end_node_id="N2",
        vehicle_type_edge_properties=[]
    )
    assert edge.edge_id == "E1"
    assert edge.start_node_id == "N1"
    assert edge.end_node_id == "N2"

def test_station_creation():
    station = Station(
        station_id="S1",
        interaction_node_ids=["N1"],
        station_name="Station 1",
        station_description="Test Station",
        station_height=1.0,
        station_position={"x": 0.0, "y": 0.0, "theta": 0.0}
    )
    assert station.station_id == "S1"
    assert station.interaction_node_ids == ["N1"]
    assert station.station_height == 1.0

def test_layout_creation():
    node = Node(
        node_id="N1",
        node_name="Node 1",
        node_description="Test Node",
        map_id="Map1",
        node_position={"x": 0.0, "y": 0.0},
        vehicle_type_node_properties=[]
    )
    edge = Edge(
        edge_id="E1",
        edge_name="Edge 1",
        edge_description="Test Edge",
        start_node_id="N1",
        end_node_id="N2",
        vehicle_type_edge_properties=[]
    )
    station = Station(
        station_id="S1",
        interaction_node_ids=["N1"],
        station_name="Station 1",
        station_description="Test Station",
        station_height=1.0,
        station_position={"x": 0.0, "y": 0.0, "theta": 0.0}
    )
    layout = Layout(
        layout_id="L1",
        layout_name="Layout 1",
        layout_version="1.0",
        layout_level_id="Level1",
        layout_description="Test Layout",
        nodes=[node],
        edges=[edge],
        stations=[station]
    )
    assert layout.layout_id == "L1"
    assert len(layout.nodes) == 1
    assert len(layout.edges) == 1
    assert len(layout.stations) == 1