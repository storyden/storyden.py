# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from .._models import BaseModel

from typing_extensions import Literal

from typing import Optional, Dict, List

from typing import Optional, Union, List, Dict, Any
from typing_extensions import Literal
from pydantic import Field as FieldInfo
from ..types import shared

__all__ = ["DatagraphListResponse", "Item"]


class Item(BaseModel):
    id: str
    """A unique identifier for this resource."""

    kind: Literal["post", "node", "profile"]

    name: str

    slug: str

    description: Optional[str] = None

    meta: Optional[Dict[str, object]] = None
    """Arbitrary metadata for the resource."""


class DatagraphListResponse(BaseModel):
    current_page: int

    items: List[Item]

    page_size: int

    results: int

    total_pages: int

    next_page: Optional[int] = None
