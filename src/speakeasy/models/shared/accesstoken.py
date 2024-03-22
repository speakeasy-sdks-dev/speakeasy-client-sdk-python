"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
import dateutil.parser
from dataclasses_json import Undefined, dataclass_json
from datetime import datetime
from speakeasy import utils
from typing import List, Optional


@dataclasses.dataclass
class Claims:
    pass


@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class AccessTokenUser:
    admin: Optional[bool] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('admin'), 'exclude': lambda f: f is None }})
    created_at: Optional[datetime] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('created_at'), 'encoder': utils.datetimeisoformat(True), 'decoder': dateutil.parser.isoparse, 'exclude': lambda f: f is None }})
    display_name: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('display_name'), 'exclude': lambda f: f is None }})
    email: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('email'), 'exclude': lambda f: f is None }})
    email_verified: Optional[bool] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('email_verified'), 'exclude': lambda f: f is None }})
    id: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('id'), 'exclude': lambda f: f is None }})
    



@dataclasses.dataclass
class Workspaces:
    pass


@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class AccessToken:
    r"""An AccessToken is a token that can be used to authenticate with the Speakeasy API."""
    access_token: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('access_token') }})
    claims: Claims = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('claims') }})
    user: AccessTokenUser = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('user') }})
    workspaces: Optional[List[Workspaces]] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('workspaces'), 'exclude': lambda f: f is None }})
    

