"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
from .namespace import Namespace, NamespaceTypedDict
from speakeasy_client_sdk_python.types import BaseModel
from typing import List, TypedDict


class GetNamespacesResponseTypedDict(TypedDict):
    items: List[NamespaceTypedDict]
    

class GetNamespacesResponse(BaseModel):
    items: List[Namespace]
    