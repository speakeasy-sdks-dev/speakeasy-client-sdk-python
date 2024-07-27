"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
import pydantic
from speakeasy_client_sdk_python.types import BaseModel
from typing import Optional, TypedDict
from typing_extensions import Annotated, NotRequired


class AnnotationsTypedDict(TypedDict):
    r"""Annotations"""
    
    org_opencontainers_image_authors: NotRequired[str]
    r"""The authors of the image"""
    org_opencontainers_image_created: NotRequired[str]
    r"""The time the image was created"""
    org_opencontainers_image_description: NotRequired[str]
    r"""Human-readable description of the software packaged in the image"""
    org_opencontainers_image_documentation: NotRequired[str]
    r"""The documentation URL of the image"""
    org_opencontainers_image_licenses: NotRequired[str]
    org_opencontainers_image_ref_name: NotRequired[str]
    r"""Name of the reference for a target"""
    org_opencontainers_image_revision: NotRequired[str]
    r"""Source control revision identifier"""
    org_opencontainers_image_source: NotRequired[str]
    r"""The URL to get source code for building the image"""
    org_opencontainers_image_title: NotRequired[str]
    r"""Human-readable title of the image"""
    org_opencontainers_image_url: NotRequired[str]
    r"""The URL of the image"""
    org_opencontainers_image_vendor: NotRequired[str]
    r"""Name of the distributing entity, organization or individual."""
    org_opencontainers_image_version: NotRequired[str]
    r"""The version of the packaged software"""
    

class Annotations(BaseModel):
    r"""Annotations"""
    
    org_opencontainers_image_authors: Annotated[Optional[str], pydantic.Field(alias="org.opencontainers.image.authors")] = None
    r"""The authors of the image"""
    org_opencontainers_image_created: Annotated[Optional[str], pydantic.Field(alias="org.opencontainers.image.created")] = None
    r"""The time the image was created"""
    org_opencontainers_image_description: Annotated[Optional[str], pydantic.Field(alias="org.opencontainers.image.description")] = None
    r"""Human-readable description of the software packaged in the image"""
    org_opencontainers_image_documentation: Annotated[Optional[str], pydantic.Field(alias="org.opencontainers.image.documentation")] = None
    r"""The documentation URL of the image"""
    org_opencontainers_image_licenses: Annotated[Optional[str], pydantic.Field(alias="org.opencontainers.image.licenses")] = None
    org_opencontainers_image_ref_name: Annotated[Optional[str], pydantic.Field(alias="org.opencontainers.image.ref.name")] = None
    r"""Name of the reference for a target"""
    org_opencontainers_image_revision: Annotated[Optional[str], pydantic.Field(alias="org.opencontainers.image.revision")] = None
    r"""Source control revision identifier"""
    org_opencontainers_image_source: Annotated[Optional[str], pydantic.Field(alias="org.opencontainers.image.source")] = None
    r"""The URL to get source code for building the image"""
    org_opencontainers_image_title: Annotated[Optional[str], pydantic.Field(alias="org.opencontainers.image.title")] = None
    r"""Human-readable title of the image"""
    org_opencontainers_image_url: Annotated[Optional[str], pydantic.Field(alias="org.opencontainers.image.url")] = None
    r"""The URL of the image"""
    org_opencontainers_image_vendor: Annotated[Optional[str], pydantic.Field(alias="org.opencontainers.image.vendor")] = None
    r"""Name of the distributing entity, organization or individual."""
    org_opencontainers_image_version: Annotated[Optional[str], pydantic.Field(alias="org.opencontainers.image.version")] = None
    r"""The version of the packaged software"""
    
