"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
from speakeasy_client_sdk_python.types import BaseModel
from typing import TypedDict


class VersionMetadataInputTypedDict(TypedDict):
    r"""A set of keys and associated values, attached to a particular version of an Api."""
    
    meta_key: str
    r"""The key for this metadata."""
    meta_value: str
    r"""One of the values for this metadata."""
    

class VersionMetadataInput(BaseModel):
    r"""A set of keys and associated values, attached to a particular version of an Api."""
    
    meta_key: str
    r"""The key for this metadata."""
    meta_value: str
    r"""One of the values for this metadata."""
    
