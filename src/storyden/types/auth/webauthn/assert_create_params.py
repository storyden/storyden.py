# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List
from typing_extensions import Required, Annotated, TypedDict

from ...._utils import PropertyInfo

__all__ = ["AssertCreateParams", "Response"]


class AssertCreateParams(TypedDict, total=False):
    id: Required[str]

    raw_id: Required[Annotated[str, PropertyInfo(alias="rawId")]]

    response: Required[Response]
    """https://www.w3.org/TR/webauthn-2/#authenticatorresponse"""

    type: Required[str]

    authenticator_attachment: Annotated[str, PropertyInfo(alias="authenticatorAttachment")]

    client_extension_results: Annotated[object, PropertyInfo(alias="clientExtensionResults")]


class Response(TypedDict, total=False):
    client_data_json: Required[Annotated[str, PropertyInfo(alias="clientDataJSON")]]

    attestation_object: Annotated[str, PropertyInfo(alias="attestationObject")]

    authenticator_data: Annotated[str, PropertyInfo(alias="authenticatorData")]

    signature: str

    transports: List[str]

    user_handle: Annotated[str, PropertyInfo(alias="userHandle")]
