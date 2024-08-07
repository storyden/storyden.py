# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import TypedDict, Literal

from typing import List

from typing import List, Union, Dict, Optional
from typing_extensions import Literal, TypedDict, Required, Annotated
from .._types import FileTypes
from .._utils import PropertyInfo
from ..types import shared_params

__all__ = ["PostSearchParams"]


class PostSearchParams(TypedDict, total=False):
    author: str
    """Show only results created by this account."""

    body: str
    """A text query to search for in post content."""

    kind: List[Literal["post", "thread"]]
    """Posts, threads or both."""
