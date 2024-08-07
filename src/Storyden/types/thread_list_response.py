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
    "ThreadAsset",
    "ThreadAuthor",
    "ThreadCategory",
    "ThreadCollection",
    "ThreadCollectionOwner",
    "ThreadReact",
    "ThreadLink",
    "ThreadLinkAsset",
]


class ThreadAsset(BaseModel):
    id: str
    """A unique identifier for this resource."""

    filename: str

    height: float

    mime_type: str

    url: str

    width: float


class ThreadAuthor(BaseModel):
    id: str
    """A unique identifier for this resource."""

    admin: bool

    handle: str
    """The unique @ handle of an account."""

    name: str
    """The account owners display name."""


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


class ThreadCollectionOwner(BaseModel):
    id: str
    """A unique identifier for this resource."""

    admin: bool

    handle: str
    """The unique @ handle of an account."""

    name: str
    """The account owners display name."""


class ThreadCollection(BaseModel):
    id: str
    """A unique identifier for this resource."""

    created_at: datetime = FieldInfo(alias="createdAt")
    """The time the resource was created."""

    description: str

    name: str

    owner: ThreadCollectionOwner
    """A minimal reference to an account."""

    updated_at: datetime = FieldInfo(alias="updatedAt")
    """The time the resource was updated."""

    deleted_at: Optional[datetime] = FieldInfo(alias="deletedAt", default=None)
    """The time the resource was soft-deleted."""

    misc: Optional[object] = None
    """Arbitrary extra data stored with the resource."""


class ThreadReact(BaseModel):
    id: Optional[str] = None
    """A unique identifier for this resource."""

    emoji: Optional[str] = None


class ThreadLinkAsset(BaseModel):
    id: str
    """A unique identifier for this resource."""

    filename: str

    height: float

    mime_type: str

    url: str

    width: float


class ThreadLink(BaseModel):
    assets: List[ThreadLinkAsset]

    domain: str

    slug: str

    url: str
    """A web address"""

    description: Optional[str] = None

    title: Optional[str] = None


class Thread(BaseModel):
    id: str
    """A unique identifier for this resource."""

    assets: List[ThreadAsset]

    author: ThreadAuthor
    """A minimal reference to an account."""

    category: ThreadCategory

    collections: List[ThreadCollection]

    created_at: datetime = FieldInfo(alias="createdAt")
    """The time the resource was created."""

    pinned: bool
    """Whether the thread is pinned in this category."""

    post_count: int
    """The number of posts under this thread."""

    reacts: List[ThreadReact]
    """A list of reactions this post has had from people."""

    short: str
    """A short version of the thread's body text for use in previews."""

    slug: str
    """
    A thread's ID and optional slug separated by a dash = it's unique mark. This
    allows endpoints to respond to varying forms of a thread's ID.

    For example, given a thread with the ID `cc5lnd2s1s4652adtu50` and the slug
    `top-10-movies-thread`, Storyden will understand both the forms:
    `cc5lnd2s1s4652adtu50-top-10-movies-thread` and `cc5lnd2s1s4652adtu50` as the
    identifier for that thread.
    """

    tags: List[str]
    """A list of tags associated with the thread."""

    title: str
    """The title of the thread."""

    updated_at: datetime = FieldInfo(alias="updatedAt")
    """The time the resource was updated."""

    deleted_at: Optional[datetime] = FieldInfo(alias="deletedAt", default=None)
    """The time the resource was soft-deleted."""

    link: Optional[ThreadLink] = None
    """A web address with content information such as title, description, etc."""

    meta: Optional[Dict[str, object]] = None
    """Arbitrary metadata for the resource."""

    misc: Optional[object] = None
    """Arbitrary extra data stored with the resource."""


class ThreadListResponse(BaseModel):
    current_page: int

    page_size: int

    results: int

    threads: List[Thread]

    total_pages: int

    next_page: Optional[int] = None
