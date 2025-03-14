from typing import Optional, List
from pydantic import BaseModel

# Define data models for VDA5050 messages
class Header(BaseModel):
    version: str
    manufacturer: str
    serialNumber: str
    timestamp: str
    messageType: str
    messageId: int
    traceId: Optional[str] = None

class State(BaseModel):
    header: Header
    # Add other fields according to VDA 5050

class Visualization(BaseModel):
    header: Header
    # Add other fields according to VDA 5050

class Order(BaseModel):
    header: Header
    # Add other fields according to VDA 5050

class Factsheet(BaseModel):
    header: Header
    # Add other fields according to VDA 5050
