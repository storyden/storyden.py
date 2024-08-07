# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict

import httpx

from ..._types import NOT_GIVEN, Body, Query, Headers, NotGiven
from ..._utils import (
    maybe_transform,
    async_maybe_transform,
)
from ..._compat import cached_property
from ..._resource import SyncAPIResource, AsyncAPIResource
from ..._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from ..._base_client import make_request_options
from ...types.threads import post_create_params
from ...types.threads.post_create_response import PostCreateResponse

__all__ = ["PostsResource", "AsyncPostsResource"]


class PostsResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> PostsResourceWithRawResponse:
        return PostsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> PostsResourceWithStreamingResponse:
        return PostsResourceWithStreamingResponse(self)

    def create(
        self,
        thread_mark: str,
        *,
        body: str,
        meta: Dict[str, object] | NotGiven = NOT_GIVEN,
        reply_to: str | NotGiven = NOT_GIVEN,
        url: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> PostCreateResponse:
        """
        Create a new post within a thread.

        Args:
          thread_mark: A thread's ID and optional slug separated by a dash = it's unique mark. This
              allows endpoints to respond to varying forms of a thread's ID.

              For example, given a thread with the ID `cc5lnd2s1s4652adtu50` and the slug
              `top-10-movies-thread`, Storyden will understand both the forms:
              `cc5lnd2s1s4652adtu50-top-10-movies-thread` and `cc5lnd2s1s4652adtu50` as the
              identifier for that thread.

          body: The body text of a post within a thread. The type is either a string or an
              object, depending on what was used during creation. Strings can be used for
              basic plain text or markdown content and objects are used for more complex types
              such as Slate.js editor documents.

          meta: Arbitrary metadata for the resource.

          reply_to: A unique identifier for this resource.

          url: A web address

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not thread_mark:
            raise ValueError(f"Expected a non-empty value for `thread_mark` but received {thread_mark!r}")
        return self._post(
            f"/v1/threads/{thread_mark}/posts",
            body=maybe_transform(
                {
                    "body": body,
                    "meta": meta,
                    "reply_to": reply_to,
                    "url": url,
                },
                post_create_params.PostCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=PostCreateResponse,
        )


class AsyncPostsResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncPostsResourceWithRawResponse:
        return AsyncPostsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncPostsResourceWithStreamingResponse:
        return AsyncPostsResourceWithStreamingResponse(self)

    async def create(
        self,
        thread_mark: str,
        *,
        body: str,
        meta: Dict[str, object] | NotGiven = NOT_GIVEN,
        reply_to: str | NotGiven = NOT_GIVEN,
        url: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> PostCreateResponse:
        """
        Create a new post within a thread.

        Args:
          thread_mark: A thread's ID and optional slug separated by a dash = it's unique mark. This
              allows endpoints to respond to varying forms of a thread's ID.

              For example, given a thread with the ID `cc5lnd2s1s4652adtu50` and the slug
              `top-10-movies-thread`, Storyden will understand both the forms:
              `cc5lnd2s1s4652adtu50-top-10-movies-thread` and `cc5lnd2s1s4652adtu50` as the
              identifier for that thread.

          body: The body text of a post within a thread. The type is either a string or an
              object, depending on what was used during creation. Strings can be used for
              basic plain text or markdown content and objects are used for more complex types
              such as Slate.js editor documents.

          meta: Arbitrary metadata for the resource.

          reply_to: A unique identifier for this resource.

          url: A web address

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not thread_mark:
            raise ValueError(f"Expected a non-empty value for `thread_mark` but received {thread_mark!r}")
        return await self._post(
            f"/v1/threads/{thread_mark}/posts",
            body=await async_maybe_transform(
                {
                    "body": body,
                    "meta": meta,
                    "reply_to": reply_to,
                    "url": url,
                },
                post_create_params.PostCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=PostCreateResponse,
        )


class PostsResourceWithRawResponse:
    def __init__(self, posts: PostsResource) -> None:
        self._posts = posts

        self.create = to_raw_response_wrapper(
            posts.create,
        )


class AsyncPostsResourceWithRawResponse:
    def __init__(self, posts: AsyncPostsResource) -> None:
        self._posts = posts

        self.create = async_to_raw_response_wrapper(
            posts.create,
        )


class PostsResourceWithStreamingResponse:
    def __init__(self, posts: PostsResource) -> None:
        self._posts = posts

        self.create = to_streamed_response_wrapper(
            posts.create,
        )


class AsyncPostsResourceWithStreamingResponse:
    def __init__(self, posts: AsyncPostsResource) -> None:
        self._posts = posts

        self.create = async_to_streamed_response_wrapper(
            posts.create,
        )
