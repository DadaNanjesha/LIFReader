from lif_reader.models.node import Node
from lif_reader.models.edge import Edge
from lif_reader.graph.lif_graph import LIFGraph

def test_lif_graph_add_node():
    lif_graph = LIFGraph()
    node = Node(
        node_id="N1",
        node_name="Node 1",
        node_description="Test Node",
        map_id="Map1",
        node_position={"x": 0.0, "y": 0.0},
        vehicle_type_node_properties=[]
    )
    lif_graph.add_node(node)
    assert "N1" in lif_graph.get_graph().nodes

def test_lif_graph_add_edge():
    lif_graph = LIFGraph()
    node1 = Node(
        node_id="N1",
        node_name="Node 1",
        node_description="Test Node",
        map_id="Map1",
        node_position={"x": 0.0, "y": 0.0},
        vehicle_type_node_properties=[]
    )
    node2 = Node(
        node_id="N2",
        node_name="Node 2",
        node_description="Test Node",
        map_id="Map1",
        node_position={"x": 1.0, "y": 1.0},
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
    lif_graph.add_node(node1)
    lif_graph.add_node(node2)
    lif_graph.add_edge(edge)
    assert ("N1", "N2") in lif_graph.get_graph().edges