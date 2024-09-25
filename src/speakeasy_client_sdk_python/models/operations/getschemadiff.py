"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
import httpx
import pydantic
from speakeasy_client_sdk_python.models.errors import error as errors_error
from speakeasy_client_sdk_python.models.shared import schemadiff as shared_schemadiff
from speakeasy_client_sdk_python.types import BaseModel
from speakeasy_client_sdk_python.utils import FieldMetadata, PathParamMetadata
from typing import Optional, TypedDict
from typing_extensions import Annotated, NotRequired


class GetSchemaDiffRequestTypedDict(TypedDict):
    api_id: str
    r"""The ID of the Api to retrieve schemas for."""
    version_id: str
    r"""The version ID of the Api to delete metadata for."""
    base_revision_id: str
    r"""The base revision ID of the schema to retrieve."""
    target_revision_id: str
    r"""The target revision ID of the schema to retrieve."""


class GetSchemaDiffRequest(BaseModel):
    api_id: Annotated[
        str,
        pydantic.Field(alias="apiID"),
        FieldMetadata(path=PathParamMetadata(style="simple", explode=False)),
    ]
    r"""The ID of the Api to retrieve schemas for."""

    version_id: Annotated[
        str,
        pydantic.Field(alias="versionID"),
        FieldMetadata(path=PathParamMetadata(style="simple", explode=False)),
    ]
    r"""The version ID of the Api to delete metadata for."""

    base_revision_id: Annotated[
        str,
        pydantic.Field(alias="baseRevisionID"),
        FieldMetadata(path=PathParamMetadata(style="simple", explode=False)),
    ]
    r"""The base revision ID of the schema to retrieve."""

    target_revision_id: Annotated[
        str,
        pydantic.Field(alias="targetRevisionID"),
        FieldMetadata(path=PathParamMetadata(style="simple", explode=False)),
    ]
    r"""The target revision ID of the schema to retrieve."""


class GetSchemaDiffResponseTypedDict(TypedDict):
    content_type: str
    r"""HTTP response content type for this operation"""
    status_code: int
    r"""HTTP response status code for this operation"""
    raw_response: httpx.Response
    r"""Raw HTTP response; suitable for custom response parsing"""
    error: NotRequired[errors_error.Error]
    r"""Default error response"""
    schema_diff: NotRequired[shared_schemadiff.SchemaDiffTypedDict]
    r"""OK"""


class GetSchemaDiffResponse(BaseModel):
    content_type: str
    r"""HTTP response content type for this operation"""

    status_code: int
    r"""HTTP response status code for this operation"""

    raw_response: httpx.Response
    r"""Raw HTTP response; suitable for custom response parsing"""

    error: Optional[errors_error.Error] = None
    r"""Default error response"""

    schema_diff: Optional[shared_schemadiff.SchemaDiff] = None
    r"""OK"""
