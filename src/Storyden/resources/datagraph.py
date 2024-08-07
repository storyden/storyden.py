# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import httpx

from .._compat import cached_property

from ..types.datagraph_list_response import DatagraphListResponse

from .._utils import maybe_transform, async_maybe_transform

from .._base_client import make_request_options

from .._response import (
    to_raw_response_wrapper,
    async_to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_streamed_response_wrapper,
)

import warnings
from typing import TYPE_CHECKING, Optional, Union, List, Dict, Any, Mapping, cast, overload
from typing_extensions import Literal
from .._utils import extract_files, maybe_transform, required_args, deepcopy_minimal, strip_not_given
from .._types import NotGiven, Timeout, Headers, NoneType, Query, Body, NOT_GIVEN, FileTypes, BinaryResponseContent
from .._resource import SyncAPIResource, AsyncAPIResource
from ..types import shared_params
from ..types import datagraph_list_params

__all__ = ["DatagraphResource", "AsyncDatagraphResource"]


class DatagraphResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> DatagraphResourceWithRawResponse:
        return DatagraphResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> DatagraphResourceWithStreamingResponse:
        return DatagraphResourceWithStreamingResponse(self)

    def list(
        self,
        *,
        page: str | NotGiven = NOT_GIVEN,
        q: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> DatagraphListResponse:
        """
        Query and search content.

        Args:
          page: Pagination query parameters.

          q: Search query string.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get(
            "/v1/datagraph",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "page": page,
                        "q": q,
                    },
                    datagraph_list_params.DatagraphListParams,
                ),
            ),
            cast_to=DatagraphListResponse,
        )


class AsyncDatagraphResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncDatagraphResourceWithRawResponse:
        return AsyncDatagraphResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncDatagraphResourceWithStreamingResponse:
        return AsyncDatagraphResourceWithStreamingResponse(self)

    async def list(
        self,
        *,
        page: str | NotGiven = NOT_GIVEN,
        q: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> DatagraphListResponse:
        """
        Query and search content.

        Args:
          page: Pagination query parameters.

          q: Search query string.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._get(
            "/v1/datagraph",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {
                        "page": page,
                        "q": q,
                    },
                    datagraph_list_params.DatagraphListParams,
                ),
            ),
            cast_to=DatagraphListResponse,
        )


class DatagraphResourceWithRawResponse:
    def __init__(self, datagraph: DatagraphResource) -> None:
        self._datagraph = datagraph

        self.list = to_raw_response_wrapper(
            datagraph.list,
        )


class AsyncDatagraphResourceWithRawResponse:
    def __init__(self, datagraph: AsyncDatagraphResource) -> None:
        self._datagraph = datagraph

        self.list = async_to_raw_response_wrapper(
            datagraph.list,
        )


class DatagraphResourceWithStreamingResponse:
    def __init__(self, datagraph: DatagraphResource) -> None:
        self._datagraph = datagraph

        self.list = to_streamed_response_wrapper(
            datagraph.list,
        )


class AsyncDatagraphResourceWithStreamingResponse:
    def __init__(self, datagraph: AsyncDatagraphResource) -> None:
        self._datagraph = datagraph

        self.list = async_to_streamed_response_wrapper(
            datagraph.list,
        )
