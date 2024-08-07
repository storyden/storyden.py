# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import httpx

from ..._compat import cached_property

from ...types.nodes.child_remove_parent_response import ChildRemoveParentResponse

from ..._base_client import make_request_options

from ...types.nodes.child_set_parent_response import ChildSetParentResponse

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

__all__ = ["ChildrenResource", "AsyncChildrenResource"]


class ChildrenResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> ChildrenResourceWithRawResponse:
        return ChildrenResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> ChildrenResourceWithStreamingResponse:
        return ChildrenResourceWithStreamingResponse(self)

    def remove_parent(
        self,
        node_slug_child: str,
        *,
        node_slug: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> ChildRemoveParentResponse:
        """
        Remove a node from its parent node and back to the top level.

        Args:
          node_slug: A unique identifier for this resource.

          node_slug_child: A unique identifier for this resource.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not node_slug:
            raise ValueError(f"Expected a non-empty value for `node_slug` but received {node_slug!r}")
        if not node_slug_child:
            raise ValueError(f"Expected a non-empty value for `node_slug_child` but received {node_slug_child!r}")
        return self._delete(
            f"/v1/nodes/{node_slug}/nodes/{node_slug_child}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ChildRemoveParentResponse,
        )

    def set_parent(
        self,
        node_slug_child: str,
        *,
        node_slug: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> ChildSetParentResponse:
        """
        Set a node's parent to the specified node

        Args:
          node_slug: A unique identifier for this resource.

          node_slug_child: A unique identifier for this resource.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not node_slug:
            raise ValueError(f"Expected a non-empty value for `node_slug` but received {node_slug!r}")
        if not node_slug_child:
            raise ValueError(f"Expected a non-empty value for `node_slug_child` but received {node_slug_child!r}")
        return self._put(
            f"/v1/nodes/{node_slug}/nodes/{node_slug_child}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ChildSetParentResponse,
        )


class AsyncChildrenResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncChildrenResourceWithRawResponse:
        return AsyncChildrenResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncChildrenResourceWithStreamingResponse:
        return AsyncChildrenResourceWithStreamingResponse(self)

    async def remove_parent(
        self,
        node_slug_child: str,
        *,
        node_slug: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> ChildRemoveParentResponse:
        """
        Remove a node from its parent node and back to the top level.

        Args:
          node_slug: A unique identifier for this resource.

          node_slug_child: A unique identifier for this resource.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not node_slug:
            raise ValueError(f"Expected a non-empty value for `node_slug` but received {node_slug!r}")
        if not node_slug_child:
            raise ValueError(f"Expected a non-empty value for `node_slug_child` but received {node_slug_child!r}")
        return await self._delete(
            f"/v1/nodes/{node_slug}/nodes/{node_slug_child}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ChildRemoveParentResponse,
        )

    async def set_parent(
        self,
        node_slug_child: str,
        *,
        node_slug: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> ChildSetParentResponse:
        """
        Set a node's parent to the specified node

        Args:
          node_slug: A unique identifier for this resource.

          node_slug_child: A unique identifier for this resource.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not node_slug:
            raise ValueError(f"Expected a non-empty value for `node_slug` but received {node_slug!r}")
        if not node_slug_child:
            raise ValueError(f"Expected a non-empty value for `node_slug_child` but received {node_slug_child!r}")
        return await self._put(
            f"/v1/nodes/{node_slug}/nodes/{node_slug_child}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ChildSetParentResponse,
        )


class ChildrenResourceWithRawResponse:
    def __init__(self, children: ChildrenResource) -> None:
        self._children = children

        self.remove_parent = to_raw_response_wrapper(
            children.remove_parent,
        )
        self.set_parent = to_raw_response_wrapper(
            children.set_parent,
        )


class AsyncChildrenResourceWithRawResponse:
    def __init__(self, children: AsyncChildrenResource) -> None:
        self._children = children

        self.remove_parent = async_to_raw_response_wrapper(
            children.remove_parent,
        )
        self.set_parent = async_to_raw_response_wrapper(
            children.set_parent,
        )


class ChildrenResourceWithStreamingResponse:
    def __init__(self, children: ChildrenResource) -> None:
        self._children = children

        self.remove_parent = to_streamed_response_wrapper(
            children.remove_parent,
        )
        self.set_parent = to_streamed_response_wrapper(
            children.set_parent,
        )


class AsyncChildrenResourceWithStreamingResponse:
    def __init__(self, children: AsyncChildrenResource) -> None:
        self._children = children

        self.remove_parent = async_to_streamed_response_wrapper(
            children.remove_parent,
        )
        self.set_parent = async_to_streamed_response_wrapper(
            children.set_parent,
        )
