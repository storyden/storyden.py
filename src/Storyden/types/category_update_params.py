# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import TypedDict

from typing import Dict

from typing import List, Union, Dict, Optional
from typing_extensions import Literal, TypedDict, Required, Annotated
from .._types import FileTypes
from .._utils import PropertyInfo
from ..types import shared_params

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
