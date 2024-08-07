# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal, Required, TypedDict

from .._types import FileTypes

__all__ = ["AssetCreateParams"]


class AssetCreateParams(TypedDict, total=False):
    body: Required[FileTypes]

    content_fill_rule: Literal["replace"]
    """Use the content extracted from the child resource to modify the target resource.

    This can be used to populate a node from a asset or link. For example, if you
    wanted to create a node that held the contents of a PDF file, you can upload the
    file with a target node and a fill rule set.
    """

    filename: str
    """The client-provided file name for the asset."""

    node_content_fill_target: str
    """
    When NodeContentFillRuleQuery is used, this option must be set in order to
    specify which node will receive content extracted from the source.
    """
