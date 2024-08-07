# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import httpx

from ..._types import NOT_GIVEN, Body, Query, Headers, NotGiven
from ..._utils import (
    maybe_transform,
    async_maybe_transform,
)
from ..._compat import cached_property
from ..._resource import SyncAPIResource, AsyncAPIResource
from ..._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from ...types.auth import password_create_params, password_signin_params, password_update_params
from ..._base_client import make_request_options
from ...types.auth.password_create_response import PasswordCreateResponse
from ...types.auth.password_signin_response import PasswordSigninResponse
from ...types.auth.password_update_response import PasswordUpdateResponse

__all__ = ["PasswordResource", "AsyncPasswordResource"]


class PasswordResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> PasswordResourceWithRawResponse:
        return PasswordResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> PasswordResourceWithStreamingResponse:
        return PasswordResourceWithStreamingResponse(self)

    def create(
        self,
        *,
        password: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> PasswordCreateResponse:
        """
        Given the requesting account does not have a password authentication, add a
        password authentication method to it with the given password.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/v1/auth/password",
            body=maybe_transform({"password": password}, password_create_params.PasswordCreateParams),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=PasswordCreateResponse,
        )

    def update(
        self,
        *,
        new: str,
        old: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> PasswordUpdateResponse:
        """
        Given the requesting account has a password authentication, update the password
        on file.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._patch(
            "/v1/auth/password",
            body=maybe_transform(
                {
                    "new": new,
                    "old": old,
                },
                password_update_params.PasswordUpdateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=PasswordUpdateResponse,
        )

    def signin(
        self,
        *,
        token: str,
        identifier: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> PasswordSigninResponse:
        """
        Sign in to an existing account with a username and password.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/v1/auth/password/signin",
            body=maybe_transform(
                {
                    "token": token,
                    "identifier": identifier,
                },
                password_signin_params.PasswordSigninParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=PasswordSigninResponse,
        )


class AsyncPasswordResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncPasswordResourceWithRawResponse:
        return AsyncPasswordResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncPasswordResourceWithStreamingResponse:
        return AsyncPasswordResourceWithStreamingResponse(self)

    async def create(
        self,
        *,
        password: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> PasswordCreateResponse:
        """
        Given the requesting account does not have a password authentication, add a
        password authentication method to it with the given password.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/v1/auth/password",
            body=await async_maybe_transform({"password": password}, password_create_params.PasswordCreateParams),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=PasswordCreateResponse,
        )

    async def update(
        self,
        *,
        new: str,
        old: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> PasswordUpdateResponse:
        """
        Given the requesting account has a password authentication, update the password
        on file.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._patch(
            "/v1/auth/password",
            body=await async_maybe_transform(
                {
                    "new": new,
                    "old": old,
                },
                password_update_params.PasswordUpdateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=PasswordUpdateResponse,
        )

    async def signin(
        self,
        *,
        token: str,
        identifier: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> PasswordSigninResponse:
        """
        Sign in to an existing account with a username and password.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/v1/auth/password/signin",
            body=await async_maybe_transform(
                {
                    "token": token,
                    "identifier": identifier,
                },
                password_signin_params.PasswordSigninParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=PasswordSigninResponse,
        )


class PasswordResourceWithRawResponse:
    def __init__(self, password: PasswordResource) -> None:
        self._password = password

        self.create = to_raw_response_wrapper(
            password.create,
        )
        self.update = to_raw_response_wrapper(
            password.update,
        )
        self.signin = to_raw_response_wrapper(
            password.signin,
        )


class AsyncPasswordResourceWithRawResponse:
    def __init__(self, password: AsyncPasswordResource) -> None:
        self._password = password

        self.create = async_to_raw_response_wrapper(
            password.create,
        )
        self.update = async_to_raw_response_wrapper(
            password.update,
        )
        self.signin = async_to_raw_response_wrapper(
            password.signin,
        )


class PasswordResourceWithStreamingResponse:
    def __init__(self, password: PasswordResource) -> None:
        self._password = password

        self.create = to_streamed_response_wrapper(
            password.create,
        )
        self.update = to_streamed_response_wrapper(
            password.update,
        )
        self.signin = to_streamed_response_wrapper(
            password.signin,
        )


class AsyncPasswordResourceWithStreamingResponse:
    def __init__(self, password: AsyncPasswordResource) -> None:
        self._password = password

        self.create = async_to_streamed_response_wrapper(
            password.create,
        )
        self.update = async_to_streamed_response_wrapper(
            password.update,
        )
        self.signin = async_to_streamed_response_wrapper(
            password.signin,
        )
