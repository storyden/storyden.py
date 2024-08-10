# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from .._models import BaseModel

from datetime import datetime

from typing import Optional, Dict, List

from typing_extensions import Literal

from typing import Optional, Union, List, Dict, Any
from typing_extensions import Literal
from pydantic import Field as FieldInfo
from ..types import shared

__all__ = [
    "ThreadUpdateResponse",
    "Asset",
    "Author",
    "Category",
    "Collection",
    "CollectionOwner",
    "Link",
    "LinkAsset",
    "React",
    "Recomentation",
    "RecomentationAsset",
    "Reply",
]


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


class Category(BaseModel):
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


class CollectionOwner(BaseModel):
    id: str
    """A unique identifier for this resource."""

    admin: bool

    handle: str
    """The unique @ handle of an account."""

    name: str
    """The account owners display name."""


class Collection(BaseModel):
    id: str
    """A unique identifier for this resource."""

    created_at: datetime = FieldInfo(alias="createdAt")
    """The time the resource was created."""

    description: str

    name: str

    owner: CollectionOwner
    """A minimal reference to an account."""

    updated_at: datetime = FieldInfo(alias="updatedAt")
    """The time the resource was updated."""

    deleted_at: Optional[datetime] = FieldInfo(alias="deletedAt", default=None)
    """The time the resource was soft-deleted."""

    misc: Optional[object] = None
    """Arbitrary extra data stored with the resource."""


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


class RecomentationAsset(BaseModel):
    id: str
    """A unique identifier for this resource."""

    filename: str

    height: float

    mime_type: str

    url: str

    width: float


class Recomentation(BaseModel):
    id: str
    """A unique identifier for this resource."""

    assets: List[RecomentationAsset]

    kind: Literal["post", "node", "profile"]

    name: str

    slug: str

    description: Optional[str] = None

    meta: Optional[Dict[str, object]] = None
    """Arbitrary metadata for the resource."""


class Reply(BaseModel):
    id: str
    """A unique identifier for this resource."""

    body: str
    """The body text of a post within a thread.

    The type is either a string or an object, depending on what was used during
    creation. Strings can be used for basic plain text or markdown content and
    objects are used for more complex types such as Slate.js editor documents.
    """

    created_at: datetime = FieldInfo(alias="createdAt")
    """The time the resource was created."""

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

    misc: Optional[object] = None
    """Arbitrary extra data stored with the resource."""

    reply_to: Optional[str] = None
    """A unique identifier for this resource."""


class ThreadUpdateResponse(BaseModel):
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

    category: Category

    collections: List[Collection]

    created_at: datetime = FieldInfo(alias="createdAt")
    """The time the resource was created."""

    links: List[Link]

    pinned: bool
    """Whether the thread is pinned in this category."""

    post_count: int
    """The number of posts under this thread."""

    reacts: List[React]
    """A list of reactions this post has had from people."""

    recomentations: List[Recomentation]

    replies: List[Reply]

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
    """The title of a thread."""

    updated_at: datetime = FieldInfo(alias="updatedAt")
    """The time the resource was updated."""

    deleted_at: Optional[datetime] = FieldInfo(alias="deletedAt", default=None)
    """The time the resource was soft-deleted."""

    description: Optional[str] = None
    """A short version of the post's body text for use in previews."""

    link: Optional[Link] = None
    """A web address with content information such as title, description, etc."""

    meta: Optional[Dict[str, object]] = None
    """Arbitrary metadata for the resource."""

    misc: Optional[object] = None
    """Arbitrary extra data stored with the resource."""
