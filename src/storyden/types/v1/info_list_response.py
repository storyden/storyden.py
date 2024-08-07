# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing_extensions import Literal

from ..._models import BaseModel

__all__ = ["InfoListResponse"]


class InfoListResponse(BaseModel):
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
