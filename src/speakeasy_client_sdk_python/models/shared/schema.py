"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
from datetime import datetime
from speakeasy_client_sdk_python.types import BaseModel
from typing_extensions import TypedDict


class SchemaTypedDict(TypedDict):
    r"""A Schema represents an API schema for a particular Api and Version."""

    api_id: str
    r"""The ID of the Api this Schema belongs to."""
    created_at: datetime
    r"""Creation timestamp."""
    description: str
    r"""A detailed description of the Schema."""
    revision_id: str
    r"""An ID referencing this particular revision of the Schema."""
    version_id: str
    r"""The version ID of the Api this Schema belongs to."""
    workspace_id: str
    r"""The workspace ID this Schema belongs to."""


class Schema(BaseModel):
    r"""A Schema represents an API schema for a particular Api and Version."""

    api_id: str
    r"""The ID of the Api this Schema belongs to."""

    created_at: datetime
    r"""Creation timestamp."""

    description: str
    r"""A detailed description of the Schema."""

    revision_id: str
    r"""An ID referencing this particular revision of the Schema."""

    version_id: str
    r"""The version ID of the Api this Schema belongs to."""

    workspace_id: str
    r"""The workspace ID this Schema belongs to."""
