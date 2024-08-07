# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import TypedDict

from typing import List, Dict

from typing import List, Union, Dict, Optional
from typing_extensions import Literal, TypedDict, Required, Annotated
from .._types import FileTypes
from .._utils import PropertyInfo
from ..types import shared_params

__all__ = ["NodeUpdateParams"]


class NodeUpdateParams(TypedDict, total=False):
    asset_ids: List[str]

    asset_sources: List[str]

    content: str
    """The body text of a post within a thread.

    The type is either a string or an object, depending on what was used during
    creation. Strings can be used for basic plain text or markdown content and
    objects are used for more complex types such as Slate.js editor documents.
    """

    meta: Dict[str, object]
    """Arbitrary metadata for the resource."""

    name: str

    parent: str
    """A URL-safe slug for uniquely identifying resources."""

    slug: str
    """A URL-safe slug for uniquely identifying resources."""

    url: str
    """A web address"""
