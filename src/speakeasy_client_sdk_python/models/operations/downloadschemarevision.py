"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import httpx
import pydantic
from speakeasy_client_sdk_python.models.errors import error as errors_error
from speakeasy_client_sdk_python.types import BaseModel
from speakeasy_client_sdk_python.utils import FieldMetadata, PathParamMetadata
from typing import Optional, TypedDict
from typing_extensions import Annotated, NotRequired


class DownloadSchemaRevisionRequestTypedDict(TypedDict):
    api_id: str
    r"""The ID of the Api to retrieve schemas for."""
    revision_id: str
    r"""The revision ID of the schema to retrieve."""
    version_id: str
    r"""The version ID of the Api to delete metadata for."""
    

class DownloadSchemaRevisionRequest(BaseModel):
    api_id: Annotated[str, pydantic.Field(alias="apiID"), FieldMetadata(path=PathParamMetadata(style="simple", explode=False))]
    r"""The ID of the Api to retrieve schemas for."""
    revision_id: Annotated[str, pydantic.Field(alias="revisionID"), FieldMetadata(path=PathParamMetadata(style="simple", explode=False))]
    r"""The revision ID of the schema to retrieve."""
    version_id: Annotated[str, pydantic.Field(alias="versionID"), FieldMetadata(path=PathParamMetadata(style="simple", explode=False))]
    r"""The version ID of the Api to delete metadata for."""
    

class DownloadSchemaRevisionResponseTypedDict(TypedDict):
    content_type: str
    r"""HTTP response content type for this operation"""
    status_code: int
    r"""HTTP response status code for this operation"""
    raw_response: httpx.Response
    r"""Raw HTTP response; suitable for custom response parsing"""
    two_hundred_application_json_schema: NotRequired[httpx.Response]
    r"""OK"""
    two_hundred_application_x_yaml_schema: NotRequired[httpx.Response]
    r"""OK"""
    error: NotRequired[errors_error.Error]
    r"""Default error response"""
    

class DownloadSchemaRevisionResponse(BaseModel):
    content_type: str
    r"""HTTP response content type for this operation"""
    status_code: int
    r"""HTTP response status code for this operation"""
    raw_response: httpx.Response
    r"""Raw HTTP response; suitable for custom response parsing"""
    two_hundred_application_json_schema: Optional[httpx.Response] = None
    r"""OK"""
    two_hundred_application_x_yaml_schema: Optional[httpx.Response] = None
    r"""OK"""
    error: Optional[errors_error.Error] = None
    r"""Default error response"""
    