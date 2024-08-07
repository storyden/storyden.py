# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import TypedDict

from typing import List, Union, Dict, Optional
from typing_extensions import Literal, TypedDict, Required, Annotated
from .._types import FileTypes
from .._utils import PropertyInfo
from ..types import shared_params

__all__ = ["NodeDeleteParams"]


class NodeDeleteParams(TypedDict, total=False):
    target_node: str
    """If set, child nodes will be moved to the target node.

    If not set, child nodes will be moved to the root.
    """
