# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict, List
from typing_extensions import Literal, Required, TypedDict

__all__ = ["ThreadCreateParams"]


class ThreadCreateParams(TypedDict, total=False):
    body: Required[str]
    """The body text of a post within a thread.

    The type is either a string or an object, depending on what was used during
    creation. Strings can be used for basic plain text or markdown content and
    objects are used for more complex types such as Slate.js editor documents.
    """

    category: Required[str]
    """A unique identifier for this resource."""

    title: Required[str]
    """The title of a thread."""

    visibility: Required[Literal["draft", "unlisted", "review", "published"]]

    meta: Dict[str, object]
    """Arbitrary metadata for the resource."""

    tags: List[str]
    """A list of tags IDs."""

    url: str
    """A web address"""
