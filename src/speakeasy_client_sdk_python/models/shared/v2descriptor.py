"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
from .annotations import Annotations, AnnotationsTypedDict
import pydantic
from speakeasy_client_sdk_python.types import BaseModel
from typing import Optional, TypedDict
from typing_extensions import Annotated, NotRequired


class V2DescriptorTypedDict(TypedDict):
    r"""V2 descriptor"""
    
    annotations: NotRequired[AnnotationsTypedDict]
    r"""Annotations"""
    digest: NotRequired[str]
    r"""Digest"""
    media_type: NotRequired[str]
    r"""Media type"""
    size: NotRequired[int]
    r"""Size"""
    

class V2Descriptor(BaseModel):
    r"""V2 descriptor"""
    
    annotations: Optional[Annotations] = None
    r"""Annotations"""
    digest: Optional[str] = None
    r"""Digest"""
    media_type: Annotated[Optional[str], pydantic.Field(alias="mediaType")] = None
    r"""Media type"""
    size: Optional[int] = None
    r"""Size"""
    