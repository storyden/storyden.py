# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from .._models import BaseModel

from datetime import datetime

from typing import Optional, List

from typing import Optional, Union, List, Dict, Any
from typing_extensions import Literal
from pydantic import Field as FieldInfo
from ..types import shared

__all__ = ["PostUpdateResponse", "BodyLink", "BodyLinkFaviconImage", "BodyLinkPrimaryImage"]


class BodyLinkFaviconImage(BaseModel):
    id: str
    """A unique identifier for this resource."""

    filename: str

    height: float

    mime_type: str

    url: str

    width: float


class BodyLinkPrimaryImage(BaseModel):
    id: str
    """A unique identifier for this resource."""

    filename: str

    height: float

    mime_type: str

    url: str

    width: float


class BodyLink(BaseModel):
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

    favicon_image: Optional[BodyLinkFaviconImage] = None

    misc: Optional[object] = None
    """Arbitrary extra data stored with the resource."""

    primary_image: Optional[BodyLinkPrimaryImage] = None

    title: Optional[str] = None


class PostUpdateResponse(BaseModel):
    id: str
    """A unique identifier for this resource."""

    body: str
    """The body text of a post within a thread.

    The type is either a string or an object, depending on what was used during
    creation. Strings can be used for basic plain text or markdown content and
    objects are used for more complex types such as Slate.js editor documents.
    """

    body_links: List[BodyLink]

    created_at: datetime = FieldInfo(alias="createdAt")
    """The time the resource was created."""

    updated_at: datetime = FieldInfo(alias="updatedAt")
    """The time the resource was updated."""

    deleted_at: Optional[datetime] = FieldInfo(alias="deletedAt", default=None)
    """The time the resource was soft-deleted."""

    misc: Optional[object] = None
    """Arbitrary extra data stored with the resource."""
