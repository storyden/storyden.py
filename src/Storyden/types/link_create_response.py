# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from .._models import BaseModel

from datetime import datetime

from typing import Optional

from typing import Optional, Union, List, Dict, Any
from typing_extensions import Literal
from pydantic import Field as FieldInfo
from ..types import shared

__all__ = ["LinkCreateResponse", "FaviconImage", "PrimaryImage"]


class FaviconImage(BaseModel):
    id: str
    """A unique identifier for this resource."""

    filename: str

    height: float

    mime_type: str

    url: str

    width: float


class PrimaryImage(BaseModel):
    id: str
    """A unique identifier for this resource."""

    filename: str

    height: float

    mime_type: str

    url: str

    width: float


class LinkCreateResponse(BaseModel):
    id: str
    """A unique identifier for this resource."""

    created_at: datetime = FieldInfo(alias="createdAt")
    """The time the resource was created."""

    domain: str

    slug: str

    updated_at: datetime = FieldInfo(alias="updatedAt")
    """The time the resource was updated."""

    url: str
    """A web address"""

    deleted_at: Optional[datetime] = FieldInfo(alias="deletedAt", default=None)
    """The time the resource was soft-deleted."""

    description: Optional[str] = None

    favicon_image: Optional[FaviconImage] = None

    misc: Optional[object] = None
    """Arbitrary extra data stored with the resource."""

    primary_image: Optional[PrimaryImage] = None

    title: Optional[str] = None
