"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
from speakeasy_client_sdk_python.types import BaseModel
from typing import TypedDict


class EmbedAccessTokenResponseTypedDict(TypedDict):
    r"""An EmbedAccessTokenResponse contains a token that can be used to embed a Speakeasy dashboard."""

    access_token: str


class EmbedAccessTokenResponse(BaseModel):
    r"""An EmbedAccessTokenResponse contains a token that can be used to embed a Speakeasy dashboard."""

    access_token: str
