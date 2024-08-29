# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from .._models import BaseModel

from datetime import datetime

from typing import Optional, List, Dict

from typing_extensions import Literal

from typing import Optional, Union, List, Dict, Any
from typing_extensions import Literal
from pydantic import Field as FieldInfo
from ..types import shared

__all__ = [
    "NodeUpdateResponse",
    "Asset",
    "Owner",
    "Link",
    "LinkFaviconImage",
    "LinkPrimaryImage",
    "Parent",
    "ParentAsset",
    "ParentOwner",
    "ParentLink",
    "ParentLinkFaviconImage",
    "ParentLinkPrimaryImage",
]


class Asset(BaseModel):
    id: str
    """A unique identifier for this resource."""

    filename: str

    height: float

    mime_type: str

    url: str

    width: float


class Owner(BaseModel):
    id: str
    """A unique identifier for this resource."""

    admin: bool

    handle: str
    """The unique @ handle of an account."""

    name: str
    """The account owners display name."""


class LinkFaviconImage(BaseModel):
    id: str
    """A unique identifier for this resource."""

    filename: str

    height: float

    mime_type: str

    url: str

    width: float


class LinkPrimaryImage(BaseModel):
    id: str
    """A unique identifier for this resource."""

    filename: str

    height: float

    mime_type: str

    url: str

    width: float


class Link(BaseModel):
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

    favicon_image: Optional[LinkFaviconImage] = None

    misc: Optional[object] = None
    """Arbitrary extra data stored with the resource."""

    primary_image: Optional[LinkPrimaryImage] = None

    title: Optional[str] = None


class ParentAsset(BaseModel):
    id: str
    """A unique identifier for this resource."""

    filename: str

    height: float

    mime_type: str

    url: str

    width: float


class ParentOwner(BaseModel):
    id: str
    """A unique identifier for this resource."""

    admin: bool

    handle: str
    """The unique @ handle of an account."""

    name: str
    """The account owners display name."""


class ParentLinkFaviconImage(BaseModel):
    id: str
    """A unique identifier for this resource."""

    filename: str

    height: float

    mime_type: str

    url: str

    width: float


class ParentLinkPrimaryImage(BaseModel):
    id: str
    """A unique identifier for this resource."""

    filename: str

    height: float

    mime_type: str

    url: str

    width: float


class ParentLink(BaseModel):
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

    favicon_image: Optional[ParentLinkFaviconImage] = None

    misc: Optional[object] = None
    """Arbitrary extra data stored with the resource."""

    primary_image: Optional[ParentLinkPrimaryImage] = None

    title: Optional[str] = None


class Parent(BaseModel):
    id: str
    """A unique identifier for this resource."""

    assets: List[ParentAsset]

    created_at: datetime = FieldInfo(alias="createdAt")
    """The time the resource was created."""

    description: str

    meta: Dict[str, object]
    """Arbitrary metadata for the resource."""

    name: str

    owner: ParentOwner
    """A minimal reference to an account."""

    slug: str
    """A URL-safe slug for uniquely identifying resources."""

    updated_at: datetime = FieldInfo(alias="updatedAt")
    """The time the resource was updated."""

    visibility: Literal["draft", "unlisted", "review", "published"]

    content: Optional[str] = None
    """The body text of a post within a thread.

    The type is either a string or an object, depending on what was used during
    creation. Strings can be used for basic plain text or markdown content and
    objects are used for more complex types such as Slate.js editor documents.
    """

    deleted_at: Optional[datetime] = FieldInfo(alias="deletedAt", default=None)
    """The time the resource was soft-deleted."""

    link: Optional[ParentLink] = None
    """A minimal object used to refer to a link without sending too much data."""

    misc: Optional[object] = None
    """Arbitrary extra data stored with the resource."""

    parent: Optional[object] = None

    relevance_score: Optional[float] = None
    """
    For recommendations and other uses, only available when a Semdex is configured
    for content indexing and contextual relativity scoring.
    """


class NodeUpdateResponse(BaseModel):
    id: str
    """A unique identifier for this resource."""

    assets: List[Asset]

    created_at: datetime = FieldInfo(alias="createdAt")
    """The time the resource was created."""

    description: str

    meta: Dict[str, object]
    """Arbitrary metadata for the resource."""

    name: str

    owner: Owner
    """A minimal reference to an account."""

    slug: str
    """A URL-safe slug for uniquely identifying resources."""

    updated_at: datetime = FieldInfo(alias="updatedAt")
    """The time the resource was updated."""

    visibility: Literal["draft", "unlisted", "review", "published"]

    content: Optional[str] = None
    """The body text of a post within a thread.

    The type is either a string or an object, depending on what was used during
    creation. Strings can be used for basic plain text or markdown content and
    objects are used for more complex types such as Slate.js editor documents.
    """

    deleted_at: Optional[datetime] = FieldInfo(alias="deletedAt", default=None)
    """The time the resource was soft-deleted."""

    link: Optional[Link] = None
    """A minimal object used to refer to a link without sending too much data."""

    misc: Optional[object] = None
    """Arbitrary extra data stored with the resource."""

    parent: Optional[Parent] = None
    """A node is a text document with children and assets.

    It serves as an abstraction for grouping structured data objects. It can
    represent things such as brands, manufacturers, authors, directors, etc. Nodes
    can be referenced in content posts and they also have their own content.
    """

    relevance_score: Optional[float] = None
    """
    For recommendations and other uses, only available when a Semdex is configured
    for content indexing and contextual relativity scoring.
    """
