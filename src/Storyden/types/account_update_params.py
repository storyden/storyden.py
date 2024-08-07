# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import TypedDict, Required

from typing import List, Iterable, Dict

from typing import List, Union, Dict, Optional
from typing_extensions import Literal, TypedDict, Required, Annotated
from .._types import FileTypes
from .._utils import PropertyInfo
from ..types import shared_params

__all__ = ["AccountUpdateParams", "Link"]


class AccountUpdateParams(TypedDict, total=False):
    bio: str
    """The rich-text bio for an account's public profile."""

    handle: str
    """The unique @ handle of an account."""

    interests: List[str]
    """A list of tags IDs."""

    links: Iterable[Link]

    meta: Dict[str, object]
    """Arbitrary metadata for the resource."""

    name: str
    """The account owners display name."""


class Link(TypedDict, total=False):
    text: Required[str]

    url: Required[str]
