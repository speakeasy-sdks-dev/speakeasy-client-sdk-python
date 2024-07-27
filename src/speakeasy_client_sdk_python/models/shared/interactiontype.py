"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
from enum import Enum


class InteractionType(str, Enum):
    r"""Type of interaction."""
    CI_EXEC = "CI_EXEC"
    CLI_EXEC = "CLI_EXEC"
    LINT = "LINT"
    OPENAPI_DIFF = "OPENAPI_DIFF"
    TARGET_GENERATE = "TARGET_GENERATE"
    TOMBSTONE = "TOMBSTONE"
    AUTHENTICATE = "AUTHENTICATE"
    QUICKSTART = "QUICKSTART"
    RUN = "RUN"
    CONFIGURE = "CONFIGURE"
    PUBLISH = "PUBLISH"
