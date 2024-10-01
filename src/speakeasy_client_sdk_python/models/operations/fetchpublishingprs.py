"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
import httpx
from speakeasy_client_sdk_python.models.shared import (
    error as shared_error,
    githubpublishingprresponse as shared_githubpublishingprresponse,
)
from speakeasy_client_sdk_python.types import BaseModel
from speakeasy_client_sdk_python.utils import FieldMetadata, QueryParamMetadata
from typing import Optional
from typing_extensions import Annotated, NotRequired, TypedDict


class FetchPublishingPRsRequestTypedDict(TypedDict):
    generate_gen_lock_id: str
    org: str
    repo: str


class FetchPublishingPRsRequest(BaseModel):
    generate_gen_lock_id: Annotated[
        str, FieldMetadata(query=QueryParamMetadata(style="form", explode=True))
    ]

    org: Annotated[
        str, FieldMetadata(query=QueryParamMetadata(style="form", explode=True))
    ]

    repo: Annotated[
        str, FieldMetadata(query=QueryParamMetadata(style="form", explode=True))
    ]


class FetchPublishingPRsResponseTypedDict(TypedDict):
    content_type: str
    r"""HTTP response content type for this operation"""
    status_code: int
    r"""HTTP response status code for this operation"""
    raw_response: httpx.Response
    r"""Raw HTTP response; suitable for custom response parsing"""
    error: NotRequired[shared_error.ErrorTypedDict]
    r"""Default error response"""
    github_publishing_pr_response: NotRequired[
        shared_githubpublishingprresponse.GithubPublishingPRResponseTypedDict
    ]
    r"""OK"""


class FetchPublishingPRsResponse(BaseModel):
    content_type: str
    r"""HTTP response content type for this operation"""

    status_code: int
    r"""HTTP response status code for this operation"""

    raw_response: httpx.Response
    r"""Raw HTTP response; suitable for custom response parsing"""

    error: Optional[shared_error.Error] = None
    r"""Default error response"""

    github_publishing_pr_response: Optional[
        shared_githubpublishingprresponse.GithubPublishingPRResponse
    ] = None
    r"""OK"""
