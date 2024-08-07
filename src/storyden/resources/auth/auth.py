# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from .phone import (
    PhoneResource,
    AsyncPhoneResource,
    PhoneResourceWithRawResponse,
    AsyncPhoneResourceWithRawResponse,
    PhoneResourceWithStreamingResponse,
    AsyncPhoneResourceWithStreamingResponse,
)
from .password import (
    PasswordResource,
    AsyncPasswordResource,
    PasswordResourceWithRawResponse,
    AsyncPasswordResourceWithRawResponse,
    PasswordResourceWithStreamingResponse,
    AsyncPasswordResourceWithStreamingResponse,
)
from .webauthn import (
    WebauthnResource,
    AsyncWebauthnResource,
    WebauthnResourceWithRawResponse,
    AsyncWebauthnResourceWithRawResponse,
    WebauthnResourceWithStreamingResponse,
    AsyncWebauthnResourceWithStreamingResponse,
)
from ..._compat import cached_property
from ..._resource import SyncAPIResource, AsyncAPIResource
from .oauth_callback import (
    OAuthCallbackResource,
    AsyncOAuthCallbackResource,
    OAuthCallbackResourceWithRawResponse,
    AsyncOAuthCallbackResourceWithRawResponse,
    OAuthCallbackResourceWithStreamingResponse,
    AsyncOAuthCallbackResourceWithStreamingResponse,
)
from .webauthn.webauthn import WebauthnResource, AsyncWebauthnResource

__all__ = ["AuthResource", "AsyncAuthResource"]


class AuthResource(SyncAPIResource):
    @cached_property
    def password(self) -> PasswordResource:
        return PasswordResource(self._client)

    @cached_property
    def oauth_callback(self) -> OAuthCallbackResource:
        return OAuthCallbackResource(self._client)

    @cached_property
    def webauthn(self) -> WebauthnResource:
        return WebauthnResource(self._client)

    @cached_property
    def phone(self) -> PhoneResource:
        return PhoneResource(self._client)

    @cached_property
    def with_raw_response(self) -> AuthResourceWithRawResponse:
        return AuthResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AuthResourceWithStreamingResponse:
        return AuthResourceWithStreamingResponse(self)


class AsyncAuthResource(AsyncAPIResource):
    @cached_property
    def password(self) -> AsyncPasswordResource:
        return AsyncPasswordResource(self._client)

    @cached_property
    def oauth_callback(self) -> AsyncOAuthCallbackResource:
        return AsyncOAuthCallbackResource(self._client)

    @cached_property
    def webauthn(self) -> AsyncWebauthnResource:
        return AsyncWebauthnResource(self._client)

    @cached_property
    def phone(self) -> AsyncPhoneResource:
        return AsyncPhoneResource(self._client)

    @cached_property
    def with_raw_response(self) -> AsyncAuthResourceWithRawResponse:
        return AsyncAuthResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncAuthResourceWithStreamingResponse:
        return AsyncAuthResourceWithStreamingResponse(self)


class AuthResourceWithRawResponse:
    def __init__(self, auth: AuthResource) -> None:
        self._auth = auth

    @cached_property
    def password(self) -> PasswordResourceWithRawResponse:
        return PasswordResourceWithRawResponse(self._auth.password)

    @cached_property
    def oauth_callback(self) -> OAuthCallbackResourceWithRawResponse:
        return OAuthCallbackResourceWithRawResponse(self._auth.oauth_callback)

    @cached_property
    def webauthn(self) -> WebauthnResourceWithRawResponse:
        return WebauthnResourceWithRawResponse(self._auth.webauthn)

    @cached_property
    def phone(self) -> PhoneResourceWithRawResponse:
        return PhoneResourceWithRawResponse(self._auth.phone)


class AsyncAuthResourceWithRawResponse:
    def __init__(self, auth: AsyncAuthResource) -> None:
        self._auth = auth

    @cached_property
    def password(self) -> AsyncPasswordResourceWithRawResponse:
        return AsyncPasswordResourceWithRawResponse(self._auth.password)

    @cached_property
    def oauth_callback(self) -> AsyncOAuthCallbackResourceWithRawResponse:
        return AsyncOAuthCallbackResourceWithRawResponse(self._auth.oauth_callback)

    @cached_property
    def webauthn(self) -> AsyncWebauthnResourceWithRawResponse:
        return AsyncWebauthnResourceWithRawResponse(self._auth.webauthn)

    @cached_property
    def phone(self) -> AsyncPhoneResourceWithRawResponse:
        return AsyncPhoneResourceWithRawResponse(self._auth.phone)


class AuthResourceWithStreamingResponse:
    def __init__(self, auth: AuthResource) -> None:
        self._auth = auth

    @cached_property
    def password(self) -> PasswordResourceWithStreamingResponse:
        return PasswordResourceWithStreamingResponse(self._auth.password)

    @cached_property
    def oauth_callback(self) -> OAuthCallbackResourceWithStreamingResponse:
        return OAuthCallbackResourceWithStreamingResponse(self._auth.oauth_callback)

    @cached_property
    def webauthn(self) -> WebauthnResourceWithStreamingResponse:
        return WebauthnResourceWithStreamingResponse(self._auth.webauthn)

    @cached_property
    def phone(self) -> PhoneResourceWithStreamingResponse:
        return PhoneResourceWithStreamingResponse(self._auth.phone)


class AsyncAuthResourceWithStreamingResponse:
    def __init__(self, auth: AsyncAuthResource) -> None:
        self._auth = auth

    @cached_property
    def password(self) -> AsyncPasswordResourceWithStreamingResponse:
        return AsyncPasswordResourceWithStreamingResponse(self._auth.password)

    @cached_property
    def oauth_callback(self) -> AsyncOAuthCallbackResourceWithStreamingResponse:
        return AsyncOAuthCallbackResourceWithStreamingResponse(self._auth.oauth_callback)

    @cached_property
    def webauthn(self) -> AsyncWebauthnResourceWithStreamingResponse:
        return AsyncWebauthnResourceWithStreamingResponse(self._auth.webauthn)

    @cached_property
    def phone(self) -> AsyncPhoneResourceWithStreamingResponse:
        return AsyncPhoneResourceWithStreamingResponse(self._auth.phone)
