"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import httpx
import pydantic
from speakeasy_client_sdk_python.models.errors import error as errors_error
from speakeasy_client_sdk_python.models.shared import apiendpoint as shared_apiendpoint
from speakeasy_client_sdk_python.types import BaseModel
from speakeasy_client_sdk_python.utils import FieldMetadata, PathParamMetadata
from typing import List, Optional, TypedDict
from typing_extensions import Annotated, NotRequired


class GetAllAPIEndpointsRequestTypedDict(TypedDict):
    api_id: str
    r"""The ID of the Api to retrieve ApiEndpoints for."""
    

class GetAllAPIEndpointsRequest(BaseModel):
    api_id: Annotated[str, pydantic.Field(alias="apiID"), FieldMetadata(path=PathParamMetadata(style="simple", explode=False))]
    r"""The ID of the Api to retrieve ApiEndpoints for."""
    

class GetAllAPIEndpointsResponseTypedDict(TypedDict):
    content_type: str
    r"""HTTP response content type for this operation"""
    status_code: int
    r"""HTTP response status code for this operation"""
    raw_response: httpx.Response
    r"""Raw HTTP response; suitable for custom response parsing"""
    api_endpoints: NotRequired[List[shared_apiendpoint.APIEndpointTypedDict]]
    r"""OK"""
    error: NotRequired[errors_error.Error]
    r"""Default error response"""
    

class GetAllAPIEndpointsResponse(BaseModel):
    content_type: str
    r"""HTTP response content type for this operation"""
    status_code: int
    r"""HTTP response status code for this operation"""
    raw_response: httpx.Response
    r"""Raw HTTP response; suitable for custom response parsing"""
    api_endpoints: Optional[List[shared_apiendpoint.APIEndpoint]] = None
    r"""OK"""
    error: Optional[errors_error.Error] = None
    r"""Default error response"""
    
