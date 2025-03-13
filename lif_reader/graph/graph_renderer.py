import networkx as nx
import matplotlib.pyplot as plt


class GraphRenderer:

    def __init__(self, lif_graph):
        self.lif_graph = lif_graph

    def visualize_graph(self):
        """
        Visualizes the LIF graph using matplotlib.
        """
        for layout_id, graph in self.lif_graph.layouts.items():
            plt.figure(figsize=(12, 8))

            # Create a dictionary of node positions
            pos = {}
            for node_id, node_data in graph.nodes(data=True):
                pos[node_id] = (
                    node_data["nodePosition"]["x"],
                    node_data["nodePosition"]["y"],
                )

            # Draw nodes
            nx.draw_networkx_nodes(graph, pos, node_color="skyblue", node_size=1500)

            # Draw edges explicitly with customization
            # can add connectionstyle="arc3,rad=0.2",
            nx.draw_networkx_edges(
                graph,
                pos,
                edge_color="black",
                width=1,
                alpha=0.7,
                style="solid",
            )

            # Draw node labels
            nx.draw_networkx_labels(graph, pos, font_size=10, font_weight="bold")

            plt.title(f"LIF Graph - Layout ID: {layout_id}")
            plt.axis("off")  # Turn off axis labels and ticks
            plt.show()
