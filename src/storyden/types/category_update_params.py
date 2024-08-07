# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict
from typing_extensions import TypedDict

__all__ = ["CategoryUpdateParams"]


class CategoryUpdateParams(TypedDict, total=False):
    admin: bool

    colour: str

    description: str

    meta: Dict[str, object]
    """Arbitrary metadata for the resource."""

    name: str
    """A category's user-facing name."""

    slug: str
    """A category's URL-safe slug."""
