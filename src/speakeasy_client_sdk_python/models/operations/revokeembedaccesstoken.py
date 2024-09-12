"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
import httpx
import pydantic
from speakeasy_client_sdk_python.models.errors import error as errors_error
from speakeasy_client_sdk_python.types import BaseModel
from speakeasy_client_sdk_python.utils import FieldMetadata, PathParamMetadata
from typing import Optional, TypedDict
from typing_extensions import Annotated, NotRequired


class RevokeEmbedAccessTokenRequestTypedDict(TypedDict):
    token_id: str
    r"""The ID of the EmbedToken to revoke."""


class RevokeEmbedAccessTokenRequest(BaseModel):
    token_id: Annotated[
        str,
        pydantic.Field(alias="tokenID"),
        FieldMetadata(path=PathParamMetadata(style="simple", explode=False)),
    ]
    r"""The ID of the EmbedToken to revoke."""


class RevokeEmbedAccessTokenResponseTypedDict(TypedDict):
    content_type: str
    r"""HTTP response content type for this operation"""
    status_code: int
    r"""HTTP response status code for this operation"""
    raw_response: httpx.Response
    r"""Raw HTTP response; suitable for custom response parsing"""
    error: NotRequired[errors_error.Error]
    r"""Default error response"""


class RevokeEmbedAccessTokenResponse(BaseModel):
    content_type: str
    r"""HTTP response content type for this operation"""

    status_code: int
    r"""HTTP response status code for this operation"""

    raw_response: httpx.Response
    r"""Raw HTTP response; suitable for custom response parsing"""

    error: Optional[errors_error.Error] = None
    r"""Default error response"""
