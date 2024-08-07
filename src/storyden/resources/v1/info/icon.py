# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal

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
from ....types.v1.info import icon_create_params

__all__ = ["IconResource", "AsyncIconResource"]


class IconResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> IconResourceWithRawResponse:
        return IconResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> IconResourceWithStreamingResponse:
        return IconResourceWithStreamingResponse(self)

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
        Upload and process the installation's logo image.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return self._post(
            "/v1/info/icon",
            body=maybe_transform(body, icon_create_params.IconCreateParams),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )

    def retrieve(
        self,
        icon_size: Literal["512x512", "32x32", "180x180", "120x120", "167x167", "152x152"],
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> BinaryAPIResponse:
        """
        Get the logo icon image.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not icon_size:
            raise ValueError(f"Expected a non-empty value for `icon_size` but received {icon_size!r}")
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return self._get(
            f"/v1/info/icon/{icon_size}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=BinaryAPIResponse,
        )


class AsyncIconResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncIconResourceWithRawResponse:
        return AsyncIconResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncIconResourceWithStreamingResponse:
        return AsyncIconResourceWithStreamingResponse(self)

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
        Upload and process the installation's logo image.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return await self._post(
            "/v1/info/icon",
            body=await async_maybe_transform(body, icon_create_params.IconCreateParams),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )

    async def retrieve(
        self,
        icon_size: Literal["512x512", "32x32", "180x180", "120x120", "167x167", "152x152"],
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> AsyncBinaryAPIResponse:
        """
        Get the logo icon image.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not icon_size:
            raise ValueError(f"Expected a non-empty value for `icon_size` but received {icon_size!r}")
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return await self._get(
            f"/v1/info/icon/{icon_size}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=AsyncBinaryAPIResponse,
        )


class IconResourceWithRawResponse:
    def __init__(self, icon: IconResource) -> None:
        self._icon = icon

        self.create = to_raw_response_wrapper(
            icon.create,
        )
        self.retrieve = to_custom_raw_response_wrapper(
            icon.retrieve,
            BinaryAPIResponse,
        )


class AsyncIconResourceWithRawResponse:
    def __init__(self, icon: AsyncIconResource) -> None:
        self._icon = icon

        self.create = async_to_raw_response_wrapper(
            icon.create,
        )
        self.retrieve = async_to_custom_raw_response_wrapper(
            icon.retrieve,
            AsyncBinaryAPIResponse,
        )


class IconResourceWithStreamingResponse:
    def __init__(self, icon: IconResource) -> None:
        self._icon = icon

        self.create = to_streamed_response_wrapper(
            icon.create,
        )
        self.retrieve = to_custom_streamed_response_wrapper(
            icon.retrieve,
            StreamedBinaryAPIResponse,
        )


class AsyncIconResourceWithStreamingResponse:
    def __init__(self, icon: AsyncIconResource) -> None:
        self._icon = icon

        self.create = async_to_streamed_response_wrapper(
            icon.create,
        )
        self.retrieve = async_to_custom_streamed_response_wrapper(
            icon.retrieve,
            AsyncStreamedBinaryAPIResponse,
        )
