# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import TypedDict

__all__ = ["LinkListParams"]


class LinkListParams(TypedDict, total=False):
    page: str
    """Pagination query parameters."""

    q: str
    """Search query string."""
