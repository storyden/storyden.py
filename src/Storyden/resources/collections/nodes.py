# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import httpx

from ..._compat import cached_property

from ...types.collections.node_add_response import NodeAddResponse

from ..._base_client import make_request_options

from ...types.collections.node_remove_response import NodeRemoveResponse

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

__all__ = ["NodesResource", "AsyncNodesResource"]


class NodesResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> NodesResourceWithRawResponse:
        return NodesResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> NodesResourceWithStreamingResponse:
        return NodesResourceWithStreamingResponse(self)

    def add(
        self,
        node_id: str,
        *,
        collection_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> NodeAddResponse:
        """Add a node to a collection.

        The collection must be owned by the account making
        the request. The node can be any published node or any node not published but
        owned by the collection owner.

        Args:
          collection_id: A unique identifier for this resource.

          node_id: A unique identifier for this resource.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not collection_id:
            raise ValueError(f"Expected a non-empty value for `collection_id` but received {collection_id!r}")
        if not node_id:
            raise ValueError(f"Expected a non-empty value for `node_id` but received {node_id!r}")
        return self._put(
            f"/v1/collections/{collection_id}/nodes/{node_id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NodeAddResponse,
        )

    def remove(
        self,
        node_id: str,
        *,
        collection_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> NodeRemoveResponse:
        """Remove a node from a collection.

        The collection must be owned by the account
        making the request.

        Args:
          collection_id: A unique identifier for this resource.

          node_id: A unique identifier for this resource.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not collection_id:
            raise ValueError(f"Expected a non-empty value for `collection_id` but received {collection_id!r}")
        if not node_id:
            raise ValueError(f"Expected a non-empty value for `node_id` but received {node_id!r}")
        return self._delete(
            f"/v1/collections/{collection_id}/nodes/{node_id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NodeRemoveResponse,
        )


class AsyncNodesResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncNodesResourceWithRawResponse:
        return AsyncNodesResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncNodesResourceWithStreamingResponse:
        return AsyncNodesResourceWithStreamingResponse(self)

    async def add(
        self,
        node_id: str,
        *,
        collection_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> NodeAddResponse:
        """Add a node to a collection.

        The collection must be owned by the account making
        the request. The node can be any published node or any node not published but
        owned by the collection owner.

        Args:
          collection_id: A unique identifier for this resource.

          node_id: A unique identifier for this resource.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not collection_id:
            raise ValueError(f"Expected a non-empty value for `collection_id` but received {collection_id!r}")
        if not node_id:
            raise ValueError(f"Expected a non-empty value for `node_id` but received {node_id!r}")
        return await self._put(
            f"/v1/collections/{collection_id}/nodes/{node_id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NodeAddResponse,
        )

    async def remove(
        self,
        node_id: str,
        *,
        collection_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> NodeRemoveResponse:
        """Remove a node from a collection.

        The collection must be owned by the account
        making the request.

        Args:
          collection_id: A unique identifier for this resource.

          node_id: A unique identifier for this resource.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not collection_id:
            raise ValueError(f"Expected a non-empty value for `collection_id` but received {collection_id!r}")
        if not node_id:
            raise ValueError(f"Expected a non-empty value for `node_id` but received {node_id!r}")
        return await self._delete(
            f"/v1/collections/{collection_id}/nodes/{node_id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NodeRemoveResponse,
        )


class NodesResourceWithRawResponse:
    def __init__(self, nodes: NodesResource) -> None:
        self._nodes = nodes

        self.add = to_raw_response_wrapper(
            nodes.add,
        )
        self.remove = to_raw_response_wrapper(
            nodes.remove,
        )


class AsyncNodesResourceWithRawResponse:
    def __init__(self, nodes: AsyncNodesResource) -> None:
        self._nodes = nodes

        self.add = async_to_raw_response_wrapper(
            nodes.add,
        )
        self.remove = async_to_raw_response_wrapper(
            nodes.remove,
        )


class NodesResourceWithStreamingResponse:
    def __init__(self, nodes: NodesResource) -> None:
        self._nodes = nodes

        self.add = to_streamed_response_wrapper(
            nodes.add,
        )
        self.remove = to_streamed_response_wrapper(
            nodes.remove,
        )


class AsyncNodesResourceWithStreamingResponse:
    def __init__(self, nodes: AsyncNodesResource) -> None:
        self._nodes = nodes

        self.add = async_to_streamed_response_wrapper(
            nodes.add,
        )
        self.remove = async_to_streamed_response_wrapper(
            nodes.remove,
        )
