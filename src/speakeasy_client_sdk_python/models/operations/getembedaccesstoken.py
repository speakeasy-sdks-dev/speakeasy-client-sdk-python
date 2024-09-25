"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
import httpx
from speakeasy_client_sdk_python.models.shared import (
    embedaccesstokenresponse as shared_embedaccesstokenresponse,
    error as shared_error,
    filters as shared_filters,
)
from speakeasy_client_sdk_python.types import BaseModel
from speakeasy_client_sdk_python.utils import FieldMetadata, QueryParamMetadata
from typing import Optional, TypedDict
from typing_extensions import Annotated, NotRequired


class GetEmbedAccessTokenRequestTypedDict(TypedDict):
    description: NotRequired[str]
    r"""The description of the embed access token."""
    duration: NotRequired[int]
    r"""The duration (in minutes) of the embed access token."""
    filters: NotRequired[shared_filters.FiltersTypedDict]
    r"""The filter to apply to the query."""


class GetEmbedAccessTokenRequest(BaseModel):
    description: Annotated[
        Optional[str],
        FieldMetadata(query=QueryParamMetadata(style="form", explode=True)),
    ] = None
    r"""The description of the embed access token."""

    duration: Annotated[
        Optional[int],
        FieldMetadata(query=QueryParamMetadata(style="form", explode=True)),
    ] = None
    r"""The duration (in minutes) of the embed access token."""

    filters: Annotated[
        Optional[shared_filters.Filters],
        FieldMetadata(query=QueryParamMetadata(serialization="json")),
    ] = None
    r"""The filter to apply to the query."""


class GetEmbedAccessTokenResponseTypedDict(TypedDict):
    content_type: str
    r"""HTTP response content type for this operation"""
    status_code: int
    r"""HTTP response status code for this operation"""
    raw_response: httpx.Response
    r"""Raw HTTP response; suitable for custom response parsing"""
    embed_access_token_response: NotRequired[
        shared_embedaccesstokenresponse.EmbedAccessTokenResponseTypedDict
    ]
    r"""OK"""
    error: NotRequired[shared_error.ErrorTypedDict]
    r"""Default error response"""


class GetEmbedAccessTokenResponse(BaseModel):
    content_type: str
    r"""HTTP response content type for this operation"""

    status_code: int
    r"""HTTP response status code for this operation"""

    raw_response: httpx.Response
    r"""Raw HTTP response; suitable for custom response parsing"""

    embed_access_token_response: Optional[
        shared_embedaccesstokenresponse.EmbedAccessTokenResponse
    ] = None
    r"""OK"""

    error: Optional[shared_error.Error] = None
    r"""Default error response"""
