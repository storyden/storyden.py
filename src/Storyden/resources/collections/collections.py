# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import httpx

from .posts import PostsResource, AsyncPostsResource

from ..._compat import cached_property

from .nodes import NodesResource, AsyncNodesResource

from ...types.collection_create_response import CollectionCreateResponse

from ..._utils import maybe_transform, async_maybe_transform

from ..._base_client import make_request_options

from ...types.collection_retrieve_response import CollectionRetrieveResponse

from ...types.collection_update_response import CollectionUpdateResponse

from ...types.collection_list_response import CollectionListResponse

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
from ...types import collection_create_params
from ...types import collection_update_params
from ...types import collection_list_params
from .posts import (
    PostsResource,
    AsyncPostsResource,
    PostsResourceWithRawResponse,
    AsyncPostsResourceWithRawResponse,
    PostsResourceWithStreamingResponse,
    AsyncPostsResourceWithStreamingResponse,
)
from .nodes import (
    NodesResource,
    AsyncNodesResource,
    NodesResourceWithRawResponse,
    AsyncNodesResourceWithRawResponse,
    NodesResourceWithStreamingResponse,
    AsyncNodesResourceWithStreamingResponse,
)

__all__ = ["CollectionsResource", "AsyncCollectionsResource"]


class CollectionsResource(SyncAPIResource):
    @cached_property
    def posts(self) -> PostsResource:
        return PostsResource(self._client)

    @cached_property
    def nodes(self) -> NodesResource:
        return NodesResource(self._client)

    @cached_property
    def with_raw_response(self) -> CollectionsResourceWithRawResponse:
        return CollectionsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> CollectionsResourceWithStreamingResponse:
        return CollectionsResourceWithStreamingResponse(self)

    def create(
        self,
        *,
        description: str,
        name: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> CollectionCreateResponse:
        """
        Create a collection for curating posts under the authenticated account.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/v1/collections",
            body=maybe_transform(
                {
                    "description": description,
                    "name": name,
                },
                collection_create_params.CollectionCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=CollectionCreateResponse,
        )

    def retrieve(
        self,
        collection_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> CollectionRetrieveResponse:
        """Get a collection by its ID.

        Collections can be public or private so the response
        will depend on which account is making the request and if the target collection
        is public, private, owned or not owned by the account.

        Args:
          collection_id: A unique identifier for this resource.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not collection_id:
            raise ValueError(f"Expected a non-empty value for `collection_id` but received {collection_id!r}")
        return self._get(
            f"/v1/collections/{collection_id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=CollectionRetrieveResponse,
        )

    def update(
        self,
        collection_id: str,
        *,
        description: str | NotGiven = NOT_GIVEN,
        name: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> CollectionUpdateResponse:
        """
        Update a collection owned by the authenticated account.

        Args:
          collection_id: A unique identifier for this resource.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not collection_id:
            raise ValueError(f"Expected a non-empty value for `collection_id` but received {collection_id!r}")
        return self._patch(
            f"/v1/collections/{collection_id}",
            body=maybe_transform(
                {
                    "description": description,
                    "name": name,
                },
                collection_update_params.CollectionUpdateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=CollectionUpdateResponse,
        )

    def list(
        self,
        *,
        account_handle: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> CollectionListResponse:
        """
        List all collections using the filtering options.

        Args:
          account_handle: Account handle.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get(
            "/v1/collections",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform({"account_handle": account_handle}, collection_list_params.CollectionListParams),
            ),
            cast_to=CollectionListResponse,
        )

    def delete(
        self,
        collection_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> None:
        """
        Delete a collection owned by the authenticated account.

        Args:
          collection_id: A unique identifier for this resource.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not collection_id:
            raise ValueError(f"Expected a non-empty value for `collection_id` but received {collection_id!r}")
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return self._delete(
            f"/v1/collections/{collection_id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )


class AsyncCollectionsResource(AsyncAPIResource):
    @cached_property
    def posts(self) -> AsyncPostsResource:
        return AsyncPostsResource(self._client)

    @cached_property
    def nodes(self) -> AsyncNodesResource:
        return AsyncNodesResource(self._client)

    @cached_property
    def with_raw_response(self) -> AsyncCollectionsResourceWithRawResponse:
        return AsyncCollectionsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncCollectionsResourceWithStreamingResponse:
        return AsyncCollectionsResourceWithStreamingResponse(self)

    async def create(
        self,
        *,
        description: str,
        name: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> CollectionCreateResponse:
        """
        Create a collection for curating posts under the authenticated account.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/v1/collections",
            body=await async_maybe_transform(
                {
                    "description": description,
                    "name": name,
                },
                collection_create_params.CollectionCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=CollectionCreateResponse,
        )

    async def retrieve(
        self,
        collection_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> CollectionRetrieveResponse:
        """Get a collection by its ID.

        Collections can be public or private so the response
        will depend on which account is making the request and if the target collection
        is public, private, owned or not owned by the account.

        Args:
          collection_id: A unique identifier for this resource.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not collection_id:
            raise ValueError(f"Expected a non-empty value for `collection_id` but received {collection_id!r}")
        return await self._get(
            f"/v1/collections/{collection_id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=CollectionRetrieveResponse,
        )

    async def update(
        self,
        collection_id: str,
        *,
        description: str | NotGiven = NOT_GIVEN,
        name: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> CollectionUpdateResponse:
        """
        Update a collection owned by the authenticated account.

        Args:
          collection_id: A unique identifier for this resource.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not collection_id:
            raise ValueError(f"Expected a non-empty value for `collection_id` but received {collection_id!r}")
        return await self._patch(
            f"/v1/collections/{collection_id}",
            body=await async_maybe_transform(
                {
                    "description": description,
                    "name": name,
                },
                collection_update_params.CollectionUpdateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=CollectionUpdateResponse,
        )

    async def list(
        self,
        *,
        account_handle: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> CollectionListResponse:
        """
        List all collections using the filtering options.

        Args:
          account_handle: Account handle.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._get(
            "/v1/collections",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {"account_handle": account_handle}, collection_list_params.CollectionListParams
                ),
            ),
            cast_to=CollectionListResponse,
        )

    async def delete(
        self,
        collection_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> None:
        """
        Delete a collection owned by the authenticated account.

        Args:
          collection_id: A unique identifier for this resource.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not collection_id:
            raise ValueError(f"Expected a non-empty value for `collection_id` but received {collection_id!r}")
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return await self._delete(
            f"/v1/collections/{collection_id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )


class CollectionsResourceWithRawResponse:
    def __init__(self, collections: CollectionsResource) -> None:
        self._collections = collections

        self.create = to_raw_response_wrapper(
            collections.create,
        )
        self.retrieve = to_raw_response_wrapper(
            collections.retrieve,
        )
        self.update = to_raw_response_wrapper(
            collections.update,
        )
        self.list = to_raw_response_wrapper(
            collections.list,
        )
        self.delete = to_raw_response_wrapper(
            collections.delete,
        )

    @cached_property
    def posts(self) -> PostsResourceWithRawResponse:
        return PostsResourceWithRawResponse(self._collections.posts)

    @cached_property
    def nodes(self) -> NodesResourceWithRawResponse:
        return NodesResourceWithRawResponse(self._collections.nodes)


class AsyncCollectionsResourceWithRawResponse:
    def __init__(self, collections: AsyncCollectionsResource) -> None:
        self._collections = collections

        self.create = async_to_raw_response_wrapper(
            collections.create,
        )
        self.retrieve = async_to_raw_response_wrapper(
            collections.retrieve,
        )
        self.update = async_to_raw_response_wrapper(
            collections.update,
        )
        self.list = async_to_raw_response_wrapper(
            collections.list,
        )
        self.delete = async_to_raw_response_wrapper(
            collections.delete,
        )

    @cached_property
    def posts(self) -> AsyncPostsResourceWithRawResponse:
        return AsyncPostsResourceWithRawResponse(self._collections.posts)

    @cached_property
    def nodes(self) -> AsyncNodesResourceWithRawResponse:
        return AsyncNodesResourceWithRawResponse(self._collections.nodes)


class CollectionsResourceWithStreamingResponse:
    def __init__(self, collections: CollectionsResource) -> None:
        self._collections = collections

        self.create = to_streamed_response_wrapper(
            collections.create,
        )
        self.retrieve = to_streamed_response_wrapper(
            collections.retrieve,
        )
        self.update = to_streamed_response_wrapper(
            collections.update,
        )
        self.list = to_streamed_response_wrapper(
            collections.list,
        )
        self.delete = to_streamed_response_wrapper(
            collections.delete,
        )

    @cached_property
    def posts(self) -> PostsResourceWithStreamingResponse:
        return PostsResourceWithStreamingResponse(self._collections.posts)

    @cached_property
    def nodes(self) -> NodesResourceWithStreamingResponse:
        return NodesResourceWithStreamingResponse(self._collections.nodes)


class AsyncCollectionsResourceWithStreamingResponse:
    def __init__(self, collections: AsyncCollectionsResource) -> None:
        self._collections = collections

        self.create = async_to_streamed_response_wrapper(
            collections.create,
        )
        self.retrieve = async_to_streamed_response_wrapper(
            collections.retrieve,
        )
        self.update = async_to_streamed_response_wrapper(
            collections.update,
        )
        self.list = async_to_streamed_response_wrapper(
            collections.list,
        )
        self.delete = async_to_streamed_response_wrapper(
            collections.delete,
        )

    @cached_property
    def posts(self) -> AsyncPostsResourceWithStreamingResponse:
        return AsyncPostsResourceWithStreamingResponse(self._collections.posts)

    @cached_property
    def nodes(self) -> AsyncNodesResourceWithStreamingResponse:
        return AsyncNodesResourceWithStreamingResponse(self._collections.nodes)
