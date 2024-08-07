# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from ..._models import BaseModel

from typing import Optional

from typing import Optional, Union, List, Dict, Any
from typing_extensions import Literal
from pydantic import Field as FieldInfo
from ...types import shared

__all__ = ["ReactUpdateResponse"]


class ReactUpdateResponse(BaseModel):
    id: Optional[str] = None
    """A unique identifier for this resource."""

    emoji: Optional[str] = None
