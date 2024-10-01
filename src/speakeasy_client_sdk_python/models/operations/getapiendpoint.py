"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
import httpx
import pydantic
from speakeasy_client_sdk_python.models.shared import (
    apiendpoint as shared_apiendpoint,
    error as shared_error,
)
from speakeasy_client_sdk_python.types import BaseModel
from speakeasy_client_sdk_python.utils import FieldMetadata, PathParamMetadata
from typing import Optional
from typing_extensions import Annotated, NotRequired, TypedDict


class GetAPIEndpointRequestTypedDict(TypedDict):
    api_id: str
    r"""The ID of the Api the ApiEndpoint belongs to."""
    version_id: str
    r"""The version ID of the Api the ApiEndpoint belongs to."""
    api_endpoint_id: str
    r"""The ID of the ApiEndpoint to retrieve."""


class GetAPIEndpointRequest(BaseModel):
    api_id: Annotated[
        str,
        pydantic.Field(alias="apiID"),
        FieldMetadata(path=PathParamMetadata(style="simple", explode=False)),
    ]
    r"""The ID of the Api the ApiEndpoint belongs to."""

    version_id: Annotated[
        str,
        pydantic.Field(alias="versionID"),
        FieldMetadata(path=PathParamMetadata(style="simple", explode=False)),
    ]
    r"""The version ID of the Api the ApiEndpoint belongs to."""

    api_endpoint_id: Annotated[
        str,
        pydantic.Field(alias="apiEndpointID"),
        FieldMetadata(path=PathParamMetadata(style="simple", explode=False)),
    ]
    r"""The ID of the ApiEndpoint to retrieve."""


class GetAPIEndpointResponseTypedDict(TypedDict):
    content_type: str
    r"""HTTP response content type for this operation"""
    status_code: int
    r"""HTTP response status code for this operation"""
    raw_response: httpx.Response
    r"""Raw HTTP response; suitable for custom response parsing"""
    api_endpoint: NotRequired[shared_apiendpoint.APIEndpointTypedDict]
    r"""OK"""
    error: NotRequired[shared_error.ErrorTypedDict]
    r"""Default error response"""


class GetAPIEndpointResponse(BaseModel):
    content_type: str
    r"""HTTP response content type for this operation"""

    status_code: int
    r"""HTTP response status code for this operation"""

    raw_response: httpx.Response
    r"""Raw HTTP response; suitable for custom response parsing"""

    api_endpoint: Optional[shared_apiendpoint.APIEndpoint] = None
    r"""OK"""

    error: Optional[shared_error.Error] = None
    r"""Default error response"""
