# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import httpx

from .password import PasswordResource, AsyncPasswordResource

from ..._compat import cached_property

from .email_password import EmailPasswordResource, AsyncEmailPasswordResource

from .email import EmailResource, AsyncEmailResource

from .oauth import OAuthResource, AsyncOAuthResource

from .webauthn.webauthn import WebauthnResource, AsyncWebauthnResource

from .phone import PhoneResource, AsyncPhoneResource

from ...types.auth_list_response import AuthListResponse

from ..._base_client import make_request_options

from ..._response import (
    to_raw_response_wrapper,
    async_to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_streamed_response_wrapper,
)

import warnings
from typing import TYPE_CHECKING, Optional, Union, List, Dict, Any, Mapping, cast, overload
from typing_extensions import Literal
from ..._utils import extract_files, maybe_transform, required_args, deepcopy_minimal, strip_not_given
from ..._types import NotGiven, Timeout, Headers, NoneType, Query, Body, NOT_GIVEN, FileTypes, BinaryResponseContent
from ..._resource import SyncAPIResource, AsyncAPIResource
from ...types import shared_params
from .password import (
    PasswordResource,
    AsyncPasswordResource,
    PasswordResourceWithRawResponse,
    AsyncPasswordResourceWithRawResponse,
    PasswordResourceWithStreamingResponse,
    AsyncPasswordResourceWithStreamingResponse,
)
from .email_password import (
    EmailPasswordResource,
    AsyncEmailPasswordResource,
    EmailPasswordResourceWithRawResponse,
    AsyncEmailPasswordResourceWithRawResponse,
    EmailPasswordResourceWithStreamingResponse,
    AsyncEmailPasswordResourceWithStreamingResponse,
)
from .email import (
    EmailResource,
    AsyncEmailResource,
    EmailResourceWithRawResponse,
    AsyncEmailResourceWithRawResponse,
    EmailResourceWithStreamingResponse,
    AsyncEmailResourceWithStreamingResponse,
)
from .oauth import (
    OAuthResource,
    AsyncOAuthResource,
    OAuthResourceWithRawResponse,
    AsyncOAuthResourceWithRawResponse,
    OAuthResourceWithStreamingResponse,
    AsyncOAuthResourceWithStreamingResponse,
)
from .webauthn import (
    WebauthnResource,
    AsyncWebauthnResource,
    WebauthnResourceWithRawResponse,
    AsyncWebauthnResourceWithRawResponse,
    WebauthnResourceWithStreamingResponse,
    AsyncWebauthnResourceWithStreamingResponse,
)
from .phone import (
    PhoneResource,
    AsyncPhoneResource,
    PhoneResourceWithRawResponse,
    AsyncPhoneResourceWithRawResponse,
    PhoneResourceWithStreamingResponse,
    AsyncPhoneResourceWithStreamingResponse,
)

__all__ = ["AuthResource", "AsyncAuthResource"]


