# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from ..._models import BaseModel

from datetime import datetime

from typing import Optional

from typing import Optional, Union, List, Dict, Any
from typing_extensions import Literal
from pydantic import Field as FieldInfo
from ...types import shared

__all__ = ["NodeAddResponse", "Owner"]


class Owner(BaseModel):
    id: str
    """A unique identifier for this resource."""

    admin: bool

    handle: str
    """The unique @ handle of an account."""

    name: str
    """The account owners display name."""


class NodeAddResponse(BaseModel):
    id: str
    """A unique identifier for this resource."""

    created_at: datetime = FieldInfo(alias="createdAt")
    """The time the resource was created."""

    description: str

    name: str

    owner: Owner
    """A minimal reference to an account."""

    updated_at: datetime = FieldInfo(alias="updatedAt")
    """The time the resource was updated."""

    deleted_at: Optional[datetime] = FieldInfo(alias="deletedAt", default=None)
    """The time the resource was soft-deleted."""

    misc: Optional[object] = None
    """Arbitrary extra data stored with the resource."""
