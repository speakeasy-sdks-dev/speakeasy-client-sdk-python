"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
from .filter_ import Filter, FilterTypedDict
from speakeasy_client_sdk_python.types import BaseModel
from typing import List
from typing_extensions import TypedDict


class FiltersTypedDict(TypedDict):
    r"""Filters are used to query requests."""

    filters: List[FilterTypedDict]
    r"""A list of filters to apply to the query."""
    limit: int
    r"""The maximum number of results to return."""
    offset: int
    r"""The offset to start the query from."""
    operator: str
    r"""The operator to use when combining filters."""


class Filters(BaseModel):
    r"""Filters are used to query requests."""

    filters: List[Filter]
    r"""A list of filters to apply to the query."""

    limit: int
    r"""The maximum number of results to return."""

    offset: int
    r"""The offset to start the query from."""

    operator: str
    r"""The operator to use when combining filters."""
