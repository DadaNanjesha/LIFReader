import asyncio
import websockets
import json
from typing import Callable, Coroutine, Any

class VDA5050Communicator:
    def __init__(self, server_address: str):
        self.server_address = server_address
        self.message_queue: asyncio.Queue = asyncio.Queue()
        self.websocket = None

    async def connect(self):
        """
        Establishes a WebSocket connection to the server.
        """
        try:
            self.websocket = await websockets.connect(self.server_address)
            print(f"Connected to {self.server_address}")
            return True
        except Exception as e:
            print(f"Connection failed: {e}")
            return False

    async def disconnect(self):
        """
        Closes the WebSocket connection.
        """
        if self.websocket:
            await self.websocket.close()
            print("Disconnected from server.")

    async def send_message(self, message: dict):
        """
        Sends a message to the server.
        """
        if self.websocket and not self.websocket.closed:
            try:
                message_json = json.dumps(message)
                await self.websocket.send(message_json)
                print(f"Sent: {message_json}")
            except Exception as e:
                print(f"Error sending message: {e}")

    async def receive_messages(self, handler: Callable[[dict], Coroutine[Any, Any, None]]):
        """
        Listens for incoming messages from the server and passes them to the handler.
        """
        if not self.websocket:
            print("WebSocket not connected.")
            return

        try:
            while True:
                try:
                    message_json = await self.websocket.recv()
                    message = json.loads(message_json)
                    print(f"Received: {message_json}")
                    await handler(message)
                except websockets.exceptions.ConnectionClosed:
                    print("Connection was closed.")
                    break
                except Exception as e:
                    print(f"Error receiving message: {e}")
                    break
        finally:
            await self.disconnect()

    async def enqueue_message(self, message: dict):
        """
        Enqueues a message to be sent.
        """
        await self.message_queue.put(message)

    async def process_queue(self):
        """
        Processes messages from the queue and sends them to the server.
        """
        while True:
            message = await self.message_queue.get()
            await self.send_message(message)
            self.message_queue.task_done()

    async def run(self, handler: Callable[[dict], Coroutine[Any, Any, None]]):
        """
        Runs the communication process, connecting to the server,
        receiving messages, and processing the message queue.
        """
        if not await self.connect():
            print("Failed to connect, cannot run.")
            return

        receive_task = asyncio.create_task(self.receive_messages(handler))
        queue_task = asyncio.create_task(self.process_queue())

        await asyncio.gather(receive_task, queue_task)
