# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import TypedDict, Required

from typing import Dict

from typing import List, Union, Dict, Optional
from typing_extensions import Literal, TypedDict, Required, Annotated
from .._types import FileTypes
from .._utils import PropertyInfo

__all__ = ["CategoryCreateParams"]


class CategoryCreateParams(TypedDict, total=False):
    admin: Required[bool]

    colour: Required[str]

    description: Required[str]

    name: Required[str]
    """A category's user-facing name."""

    meta: Dict[str, object]
    """Arbitrary metadata for the resource."""

    slug: str
    """A category's URL-safe slug."""
