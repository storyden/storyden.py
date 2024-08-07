# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List

from ..._models import BaseModel

__all__ = ["AuthListResponse", "Provider"]


class Provider(BaseModel):
    link: str
    """The hyperlink to render for the user."""

    name: str
    """The human-readable name of the provider."""

    provider: str
    """The slug name of the provider."""


class AuthListResponse(BaseModel):
    providers: List[Provider]
