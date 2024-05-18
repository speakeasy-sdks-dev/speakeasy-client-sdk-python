"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
import dateutil.parser
from .organizationusage import OrganizationUsage
from dataclasses_json import Undefined, dataclass_json
from datetime import datetime
from speakeasy import utils
from typing import List, Optional


@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class OrganizationUsageResponse:
    r"""A billing summary of organization usage"""
    allowed_languages: List[str] = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('allowed_languages') }})
    r"""List of allowed languages"""
    total_allowed_languages: int = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('total_allowed_languages') }})
    r"""Total number of allowed languages, -1 if unlimited"""
    usage: List[OrganizationUsage] = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('usage') }})
    free_trial_expiry: Optional[datetime] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('free_trial_expiry'), 'encoder': utils.datetimeisoformat(True), 'decoder': dateutil.parser.isoparse, 'exclude': lambda f: f is None }})
    r"""Expiry date of the free trial, will be null if no trial"""
    

