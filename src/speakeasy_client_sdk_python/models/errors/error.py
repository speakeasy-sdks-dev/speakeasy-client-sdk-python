"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
from speakeasy_client_sdk_python.types import BaseModel
import speakeasy_client_sdk_python.utils as utils

class ErrorData(BaseModel):
    message: str
    r"""A developer-facing error message."""
    status_code: int
    r"""The HTTP status code"""
    


class Error(Exception):
    r"""The `Status` type defines a logical error model"""
    data: ErrorData

    def __init__(self, data: ErrorData):
        self.data = data

    def __str__(self) -> str:
        return utils.marshal_json(self.data, ErrorData)

