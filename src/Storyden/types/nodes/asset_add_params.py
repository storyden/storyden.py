# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import TypedDict, Required, Literal

from typing import List, Union, Dict, Optional
from typing_extensions import Literal, TypedDict, Required, Annotated
from ..._types import FileTypes
from ..._utils import PropertyInfo

__all__ = ["AssetAddParams"]


class AssetAddParams(TypedDict, total=False):
    node_slug: Required[str]
    """A unique identifier for this resource."""

    content_fill_rule: Literal["replace"]
    """Use the content extracted from the child resource to modify the target resource.

    This can be used to populate a node from a asset or link. For example, if you
    wanted to create a node that held the contents of a PDF file, you can upload the
    file with a target node and a fill rule set.
    """

    node_content_fill_target: str
    """
    When NodeContentFillRuleQuery is used, this option must be set in order to
    specify which node will receive content extracted from the source.
    """
