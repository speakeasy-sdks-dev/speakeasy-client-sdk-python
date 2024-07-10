"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
from speakeasy_client_sdk_python.types import BaseModel
from typing import TypedDict


class GithubConfigureTargetRequestTypedDict(TypedDict):
    r"""A request to configure a GitHub target"""
    
    org: str
    r"""The GitHub organization name"""
    repo_name: str
    r"""The GitHub repository name"""
    

class GithubConfigureTargetRequest(BaseModel):
    r"""A request to configure a GitHub target"""
    
    org: str
    r"""The GitHub organization name"""
    repo_name: str
    r"""The GitHub repository name"""
    