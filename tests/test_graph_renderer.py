import networkx as nx
from lif_reader.graph.graph_renderer import GraphRenderer

def test_graph_renderer():
    graph = nx.Graph()
    graph.add_node("N1", pos=(0.0, 0.0))
    graph.add_node("N2", pos=(1.0, 1.0))
    graph.add_edge("N1", "N2")

    renderer = GraphRenderer(graph)
    # This test just ensures the renderer runs without errors
    renderer.render()