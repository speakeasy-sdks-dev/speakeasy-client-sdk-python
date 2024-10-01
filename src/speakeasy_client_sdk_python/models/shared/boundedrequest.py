"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
from .requestmetadata import RequestMetadata, RequestMetadataTypedDict
from datetime import datetime
from speakeasy_client_sdk_python.types import BaseModel
from typing import List, Optional
from typing_extensions import NotRequired, TypedDict


class BoundedRequestTypedDict(TypedDict):
    r"""A BoundedRequest is a request that has been logged by the Speakeasy without the contents of the request."""

    api_endpoint_id: str
    r"""The ID of the ApiEndpoint this request was made to."""
    api_id: str
    r"""The ID of the Api this request was made to."""
    created_at: datetime
    r"""Creation timestamp."""
    customer_id: str
    r"""The ID of the customer that made this request."""
    latency: int
    r"""The latency of the request."""
    method: str
    r"""HTTP verb."""
    path: str
    r"""The path of the request."""
    request_finish_time: datetime
    r"""The time the request finished."""
    request_id: str
    r"""The ID of this request."""
    request_start_time: datetime
    r"""The time the request was made."""
    status: int
    r"""The status code of the request."""
    version_id: str
    r"""The version ID of the Api this request was made to."""
    workspace_id: str
    r"""The workspace ID this request was made to."""
    metadata: NotRequired[List[RequestMetadataTypedDict]]
    r"""Metadata associated with this request"""


class BoundedRequest(BaseModel):
    r"""A BoundedRequest is a request that has been logged by the Speakeasy without the contents of the request."""

    api_endpoint_id: str
    r"""The ID of the ApiEndpoint this request was made to."""

    api_id: str
    r"""The ID of the Api this request was made to."""

    created_at: datetime
    r"""Creation timestamp."""

    customer_id: str
    r"""The ID of the customer that made this request."""

    latency: int
    r"""The latency of the request."""

    method: str
    r"""HTTP verb."""

    path: str
    r"""The path of the request."""

    request_finish_time: datetime
    r"""The time the request finished."""

    request_id: str
    r"""The ID of this request."""

    request_start_time: datetime
    r"""The time the request was made."""

    status: int
    r"""The status code of the request."""

    version_id: str
    r"""The version ID of the Api this request was made to."""

    workspace_id: str
    r"""The workspace ID this request was made to."""

    metadata: Optional[List[RequestMetadata]] = None
    r"""Metadata associated with this request"""
