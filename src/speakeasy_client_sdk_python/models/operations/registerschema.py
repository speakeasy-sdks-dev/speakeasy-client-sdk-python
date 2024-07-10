"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import httpx
import io
import pydantic
from speakeasy_client_sdk_python.models.errors import error as errors_error
from speakeasy_client_sdk_python.types import BaseModel
from speakeasy_client_sdk_python.utils import FieldMetadata, MultipartFormMetadata, PathParamMetadata, RequestMetadata
from typing import IO, Optional, TypedDict, Union
from typing_extensions import Annotated, NotRequired


class RegisterSchemaFileTypedDict(TypedDict):
    content: Union[bytes, IO[bytes], io.BufferedReader]
    file_name: str
    content_type: NotRequired[str]
    

class RegisterSchemaFile(BaseModel):
    content: Annotated[Union[bytes, IO[bytes], io.BufferedReader], pydantic.Field(alias=""), FieldMetadata(multipart=MultipartFormMetadata(content=True))]
    file_name: Annotated[str, pydantic.Field(alias="file"), FieldMetadata(multipart=True)]
    content_type: Annotated[Optional[str], pydantic.Field(alias="Content-Type"), FieldMetadata(multipart=True)] = None
    

class RegisterSchemaRequestBodyTypedDict(TypedDict):
    r"""The schema file to upload provided as a multipart/form-data file segment."""
    
    file: RegisterSchemaFileTypedDict
    

class RegisterSchemaRequestBody(BaseModel):
    r"""The schema file to upload provided as a multipart/form-data file segment."""
    
    file: Annotated[RegisterSchemaFile, pydantic.Field(alias=""), FieldMetadata(multipart=MultipartFormMetadata(file=True))]
    

class RegisterSchemaRequestTypedDict(TypedDict):
    request_body: RegisterSchemaRequestBodyTypedDict
    r"""The schema file to upload provided as a multipart/form-data file segment."""
    api_id: str
    r"""The ID of the Api to get the schema for."""
    version_id: str
    r"""The version ID of the Api to delete metadata for."""
    

class RegisterSchemaRequest(BaseModel):
    request_body: Annotated[RegisterSchemaRequestBody, FieldMetadata(request=RequestMetadata(media_type="multipart/form-data"))]
    r"""The schema file to upload provided as a multipart/form-data file segment."""
    api_id: Annotated[str, pydantic.Field(alias="apiID"), FieldMetadata(path=PathParamMetadata(style="simple", explode=False))]
    r"""The ID of the Api to get the schema for."""
    version_id: Annotated[str, pydantic.Field(alias="versionID"), FieldMetadata(path=PathParamMetadata(style="simple", explode=False))]
    r"""The version ID of the Api to delete metadata for."""
    

class RegisterSchemaResponseTypedDict(TypedDict):
    content_type: str
    r"""HTTP response content type for this operation"""
    status_code: int
    r"""HTTP response status code for this operation"""
    raw_response: httpx.Response
    r"""Raw HTTP response; suitable for custom response parsing"""
    error: NotRequired[errors_error.Error]
    r"""Default error response"""
    

class RegisterSchemaResponse(BaseModel):
    content_type: str
    r"""HTTP response content type for this operation"""
    status_code: int
    r"""HTTP response status code for this operation"""
    raw_response: httpx.Response
    r"""Raw HTTP response; suitable for custom response parsing"""
    error: Optional[errors_error.Error] = None
    r"""Default error response"""
    
