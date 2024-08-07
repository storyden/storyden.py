# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import httpx

from ..._compat import cached_property

from ...types.nodes.visibility_update_response import VisibilityUpdateResponse

from ..._utils import maybe_transform, async_maybe_transform

from ..._base_client import make_request_options

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
from ...types.nodes import visibility_update_params

__all__ = ["VisibilityResource", "AsyncVisibilityResource"]


class VisibilityResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> VisibilityResourceWithRawResponse:
        return VisibilityResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> VisibilityResourceWithStreamingResponse:
        return VisibilityResourceWithStreamingResponse(self)

    def update(
        self,
        node_slug: str,
        *,
        visibility: Literal["draft", "unlisted", "review", "published"],
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> VisibilityUpdateResponse:
        """Update the visibility of a node.

        When changed, this may trigger other operations
        such as notifications/newsletters. Changing the visibility of anything to
        "published" is often accompanied by some other side effects.

        Args:
          node_slug: A unique identifier for this resource.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not node_slug:
            raise ValueError(f"Expected a non-empty value for `node_slug` but received {node_slug!r}")
        return self._patch(
            f"/v1/nodes/{node_slug}/visibility",
            body=maybe_transform({"visibility": visibility}, visibility_update_params.VisibilityUpdateParams),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=VisibilityUpdateResponse,
        )


class AsyncVisibilityResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncVisibilityResourceWithRawResponse:
        return AsyncVisibilityResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncVisibilityResourceWithStreamingResponse:
        return AsyncVisibilityResourceWithStreamingResponse(self)

    async def update(
        self,
        node_slug: str,
        *,
        visibility: Literal["draft", "unlisted", "review", "published"],
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> VisibilityUpdateResponse:
        """Update the visibility of a node.

        When changed, this may trigger other operations
        such as notifications/newsletters. Changing the visibility of anything to
        "published" is often accompanied by some other side effects.

        Args:
          node_slug: A unique identifier for this resource.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not node_slug:
            raise ValueError(f"Expected a non-empty value for `node_slug` but received {node_slug!r}")
        return await self._patch(
            f"/v1/nodes/{node_slug}/visibility",
            body=await async_maybe_transform(
                {"visibility": visibility}, visibility_update_params.VisibilityUpdateParams
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=VisibilityUpdateResponse,
        )


class VisibilityResourceWithRawResponse:
    def __init__(self, visibility: VisibilityResource) -> None:
        self._visibility = visibility

        self.update = to_raw_response_wrapper(
            visibility.update,
        )


class AsyncVisibilityResourceWithRawResponse:
    def __init__(self, visibility: AsyncVisibilityResource) -> None:
        self._visibility = visibility

        self.update = async_to_raw_response_wrapper(
            visibility.update,
        )


class VisibilityResourceWithStreamingResponse:
    def __init__(self, visibility: VisibilityResource) -> None:
        self._visibility = visibility

        self.update = to_streamed_response_wrapper(
            visibility.update,
        )


class AsyncVisibilityResourceWithStreamingResponse:
    def __init__(self, visibility: AsyncVisibilityResource) -> None:
        self._visibility = visibility

        self.update = async_to_streamed_response_wrapper(
            visibility.update,
        )
