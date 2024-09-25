"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
import httpx
from speakeasy_client_sdk_python.models.shared import shorturl as shared_shorturl
from speakeasy_client_sdk_python.types import BaseModel
from typing import Optional, TypedDict
from typing_extensions import NotRequired


class CreateRequestBodyTypedDict(TypedDict):
    url: str
    r"""URL to shorten"""


class CreateRequestBody(BaseModel):
    url: str
    r"""URL to shorten"""


class CreateResponseTypedDict(TypedDict):
    content_type: str
    r"""HTTP response content type for this operation"""
    status_code: int
    r"""HTTP response status code for this operation"""
    raw_response: httpx.Response
    r"""Raw HTTP response; suitable for custom response parsing"""
    short_url: NotRequired[shared_shorturl.ShortURLTypedDict]
    r"""OK"""


class CreateResponse(BaseModel):
    content_type: str
    r"""HTTP response content type for this operation"""

    status_code: int
    r"""HTTP response status code for this operation"""

    raw_response: httpx.Response
    r"""Raw HTTP response; suitable for custom response parsing"""

    short_url: Optional[shared_shorturl.ShortURL] = None
    r"""OK"""
