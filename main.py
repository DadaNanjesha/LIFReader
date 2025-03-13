from lif_reader.json_reader import JSONReader
from lif_reader.models.layout import Layout
from lif_reader.models.node import Node
from lif_reader.models.edge import Edge
from lif_reader.models.station import Station
from lif_reader.graph.lif_graph import LIFGraph
from lif_reader.graph.graph_renderer import GraphRenderer
from lif_reader.utils.config_loader import ConfigLoader
import logging


def setup_logging():
    """Set up logging based on the configuration."""
    config = ConfigLoader()
    log_level = config.get_logging_setting("log_level")
    log_file = config.get_logging_setting("log_file")

    logging.basicConfig(
        level=log_level,
        filename=log_file,
        format="%(asctime)s - %(levelname)s - %(message)s",
    )


def main():
    setup_logging()
    logging.info("Starting LIFReader application...")
    # Load configuration
    config = ConfigLoader()

    # Read the LIF file
    example_file = config.get_file_path("lif_file")
    reader = JSONReader(example_file)
    data = reader.read()

    # Create models from the JSON data
    layouts = []
    for layout_data in data["layouts"]:
        nodes = []
        for node in layout_data["nodes"]:
            # Extract actions from vehicleTypeNodeProperties
            actions = []
            for vehicle_property in node["vehicleTypeNodeProperties"]:
                actions.extend(vehicle_property.get("actions", []))

            # Determine node_type based on the first actionType in actions
            node_type = "default"  # Default value
            if actions:
                node_type = actions[0]["actionType"]  # Use the first action's actionType

            # Create Node object
            node_obj = Node(
                node_id=node["nodeId"],
                node_name=node["nodeName"],
                node_description=node["nodeDescription"],
                map_id=node["mapId"],
                node_position=node["nodePosition"],
                vehicle_type_node_properties=node["vehicleTypeNodeProperties"],
                actions=actions,
                node_type=node_type  # Set node_type to actionType
            )
            nodes.append(node_obj)

        edges = [
            Edge(
                edge_id=edge["edgeId"],
                edge_name=edge["edgeName"],
                edge_description=edge["edgeDescription"],
                start_node_id=edge["startNodeId"],
                end_node_id=edge["endNodeId"],
                vehicle_type_edge_properties=edge["vehicleTypeEdgeProperties"],
            )
            for edge in layout_data["edges"]
        ]
        stations = [
            Station(
                station_id=station["stationId"],
                interaction_node_ids=station["interactionNodeIds"],
                station_name=station["stationName"],
                station_description=station["stationDescription"],
                station_height=station["stationHeight"],
                station_position=station["stationPosition"],
                station_type="station" 
            )
            for station in layout_data["stations"]
        ]
        layout = Layout(
            layout_id=layout_data["layoutId"],
            layout_name=layout_data["layoutName"],
            layout_version=layout_data["layoutVersion"],
            layout_level_id=layout_data["layoutLevelId"],
            layout_description=layout_data["layoutDescription"],
            nodes=nodes,
            edges=edges,
            stations=stations,
        )
        layouts.append(layout)

    # Build and render the graph
    for layout in layouts:
        lif_graph = LIFGraph()
        for node in layout.nodes:
            lif_graph.add_node(node)
        for edge in layout.edges:
            lif_graph.add_edge(edge)
        for station in layout.stations:
            lif_graph.add_station(station)

        # Render the graph
        graph = lif_graph.get_graph()
        renderer = GraphRenderer(graph)
        renderer.render(
            node_size=config.get_graph_setting("node_size"),
            node_color=config.get_graph_setting("node_color"),
            with_labels=config.get_graph_setting("with_labels"),
        )


if __name__ == "__main__":
    main()