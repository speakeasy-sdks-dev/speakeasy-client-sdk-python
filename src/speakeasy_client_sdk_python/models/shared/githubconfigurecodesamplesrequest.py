"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import pydantic
from speakeasy_client_sdk_python.types import BaseModel
from typing import TypedDict
from typing_extensions import Annotated


class GithubConfigureCodeSamplesRequestTypedDict(TypedDict):
    r"""A request to configure GitHub code samples"""
    
    org: str
    r"""The GitHub organization name"""
    repo: str
    r"""The GitHub repository name"""
    target_name: str
    r"""The target name for the code samples"""
    

class GithubConfigureCodeSamplesRequest(BaseModel):
    r"""A request to configure GitHub code samples"""
    
    org: str
    r"""The GitHub organization name"""
    repo: str
    r"""The GitHub repository name"""
    target_name: Annotated[str, pydantic.Field(alias="targetName")]
    r"""The target name for the code samples"""
    