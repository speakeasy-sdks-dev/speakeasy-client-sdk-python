"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
from enum import Enum
from speakeasy_client_sdk_python.types import BaseModel
from typing import Optional, TypedDict
from typing_extensions import NotRequired


class DepthStyle(str, Enum):
    ORIGINAL = "original"
    FLAT = "flat"
    NESTED = "nested"
    DEEP = "deep"


class Style(str, Enum):
    STANDARDIZE = "standardize"
    RESOURCE = "resource"


class SuggestOperationIDsOptsTypedDict(TypedDict):
    depth_style: NotRequired[DepthStyle]
    style: NotRequired[Style]
    

class SuggestOperationIDsOpts(BaseModel):
    depth_style: Optional[DepthStyle] = None
    style: Optional[Style] = None
    
