"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
from .organizationusage import OrganizationUsage, OrganizationUsageTypedDict
from datetime import datetime
from speakeasy_client_sdk_python.types import BaseModel
from typing import List, Optional, TypedDict
from typing_extensions import NotRequired


class OrganizationUsageResponseTypedDict(TypedDict):
    r"""A billing summary of organization usage"""
    
    allowed_languages: List[str]
    r"""List of allowed languages"""
    total_allowed_languages: int
    r"""Total number of allowed languages, -1 if unlimited"""
    usage: List[OrganizationUsageTypedDict]
    free_trial_expiry: NotRequired[datetime]
    r"""Expiry date of the free trial, will be null if no trial"""
    

class OrganizationUsageResponse(BaseModel):
    r"""A billing summary of organization usage"""
    
    allowed_languages: List[str]
    r"""List of allowed languages"""
    total_allowed_languages: int
    r"""Total number of allowed languages, -1 if unlimited"""
    usage: List[OrganizationUsage]
    free_trial_expiry: Optional[datetime] = None
    r"""Expiry date of the free trial, will be null if no trial"""
    
