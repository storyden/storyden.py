# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from .._models import BaseModel

from typing import List, Optional

from typing import Optional, Union, List, Dict, Any
from typing_extensions import Literal
from pydantic import Field as FieldInfo
from ..types import shared

__all__ = ["NodeListResponse", "Node"]


class Node:
    pass


class NodeListResponse(BaseModel):
    current_page: int

    nodes: List[Node]

    page_size: int

    results: int

    total_pages: int

    next_page: Optional[int] = None
