"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
from speakeasy_client_sdk_python.types import BaseModel
from typing import Optional, TypedDict
from typing_extensions import NotRequired


class RequestMetadataTypedDict(TypedDict):
    r"""Key-Value pairs associated with a request"""
    
    key: NotRequired[str]
    value: NotRequired[str]
    

class RequestMetadata(BaseModel):
    r"""Key-Value pairs associated with a request"""
    
    key: Optional[str] = None
    value: Optional[str] = None
    
