import argparse
import asyncio
import logging

from lif_reader.lif_reader import LIFReader
from lif_reader.graph.graph_renderer import GraphRenderer
from lif_reader.graph.lif_graph import LIFGraph  # Import LIFGraph
from lif_reader.vda5050.communication import VDA5050Communicator
from lif_reader.vda5050.message_handler import handle_vda5050_message
from lif_reader.utils.config_loader import ConfigLoader  # Import ConfigLoader

# Configure logging
logging.basicConfig(
    level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s"
)
logger = logging.getLogger(__name__)

async def main():
    """
    Main function to parse command-line arguments and execute the
    corresponding actions.
    """
    parser = argparse.ArgumentParser(
        description="LIFReader: Parse LIF files, visualize graphs, and communicate via VDA5050."
    )
    parser.add_argument("--lif", type=str, help="Path to the LIF JSON file to parse.")
    parser.add_argument(
        "--visualize",
        action="store_true",
        help="Visualize the parsed LIF graph using matplotlib.",
    )
    parser.add_argument(
        "--vda5050",
        action="store_true",
        help="Enable VDA5050 communication with a central server.",
    )
    parser.add_argument(
        "--vda5050_server",
        type=str,
        default="ws://localhost:8080",
        help="Address of the VDA5050 server.",
    )

    args = parser.parse_args()

    # Load configuration
    config_loader = ConfigLoader()
    lif_graph = LIFGraph()  # Initialize LIFGraph
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
    # Set lif file path
    lif_file_path = config_loader.get_file_path("lif_file")

    if args.lif or lif_file_path:
        try:
            # Parse LIF file
            json_reader = LIFReader(lif_graph)  # Pass lif_graph here
            json_reader.parse_lif_file(args.lif or lif_file_path)
            logger.info(f"Successfully parsed LIF file: {args.lif or lif_file_path}")

            # Visualize the graph
            if args.visualize:
                graph_renderer = GraphRenderer(
                    lif_graph, config_loader
                )  # Pass config_loader
                graph_renderer.visualize_graph()
                logger.info("Graph visualization completed.")

        except FileNotFoundError as e:
            logger.error(f"Error: LIF file not found: {e}")
        except Exception as e:
            logger.error(f"Error processing LIF file: {e}")

    if args.vda5050:
        # Run VDA5050 communication
        communicator = VDA5050Communicator(args.vda5050_server)
        try:
            logger.info(f"Starting VDA5050 communication with {args.vda5050_server}")
            await communicator.run(handle_vda5050_message)
        except Exception as e:
            logger.error(f"VDA5050 communication error: {e}")
        finally:
            await communicator.disconnect()

    if not any([args.lif, args.vda5050, lif_file_path]):
        logger.warning("No action specified. Use --lif, --visualize, or --vda5050.")

if __name__ == "__main__":
    asyncio.run(main())
