# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import httpx

from ...._types import NOT_GIVEN, Body, Query, Headers, NotGiven
from ...._compat import cached_property
from ...._resource import SyncAPIResource, AsyncAPIResource
from ...._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from ...._base_client import make_request_options
from ....types.v1.accounts.auth_method_list_response import AuthMethodListResponse
from ....types.v1.accounts.auth_method_delete_response import AuthMethodDeleteResponse

__all__ = ["AuthMethodsResource", "AsyncAuthMethodsResource"]


class AuthMethodsResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AuthMethodsResourceWithRawResponse:
        return AuthMethodsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AuthMethodsResourceWithStreamingResponse:
        return AuthMethodsResourceWithStreamingResponse(self)

    def list(
        self,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> AuthMethodListResponse:
        """
        Retrieve a list of authentication providers with a flag indicating which ones
        are active for the currently authenticated account.
        """
        return self._get(
            "/v1/accounts/self/auth-methods",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=AuthMethodListResponse,
        )

    def delete(
        self,
        auth_method_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> AuthMethodDeleteResponse:
        """
        Retrieve a list of authentication providers with a flag indicating which ones
        are active for the currently authenticated account.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not auth_method_id:
            raise ValueError(f"Expected a non-empty value for `auth_method_id` but received {auth_method_id!r}")
        return self._delete(
            f"/v1/accounts/self/auth-methods/{auth_method_id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=AuthMethodDeleteResponse,
        )


class AsyncAuthMethodsResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncAuthMethodsResourceWithRawResponse:
        return AsyncAuthMethodsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncAuthMethodsResourceWithStreamingResponse:
        return AsyncAuthMethodsResourceWithStreamingResponse(self)

    async def list(
        self,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> AuthMethodListResponse:
        """
        Retrieve a list of authentication providers with a flag indicating which ones
        are active for the currently authenticated account.
        """
        return await self._get(
            "/v1/accounts/self/auth-methods",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=AuthMethodListResponse,
        )

    async def delete(
        self,
        auth_method_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> AuthMethodDeleteResponse:
        """
        Retrieve a list of authentication providers with a flag indicating which ones
        are active for the currently authenticated account.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not auth_method_id:
            raise ValueError(f"Expected a non-empty value for `auth_method_id` but received {auth_method_id!r}")
        return await self._delete(
            f"/v1/accounts/self/auth-methods/{auth_method_id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=AuthMethodDeleteResponse,
        )


class AuthMethodsResourceWithRawResponse:
    def __init__(self, auth_methods: AuthMethodsResource) -> None:
        self._auth_methods = auth_methods

        self.list = to_raw_response_wrapper(
            auth_methods.list,
        )
        self.delete = to_raw_response_wrapper(
            auth_methods.delete,
        )


class AsyncAuthMethodsResourceWithRawResponse:
    def __init__(self, auth_methods: AsyncAuthMethodsResource) -> None:
        self._auth_methods = auth_methods

        self.list = async_to_raw_response_wrapper(
            auth_methods.list,
        )
        self.delete = async_to_raw_response_wrapper(
            auth_methods.delete,
        )


class AuthMethodsResourceWithStreamingResponse:
    def __init__(self, auth_methods: AuthMethodsResource) -> None:
        self._auth_methods = auth_methods

        self.list = to_streamed_response_wrapper(
            auth_methods.list,
        )
        self.delete = to_streamed_response_wrapper(
            auth_methods.delete,
        )


class AsyncAuthMethodsResourceWithStreamingResponse:
    def __init__(self, auth_methods: AsyncAuthMethodsResource) -> None:
        self._auth_methods = auth_methods

        self.list = async_to_streamed_response_wrapper(
            auth_methods.list,
        )
        self.delete = async_to_streamed_response_wrapper(
            auth_methods.delete,
        )
