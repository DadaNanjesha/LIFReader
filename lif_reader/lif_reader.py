import json
import logging
from typing import Dict, Any, List
from pydantic import ValidationError
from .models.lif import LIF  # Import the root LIF model
from .graph.lif_graph import LIFGraph  # Import LIFGraph

logger = logging.getLogger(__name__)


class LIFReader:

    def __init__(self, lif_graph):
        self.lif_graph = lif_graph

    def parse_lif_file(self, file_path: str):
        with open(file_path, "r") as file:
            data = json.load(file)

        try:
            lif_data = LIF(**data)  # Validate and parse the entire LIF structure
            self.lif_graph.clear()  # Clear the graph before parsing

            if lif_data.layouts:
                for layout in lif_data.layouts:
                    if layout.layoutId:
                        self.lif_graph.add_layout(layout.layoutId)
                        if layout.nodes:
                            for node in layout.nodes:
                                if node.nodeId:
                                    self.lif_graph.add_node(node, layout.layoutId)
                                else:
                                    logger.warning(
                                        "Node found without nodeId, skipping."
                                    )
                        else:
                            logger.info(f"No nodes found in layout {layout.layoutId}.")

                        if layout.edges:
                            for edge in layout.edges:
                                if edge.edgeId and edge.startNodeId and edge.endNodeId:
                                    self.lif_graph.add_edge(edge, layout.layoutId)
                                else:
                                    logger.warning(
                                        f"Edge found with missing properties, skipping."
                                    )
                        else:
                            logger.info(f"No edges found in layout {layout.layoutId}.")

                        if layout.stations:
                            for station in layout.stations:
                                if station.stationId and station.interactionNodeIds:
                                    self.lif_graph.add_station(station)
                                else:
                                    logger.warning(
                                        f"Station found with missing properties, skipping."
                                    )
                        else:
                            logger.info(
                                f"No stations found in layout {layout.layoutId}."
                            )
                    else:
                        logger.warning("Layout found without layoutId, skipping.")
            else:
                logger.info("No layouts found in LIF data.")

            logger.info(f"Successfully parsed LIF file in LIFReader: {file_path}")

        except ValidationError as e:
            logger.error(f"Error parsing LIF file: {e}")
            raise e  # Re-raise the exception after logging
