"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
from speakeasy_client_sdk_python.types import BaseModel
from typing import List
from typing_extensions import TypedDict


class OASOperationTypedDict(TypedDict):
    description: str
    method: str
    operation_id: str
    path: str
    tags: List[str]


class OASOperation(BaseModel):
    description: str

    method: str

    operation_id: str

    path: str

    tags: List[str]
