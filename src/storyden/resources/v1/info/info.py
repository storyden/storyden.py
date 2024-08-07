# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import httpx

from .icon import (
    IconResource,
    AsyncIconResource,
    IconResourceWithRawResponse,
    AsyncIconResourceWithRawResponse,
    IconResourceWithStreamingResponse,
    AsyncIconResourceWithStreamingResponse,
)
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
from ....types.v1.info_list_response import InfoListResponse

__all__ = ["InfoResource", "AsyncInfoResource"]


class InfoResource(SyncAPIResource):
    @cached_property
    def icon(self) -> IconResource:
        return IconResource(self._client)

    @cached_property
    def with_raw_response(self) -> InfoResourceWithRawResponse:
        return InfoResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> InfoResourceWithStreamingResponse:
        return InfoResourceWithStreamingResponse(self)

    def list(
        self,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> InfoListResponse:
        """Get the basic forum installation info such as title, description, etc."""
        return self._get(
            "/v1/info",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=InfoListResponse,
        )


class AsyncInfoResource(AsyncAPIResource):
    @cached_property
    def icon(self) -> AsyncIconResource:
        return AsyncIconResource(self._client)

    @cached_property
    def with_raw_response(self) -> AsyncInfoResourceWithRawResponse:
        return AsyncInfoResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncInfoResourceWithStreamingResponse:
        return AsyncInfoResourceWithStreamingResponse(self)

    async def list(
        self,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> InfoListResponse:
        """Get the basic forum installation info such as title, description, etc."""
        return await self._get(
            "/v1/info",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=InfoListResponse,
        )


class InfoResourceWithRawResponse:
    def __init__(self, info: InfoResource) -> None:
        self._info = info

        self.list = to_raw_response_wrapper(
            info.list,
        )

    @cached_property
    def icon(self) -> IconResourceWithRawResponse:
        return IconResourceWithRawResponse(self._info.icon)


class AsyncInfoResourceWithRawResponse:
    def __init__(self, info: AsyncInfoResource) -> None:
        self._info = info

        self.list = async_to_raw_response_wrapper(
            info.list,
        )

    @cached_property
    def icon(self) -> AsyncIconResourceWithRawResponse:
        return AsyncIconResourceWithRawResponse(self._info.icon)


class InfoResourceWithStreamingResponse:
    def __init__(self, info: InfoResource) -> None:
        self._info = info

        self.list = to_streamed_response_wrapper(
            info.list,
        )

    @cached_property
    def icon(self) -> IconResourceWithStreamingResponse:
        return IconResourceWithStreamingResponse(self._info.icon)


class AsyncInfoResourceWithStreamingResponse:
    def __init__(self, info: AsyncInfoResource) -> None:
        self._info = info

        self.list = async_to_streamed_response_wrapper(
            info.list,
        )

    @cached_property
    def icon(self) -> AsyncIconResourceWithStreamingResponse:
        return AsyncIconResourceWithStreamingResponse(self._info.icon)
