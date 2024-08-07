# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import httpx

from .._types import NOT_GIVEN, Body, Query, Headers, NotGiven
from .._compat import cached_property
from .._resource import SyncAPIResource, AsyncAPIResource
from .._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from .._base_client import make_request_options

__all__ = ["OpenAPIJsonResource", "AsyncOpenAPIJsonResource"]


class OpenAPIJsonResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> OpenAPIJsonResourceWithRawResponse:
        return OpenAPIJsonResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> OpenAPIJsonResourceWithStreamingResponse:
        return OpenAPIJsonResourceWithStreamingResponse(self)

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
        Note: the generator creates a `map[string]interface{}` if this is set to
        `application/json`... so I'm just using plain text for now.
        """
        extra_headers = {"Accept": "text/plain", **(extra_headers or {})}
        return self._get(
            "/openapi.json",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=str,
        )


class AsyncOpenAPIJsonResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncOpenAPIJsonResourceWithRawResponse:
        return AsyncOpenAPIJsonResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncOpenAPIJsonResourceWithStreamingResponse:
        return AsyncOpenAPIJsonResourceWithStreamingResponse(self)

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
        Note: the generator creates a `map[string]interface{}` if this is set to
        `application/json`... so I'm just using plain text for now.
        """
        extra_headers = {"Accept": "text/plain", **(extra_headers or {})}
        return await self._get(
            "/openapi.json",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=str,
        )


class OpenAPIJsonResourceWithRawResponse:
    def __init__(self, openapi_json: OpenAPIJsonResource) -> None:
        self._openapi_json = openapi_json

        self.retrieve = to_raw_response_wrapper(
            openapi_json.retrieve,
        )


class AsyncOpenAPIJsonResourceWithRawResponse:
    def __init__(self, openapi_json: AsyncOpenAPIJsonResource) -> None:
        self._openapi_json = openapi_json

        self.retrieve = async_to_raw_response_wrapper(
            openapi_json.retrieve,
        )


class OpenAPIJsonResourceWithStreamingResponse:
    def __init__(self, openapi_json: OpenAPIJsonResource) -> None:
        self._openapi_json = openapi_json

        self.retrieve = to_streamed_response_wrapper(
            openapi_json.retrieve,
        )


class AsyncOpenAPIJsonResourceWithStreamingResponse:
    def __init__(self, openapi_json: AsyncOpenAPIJsonResource) -> None:
        self._openapi_json = openapi_json

        self.retrieve = async_to_streamed_response_wrapper(
            openapi_json.retrieve,
        )
