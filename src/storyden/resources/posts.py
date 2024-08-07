# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict, List
from typing_extensions import Literal

import httpx

from ..types import post_reacts_params, post_search_params, post_update_params
from .._types import NOT_GIVEN, Body, Query, Headers, NoneType, NotGiven
from .._utils import (
    maybe_transform,
    async_maybe_transform,
)
from .._compat import cached_property
from .._resource import SyncAPIResource, AsyncAPIResource
from .._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from .._base_client import make_request_options
from ..types.post_reacts_response import PostReactsResponse
from ..types.post_search_response import PostSearchResponse
from ..types.post_update_response import PostUpdateResponse

__all__ = ["PostsResource", "AsyncPostsResource"]


class PostsResource(SyncAPIResource):
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

    def archive(
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

    def reacts(
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
    ) -> PostReactsResponse:
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
            body=maybe_transform({"emoji": emoji}, post_reacts_params.PostReactsParams),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=PostReactsResponse,
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

    async def archive(
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

    async def reacts(
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
    ) -> PostReactsResponse:
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
            body=await async_maybe_transform({"emoji": emoji}, post_reacts_params.PostReactsParams),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=PostReactsResponse,
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
        self.archive = to_raw_response_wrapper(
            posts.archive,
        )
        self.reacts = to_raw_response_wrapper(
            posts.reacts,
        )
        self.search = to_raw_response_wrapper(
            posts.search,
        )


class AsyncPostsResourceWithRawResponse:
    def __init__(self, posts: AsyncPostsResource) -> None:
        self._posts = posts

        self.update = async_to_raw_response_wrapper(
            posts.update,
        )
        self.archive = async_to_raw_response_wrapper(
            posts.archive,
        )
        self.reacts = async_to_raw_response_wrapper(
            posts.reacts,
        )
        self.search = async_to_raw_response_wrapper(
            posts.search,
        )


class PostsResourceWithStreamingResponse:
    def __init__(self, posts: PostsResource) -> None:
        self._posts = posts

        self.update = to_streamed_response_wrapper(
            posts.update,
        )
        self.archive = to_streamed_response_wrapper(
            posts.archive,
        )
        self.reacts = to_streamed_response_wrapper(
            posts.reacts,
        )
        self.search = to_streamed_response_wrapper(
            posts.search,
        )


class AsyncPostsResourceWithStreamingResponse:
    def __init__(self, posts: AsyncPostsResource) -> None:
        self._posts = posts

        self.update = async_to_streamed_response_wrapper(
            posts.update,
        )
        self.archive = async_to_streamed_response_wrapper(
            posts.archive,
        )
        self.reacts = async_to_streamed_response_wrapper(
            posts.reacts,
        )
        self.search = async_to_streamed_response_wrapper(
            posts.search,
        )
