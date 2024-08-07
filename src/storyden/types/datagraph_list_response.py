# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Dict, List, Optional
from typing_extensions import Literal

from .._models import BaseModel

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
