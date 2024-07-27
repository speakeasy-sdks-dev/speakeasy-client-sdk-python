"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
from .oasinfo import OASInfo, OASInfoTypedDict
from .oasoperation import OASOperation, OASOperationTypedDict
from speakeasy_client_sdk_python.types import BaseModel
from typing import List, TypedDict


class OASSummaryTypedDict(TypedDict):
    info: OASInfoTypedDict
    operations: List[OASOperationTypedDict]
    

class OASSummary(BaseModel):
    info: OASInfo
    operations: List[OASOperation]
    
