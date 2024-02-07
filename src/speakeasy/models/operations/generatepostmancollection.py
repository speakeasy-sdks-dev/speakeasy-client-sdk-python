"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
import requests as requests_http
from ...models.shared import error as shared_error
from typing import Optional


@dataclasses.dataclass
class GeneratePostmanCollectionRequest:
    api_id: str = dataclasses.field(metadata={'path_param': { 'field_name': 'apiID', 'style': 'simple', 'explode': False }})
    r"""The ID of the Api to generate a Postman collection for."""
    version_id: str = dataclasses.field(metadata={'path_param': { 'field_name': 'versionID', 'style': 'simple', 'explode': False }})
    r"""The version ID of the Api to generate a Postman collection for."""
    



@dataclasses.dataclass
class GeneratePostmanCollectionResponse:
    content_type: str = dataclasses.field()
    r"""HTTP response content type for this operation"""
    status_code: int = dataclasses.field()
    r"""HTTP response status code for this operation"""
    raw_response: requests_http.Response = dataclasses.field()
    r"""Raw HTTP response; suitable for custom response parsing"""
    error: Optional[shared_error.Error] = dataclasses.field(default=None)
    r"""Default error response"""
    postman_collection: Optional[requests_http.Response] = dataclasses.field(default=None)
    r"""OK"""
    

