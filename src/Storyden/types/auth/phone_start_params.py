# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import TypedDict, Required

from typing import List, Union, Dict, Optional
from typing_extensions import Literal, TypedDict, Required, Annotated
from ..._types import FileTypes
from ..._utils import PropertyInfo
from ...types import shared_params

__all__ = ["PhoneStartParams"]


class PhoneStartParams(TypedDict, total=False):
    identifier: Required[str]
    """The desired username to link to the phone number."""

    phone_number: Required[str]
    """The phone number to receive the one-time code on."""
