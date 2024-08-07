# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import httpx

from .reacts import ReactsResource, AsyncReactsResource

from ..._compat import cached_property

from ...types.post_update_response import PostUpdateResponse

from ..._utils import maybe_transform, async_maybe_transform

from ..._base_client import make_request_options

from typing import Dict, List

from ...types.post_search_response import PostSearchResponse

from typing_extensions import Literal

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
from ...types import post_update_params
from ...types import post_search_params
from .reacts import (
    ReactsResource,
    AsyncReactsResource,
    ReactsResourceWithRawResponse,
    AsyncReactsResourceWithRawResponse,
    ReactsResourceWithStreamingResponse,
    AsyncReactsResourceWithStreamingResponse,
)

__all__ = ["PostsResource", "AsyncPostsResource"]


class PostsResource(SyncAPIResource):
    @cached_property
    def reacts(self) -> ReactsResource:
        return ReactsResource(self._client)

    @cached_property
    def with_raw_response(self) -> PostsResourceWithRawResponse:
        return PostsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> PostsResourceWithStreamingResponse:
        return PostsResourceWithStreamingResponse(self)

    def update(
        self,
        post_id: str,
        *,
        body: str | NotGiven = NOT_GIVEN,
        meta: Dict[str, object] | NotGiven = NOT_GIVEN,
        url: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> PostUpdateResponse:
        """
        Publish changes to a single post.

        Args:
          post_id: A unique identifier for this resource.

          body: The body text of a post within a thread. The type is either a string or an
              object, depending on what was used during creation. Strings can be used for
              basic plain text or markdown content and objects are used for more complex types
              such as Slate.js editor documents.

          meta: Arbitrary metadata for the resource.

          url: A web address

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not post_id:
            raise ValueError(f"Expected a non-empty value for `post_id` but received {post_id!r}")
        return self._patch(
            f"/v1/posts/{post_id}",
            body=maybe_transform(
                {
                    "body": body,
                    "meta": meta,
                    "url": url,
                },
                post_update_params.PostUpdateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=PostUpdateResponse,
        )

    def delete(
        self,
        post_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> None:
        """
        Archive a post using soft-delete.

        Args:
          post_id: A unique identifier for this resource.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not post_id:
            raise ValueError(f"Expected a non-empty value for `post_id` but received {post_id!r}")
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return self._delete(
            f"/v1/posts/{post_id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )

    def search(
        self,
        *,
        author: str | NotGiven = NOT_GIVEN,
        body: str | NotGiven = NOT_GIVEN,
        kind: List[Literal["post", "thread"]] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> PostSearchResponse:
        """
        Search through posts using various queries and filters.

        Args:
          author: Show only results created by this account.

          body: A text query to search for in post content.

          kind: Posts, threads or both.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get(
            "/v1/posts/search",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "author": author,
                        "body": body,
                        "kind": kind,
                    },
                    post_search_params.PostSearchParams,
                ),
            ),
            cast_to=PostSearchResponse,
        )


class AsyncPostsResource(AsyncAPIResource):
    @cached_property
    def reacts(self) -> AsyncReactsResource:
        return AsyncReactsResource(self._client)

    @cached_property
    def with_raw_response(self) -> AsyncPostsResourceWithRawResponse:
        return AsyncPostsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncPostsResourceWithStreamingResponse:
        return AsyncPostsResourceWithStreamingResponse(self)

    async def update(
        self,
        post_id: str,
        *,
        body: str | NotGiven = NOT_GIVEN,
        meta: Dict[str, object] | NotGiven = NOT_GIVEN,
        url: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> PostUpdateResponse:
        """
        Publish changes to a single post.

        Args:
          post_id: A unique identifier for this resource.

          body: The body text of a post within a thread. The type is either a string or an
              object, depending on what was used during creation. Strings can be used for
              basic plain text or markdown content and objects are used for more complex types
              such as Slate.js editor documents.

          meta: Arbitrary metadata for the resource.

          url: A web address

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not post_id:
            raise ValueError(f"Expected a non-empty value for `post_id` but received {post_id!r}")
        return await self._patch(
            f"/v1/posts/{post_id}",
            body=await async_maybe_transform(
                {
                    "body": body,
                    "meta": meta,
                    "url": url,
                },
                post_update_params.PostUpdateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=PostUpdateResponse,
        )

    async def delete(
        self,
        post_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> None:
        """
        Archive a post using soft-delete.

        Args:
          post_id: A unique identifier for this resource.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not post_id:
            raise ValueError(f"Expected a non-empty value for `post_id` but received {post_id!r}")
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return await self._delete(
            f"/v1/posts/{post_id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )

    async def search(
        self,
        *,
        author: str | NotGiven = NOT_GIVEN,
        body: str | NotGiven = NOT_GIVEN,
        kind: List[Literal["post", "thread"]] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> PostSearchResponse:
        """
        Search through posts using various queries and filters.

        Args:
          author: Show only results created by this account.

          body: A text query to search for in post content.

          kind: Posts, threads or both.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._get(
            "/v1/posts/search",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {
                        "author": author,
                        "body": body,
                        "kind": kind,
                    },
                    post_search_params.PostSearchParams,
                ),
            ),
            cast_to=PostSearchResponse,
        )


class PostsResourceWithRawResponse:
    def __init__(self, posts: PostsResource) -> None:
        self._posts = posts

        self.update = to_raw_response_wrapper(
            posts.update,
        )
        self.delete = to_raw_response_wrapper(
            posts.delete,
        )
        self.search = to_raw_response_wrapper(
            posts.search,
        )

    @cached_property
    def reacts(self) -> ReactsResourceWithRawResponse:
        return ReactsResourceWithRawResponse(self._posts.reacts)


class AsyncPostsResourceWithRawResponse:
    def __init__(self, posts: AsyncPostsResource) -> None:
        self._posts = posts

        self.update = async_to_raw_response_wrapper(
            posts.update,
        )
        self.delete = async_to_raw_response_wrapper(
            posts.delete,
        )
        self.search = async_to_raw_response_wrapper(
            posts.search,
        )

    @cached_property
    def reacts(self) -> AsyncReactsResourceWithRawResponse:
        return AsyncReactsResourceWithRawResponse(self._posts.reacts)


class PostsResourceWithStreamingResponse:
    def __init__(self, posts: PostsResource) -> None:
        self._posts = posts

        self.update = to_streamed_response_wrapper(
            posts.update,
        )
        self.delete = to_streamed_response_wrapper(
            posts.delete,
        )
        self.search = to_streamed_response_wrapper(
            posts.search,
        )

    @cached_property
    def reacts(self) -> ReactsResourceWithStreamingResponse:
        return ReactsResourceWithStreamingResponse(self._posts.reacts)


class AsyncPostsResourceWithStreamingResponse:
    def __init__(self, posts: AsyncPostsResource) -> None:
        self._posts = posts

        self.update = async_to_streamed_response_wrapper(
            posts.update,
        )
        self.delete = async_to_streamed_response_wrapper(
            posts.delete,
        )
        self.search = async_to_streamed_response_wrapper(
            posts.search,
        )

    @cached_property
    def reacts(self) -> AsyncReactsResourceWithStreamingResponse:
        return AsyncReactsResourceWithStreamingResponse(self._posts.reacts)
