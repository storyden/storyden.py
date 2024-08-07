# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from ..._models import BaseModel

from typing import List, Optional, Dict

from datetime import datetime

from typing_extensions import Literal

from typing import Optional, Union, List, Dict, Any
from typing_extensions import Literal
from pydantic import Field as FieldInfo
from ...types import shared

__all__ = [
    "AssetAddResponse",
    "Asset",
    "Owner",
    "Link",
    "LinkAsset",
    "Parent",
    "ParentAsset",
    "ParentOwner",
    "ParentLink",
    "ParentLinkAsset",
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


class ParentLinkAsset(BaseModel):
    id: str
    """A unique identifier for this resource."""

    filename: str

    height: float

    mime_type: str

    url: str

    width: float


class ParentLink(BaseModel):
    assets: List[ParentLinkAsset]

    domain: str

    slug: str

    url: str
    """A web address"""

    description: Optional[str] = None

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
    """A web address with content information such as title, description, etc."""

    misc: Optional[object] = None
    """Arbitrary extra data stored with the resource."""

    parent: Optional[object] = None

    relevance_score: Optional[float] = None
    """
    For recommendations and other uses, only available when a Semdex is configured
    for content indexing and contextual relativity scoring.
    """


class AssetAddResponse(BaseModel):
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
    """A web address with content information such as title, description, etc."""

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
