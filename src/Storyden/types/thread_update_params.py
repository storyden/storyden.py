# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import TypedDict, Literal

from typing import Dict, List

from typing import List, Union, Dict, Optional
from typing_extensions import Literal, TypedDict, Required, Annotated
from .._types import FileTypes
from .._utils import PropertyInfo
from ..types import shared_params

__all__ = ["ThreadUpdateParams"]


class ThreadUpdateParams(TypedDict, total=False):
    body: str
    """The body text of a post within a thread.

    The type is either a string or an object, depending on what was used during
    creation. Strings can be used for basic plain text or markdown content and
    objects are used for more complex types such as Slate.js editor documents.
    """

    category: str
    """A unique identifier for this resource."""

    meta: Dict[str, object]
    """Arbitrary metadata for the resource."""

    tags: List[str]
    """A list of tags IDs."""

    title: str
    """The title of a thread."""

    url: str
    """A web address"""

    visibility: Literal["draft", "unlisted", "review", "published"]
