# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import httpx

from ..._types import NOT_GIVEN, Body, Query, Headers, NotGiven
from ..._compat import cached_property
from ..._resource import SyncAPIResource, AsyncAPIResource
from ..._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from ..._base_client import make_request_options

__all__ = ["VersionResource", "AsyncVersionResource"]


class VersionResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> VersionResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/storyden/storyden.py#accessing-raw-response-data-eg-headers
        """
        return VersionResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> VersionResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/storyden/storyden.py#with_streaming_response
        """
        return VersionResourceWithStreamingResponse(self)

    def retrieve(
        self,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> str:
        """
        The version number includes the date and time of the release build as well as a
        short representation of the Git commit hash.
        """
        extra_headers = {"Accept": "text/plain", **(extra_headers or {})}
        return self._get(
            "/version",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=str,
        )


class AsyncVersionResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncVersionResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/storyden/storyden.py#accessing-raw-response-data-eg-headers
        """
        return AsyncVersionResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncVersionResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/storyden/storyden.py#with_streaming_response
        """
        return AsyncVersionResourceWithStreamingResponse(self)

    async def retrieve(
        self,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> str:
        """
        The version number includes the date and time of the release build as well as a
        short representation of the Git commit hash.
        """
        extra_headers = {"Accept": "text/plain", **(extra_headers or {})}
        return await self._get(
            "/version",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=str,
        )


class VersionResourceWithRawResponse:
    def __init__(self, version: VersionResource) -> None:
        self._version = version

        self.retrieve = to_raw_response_wrapper(
            version.retrieve,
        )


class AsyncVersionResourceWithRawResponse:
    def __init__(self, version: AsyncVersionResource) -> None:
        self._version = version

        self.retrieve = async_to_raw_response_wrapper(
            version.retrieve,
        )


class VersionResourceWithStreamingResponse:
    def __init__(self, version: VersionResource) -> None:
        self._version = version

        self.retrieve = to_streamed_response_wrapper(
            version.retrieve,
        )


class AsyncVersionResourceWithStreamingResponse:
    def __init__(self, version: AsyncVersionResource) -> None:
        self._version = version

        self.retrieve = async_to_streamed_response_wrapper(
            version.retrieve,
        )
