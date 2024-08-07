# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List
from datetime import datetime

from ...._models import BaseModel

__all__ = ["AuthMethodDeleteResponse", "Active", "ActiveProvider", "Available"]


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


class AuthMethodDeleteResponse(BaseModel):
    active: List[Active]

    available: List[Available]
