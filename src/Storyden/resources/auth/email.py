# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import httpx

from ..._compat import cached_property

from ...types.auth.email_signin_response import EmailSigninResponse

from ..._utils import maybe_transform, async_maybe_transform

from ..._base_client import make_request_options

from ...types.auth.email_signup_response import EmailSignupResponse

from ...types.auth.email_verify_response import EmailVerifyResponse

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
from ...types.auth import email_signin_params
from ...types.auth import email_signup_params
from ...types.auth import email_verify_params

__all__ = ["EmailResource", "AsyncEmailResource"]


class EmailResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> EmailResourceWithRawResponse:
        return EmailResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> EmailResourceWithStreamingResponse:
        return EmailResourceWithStreamingResponse(self)

    def signin(
        self,
        *,
        email: str,
        handle: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> EmailSigninResponse:
        """Sign in to an existing account with an email and optional password.

        The
        behaviour of this endpoint depends on how the instance is configured. If
        email+password is the preferred method, a cookie is returned on success but if
        magic links are preferred, the endpoint will start the code flow.

        Args:
          handle: The unique @ handle of an account.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/v1/auth/email/signin",
            body=maybe_transform(
                {
                    "email": email,
                    "handle": handle,
                },
                email_signin_params.EmailSigninParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=EmailSigninResponse,
        )

    def signup(
        self,
        *,
        email: str,
        handle: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> EmailSignupResponse:
        """Register a new account with an email and optional password.

        The password
        requirement is dependent on how the instance is configured for account
        authentication with email addresses (password vs magic link.)

        When the email address has not been registered, this endpoint will send a
        verification email however it will also return a session cookie to facilitate
        pre-verification usage of the platform. If the email address already exists, no
        session cookie will be returned in order to prevent arbitrary account control by
        a malicious actor. In this case, the email will be sent again with the same OTP
        for the case where the user has cleared their cookies or switched device but
        hasn't yet verified due to missing the email or a delivery failure. In this
        sense, the endpoint can act as a "resend verification email" operation as well
        as registration.

        In the first case, a 200 response is provided with the session cookie, in the
        second case, a 422 response is provided without a session cookie.

        Given that this is an unauthenticated endpoint that triggers an email to be sent
        to any public address, it MUST be heavily rate limited.

        Args:
          handle: The unique @ handle of an account.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/v1/auth/email/signup",
            body=maybe_transform(
                {
                    "email": email,
                    "handle": handle,
                },
                email_signup_params.EmailSignupParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=EmailSignupResponse,
        )

    def verify(
        self,
        *,
        code: str,
        email: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> EmailVerifyResponse:
        """
        Verify an email address using a token that was emailed to one of the account's
        email addresses either set via sign up or added later.

        Args:
          email: The email address to be verified, only necessary for when submitting a
              verification without a session cookie present.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/v1/auth/email/verify",
            body=maybe_transform(
                {
                    "code": code,
                    "email": email,
                },
                email_verify_params.EmailVerifyParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=EmailVerifyResponse,
        )


class AsyncEmailResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncEmailResourceWithRawResponse:
        return AsyncEmailResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncEmailResourceWithStreamingResponse:
        return AsyncEmailResourceWithStreamingResponse(self)

    async def signin(
        self,
        *,
        email: str,
        handle: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> EmailSigninResponse:
        """Sign in to an existing account with an email and optional password.

        The
        behaviour of this endpoint depends on how the instance is configured. If
        email+password is the preferred method, a cookie is returned on success but if
        magic links are preferred, the endpoint will start the code flow.

        Args:
          handle: The unique @ handle of an account.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/v1/auth/email/signin",
            body=await async_maybe_transform(
                {
                    "email": email,
                    "handle": handle,
                },
                email_signin_params.EmailSigninParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=EmailSigninResponse,
        )

    async def signup(
        self,
        *,
        email: str,
        handle: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> EmailSignupResponse:
        """Register a new account with an email and optional password.

        The password
        requirement is dependent on how the instance is configured for account
        authentication with email addresses (password vs magic link.)

        When the email address has not been registered, this endpoint will send a
        verification email however it will also return a session cookie to facilitate
        pre-verification usage of the platform. If the email address already exists, no
        session cookie will be returned in order to prevent arbitrary account control by
        a malicious actor. In this case, the email will be sent again with the same OTP
        for the case where the user has cleared their cookies or switched device but
        hasn't yet verified due to missing the email or a delivery failure. In this
        sense, the endpoint can act as a "resend verification email" operation as well
        as registration.

        In the first case, a 200 response is provided with the session cookie, in the
        second case, a 422 response is provided without a session cookie.

        Given that this is an unauthenticated endpoint that triggers an email to be sent
        to any public address, it MUST be heavily rate limited.

        Args:
          handle: The unique @ handle of an account.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/v1/auth/email/signup",
            body=await async_maybe_transform(
                {
                    "email": email,
                    "handle": handle,
                },
                email_signup_params.EmailSignupParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=EmailSignupResponse,
        )

    async def verify(
        self,
        *,
        code: str,
        email: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> EmailVerifyResponse:
        """
        Verify an email address using a token that was emailed to one of the account's
        email addresses either set via sign up or added later.

        Args:
          email: The email address to be verified, only necessary for when submitting a
              verification without a session cookie present.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/v1/auth/email/verify",
            body=await async_maybe_transform(
                {
                    "code": code,
                    "email": email,
                },
                email_verify_params.EmailVerifyParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=EmailVerifyResponse,
        )


class EmailResourceWithRawResponse:
    def __init__(self, email: EmailResource) -> None:
        self._email = email

        self.signin = to_raw_response_wrapper(
            email.signin,
        )
        self.signup = to_raw_response_wrapper(
            email.signup,
        )
        self.verify = to_raw_response_wrapper(
            email.verify,
        )


class AsyncEmailResourceWithRawResponse:
    def __init__(self, email: AsyncEmailResource) -> None:
        self._email = email

        self.signin = async_to_raw_response_wrapper(
            email.signin,
        )
        self.signup = async_to_raw_response_wrapper(
            email.signup,
        )
        self.verify = async_to_raw_response_wrapper(
            email.verify,
        )


class EmailResourceWithStreamingResponse:
    def __init__(self, email: EmailResource) -> None:
        self._email = email

        self.signin = to_streamed_response_wrapper(
            email.signin,
        )
        self.signup = to_streamed_response_wrapper(
            email.signup,
        )
        self.verify = to_streamed_response_wrapper(
            email.verify,
        )


class AsyncEmailResourceWithStreamingResponse:
    def __init__(self, email: AsyncEmailResource) -> None:
        self._email = email

        self.signin = async_to_streamed_response_wrapper(
            email.signin,
        )
        self.signup = async_to_streamed_response_wrapper(
            email.signup,
        )
        self.verify = async_to_streamed_response_wrapper(
            email.verify,
        )
