# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import TypedDict

from typing import List

from typing import List, Union, Dict, Optional
from typing_extensions import Literal, TypedDict, Required, Annotated
from .._types import FileTypes
from .._utils import PropertyInfo

__all__ = ["ThreadListParams"]


class ThreadListParams(TypedDict, total=False):
    author: str
    """Show only results creeated by this user."""

    categories: List[str]
    """Show only results with these categories"""

    page: str
    """Pagination query parameters."""

    q: str
    """Search query string."""

    tags: List[str]
    """Show only results with these tags"""
