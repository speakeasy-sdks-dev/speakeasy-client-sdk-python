"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
from .accounttype import AccountType
import pydantic
from pydantic.functional_validators import PlainValidator
from speakeasy_client_sdk_python.types import BaseModel
from speakeasy_client_sdk_python.utils import validate_open_enum
from typing import List, Optional
from typing_extensions import Annotated, NotRequired, TypedDict


class APIKeyDetailsTypedDict(TypedDict):
    account_type_v2: AccountType
    enabled_features: List[str]
    org_slug: str
    telemetry_disabled: bool
    workspace_id: str
    workspace_slug: str
    feature_flags: NotRequired[List[str]]
    generation_access_unlimited: NotRequired[bool]


class APIKeyDetails(BaseModel):
    account_type_v2: Annotated[AccountType, PlainValidator(validate_open_enum(False))]

    enabled_features: List[str]

    org_slug: str

    telemetry_disabled: bool

    workspace_id: str

    workspace_slug: str

    feature_flags: Annotated[
        Optional[List[str]],
        pydantic.Field(
            deprecated="warning: ** DEPRECATED ** - This will be removed in a future release, please migrate away from it as soon as possible."
        ),
    ] = None

    generation_access_unlimited: Optional[bool] = None
