"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
import httpx
import pydantic
from speakeasy_client_sdk_python.models.errors import error as errors_error
from speakeasy_client_sdk_python.models.shared import (
    organization as shared_organization,
)
from speakeasy_client_sdk_python.types import BaseModel
from speakeasy_client_sdk_python.utils import FieldMetadata, PathParamMetadata
from typing import Optional, TypedDict
from typing_extensions import Annotated, NotRequired


class GetOrganizationRequestTypedDict(TypedDict):
    organization_id: str
    r"""Unique identifier of the organization."""


class GetOrganizationRequest(BaseModel):
    organization_id: Annotated[
        str,
        pydantic.Field(alias="organizationID"),
        FieldMetadata(path=PathParamMetadata(style="simple", explode=False)),
    ]
    r"""Unique identifier of the organization."""


class GetOrganizationResponseTypedDict(TypedDict):
    content_type: str
    r"""HTTP response content type for this operation"""
    status_code: int
    r"""HTTP response status code for this operation"""
    raw_response: httpx.Response
    r"""Raw HTTP response; suitable for custom response parsing"""
    error: NotRequired[errors_error.Error]
    r"""Default error response"""
    organization: NotRequired[shared_organization.OrganizationTypedDict]
    r"""OK"""


class GetOrganizationResponse(BaseModel):
    content_type: str
    r"""HTTP response content type for this operation"""

    status_code: int
    r"""HTTP response status code for this operation"""

    raw_response: httpx.Response
    r"""Raw HTTP response; suitable for custom response parsing"""

    error: Optional[errors_error.Error] = None
    r"""Default error response"""

    organization: Optional[shared_organization.Organization] = None
    r"""OK"""
