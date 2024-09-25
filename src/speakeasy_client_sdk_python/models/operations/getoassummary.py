"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
import httpx
from speakeasy_client_sdk_python.models.shared import (
    error as shared_error,
    oassummary as shared_oassummary,
)
from speakeasy_client_sdk_python.types import BaseModel
from speakeasy_client_sdk_python.utils import FieldMetadata, PathParamMetadata
from typing import Optional, TypedDict
from typing_extensions import Annotated, NotRequired


class GetOASSummaryRequestTypedDict(TypedDict):
    namespace_name: str
    revision_reference: str


class GetOASSummaryRequest(BaseModel):
    namespace_name: Annotated[
        str, FieldMetadata(path=PathParamMetadata(style="simple", explode=False))
    ]

    revision_reference: Annotated[
        str, FieldMetadata(path=PathParamMetadata(style="simple", explode=False))
    ]


class GetOASSummaryResponseTypedDict(TypedDict):
    content_type: str
    r"""HTTP response content type for this operation"""
    status_code: int
    r"""HTTP response status code for this operation"""
    raw_response: httpx.Response
    r"""Raw HTTP response; suitable for custom response parsing"""
    error: NotRequired[shared_error.ErrorTypedDict]
    r"""Default error response"""
    oas_summary: NotRequired[shared_oassummary.OASSummaryTypedDict]
    r"""OK"""


class GetOASSummaryResponse(BaseModel):
    content_type: str
    r"""HTTP response content type for this operation"""

    status_code: int
    r"""HTTP response status code for this operation"""

    raw_response: httpx.Response
    r"""Raw HTTP response; suitable for custom response parsing"""

    error: Optional[shared_error.Error] = None
    r"""Default error response"""

    oas_summary: Optional[shared_oassummary.OASSummary] = None
    r"""OK"""
