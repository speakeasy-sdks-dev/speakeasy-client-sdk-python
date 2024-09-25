"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
import httpx
import pydantic
from speakeasy_client_sdk_python.models.shared import (
    api as shared_api,
    error as shared_error,
)
from speakeasy_client_sdk_python.types import BaseModel
from speakeasy_client_sdk_python.utils import FieldMetadata, QueryParamMetadata
from typing import Dict, List, Optional, TypedDict
from typing_extensions import Annotated, NotRequired


class QueryParamOpTypedDict(TypedDict):
    r"""Configuration for filter operations"""

    and_: bool
    r"""Whether to AND or OR the filters"""


class QueryParamOp(BaseModel):
    r"""Configuration for filter operations"""

    and_: Annotated[bool, pydantic.Field(alias="and"), FieldMetadata(query=True)]
    r"""Whether to AND or OR the filters"""


class GetApisRequestTypedDict(TypedDict):
    op: NotRequired[QueryParamOpTypedDict]
    r"""Configuration for filter operations"""
    metadata: NotRequired[Dict[str, List[str]]]
    r"""Metadata to filter Apis on"""


class GetApisRequest(BaseModel):
    op: Annotated[
        Optional[QueryParamOp],
        FieldMetadata(query=QueryParamMetadata(style="deepObject", explode=True)),
    ] = None
    r"""Configuration for filter operations"""

    metadata: Annotated[
        Optional[Dict[str, List[str]]],
        FieldMetadata(query=QueryParamMetadata(style="deepObject", explode=True)),
    ] = None
    r"""Metadata to filter Apis on"""


class GetApisResponseTypedDict(TypedDict):
    content_type: str
    r"""HTTP response content type for this operation"""
    status_code: int
    r"""HTTP response status code for this operation"""
    raw_response: httpx.Response
    r"""Raw HTTP response; suitable for custom response parsing"""
    apis: NotRequired[List[shared_api.APITypedDict]]
    r"""OK"""
    error: NotRequired[shared_error.ErrorTypedDict]
    r"""Default error response"""


class GetApisResponse(BaseModel):
    content_type: str
    r"""HTTP response content type for this operation"""

    status_code: int
    r"""HTTP response status code for this operation"""

    raw_response: httpx.Response
    r"""Raw HTTP response; suitable for custom response parsing"""

    apis: Optional[List[shared_api.API]] = None
    r"""OK"""

    error: Optional[shared_error.Error] = None
    r"""Default error response"""
