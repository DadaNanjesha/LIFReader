async def handle_vda5050_message(message: dict):
    """
    Handles VDA 5050 messages based on their message type.
    """
    message_type = message.get("header", {}).get("messageType")

    if message_type == "State":
        await handle_state_message(message)
    elif message_type == "Visualization":
        await handle_visualization_message(message)
    elif message_type == "Order":
        await handle_order_message(message)
    elif message_type == "Factsheet":
        await handle_factsheet_message(message)
    else:
        print(f"Received unknown message type: {message_type}")

async def handle_state_message(state_message: dict):
    """
    Handles VDA 5050 State messages.
    """
    # Process the state message
    print("Handling State message:", state_message)
    # Extract relevant information from the state message
    # e.g., vehicle state, localization, etc.

async def handle_visualization_message(visualization_message: dict):
    """
    Handles VDA 5050 Visualization messages.
    """
    # Process the visualization message
    print("Handling Visualization message:", visualization_message)
    # Extract relevant information for visualization purposes

async def handle_order_message(order_message: dict):
    """
    Handles VDA 5050 Order messages.
    """
    # Process the order message
    print("Handling Order message:", order_message)
    # Extract order details and manage the order execution

async def handle_factsheet_message(factsheet_message: dict):
    """
    Handles VDA 5050 Factsheet messages.
    """
    # Process the factsheet message
    print("Handling Factsheet message:", factsheet_message)
    # Extract vehicle factsheet information

# Additional handler functions for other message types
