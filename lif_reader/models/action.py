from typing import List, Optional
from pydantic import BaseModel
from .action_parameter import ActionParameter
class Action(BaseModel):
    actionType: Optional[str] = None
    actionDescription: Optional[str] = None
    required: Optional[bool] = None
    blockingType: Optional[str] = None
    actionParameters: Optional[List[ActionParameter]] = None  # Forward reference
