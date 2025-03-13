import matplotlib.pyplot as plt
import networkx as nx

class GraphRenderer:
    def __init__(self, graph):
        """
        Initialize the GraphRenderer with a graph.
        """
        self.graph = graph

    def render(self, node_size: int = 500, node_color: str = "lightblue", with_labels: bool = True):
        """
        Render the graph with different colors for nodes and stations.
        """
        # Get node positions
        pos = nx.get_node_attributes(self.graph, "pos")

        # Define color map for node types
        color_map = {
            "default": "blue",  # Default color for nodes
            "parking": "red",      # Color for parking nodes
            "drop": "yellow",           # Color for drop nodes
            "station": "orange"      # Color for station nodes
        }

        # Assign colors to nodes based on their type
        node_colors = []
        for node in self.graph.nodes:
            node_type = self.graph.nodes[node].get("node_type", "default")  # Get node type, default to "default"
            node_colors.append(color_map.get(node_type, "lightblue"))  # Use color_map or default to lightblue

        # Draw the graph
        nx.draw(
            self.graph,
            pos,
            with_labels=with_labels,
            node_size=node_size,
            node_color=node_colors,
            font_size=8,
            font_color="black",
            font_weight="bold",
            edge_color="gray"
        )

        # Show the graph
        plt.title("LIF Graph Visualization")
        plt.show()