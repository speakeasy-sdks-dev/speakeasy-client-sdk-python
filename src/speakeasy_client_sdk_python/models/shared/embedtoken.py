"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
from datetime import datetime
from speakeasy_client_sdk_python.types import BaseModel
from typing import Optional, TypedDict
from typing_extensions import NotRequired


class EmbedTokenTypedDict(TypedDict):
    r"""A representation of an embed token granted for working with Speakeasy components."""
    
    created_at: datetime
    r"""Creation timestamp."""
    created_by: str
    r"""The ID of the user that created this token."""
    description: str
    r"""A detailed description of the EmbedToken."""
    expires_at: datetime
    r"""The time this token expires."""
    filters: str
    r"""The filters applied to this token."""
    id: str
    r"""The ID of this EmbedToken."""
    workspace_id: str
    r"""The workspace ID this token belongs to."""
    last_used: NotRequired[datetime]
    r"""The last time this token was used."""
    revoked_at: NotRequired[datetime]
    r"""The time this token was revoked."""
    revoked_by: NotRequired[str]
    r"""The ID of the user that revoked this token."""
    

class EmbedToken(BaseModel):
    r"""A representation of an embed token granted for working with Speakeasy components."""
    
    created_at: datetime
    r"""Creation timestamp."""
    created_by: str
    r"""The ID of the user that created this token."""
    description: str
    r"""A detailed description of the EmbedToken."""
    expires_at: datetime
    r"""The time this token expires."""
    filters: str
    r"""The filters applied to this token."""
    id: str
    r"""The ID of this EmbedToken."""
    workspace_id: str
    r"""The workspace ID this token belongs to."""
    last_used: Optional[datetime] = None
    r"""The last time this token was used."""
    revoked_at: Optional[datetime] = None
    r"""The time this token was revoked."""
    revoked_by: Optional[str] = None
    r"""The ID of the user that revoked this token."""
    
