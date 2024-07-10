"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
from .workflowdocument import WorkflowDocument, WorkflowDocumentTypedDict
import pydantic
from speakeasy_client_sdk_python.types import BaseModel
from typing import Optional, TypedDict
from typing_extensions import Annotated, NotRequired


class GithubConfigureCodeSamplesResponseTypedDict(TypedDict):
    r"""A response to configure GitHub code samples"""
    
    code_sample_overlay_registry_url: str
    r"""The URL of the code sample overlay registry"""
    source: WorkflowDocumentTypedDict
    r"""A document referenced by a workflow"""
    gh_action_id: NotRequired[str]
    r"""The ID of the GitHub action that was dispatched"""
    

class GithubConfigureCodeSamplesResponse(BaseModel):
    r"""A response to configure GitHub code samples"""
    
    code_sample_overlay_registry_url: Annotated[str, pydantic.Field(alias="codeSampleOverlayRegistryURL")]
    r"""The URL of the code sample overlay registry"""
    source: WorkflowDocument
    r"""A document referenced by a workflow"""
    gh_action_id: Annotated[Optional[str], pydantic.Field(alias="ghActionID")] = None
    r"""The ID of the GitHub action that was dispatched"""
    
