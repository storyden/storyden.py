# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List
from typing_extensions import Literal, TypedDict

__all__ = ["PostSearchParams"]


class PostSearchParams(TypedDict, total=False):
    author: str
    """Show only results created by this account."""

    body: str
    """A text query to search for in post content."""

    kind: List[Literal["post", "thread"]]
    """Posts, threads or both."""
