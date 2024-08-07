# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from ...._models import BaseModel

from datetime import datetime

from typing import List

from typing import Optional, Union, List, Dict, Any
from typing_extensions import Literal
from pydantic import Field as FieldInfo
from ....types import shared

__all__ = ["AuthMethodListResponse", "Active", "ActiveProvider", "Available"]


class ActiveProvider(BaseModel):
    link: str
    """The hyperlink to render for the user."""

    name: str
    """The human-readable name of the provider."""

    provider: str
    """The slug name of the provider."""


class Active(BaseModel):
    id: str
    """The internal unique ID this method has."""

    created_at: datetime
    """When this auth method was registered to the account."""

    identifier: str
    """The external identifier (third party ID or device ID)"""

    name: str
    """The personal name given to the method."""

    provider: ActiveProvider


class Available(BaseModel):
    link: str
    """The hyperlink to render for the user."""

    name: str
    """The human-readable name of the provider."""

    provider: str
    """The slug name of the provider."""


class AuthMethodListResponse(BaseModel):
    active: List[Active]

    available: List[Available]
