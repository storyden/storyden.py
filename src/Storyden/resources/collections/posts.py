# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import httpx

from ..._compat import cached_property

from ...types.collections.post_add_response import PostAddResponse

from ..._base_client import make_request_options

from ...types.collections.post_remove_response import PostRemoveResponse

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

__all__ = ["PostsResource", "AsyncPostsResource"]


class PostsResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> PostsResourceWithRawResponse:
        return PostsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> PostsResourceWithStreamingResponse:
        return PostsResourceWithStreamingResponse(self)

    def add(
        self,
        post_id: str,
        *,
        collection_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> PostAddResponse:
        """Add a post to a collection.

        The collection must be owned by the account making
        the request. The post can be any published post of any kind.

        Args:
          collection_id: A unique identifier for this resource.

          post_id: A unique identifier for this resource.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not collection_id:
            raise ValueError(f"Expected a non-empty value for `collection_id` but received {collection_id!r}")
        if not post_id:
            raise ValueError(f"Expected a non-empty value for `post_id` but received {post_id!r}")
        return self._put(
            f"/v1/collections/{collection_id}/posts/{post_id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=PostAddResponse,
        )

    def remove(
        self,
        post_id: str,
        *,
        collection_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> PostRemoveResponse:
        """Remove a post from a collection.

        The collection must be owned by the account
        making the request.

        Args:
          collection_id: A unique identifier for this resource.

          post_id: A unique identifier for this resource.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not collection_id:
            raise ValueError(f"Expected a non-empty value for `collection_id` but received {collection_id!r}")
        if not post_id:
            raise ValueError(f"Expected a non-empty value for `post_id` but received {post_id!r}")
        return self._delete(
            f"/v1/collections/{collection_id}/posts/{post_id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=PostRemoveResponse,
        )


class AsyncPostsResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncPostsResourceWithRawResponse:
        return AsyncPostsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncPostsResourceWithStreamingResponse:
        return AsyncPostsResourceWithStreamingResponse(self)

    async def add(
        self,
        post_id: str,
        *,
        collection_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> PostAddResponse:
        """Add a post to a collection.

        The collection must be owned by the account making
        the request. The post can be any published post of any kind.

        Args:
          collection_id: A unique identifier for this resource.

          post_id: A unique identifier for this resource.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not collection_id:
            raise ValueError(f"Expected a non-empty value for `collection_id` but received {collection_id!r}")
        if not post_id:
            raise ValueError(f"Expected a non-empty value for `post_id` but received {post_id!r}")
        return await self._put(
            f"/v1/collections/{collection_id}/posts/{post_id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=PostAddResponse,
        )

    async def remove(
        self,
        post_id: str,
        *,
        collection_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> PostRemoveResponse:
        """Remove a post from a collection.

        The collection must be owned by the account
        making the request.

        Args:
          collection_id: A unique identifier for this resource.

          post_id: A unique identifier for this resource.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not collection_id:
            raise ValueError(f"Expected a non-empty value for `collection_id` but received {collection_id!r}")
        if not post_id:
            raise ValueError(f"Expected a non-empty value for `post_id` but received {post_id!r}")
        return await self._delete(
            f"/v1/collections/{collection_id}/posts/{post_id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=PostRemoveResponse,
        )


class PostsResourceWithRawResponse:
    def __init__(self, posts: PostsResource) -> None:
        self._posts = posts

        self.add = to_raw_response_wrapper(
            posts.add,
        )
        self.remove = to_raw_response_wrapper(
            posts.remove,
        )


class AsyncPostsResourceWithRawResponse:
    def __init__(self, posts: AsyncPostsResource) -> None:
        self._posts = posts

        self.add = async_to_raw_response_wrapper(
            posts.add,
        )
        self.remove = async_to_raw_response_wrapper(
            posts.remove,
        )


class PostsResourceWithStreamingResponse:
    def __init__(self, posts: PostsResource) -> None:
        self._posts = posts

        self.add = to_streamed_response_wrapper(
            posts.add,
        )
        self.remove = to_streamed_response_wrapper(
            posts.remove,
        )


class AsyncPostsResourceWithStreamingResponse:
    def __init__(self, posts: AsyncPostsResource) -> None:
        self._posts = posts

        self.add = async_to_streamed_response_wrapper(
            posts.add,
        )
        self.remove = async_to_streamed_response_wrapper(
            posts.remove,
        )
