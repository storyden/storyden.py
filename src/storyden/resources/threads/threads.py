# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict, List
from typing_extensions import Literal

import httpx

from .posts import (
    PostsResource,
    AsyncPostsResource,
    PostsResourceWithRawResponse,
    AsyncPostsResourceWithRawResponse,
    PostsResourceWithStreamingResponse,
    AsyncPostsResourceWithStreamingResponse,
)
from ...types import thread_list_params, thread_create_params, thread_publish_changes_params
from ..._types import NOT_GIVEN, Body, Query, Headers, NoneType, NotGiven
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
from ...types.thread_list_response import ThreadListResponse
from ...types.thread_create_response import ThreadCreateResponse
from ...types.thread_publish_changes_response import ThreadPublishChangesResponse
from ...types.thread_retrieve_information_response import ThreadRetrieveInformationResponse

__all__ = ["ThreadsResource", "AsyncThreadsResource"]


class ThreadsResource(SyncAPIResource):
    @cached_property
    def posts(self) -> PostsResource:
        return PostsResource(self._client)

    @cached_property
    def with_raw_response(self) -> ThreadsResourceWithRawResponse:
        return ThreadsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> ThreadsResourceWithStreamingResponse:
        return ThreadsResourceWithStreamingResponse(self)

    def create(
        self,
        *,
        body: str,
        category: str,
        title: str,
        visibility: Literal["draft", "unlisted", "review", "published"],
        meta: Dict[str, object] | NotGiven = NOT_GIVEN,
        tags: List[str] | NotGiven = NOT_GIVEN,
        url: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> ThreadCreateResponse:
        """
        Create a new thread within the specified category.

        Args:
          body: The body text of a post within a thread. The type is either a string or an
              object, depending on what was used during creation. Strings can be used for
              basic plain text or markdown content and objects are used for more complex types
              such as Slate.js editor documents.

          category: A unique identifier for this resource.

          title: The title of a thread.

          meta: Arbitrary metadata for the resource.

          tags: A list of tags IDs.

          url: A web address

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/v1/threads",
            body=maybe_transform(
                {
                    "body": body,
                    "category": category,
                    "title": title,
                    "visibility": visibility,
                    "meta": meta,
                    "tags": tags,
                    "url": url,
                },
                thread_create_params.ThreadCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ThreadCreateResponse,
        )

    def list(
        self,
        *,
        author: str | NotGiven = NOT_GIVEN,
        categories: List[str] | NotGiven = NOT_GIVEN,
        page: str | NotGiven = NOT_GIVEN,
        q: str | NotGiven = NOT_GIVEN,
        tags: List[str] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> ThreadListResponse:
        """
        Get a list of all threads.

        Args:
          author: Show only results creeated by this user.

          categories: Show only results with these categories

          page: Pagination query parameters.

          q: Search query string.

          tags: Show only results with these tags

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get(
            "/v1/threads",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "author": author,
                        "categories": categories,
                        "page": page,
                        "q": q,
                        "tags": tags,
                    },
                    thread_list_params.ThreadListParams,
                ),
            ),
            cast_to=ThreadListResponse,
        )

    def archive(
        self,
        thread_mark: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> None:
        """
        Archive a thread using soft-delete.

        Args:
          thread_mark: A thread's ID and optional slug separated by a dash = it's unique mark. This
              allows endpoints to respond to varying forms of a thread's ID.

              For example, given a thread with the ID `cc5lnd2s1s4652adtu50` and the slug
              `top-10-movies-thread`, Storyden will understand both the forms:
              `cc5lnd2s1s4652adtu50-top-10-movies-thread` and `cc5lnd2s1s4652adtu50` as the
              identifier for that thread.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not thread_mark:
            raise ValueError(f"Expected a non-empty value for `thread_mark` but received {thread_mark!r}")
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return self._delete(
            f"/v1/threads/{thread_mark}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )

    def publish_changes(
        self,
        thread_mark: str,
        *,
        body: str | NotGiven = NOT_GIVEN,
        category: str | NotGiven = NOT_GIVEN,
        meta: Dict[str, object] | NotGiven = NOT_GIVEN,
        tags: List[str] | NotGiven = NOT_GIVEN,
        title: str | NotGiven = NOT_GIVEN,
        url: str | NotGiven = NOT_GIVEN,
        visibility: Literal["draft", "unlisted", "review", "published"] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> ThreadPublishChangesResponse:
        """
        Publish changes to a thread.

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

          category: A unique identifier for this resource.

          meta: Arbitrary metadata for the resource.

          tags: A list of tags IDs.

          title: The title of a thread.

          url: A web address

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not thread_mark:
            raise ValueError(f"Expected a non-empty value for `thread_mark` but received {thread_mark!r}")
        return self._patch(
            f"/v1/threads/{thread_mark}",
            body=maybe_transform(
                {
                    "body": body,
                    "category": category,
                    "meta": meta,
                    "tags": tags,
                    "title": title,
                    "url": url,
                    "visibility": visibility,
                },
                thread_publish_changes_params.ThreadPublishChangesParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ThreadPublishChangesResponse,
        )

    def retrieve_information(
        self,
        thread_mark: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> ThreadRetrieveInformationResponse:
        """
        Get information about a thread such as its title, author, when it was created as
        well as a list of the posts within the thread.

        Args:
          thread_mark: A thread's ID and optional slug separated by a dash = it's unique mark. This
              allows endpoints to respond to varying forms of a thread's ID.

              For example, given a thread with the ID `cc5lnd2s1s4652adtu50` and the slug
              `top-10-movies-thread`, Storyden will understand both the forms:
              `cc5lnd2s1s4652adtu50-top-10-movies-thread` and `cc5lnd2s1s4652adtu50` as the
              identifier for that thread.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not thread_mark:
            raise ValueError(f"Expected a non-empty value for `thread_mark` but received {thread_mark!r}")
        return self._get(
            f"/v1/threads/{thread_mark}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ThreadRetrieveInformationResponse,
        )


class AsyncThreadsResource(AsyncAPIResource):
    @cached_property
    def posts(self) -> AsyncPostsResource:
        return AsyncPostsResource(self._client)

    @cached_property
    def with_raw_response(self) -> AsyncThreadsResourceWithRawResponse:
        return AsyncThreadsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncThreadsResourceWithStreamingResponse:
        return AsyncThreadsResourceWithStreamingResponse(self)

    async def create(
        self,
        *,
        body: str,
        category: str,
        title: str,
        visibility: Literal["draft", "unlisted", "review", "published"],
        meta: Dict[str, object] | NotGiven = NOT_GIVEN,
        tags: List[str] | NotGiven = NOT_GIVEN,
        url: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> ThreadCreateResponse:
        """
        Create a new thread within the specified category.

        Args:
          body: The body text of a post within a thread. The type is either a string or an
              object, depending on what was used during creation. Strings can be used for
              basic plain text or markdown content and objects are used for more complex types
              such as Slate.js editor documents.

          category: A unique identifier for this resource.

          title: The title of a thread.

          meta: Arbitrary metadata for the resource.

          tags: A list of tags IDs.

          url: A web address

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/v1/threads",
            body=await async_maybe_transform(
                {
                    "body": body,
                    "category": category,
                    "title": title,
                    "visibility": visibility,
                    "meta": meta,
                    "tags": tags,
                    "url": url,
                },
                thread_create_params.ThreadCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ThreadCreateResponse,
        )

    async def list(
        self,
        *,
        author: str | NotGiven = NOT_GIVEN,
        categories: List[str] | NotGiven = NOT_GIVEN,
        page: str | NotGiven = NOT_GIVEN,
        q: str | NotGiven = NOT_GIVEN,
        tags: List[str] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> ThreadListResponse:
        """
        Get a list of all threads.

        Args:
          author: Show only results creeated by this user.

          categories: Show only results with these categories

          page: Pagination query parameters.

          q: Search query string.

          tags: Show only results with these tags

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._get(
            "/v1/threads",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {
                        "author": author,
                        "categories": categories,
                        "page": page,
                        "q": q,
                        "tags": tags,
                    },
                    thread_list_params.ThreadListParams,
                ),
            ),
            cast_to=ThreadListResponse,
        )

    async def archive(
        self,
        thread_mark: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> None:
        """
        Archive a thread using soft-delete.

        Args:
          thread_mark: A thread's ID and optional slug separated by a dash = it's unique mark. This
              allows endpoints to respond to varying forms of a thread's ID.

              For example, given a thread with the ID `cc5lnd2s1s4652adtu50` and the slug
              `top-10-movies-thread`, Storyden will understand both the forms:
              `cc5lnd2s1s4652adtu50-top-10-movies-thread` and `cc5lnd2s1s4652adtu50` as the
              identifier for that thread.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not thread_mark:
            raise ValueError(f"Expected a non-empty value for `thread_mark` but received {thread_mark!r}")
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return await self._delete(
            f"/v1/threads/{thread_mark}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )

    async def publish_changes(
        self,
        thread_mark: str,
        *,
        body: str | NotGiven = NOT_GIVEN,
        category: str | NotGiven = NOT_GIVEN,
        meta: Dict[str, object] | NotGiven = NOT_GIVEN,
        tags: List[str] | NotGiven = NOT_GIVEN,
        title: str | NotGiven = NOT_GIVEN,
        url: str | NotGiven = NOT_GIVEN,
        visibility: Literal["draft", "unlisted", "review", "published"] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> ThreadPublishChangesResponse:
        """
        Publish changes to a thread.

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

          category: A unique identifier for this resource.

          meta: Arbitrary metadata for the resource.

          tags: A list of tags IDs.

          title: The title of a thread.

          url: A web address

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not thread_mark:
            raise ValueError(f"Expected a non-empty value for `thread_mark` but received {thread_mark!r}")
        return await self._patch(
            f"/v1/threads/{thread_mark}",
            body=await async_maybe_transform(
                {
                    "body": body,
                    "category": category,
                    "meta": meta,
                    "tags": tags,
                    "title": title,
                    "url": url,
                    "visibility": visibility,
                },
                thread_publish_changes_params.ThreadPublishChangesParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ThreadPublishChangesResponse,
        )

    async def retrieve_information(
        self,
        thread_mark: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> ThreadRetrieveInformationResponse:
        """
        Get information about a thread such as its title, author, when it was created as
        well as a list of the posts within the thread.

        Args:
          thread_mark: A thread's ID and optional slug separated by a dash = it's unique mark. This
              allows endpoints to respond to varying forms of a thread's ID.

              For example, given a thread with the ID `cc5lnd2s1s4652adtu50` and the slug
              `top-10-movies-thread`, Storyden will understand both the forms:
              `cc5lnd2s1s4652adtu50-top-10-movies-thread` and `cc5lnd2s1s4652adtu50` as the
              identifier for that thread.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not thread_mark:
            raise ValueError(f"Expected a non-empty value for `thread_mark` but received {thread_mark!r}")
        return await self._get(
            f"/v1/threads/{thread_mark}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ThreadRetrieveInformationResponse,
        )


class ThreadsResourceWithRawResponse:
    def __init__(self, threads: ThreadsResource) -> None:
        self._threads = threads

        self.create = to_raw_response_wrapper(
            threads.create,
        )
        self.list = to_raw_response_wrapper(
            threads.list,
        )
        self.archive = to_raw_response_wrapper(
            threads.archive,
        )
        self.publish_changes = to_raw_response_wrapper(
            threads.publish_changes,
        )
        self.retrieve_information = to_raw_response_wrapper(
            threads.retrieve_information,
        )

    @cached_property
    def posts(self) -> PostsResourceWithRawResponse:
        return PostsResourceWithRawResponse(self._threads.posts)


class AsyncThreadsResourceWithRawResponse:
    def __init__(self, threads: AsyncThreadsResource) -> None:
        self._threads = threads

        self.create = async_to_raw_response_wrapper(
            threads.create,
        )
        self.list = async_to_raw_response_wrapper(
            threads.list,
        )
        self.archive = async_to_raw_response_wrapper(
            threads.archive,
        )
        self.publish_changes = async_to_raw_response_wrapper(
            threads.publish_changes,
        )
        self.retrieve_information = async_to_raw_response_wrapper(
            threads.retrieve_information,
        )

    @cached_property
    def posts(self) -> AsyncPostsResourceWithRawResponse:
        return AsyncPostsResourceWithRawResponse(self._threads.posts)


class ThreadsResourceWithStreamingResponse:
    def __init__(self, threads: ThreadsResource) -> None:
        self._threads = threads

        self.create = to_streamed_response_wrapper(
            threads.create,
        )
        self.list = to_streamed_response_wrapper(
            threads.list,
        )
        self.archive = to_streamed_response_wrapper(
            threads.archive,
        )
        self.publish_changes = to_streamed_response_wrapper(
            threads.publish_changes,
        )
        self.retrieve_information = to_streamed_response_wrapper(
            threads.retrieve_information,
        )

    @cached_property
    def posts(self) -> PostsResourceWithStreamingResponse:
        return PostsResourceWithStreamingResponse(self._threads.posts)


class AsyncThreadsResourceWithStreamingResponse:
    def __init__(self, threads: AsyncThreadsResource) -> None:
        self._threads = threads

        self.create = async_to_streamed_response_wrapper(
            threads.create,
        )
        self.list = async_to_streamed_response_wrapper(
            threads.list,
        )
        self.archive = async_to_streamed_response_wrapper(
            threads.archive,
        )
        self.publish_changes = async_to_streamed_response_wrapper(
            threads.publish_changes,
        )
        self.retrieve_information = async_to_streamed_response_wrapper(
            threads.retrieve_information,
        )

    @cached_property
    def posts(self) -> AsyncPostsResourceWithStreamingResponse:
        return AsyncPostsResourceWithStreamingResponse(self._threads.posts)