class AuthResource(SyncAPIResource):
    @cached_property
    def password(self) -> PasswordResource:
        return PasswordResource(self._client)

    @cached_property
    def email_password(self) -> EmailPasswordResource:
        return EmailPasswordResource(self._client)

    @cached_property
    def email(self) -> EmailResource:
        return EmailResource(self._client)

    @cached_property
    def oauth(self) -> OAuthResource:
        return OAuthResource(self._client)

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

    def list(
        self,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> AuthListResponse:
        """Retrieve a list of authentication providers.

        Storyden supports a few ways to
        authenticate, from simple passwords to OAuth and WebAuthn. This endpoint tells a
        client which auth capabilities are enabled.
        """
        return self._get(
            "/v1/auth",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=AuthListResponse,
        )

    def logout(
        self,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> None:
        """Remove cookies from requesting client."""
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return self._get(
            "/v1/auth/logout",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )


class AsyncAuthResource(AsyncAPIResource):
    @cached_property
    def password(self) -> AsyncPasswordResource:
        return AsyncPasswordResource(self._client)

    @cached_property
    def email_password(self) -> AsyncEmailPasswordResource:
        return AsyncEmailPasswordResource(self._client)

    @cached_property
    def email(self) -> AsyncEmailResource:
        return AsyncEmailResource(self._client)

    @cached_property
    def oauth(self) -> AsyncOAuthResource:
        return AsyncOAuthResource(self._client)

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

    async def list(
        self,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> AuthListResponse:
        """Retrieve a list of authentication providers.

        Storyden supports a few ways to
        authenticate, from simple passwords to OAuth and WebAuthn. This endpoint tells a
        client which auth capabilities are enabled.
        """
        return await self._get(
            "/v1/auth",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=AuthListResponse,
        )

    async def logout(
        self,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> None:
        """Remove cookies from requesting client."""
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return await self._get(
            "/v1/auth/logout",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )


class AuthResourceWithRawResponse:
    def __init__(self, auth: AuthResource) -> None:
        self._auth = auth

        self.list = to_raw_response_wrapper(
            auth.list,
        )
        self.logout = to_raw_response_wrapper(
            auth.logout,
        )

    @cached_property
    def password(self) -> PasswordResourceWithRawResponse:
        return PasswordResourceWithRawResponse(self._auth.password)

    @cached_property
    def email_password(self) -> EmailPasswordResourceWithRawResponse:
        return EmailPasswordResourceWithRawResponse(self._auth.email_password)

    @cached_property
    def email(self) -> EmailResourceWithRawResponse:
        return EmailResourceWithRawResponse(self._auth.email)

    @cached_property
    def oauth(self) -> OAuthResourceWithRawResponse:
        return OAuthResourceWithRawResponse(self._auth.oauth)

    @cached_property
    def webauthn(self) -> WebauthnResourceWithRawResponse:
        return WebauthnResourceWithRawResponse(self._auth.webauthn)

    @cached_property
    def phone(self) -> PhoneResourceWithRawResponse:
        return PhoneResourceWithRawResponse(self._auth.phone)


class AsyncAuthResourceWithRawResponse:
    def __init__(self, auth: AsyncAuthResource) -> None:
        self._auth = auth

        self.list = async_to_raw_response_wrapper(
            auth.list,
        )
        self.logout = async_to_raw_response_wrapper(
            auth.logout,
        )

    @cached_property
    def password(self) -> AsyncPasswordResourceWithRawResponse:
        return AsyncPasswordResourceWithRawResponse(self._auth.password)

    @cached_property
    def email_password(self) -> AsyncEmailPasswordResourceWithRawResponse:
        return AsyncEmailPasswordResourceWithRawResponse(self._auth.email_password)

    @cached_property
    def email(self) -> AsyncEmailResourceWithRawResponse:
        return AsyncEmailResourceWithRawResponse(self._auth.email)

    @cached_property
    def oauth(self) -> AsyncOAuthResourceWithRawResponse:
        return AsyncOAuthResourceWithRawResponse(self._auth.oauth)

    @cached_property
    def webauthn(self) -> AsyncWebauthnResourceWithRawResponse:
        return AsyncWebauthnResourceWithRawResponse(self._auth.webauthn)

    @cached_property
    def phone(self) -> AsyncPhoneResourceWithRawResponse:
        return AsyncPhoneResourceWithRawResponse(self._auth.phone)


class AuthResourceWithStreamingResponse:
    def __init__(self, auth: AuthResource) -> None:
        self._auth = auth

        self.list = to_streamed_response_wrapper(
            auth.list,
        )
        self.logout = to_streamed_response_wrapper(
            auth.logout,
        )

    @cached_property
    def password(self) -> PasswordResourceWithStreamingResponse:
        return PasswordResourceWithStreamingResponse(self._auth.password)

    @cached_property
    def email_password(self) -> EmailPasswordResourceWithStreamingResponse:
        return EmailPasswordResourceWithStreamingResponse(self._auth.email_password)

    @cached_property
    def email(self) -> EmailResourceWithStreamingResponse:
        return EmailResourceWithStreamingResponse(self._auth.email)

    @cached_property
    def oauth(self) -> OAuthResourceWithStreamingResponse:
        return OAuthResourceWithStreamingResponse(self._auth.oauth)

    @cached_property
    def webauthn(self) -> WebauthnResourceWithStreamingResponse:
        return WebauthnResourceWithStreamingResponse(self._auth.webauthn)

    @cached_property
    def phone(self) -> PhoneResourceWithStreamingResponse:
        return PhoneResourceWithStreamingResponse(self._auth.phone)


class AsyncAuthResourceWithStreamingResponse:
    def __init__(self, auth: AsyncAuthResource) -> None:
        self._auth = auth

        self.list = async_to_streamed_response_wrapper(
            auth.list,
        )
        self.logout = async_to_streamed_response_wrapper(
            auth.logout,
        )

    @cached_property
    def password(self) -> AsyncPasswordResourceWithStreamingResponse:
        return AsyncPasswordResourceWithStreamingResponse(self._auth.password)

    @cached_property
    def email_password(self) -> AsyncEmailPasswordResourceWithStreamingResponse:
        return AsyncEmailPasswordResourceWithStreamingResponse(self._auth.email_password)

    @cached_property
    def email(self) -> AsyncEmailResourceWithStreamingResponse:
        return AsyncEmailResourceWithStreamingResponse(self._auth.email)

    @cached_property
    def oauth(self) -> AsyncOAuthResourceWithStreamingResponse:
        return AsyncOAuthResourceWithStreamingResponse(self._auth.oauth)

    @cached_property
    def webauthn(self) -> AsyncWebauthnResourceWithStreamingResponse:
        return AsyncWebauthnResourceWithStreamingResponse(self._auth.webauthn)

    @cached_property
    def phone(self) -> AsyncPhoneResourceWithStreamingResponse:
        return AsyncPhoneResourceWithStreamingResponse(self._auth.phone)
