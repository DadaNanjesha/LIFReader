import networkx as nx
import matplotlib.pyplot as plt
import logging

logger = logging.getLogger(__name__)


class GraphRenderer:

    def __init__(self, lif_graph, config_loader):
        self.lif_graph = lif_graph
        self.config_loader = config_loader

    def visualize_graph(self):
        """
        Visualizes the LIF graph using matplotlib, loading settings from config.
        """
        for layout_id, graph in self.lif_graph.layouts.items():
            logger.info(f"Visualizing graph for layout: {layout_id}")
            plt.figure(figsize=(12, 8))

            # Load graph settings from config
            node_size = self.config_loader.get_graph_setting("node_size") or 300
            node_color = self.config_loader.get_graph_setting("node_color") or "skyblue"
            with_labels = self.config_loader.get_graph_setting("with_labels") or True

            edge_color = self.config_loader.get_graph_setting("edge_color") or "gray"
            edge_width = self.config_loader.get_graph_setting("edge_width") or 1.0
            edge_alpha = self.config_loader.get_graph_setting("edge_alpha") or 0.7
            edge_style = self.config_loader.get_graph_setting("edge_style") or "solid"
            edge_connectionstyle = (
                self.config_loader.get_graph_setting("edge_connectionstyle") or "-"
            )

            # Create a dictionary of node positions
            pos = {}
            for node_id, node_data in graph.nodes(data=True):
                if node_data.get("nodePosition"):  # Check if nodePosition exists
                    x = node_data["nodePosition"].get(
                        "x", 0
                    )  # Get x coordinate, default to 0
                    y = node_data["nodePosition"].get(
                        "y", 0
                    )  # Get y coordinate, default to 0
                    pos[node_id] = (x, y)
                else:
                    logger.warning(
                        f"Node {node_id} has no position data.  Using (0, 0)."
                    )
                    pos[node_id] = (0, 0)  # Default position if nodePosition is missing

            # Draw nodes
            nx.draw_networkx_nodes(
                graph, pos, node_color=node_color, node_size=node_size
            )

            # Draw edges explicitly with customization
            nx.draw_networkx_edges(
                graph,
                pos,
                edge_color=edge_color,
                width=edge_width,
                alpha=edge_alpha,
                style=edge_style,
                connectionstyle=edge_connectionstyle,
            )

            # Draw node labels
            nx.draw_networkx_labels(
                graph, pos, font_size=10, font_weight="bold", font_color="black"
            )

            plt.title(f"LIF Graph - Layout ID: {layout_id}")
            plt.axis("off")  # Turn off axis labels and ticks
            output_path = self.config_loader.get_file_path(
                "output_graph"
            )  # Get output path
            if output_path:
                plt.savefig(output_path)  # Save the figure to a file
                logger.info(f"Graph saved to {output_path}")
            plt.show()
