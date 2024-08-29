# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from .._models import BaseModel

from datetime import datetime

from typing import Optional, Dict, List

from typing import Optional, Union, List, Dict, Any
from typing_extensions import Literal
from pydantic import Field as FieldInfo
from ..types import shared

__all__ = [
    "ThreadListResponse",
    "Thread",
    "ThreadBodyLink",
    "ThreadBodyLinkFaviconImage",
    "ThreadBodyLinkPrimaryImage",
    "ThreadCategory",
    "ThreadLink",
    "ThreadLinkFaviconImage",
    "ThreadLinkPrimaryImage",
]


class ThreadBodyLinkFaviconImage(BaseModel):
    id: str
    """A unique identifier for this resource."""

    filename: str

    height: float

    mime_type: str

    url: str

    width: float


class ThreadBodyLinkPrimaryImage(BaseModel):
    id: str
    """A unique identifier for this resource."""

    filename: str

    height: float

    mime_type: str

    url: str

    width: float


class ThreadBodyLink(BaseModel):
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

    favicon_image: Optional[ThreadBodyLinkFaviconImage] = None

    misc: Optional[object] = None
    """Arbitrary extra data stored with the resource."""

    primary_image: Optional[ThreadBodyLinkPrimaryImage] = None

    title: Optional[str] = None


class ThreadCategory(BaseModel):
    id: str
    """A unique identifier for this resource."""

    admin: bool

    colour: str

    created_at: datetime = FieldInfo(alias="createdAt")
    """The time the resource was created."""

    description: str

    name: str
    """A category's user-facing name."""

    slug: str
    """A category's URL-safe slug."""

    sort: int

    updated_at: datetime = FieldInfo(alias="updatedAt")
    """The time the resource was updated."""

    deleted_at: Optional[datetime] = FieldInfo(alias="deletedAt", default=None)
    """The time the resource was soft-deleted."""

    meta: Optional[Dict[str, object]] = None
    """Arbitrary metadata for the resource."""

    misc: Optional[object] = None
    """Arbitrary extra data stored with the resource."""


class ThreadLinkFaviconImage(BaseModel):
    id: str
    """A unique identifier for this resource."""

    filename: str

    height: float

    mime_type: str

    url: str

    width: float


class ThreadLinkPrimaryImage(BaseModel):
    id: str
    """A unique identifier for this resource."""

    filename: str

    height: float

    mime_type: str

    url: str

    width: float


class ThreadLink(BaseModel):
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

    favicon_image: Optional[ThreadLinkFaviconImage] = None

    misc: Optional[object] = None
    """Arbitrary extra data stored with the resource."""

    primary_image: Optional[ThreadLinkPrimaryImage] = None

    title: Optional[str] = None


class Thread(BaseModel):
    id: str
    """A unique identifier for this resource."""

    body: str
    """The body text of a post within a thread.

    The type is either a string or an object, depending on what was used during
    creation. Strings can be used for basic plain text or markdown content and
    objects are used for more complex types such as Slate.js editor documents.
    """

    body_links: List[ThreadBodyLink]

    category: ThreadCategory

    created_at: datetime = FieldInfo(alias="createdAt")
    """The time the resource was created."""

    pinned: bool
    """Whether the thread is pinned in this category."""

    post_count: int
    """The number of posts under this thread."""

    tags: List[str]
    """A list of tags associated with the thread."""

    updated_at: datetime = FieldInfo(alias="updatedAt")
    """The time the resource was updated."""

    deleted_at: Optional[datetime] = FieldInfo(alias="deletedAt", default=None)
    """The time the resource was soft-deleted."""

    link: Optional[ThreadLink] = None
    """A minimal object used to refer to a link without sending too much data."""

    misc: Optional[object] = None
    """Arbitrary extra data stored with the resource."""


class ThreadListResponse(BaseModel):
    current_page: int

    page_size: int

    results: int

    threads: List[Thread]

    total_pages: int

    next_page: Optional[int] = None
