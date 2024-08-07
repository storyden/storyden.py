# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from .._models import BaseModel

from typing import Optional, Union, List, Dict, Any
from typing_extensions import Literal
from pydantic import Field as FieldInfo
from ..types import shared

__all__ = ["AssetCreateResponse"]


class AssetCreateResponse(BaseModel):
    id: str
    """A unique identifier for this resource."""

    filename: str

    height: float

    mime_type: str

    url: str

    width: float
