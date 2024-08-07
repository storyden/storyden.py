# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from .._models import BaseModel

from typing import List, Optional, Dict

from datetime import datetime

from typing import Optional, Union, List, Dict, Any
from typing_extensions import Literal
from pydantic import Field as FieldInfo
from ..types import shared

__all__ = ["PostUpdateResponse", "Asset", "Author", "Link", "LinkAsset", "React"]


class Asset(BaseModel):
    id: str
    """A unique identifier for this resource."""

    filename: str

    height: float

    mime_type: str

    url: str

    width: float


class Author(BaseModel):
    id: str
    """A unique identifier for this resource."""

    admin: bool

    handle: str
    """The unique @ handle of an account."""

    name: str
    """The account owners display name."""


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


class React(BaseModel):
    id: Optional[str] = None
    """A unique identifier for this resource."""

    emoji: Optional[str] = None


class PostUpdateResponse(BaseModel):
    id: str
    """A unique identifier for this resource."""

    assets: List[Asset]

    author: Author
    """A minimal reference to an account."""

    body: str
    """The body text of a post within a thread.

    The type is either a string or an object, depending on what was used during
    creation. Strings can be used for basic plain text or markdown content and
    objects are used for more complex types such as Slate.js editor documents.
    """

    created_at: datetime = FieldInfo(alias="createdAt")
    """The time the resource was created."""

    links: List[Link]

    reacts: List[React]
    """A list of reactions this post has had from people."""

    root_id: str
    """A unique identifier for this resource."""

    root_slug: str
    """
    A thread's ID and optional slug separated by a dash = it's unique mark. This
    allows endpoints to respond to varying forms of a thread's ID.

    For example, given a thread with the ID `cc5lnd2s1s4652adtu50` and the slug
    `top-10-movies-thread`, Storyden will understand both the forms:
    `cc5lnd2s1s4652adtu50-top-10-movies-thread` and `cc5lnd2s1s4652adtu50` as the
    identifier for that thread.
    """

    updated_at: datetime = FieldInfo(alias="updatedAt")
    """The time the resource was updated."""

    deleted_at: Optional[datetime] = FieldInfo(alias="deletedAt", default=None)
    """The time the resource was soft-deleted."""

    meta: Optional[Dict[str, object]] = None
    """Arbitrary metadata for the resource."""

    misc: Optional[object] = None
    """Arbitrary extra data stored with the resource."""

    reply_to: Optional[str] = None
    """A unique identifier for this resource."""
