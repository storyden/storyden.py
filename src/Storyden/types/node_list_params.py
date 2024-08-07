# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import TypedDict, Literal

from typing import List

from typing import List, Union, Dict, Optional
from typing_extensions import Literal, TypedDict, Required, Annotated
from .._types import FileTypes
from .._utils import PropertyInfo
from ..types import shared_params

__all__ = ["NodeListParams"]


class NodeListParams(TypedDict, total=False):
    author: str
    """Show only results owned by this account."""

    depth: str
    """
    When set to a positive value, the nodes in the response will include all child
    nodes up to the specified depth. When set to zero, then if the request includes
    a node ID only that node will be returned, otherwise only top-level (root) nodes
    will be returned.
    """

    node_id: str
    """List this node and all child nodes."""

    page: str
    """Pagination query parameters."""

    q: str
    """Search query string."""

    visibility: List[Literal["draft", "unlisted", "review", "published"]]
    """Filter nodes with specific visibility values.

    Note that by default, only published nodes are returned. When 'draft' is
    specified, only drafts owned by the requesting account are included. When
    'review' is specified, the request will fail if the requesting account is not an
    administrator.
    """
