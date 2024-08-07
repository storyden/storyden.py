# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict
from typing_extensions import TypedDict

__all__ = ["PostUpdateParams"]


class PostUpdateParams(TypedDict, total=False):
    body: str
    """The body text of a post within a thread.

    The type is either a string or an object, depending on what was used during
    creation. Strings can be used for basic plain text or markdown content and
    objects are used for more complex types such as Slate.js editor documents.
    """

    meta: Dict[str, object]
    """Arbitrary metadata for the resource."""

    url: str
    """A web address"""
