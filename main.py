import asyncio
import logging

from lif_reader.lif_reader import LIFReader
from lif_reader.graph.graph_renderer import GraphRenderer
from lif_reader.graph.lif_graph import LIFGraph  # Import LIFGraph
from lif_reader.vda5050.communication import VDA5050Communicator
from lif_reader.vda5050.message_handler import handle_vda5050_message
from lif_reader.utils.config_loader import ConfigLoader  # Import ConfigLoader


logger = logging.getLogger(__name__)


async def main():
    # Load configuration
    config_loader = ConfigLoader()

    # Set up logging based on config
    log_level = config_loader.get_logging_setting("log_level")
    log_file = config_loader.get_logging_setting("log_file")

    numeric_level = getattr(logging, log_level.upper(), None)
    if not isinstance(numeric_level, int):
        raise ValueError("Invalid log level: %s" % log_level)

    logging.basicConfig(
        level=numeric_level,
        format="%(asctime)s - %(levelname)s - %(message)s",
        filename=log_file,  # Use log_file from config
    )

    # Get settings from config
    lif_file_path = config_loader.get_file_path("lif_file")
    visualize = config_loader.get_command_line_arg("visualize")
    vda5050 = config_loader.get_command_line_arg("vda5050")
    vda5050_server = config_loader.get_command_line_arg("vda5050_server")

    lif_graph = LIFGraph()  # Initialize LIFGraph

    if lif_file_path:
        try:
            # Parse LIF file
            lif_reader = LIFReader(lif_graph)  # Pass lif_graph here
            lif_reader.parse_lif_file(lif_file_path)
            logger.info(f"Successfully parsed LIF file: {lif_file_path}")

            # Visualize the graph
            if visualize:
                graph_renderer = GraphRenderer(
                    lif_graph, config_loader
                )  # Pass config_loader
                graph_renderer.visualize_graph()
                logger.info("Graph visualization completed.")

        except FileNotFoundError as e:
            logger.error(f"Error: LIF file not found: {e}")
        except Exception as e:
            logger.error(f"Error processing LIF file: {e}")

    if vda5050:
        # Run VDA5050 communication
        communicator = VDA5050Communicator(vda5050_server)
        try:
            logger.info(f"Starting VDA5050 communication with {vda5050_server}")
            await communicator.run(handle_vda5050_message)
        except Exception as e:
            logger.error(f"VDA5050 communication error: {e}")
        finally:
            await communicator.disconnect()

    if not any([lif_file_path, vda5050]):
        logger.warning("No action specified. Set lif_file or vda5050 in config.json.")


if __name__ == "__main__":
    asyncio.run(main())
