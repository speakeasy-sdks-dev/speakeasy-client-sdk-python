"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
import requests as requests_http
from ...models.shared import api as shared_api
from ...models.shared import error as shared_error
from typing import Dict, List, Optional


@dataclasses.dataclass
class Op:
    r"""Configuration for filter operations"""
    and_: bool = dataclasses.field(metadata={'query_param': { 'field_name': 'and' }})
    r"""Whether to AND or OR the filters"""
    



@dataclasses.dataclass
class GetAllAPIVersionsRequest:
    api_id: str = dataclasses.field(metadata={'path_param': { 'field_name': 'apiID', 'style': 'simple', 'explode': False }})
    r"""The ID of the Api to retrieve."""
    metadata: Optional[Dict[str, List[str]]] = dataclasses.field(default=None, metadata={'query_param': { 'field_name': 'metadata', 'style': 'deepObject', 'explode': True }})
    r"""Metadata to filter Apis on"""
    op: Optional[Op] = dataclasses.field(default=None, metadata={'query_param': { 'field_name': 'op', 'style': 'deepObject', 'explode': True }})
    r"""Configuration for filter operations"""
    



@dataclasses.dataclass
class GetAllAPIVersionsResponse:
    content_type: str = dataclasses.field()
    r"""HTTP response content type for this operation"""
    status_code: int = dataclasses.field()
    r"""HTTP response status code for this operation"""
    raw_response: requests_http.Response = dataclasses.field()
    r"""Raw HTTP response; suitable for custom response parsing"""
    apis: Optional[List[shared_api.API]] = dataclasses.field(default=None)
    r"""OK"""
    error: Optional[shared_error.Error] = dataclasses.field(default=None)
    r"""Default error response"""
    

