from typing import List, Optional
from pydantic import BaseModel
from .load_restriction import LoadRestriction
from .action import Action  # Import Action
from .trajectory import Trajectory  # Import Trajectory


class VehicleTypeNodeProperty(BaseModel):
    vehicleTypeId: Optional[str] = None
    theta: Optional[float] = None
    actions: Optional[List[Action]] = None


class VehicleTypeEdgeProperty(BaseModel):
    vehicleTypeId: Optional[str] = None
    vehicleOrientation: Optional[float] = None
    orientationType: Optional[str] = None
    rotationAllowed: Optional[bool] = None
    rotationAtStartNodeAllowed: Optional[str] = (
        None  # boolean or string?  LIF is inconsistent
    )
    rotationAtEndNodeAllowed: Optional[str] = (
        None  # boolean or string?  LIF is inconsistent
    )
    maxSpeed: Optional[float] = None
    maxRotationSpeed: Optional[float] = None
    minHeight: Optional[float] = None
    maxHeight: Optional[float] = None
    loadRestriction: Optional[LoadRestriction] = None
    actions: Optional[List[Action]] = None
    trajectory: Optional[Trajectory] = None
    reentryAllowed: Optional[bool] = None
