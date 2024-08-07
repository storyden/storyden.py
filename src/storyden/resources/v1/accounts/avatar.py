# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import httpx

from ...._types import NOT_GIVEN, Body, Query, Headers, NoneType, NotGiven, FileTypes
from ...._utils import (
    maybe_transform,
    async_maybe_transform,
)
from ...._compat import cached_property
from ...._resource import SyncAPIResource, AsyncAPIResource
from ...._response import (
    BinaryAPIResponse,
    AsyncBinaryAPIResponse,
    StreamedBinaryAPIResponse,
    AsyncStreamedBinaryAPIResponse,
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    to_custom_raw_response_wrapper,
    async_to_streamed_response_wrapper,
    to_custom_streamed_response_wrapper,
    async_to_custom_raw_response_wrapper,
    async_to_custom_streamed_response_wrapper,
)
from ...._base_client import make_request_options
from ....types.v1.accounts import avatar_create_params

__all__ = ["AvatarResource", "AsyncAvatarResource"]


class AvatarResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AvatarResourceWithRawResponse:
        return AvatarResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AvatarResourceWithStreamingResponse:
        return AvatarResourceWithStreamingResponse(self)

    def create(
        self,
        *,
        body: FileTypes,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> None:
        """
        Upload an avatar for the authenticated account.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return self._post(
            "/v1/accounts/self/avatar",
            body=maybe_transform(body, avatar_create_params.AvatarCreateParams),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )

    def retrieve(
        self,
        account_handle: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> BinaryAPIResponse:
        """
        Get an avatar for the specified account.

        Args:
          account_handle: The unique @ handle of an account.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_handle:
            raise ValueError(f"Expected a non-empty value for `account_handle` but received {account_handle!r}")
        extra_headers = {"Accept": "image/png", **(extra_headers or {})}
        return self._get(
            f"/v1/accounts/{account_handle}/avatar",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=BinaryAPIResponse,
        )


class AsyncAvatarResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncAvatarResourceWithRawResponse:
        return AsyncAvatarResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncAvatarResourceWithStreamingResponse:
        return AsyncAvatarResourceWithStreamingResponse(self)

    async def create(
        self,
        *,
        body: FileTypes,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> None:
        """
        Upload an avatar for the authenticated account.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return await self._post(
            "/v1/accounts/self/avatar",
            body=await async_maybe_transform(body, avatar_create_params.AvatarCreateParams),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )

    async def retrieve(
        self,
        account_handle: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> AsyncBinaryAPIResponse:
        """
        Get an avatar for the specified account.

        Args:
          account_handle: The unique @ handle of an account.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_handle:
            raise ValueError(f"Expected a non-empty value for `account_handle` but received {account_handle!r}")
        extra_headers = {"Accept": "image/png", **(extra_headers or {})}
        return await self._get(
            f"/v1/accounts/{account_handle}/avatar",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=AsyncBinaryAPIResponse,
        )


class AvatarResourceWithRawResponse:
    def __init__(self, avatar: AvatarResource) -> None:
        self._avatar = avatar

        self.create = to_raw_response_wrapper(
            avatar.create,
        )
        self.retrieve = to_custom_raw_response_wrapper(
            avatar.retrieve,
            BinaryAPIResponse,
        )


class AsyncAvatarResourceWithRawResponse:
    def __init__(self, avatar: AsyncAvatarResource) -> None:
        self._avatar = avatar

        self.create = async_to_raw_response_wrapper(
            avatar.create,
        )
        self.retrieve = async_to_custom_raw_response_wrapper(
            avatar.retrieve,
            AsyncBinaryAPIResponse,
        )


class AvatarResourceWithStreamingResponse:
    def __init__(self, avatar: AvatarResource) -> None:
        self._avatar = avatar

        self.create = to_streamed_response_wrapper(
            avatar.create,
        )
        self.retrieve = to_custom_streamed_response_wrapper(
            avatar.retrieve,
            StreamedBinaryAPIResponse,
        )


class AsyncAvatarResourceWithStreamingResponse:
    def __init__(self, avatar: AsyncAvatarResource) -> None:
        self._avatar = avatar

        self.create = async_to_streamed_response_wrapper(
            avatar.create,
        )
        self.retrieve = async_to_custom_streamed_response_wrapper(
            avatar.retrieve,
            AsyncStreamedBinaryAPIResponse,
        )
