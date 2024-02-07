"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
import requests as requests_http
from ...models.shared import error as shared_error
from ...models.shared import schemadiff as shared_schemadiff
from typing import Optional


@dataclasses.dataclass
class GetSchemaDiffRequest:
    api_id: str = dataclasses.field(metadata={'path_param': { 'field_name': 'apiID', 'style': 'simple', 'explode': False }})
    r"""The ID of the Api to retrieve schemas for."""
    base_revision_id: str = dataclasses.field(metadata={'path_param': { 'field_name': 'baseRevisionID', 'style': 'simple', 'explode': False }})
    r"""The base revision ID of the schema to retrieve."""
    target_revision_id: str = dataclasses.field(metadata={'path_param': { 'field_name': 'targetRevisionID', 'style': 'simple', 'explode': False }})
    r"""The target revision ID of the schema to retrieve."""
    version_id: str = dataclasses.field(metadata={'path_param': { 'field_name': 'versionID', 'style': 'simple', 'explode': False }})
    r"""The version ID of the Api to delete metadata for."""
    



@dataclasses.dataclass
class GetSchemaDiffResponse:
    content_type: str = dataclasses.field()
    r"""HTTP response content type for this operation"""
    status_code: int = dataclasses.field()
    r"""HTTP response status code for this operation"""
    raw_response: requests_http.Response = dataclasses.field()
    r"""Raw HTTP response; suitable for custom response parsing"""
    error: Optional[shared_error.Error] = dataclasses.field(default=None)
    r"""Default error response"""
    schema_diff: Optional[shared_schemadiff.SchemaDiff] = dataclasses.field(default=None)
    r"""OK"""
    

