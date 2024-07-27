"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
import httpx
from speakeasy_client_sdk_python.models.errors import error as errors_error
from speakeasy_client_sdk_python.models.shared import githubmissingpublishingsecretsresponse as shared_githubmissingpublishingsecretsresponse
from speakeasy_client_sdk_python.types import BaseModel
from speakeasy_client_sdk_python.utils import FieldMetadata, QueryParamMetadata
from typing import Optional, TypedDict
from typing_extensions import Annotated, NotRequired


class GithubCheckPublishingSecretsRequestTypedDict(TypedDict):
    generate_gen_lock_id: str
    

class GithubCheckPublishingSecretsRequest(BaseModel):
    generate_gen_lock_id: Annotated[str, FieldMetadata(query=QueryParamMetadata(style="form", explode=True))]
    

class GithubCheckPublishingSecretsResponseTypedDict(TypedDict):
    content_type: str
    r"""HTTP response content type for this operation"""
    status_code: int
    r"""HTTP response status code for this operation"""
    raw_response: httpx.Response
    r"""Raw HTTP response; suitable for custom response parsing"""
    error: NotRequired[errors_error.Error]
    r"""Default error response"""
    github_missing_publishing_secrets_response: NotRequired[shared_githubmissingpublishingsecretsresponse.GithubMissingPublishingSecretsResponseTypedDict]
    r"""OK"""
    

class GithubCheckPublishingSecretsResponse(BaseModel):
    content_type: str
    r"""HTTP response content type for this operation"""
    status_code: int
    r"""HTTP response status code for this operation"""
    raw_response: httpx.Response
    r"""Raw HTTP response; suitable for custom response parsing"""
    error: Optional[errors_error.Error] = None
    r"""Default error response"""
    github_missing_publishing_secrets_response: Optional[shared_githubmissingpublishingsecretsresponse.GithubMissingPublishingSecretsResponse] = None
    r"""OK"""
    
