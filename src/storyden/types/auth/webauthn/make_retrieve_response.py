# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Dict, List, Optional
from typing_extensions import Literal

from pydantic import Field as FieldInfo

from ...._models import BaseModel

__all__ = [
    "MakeRetrieveResponse",
    "PublicKey",
    "PublicKeyExcludeCredential",
    "PublicKeyPubKeyCredParam",
    "PublicKeyRp",
    "PublicKeyUser",
    "PublicKeyAuthenticatorSelection",
]


class PublicKeyExcludeCredential(BaseModel):
    id: str

    type: Literal["public-key"]
    """https://www.w3.org/TR/webauthn-2/#enumdef-publickeycredentialtype"""

    transports: Optional[List[Literal["ble", "internal", "nfc", "usb", "cable", "hybrid"]]] = None


class PublicKeyPubKeyCredParam(BaseModel):
    alg: float

    type: Literal["public-key"]
    """https://www.w3.org/TR/webauthn-2/#enumdef-publickeycredentialtype"""


class PublicKeyRp(BaseModel):
    id: str

    name: str


class PublicKeyUser(BaseModel):
    id: str

    display_name: str = FieldInfo(alias="displayName")

    name: str


class PublicKeyAuthenticatorSelection(BaseModel):
    authenticator_attachment: Literal["platform", "cross-platform"] = FieldInfo(alias="authenticatorAttachment")
    """https://www.w3.org/TR/webauthn-2/#enumdef-authenticatorattachment"""

    resident_key: Literal["discouraged", "preferred", "required"] = FieldInfo(alias="residentKey")
    """https://www.w3.org/TR/webauthn-2/#enumdef-residentkeyrequirement"""

    require_resident_key: Optional[bool] = FieldInfo(alias="requireResidentKey", default=None)

    user_verification: Optional[Literal["discouraged", "preferred", "required"]] = FieldInfo(
        alias="userVerification", default=None
    )
    """https://www.w3.org/TR/webauthn-2/#enumdef-userverificationrequirement"""


class PublicKey(BaseModel):
    challenge: str

    exclude_credentials: List[PublicKeyExcludeCredential] = FieldInfo(alias="excludeCredentials")

    pub_key_cred_params: List[PublicKeyPubKeyCredParam] = FieldInfo(alias="pubKeyCredParams")

    rp: PublicKeyRp
    """https://www.w3.org/TR/webauthn-2/#dictdef-publickeycredentialrpentity"""

    user: PublicKeyUser
    """https://www.w3.org/TR/webauthn-2/#dictdef-publickeycredentialuserentity"""

    attestation: Optional[Literal["direct", "enterprise", "indirect", "none"]] = None
    """https://www.w3.org/TR/webauthn-2/#enum-attestation-convey"""

    authenticator_selection: Optional[PublicKeyAuthenticatorSelection] = FieldInfo(
        alias="authenticatorSelection", default=None
    )
    """https://www.w3.org/TR/webauthn-2/#dictdef-authenticatorselectioncriteria"""

    extensions: Optional[Dict[str, object]] = None
    """https://www.w3.org/TR/webauthn-2/#dictdef-authenticationextensionsclientinputs"""

    timeout: Optional[int] = None


class MakeRetrieveResponse(BaseModel):
    public_key: PublicKey = FieldInfo(alias="publicKey")
    """https://www.w3.org/TR/webautehn-2/#dictdef-publickeycredentialcreationoptions"""
