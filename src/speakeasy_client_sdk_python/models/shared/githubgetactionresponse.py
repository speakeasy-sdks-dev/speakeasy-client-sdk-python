"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
from speakeasy_client_sdk_python.types import BaseModel
from typing import Optional, TypedDict
from typing_extensions import NotRequired


class GithubGetActionResponseTypedDict(TypedDict):
    r"""response to a getting the latest action run on a GitHub request"""
    
    run_status: NotRequired[str]
    r"""The status of the latest action run if available"""
    run_url: NotRequired[str]
    r"""The URL for latest action run if available"""
    

class GithubGetActionResponse(BaseModel):
    r"""response to a getting the latest action run on a GitHub request"""
    
    run_status: Optional[str] = None
    r"""The status of the latest action run if available"""
    run_url: Optional[str] = None
    r"""The URL for latest action run if available"""
    
