"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
from speakeasy_client_sdk_python.types import BaseModel
from typing import TypedDict


class PreflightRequestTypedDict(TypedDict):
    namespace_name: str
    

class PreflightRequest(BaseModel):
    namespace_name: str
    