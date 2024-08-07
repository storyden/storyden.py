# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import httpx

from ..._compat import cached_property

from ...types.auth.email_password_signin_response import EmailPasswordSigninResponse

from ..._utils import maybe_transform, async_maybe_transform

from ..._base_client import make_request_options

from ...types.auth.email_password_signup_response import EmailPasswordSignupResponse

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
from ...types.auth import email_password_signin_params
from ...types.auth import email_password_signup_params

__all__ = ["EmailPasswordResource", "AsyncEmailPasswordResource"]


class EmailPasswordResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> EmailPasswordResourceWithRawResponse:
        return EmailPasswordResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> EmailPasswordResourceWithStreamingResponse:
        return EmailPasswordResourceWithStreamingResponse(self)

    def signin(
        self,
        *,
        email: str,
        password: str,
        handle: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> EmailPasswordSigninResponse:
        """
        Sign in to an existing account with a email and password.

        Args:
          handle: The unique @ handle of an account.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/v1/auth/email-password/signin",
            body=maybe_transform(
                {
                    "email": email,
                    "password": password,
                    "handle": handle,
                },
                email_password_signin_params.EmailPasswordSigninParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=EmailPasswordSigninResponse,
        )

    def signup(
        self,
        *,
        email: str,
        password: str,
        handle: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> EmailPasswordSignupResponse:
        """
        Register a new account with a email and password.

        Args:
          handle: The unique @ handle of an account.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/v1/auth/email-password/signup",
            body=maybe_transform(
                {
                    "email": email,
                    "password": password,
                    "handle": handle,
                },
                email_password_signup_params.EmailPasswordSignupParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=EmailPasswordSignupResponse,
        )


class AsyncEmailPasswordResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncEmailPasswordResourceWithRawResponse:
        return AsyncEmailPasswordResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncEmailPasswordResourceWithStreamingResponse:
        return AsyncEmailPasswordResourceWithStreamingResponse(self)

    async def signin(
        self,
        *,
        email: str,
        password: str,
        handle: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> EmailPasswordSigninResponse:
        """
        Sign in to an existing account with a email and password.

        Args:
          handle: The unique @ handle of an account.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/v1/auth/email-password/signin",
            body=await async_maybe_transform(
                {
                    "email": email,
                    "password": password,
                    "handle": handle,
                },
                email_password_signin_params.EmailPasswordSigninParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=EmailPasswordSigninResponse,
        )

    async def signup(
        self,
        *,
        email: str,
        password: str,
        handle: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> EmailPasswordSignupResponse:
        """
        Register a new account with a email and password.

        Args:
          handle: The unique @ handle of an account.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/v1/auth/email-password/signup",
            body=await async_maybe_transform(
                {
                    "email": email,
                    "password": password,
                    "handle": handle,
                },
                email_password_signup_params.EmailPasswordSignupParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=EmailPasswordSignupResponse,
        )


class EmailPasswordResourceWithRawResponse:
    def __init__(self, email_password: EmailPasswordResource) -> None:
        self._email_password = email_password

        self.signin = to_raw_response_wrapper(
            email_password.signin,
        )
        self.signup = to_raw_response_wrapper(
            email_password.signup,
        )


class AsyncEmailPasswordResourceWithRawResponse:
    def __init__(self, email_password: AsyncEmailPasswordResource) -> None:
        self._email_password = email_password

        self.signin = async_to_raw_response_wrapper(
            email_password.signin,
        )
        self.signup = async_to_raw_response_wrapper(
            email_password.signup,
        )


class EmailPasswordResourceWithStreamingResponse:
    def __init__(self, email_password: EmailPasswordResource) -> None:
        self._email_password = email_password

        self.signin = to_streamed_response_wrapper(
            email_password.signin,
        )
        self.signup = to_streamed_response_wrapper(
            email_password.signup,
        )


class AsyncEmailPasswordResourceWithStreamingResponse:
    def __init__(self, email_password: AsyncEmailPasswordResource) -> None:
        self._email_password = email_password

        self.signin = async_to_streamed_response_wrapper(
            email_password.signin,
        )
        self.signup = async_to_streamed_response_wrapper(
            email_password.signup,
        )
