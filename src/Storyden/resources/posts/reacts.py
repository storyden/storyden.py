# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import httpx

from ..._compat import cached_property

from ...types.posts.react_update_response import ReactUpdateResponse

from ..._utils import maybe_transform, async_maybe_transform

from ..._base_client import make_request_options

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
from ...types.posts import react_update_params

__all__ = ["ReactsResource", "AsyncReactsResource"]


class ReactsResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> ReactsResourceWithRawResponse:
        return ReactsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> ReactsResourceWithStreamingResponse:
        return ReactsResourceWithStreamingResponse(self)

    def update(
        self,
        post_id: str,
        *,
        emoji: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> ReactUpdateResponse:
        """
        Add a reaction to a post.

        Args:
          post_id: A unique identifier for this resource.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not post_id:
            raise ValueError(f"Expected a non-empty value for `post_id` but received {post_id!r}")
        return self._put(
            f"/v1/posts/{post_id}/reacts",
            body=maybe_transform({"emoji": emoji}, react_update_params.ReactUpdateParams),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ReactUpdateResponse,
        )


class AsyncReactsResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncReactsResourceWithRawResponse:
        return AsyncReactsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncReactsResourceWithStreamingResponse:
        return AsyncReactsResourceWithStreamingResponse(self)

    async def update(
        self,
        post_id: str,
        *,
        emoji: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> ReactUpdateResponse:
        """
        Add a reaction to a post.

        Args:
          post_id: A unique identifier for this resource.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not post_id:
            raise ValueError(f"Expected a non-empty value for `post_id` but received {post_id!r}")
        return await self._put(
            f"/v1/posts/{post_id}/reacts",
            body=await async_maybe_transform({"emoji": emoji}, react_update_params.ReactUpdateParams),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ReactUpdateResponse,
        )


class ReactsResourceWithRawResponse:
    def __init__(self, reacts: ReactsResource) -> None:
        self._reacts = reacts

        self.update = to_raw_response_wrapper(
            reacts.update,
        )


class AsyncReactsResourceWithRawResponse:
    def __init__(self, reacts: AsyncReactsResource) -> None:
        self._reacts = reacts

        self.update = async_to_raw_response_wrapper(
            reacts.update,
        )


class ReactsResourceWithStreamingResponse:
    def __init__(self, reacts: ReactsResource) -> None:
        self._reacts = reacts

        self.update = to_streamed_response_wrapper(
            reacts.update,
        )


class AsyncReactsResourceWithStreamingResponse:
    def __init__(self, reacts: AsyncReactsResource) -> None:
        self._reacts = reacts

        self.update = async_to_streamed_response_wrapper(
            reacts.update,
        )
