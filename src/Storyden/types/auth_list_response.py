# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from .._models import BaseModel

from typing import List

from typing import Optional, Union, List, Dict, Any
from typing_extensions import Literal
from pydantic import Field as FieldInfo
from ..types import shared

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
