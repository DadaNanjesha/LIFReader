import networkx as nx
import logging
from typing import Dict, List
from lif_reader.models.node import Node
from lif_reader.models.edge import Edge
from lif_reader.models.station import Station

logger = logging.getLogger(__name__)

class LIFGraph:
    def __init__(self):
        self.graph = nx.DiGraph()
        self.layouts: Dict[str, nx.DiGraph] = {}
        self.stations: Dict[str, Station] = {}

    def clear(self):
        """Clears the graph data, removing all nodes, edges, and layouts."""
        self.graph.clear()
        self.layouts.clear()
        self.stations.clear()
        logger.info("LIFGraph cleared.")

    def add_layout(self, layout_id: str):
        """Adds a new layout (subgraph) to the LIFGraph."""
        self.layouts[layout_id] = nx.DiGraph()
        logger.info(f"Layout '{layout_id}' added.")

    def add_node(self, node: Node, layout_id: str):
        """Adds a node to the specified layout."""
        try:
            self.layouts[layout_id].add_node(node.nodeId, **node.model_dump())
            logger.debug(f"Node '{node.nodeId}' added to layout '{layout_id}'.")
        except Exception as e:
            logger.error(
                f"Error adding node '{node.nodeId}' to layout '{layout_id}': {e}"
            )

    def add_edge(self, edge: Edge, layout_id: str):
        """Adds an edge to the specified layout."""
        try:
            self.layouts[layout_id].add_edge(
                edge.startNodeId, edge.endNodeId, **edge.model_dump()
            )
            logger.debug(f"Edge '{edge.edgeId}' added to layout '{layout_id}'.")
        except Exception as e:
            logger.error(
                f"Error adding edge '{edge.edgeId}' to layout '{layout_id}': {e}"
            )

    def add_station(self, station: Station):
        """Adds a station to the LIFGraph."""
        self.stations[station.stationId] = station
        logger.debug(f"Station '{station.stationId}' added.")

    def get_shortest_path(
        self, start_node: str, end_node: str, layout_id: str
    ) -> List[str]:
        """Calculates the shortest path between two nodes in a layout."""
        try:
            path = nx.shortest_path(self.layouts[layout_id], start_node, end_node)
            logger.debug(
                f"Shortest path from '{start_node}' to '{end_node}' in layout '{layout_id}': {path}"
            )
            return path
        except nx.NetworkXNoPath:
            logger.warning(
                f"No path found from '{start_node}' to '{end_node}' in layout '{layout_id}'."
            )
            return []  # Or raise an exception if appropriate
        except Exception as e:
            logger.error(
                f"Error calculating shortest path from '{start_node}' to '{end_node}' in layout '{layout_id}': {e}"
            )
            return []

    def get_all_paths(
        self, start_node: str, end_node: str, layout_id: str
    ) -> List[List[str]]:
        """Finds all simple paths between two nodes in a layout."""
        try:
            paths = list(
                nx.all_simple_paths(self.layouts[layout_id], start_node, end_node)
            )
            logger.debug(
                f"All paths from '{start_node}' to '{end_node}' in layout '{layout_id}': {paths}"
            )
            return paths
        except nx.NetworkXNoPath:
            logger.warning(
                f"No paths found from '{start_node}' to '{end_node}' in layout '{layout_id}'."
            )
            return []
        except Exception as e:
            logger.error(
                f"Error calculating all paths from '{start_node}' to '{end_node}' in layout '{layout_id}': {e}"
            )
            return []
