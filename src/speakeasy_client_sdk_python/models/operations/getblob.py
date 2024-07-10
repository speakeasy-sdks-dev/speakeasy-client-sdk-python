"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import httpx
from speakeasy_client_sdk_python.models.errors import error as errors_error
from speakeasy_client_sdk_python.types import BaseModel
from speakeasy_client_sdk_python.utils import FieldMetadata, PathParamMetadata
from typing import Optional, TypedDict
from typing_extensions import Annotated, NotRequired


class GetBlobRequestTypedDict(TypedDict):
    digest: str
    namespace_name: str
    organization_slug: str
    workspace_slug: str
    

class GetBlobRequest(BaseModel):
    digest: Annotated[str, FieldMetadata(path=PathParamMetadata(style="simple", explode=False))]
    namespace_name: Annotated[str, FieldMetadata(path=PathParamMetadata(style="simple", explode=False))]
    organization_slug: Annotated[str, FieldMetadata(path=PathParamMetadata(style="simple", explode=False))]
    workspace_slug: Annotated[str, FieldMetadata(path=PathParamMetadata(style="simple", explode=False))]
    

class GetBlobResponseTypedDict(TypedDict):
    content_type: str
    r"""HTTP response content type for this operation"""
    status_code: int
    r"""HTTP response status code for this operation"""
    raw_response: httpx.Response
    r"""Raw HTTP response; suitable for custom response parsing"""
    blob: NotRequired[httpx.Response]
    r"""OK"""
    error: NotRequired[errors_error.Error]
    r"""Default error response"""
    

class GetBlobResponse(BaseModel):
    content_type: str
    r"""HTTP response content type for this operation"""
    status_code: int
    r"""HTTP response status code for this operation"""
    raw_response: httpx.Response
    r"""Raw HTTP response; suitable for custom response parsing"""
    blob: Optional[httpx.Response] = None
    r"""OK"""
    error: Optional[errors_error.Error] = None
    r"""Default error response"""
    