"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import httpx
import pydantic
from speakeasy_client_sdk_python.types import BaseModel
from speakeasy_client_sdk_python.utils import FieldMetadata, PathParamMetadata
from typing import Optional, TypedDict
from typing_extensions import Annotated, NotRequired


class GetLintingReportSignedURLRequestTypedDict(TypedDict):
    document_checksum: str
    r"""The checksum of the document to retrieve the signed access url for."""
    

class GetLintingReportSignedURLRequest(BaseModel):
    document_checksum: Annotated[str, pydantic.Field(alias="documentChecksum"), FieldMetadata(path=PathParamMetadata(style="simple", explode=False))]
    r"""The checksum of the document to retrieve the signed access url for."""
    

class GetLintingReportSignedURLSignedAccessTypedDict(TypedDict):
    r"""OK"""
    
    url: str
    

class GetLintingReportSignedURLSignedAccess(BaseModel):
    r"""OK"""
    
    url: str
    

class GetLintingReportSignedURLResponseTypedDict(TypedDict):
    content_type: str
    r"""HTTP response content type for this operation"""
    status_code: int
    r"""HTTP response status code for this operation"""
    raw_response: httpx.Response
    r"""Raw HTTP response; suitable for custom response parsing"""
    signed_access: NotRequired[GetLintingReportSignedURLSignedAccessTypedDict]
    r"""OK"""
    

class GetLintingReportSignedURLResponse(BaseModel):
    content_type: str
    r"""HTTP response content type for this operation"""
    status_code: int
    r"""HTTP response status code for this operation"""
    raw_response: httpx.Response
    r"""Raw HTTP response; suitable for custom response parsing"""
    signed_access: Optional[GetLintingReportSignedURLSignedAccess] = None
    r"""OK"""
    
