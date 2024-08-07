# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from ..._models import BaseModel

from typing_extensions import Literal

from typing import Optional, Union, List, Dict, Any
from typing_extensions import Literal
from pydantic import Field as FieldInfo
from ...types import shared

__all__ = ["InfoRetrieveResponse"]


class InfoRetrieveResponse(BaseModel):
    accent_colour: str

    description: str

    onboarding_status: Literal[
        "requires_first_account", "requires_category", "requires_more_accounts", "requires_first_post", "complete"
    ]
    """
    Derived from data state, indicates what stage in the onboarding process the
    Storyden installation is in for directing first-time setup steps.
    """

    title: str
