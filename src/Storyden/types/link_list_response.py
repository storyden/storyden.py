# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from .._models import BaseModel

from typing import List, Optional

from typing import Optional, Union, List, Dict, Any
from typing_extensions import Literal
from pydantic import Field as FieldInfo
from ..types import shared

__all__ = ["LinkListResponse", "Link", "LinkAsset"]


class LinkAsset(BaseModel):
    id: str
    """A unique identifier for this resource."""

    filename: str

    height: float

    mime_type: str

    url: str

    width: float


class Link(BaseModel):
    assets: List[LinkAsset]

    domain: str

    slug: str

    url: str
    """A web address"""

    description: Optional[str] = None

    title: Optional[str] = None


class LinkListResponse(BaseModel):
    current_page: int

    links: List[Link]

    page_size: int

    results: int

    total_pages: int

    next_page: Optional[int] = None
