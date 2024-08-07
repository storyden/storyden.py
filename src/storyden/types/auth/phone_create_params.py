# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, TypedDict

__all__ = ["PhoneCreateParams"]


class PhoneCreateParams(TypedDict, total=False):
    identifier: Required[str]
    """The desired username to link to the phone number."""

    phone_number: Required[str]
    """The phone number to receive the one-time code on."""
