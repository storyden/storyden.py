# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from ...._models import BaseModel

from typing_extensions import Literal

from typing import Optional, List

from typing import Optional, Union, List, Dict, Any
from typing_extensions import Literal
from pydantic import Field as FieldInfo
from ....types import shared

__all__ = ["AssertStartResponse", "PublicKey", "PublicKeyAllowCredential"]


class PublicKeyAllowCredential(BaseModel):
    id: str

    type: Literal["public-key"]
    """https://www.w3.org/TR/webauthn-2/#enumdef-publickeycredentialtype"""

    transports: Optional[List[Literal["ble", "internal", "nfc", "usb", "cable", "hybrid"]]] = None


class PublicKey(BaseModel):
    challenge: str

    allow_credentials: Optional[List[PublicKeyAllowCredential]] = FieldInfo(alias="allowCredentials", default=None)

    rp_id: Optional[str] = FieldInfo(alias="rpId", default=None)

    timeout: Optional[int] = None

    user_verification: Optional[Literal["discouraged", "preferred", "required"]] = FieldInfo(
        alias="userVerification", default=None
    )


class AssertStartResponse(BaseModel):
    public_key: PublicKey = FieldInfo(alias="publicKey")
    """https://www.w3.org/TR/webauthn-2/#dictdef-publickeycredentialrequestoptions"""
