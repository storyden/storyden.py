# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import httpx

from ..._compat import cached_property

from ...types.nodes.asset_add_response import AssetAddResponse

from ..._utils import maybe_transform, async_maybe_transform

from ..._base_client import make_request_options

from typing_extensions import Literal

from ...types.nodes.asset_remove_response import AssetRemoveResponse

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
from ...types.nodes import asset_add_params

__all__ = ["AssetsResource", "AsyncAssetsResource"]


class AssetsResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AssetsResourceWithRawResponse:
        return AssetsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AssetsResourceWithStreamingResponse:
        return AssetsResourceWithStreamingResponse(self)

    def add(
        self,
        asset_id: str,
        *,
        node_slug: str,
        content_fill_rule: Literal["replace"] | NotGiven = NOT_GIVEN,
        node_content_fill_target: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> AssetAddResponse:
        """
        Add an asset to a node.

        Args:
          node_slug: A unique identifier for this resource.

          content_fill_rule: Use the content extracted from the child resource to modify the target resource.
              This can be used to populate a node from a asset or link. For example, if you
              wanted to create a node that held the contents of a PDF file, you can upload the
              file with a target node and a fill rule set.

          node_content_fill_target: When NodeContentFillRuleQuery is used, this option must be set in order to
              specify which node will receive content extracted from the source.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not node_slug:
            raise ValueError(f"Expected a non-empty value for `node_slug` but received {node_slug!r}")
        if not asset_id:
            raise ValueError(f"Expected a non-empty value for `asset_id` but received {asset_id!r}")
        return self._put(
            f"/v1/nodes/{node_slug}/assets/{asset_id}",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "content_fill_rule": content_fill_rule,
                        "node_content_fill_target": node_content_fill_target,
                    },
                    asset_add_params.AssetAddParams,
                ),
            ),
            cast_to=AssetAddResponse,
        )

    def remove(
        self,
        asset_id: str,
        *,
        node_slug: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> AssetRemoveResponse:
        """
        Remove an asset from a node.

        Args:
          node_slug: A unique identifier for this resource.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not node_slug:
            raise ValueError(f"Expected a non-empty value for `node_slug` but received {node_slug!r}")
        if not asset_id:
            raise ValueError(f"Expected a non-empty value for `asset_id` but received {asset_id!r}")
        return self._delete(
            f"/v1/nodes/{node_slug}/assets/{asset_id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=AssetRemoveResponse,
        )


class AsyncAssetsResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncAssetsResourceWithRawResponse:
        return AsyncAssetsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncAssetsResourceWithStreamingResponse:
        return AsyncAssetsResourceWithStreamingResponse(self)

    async def add(
        self,
        asset_id: str,
        *,
        node_slug: str,
        content_fill_rule: Literal["replace"] | NotGiven = NOT_GIVEN,
        node_content_fill_target: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> AssetAddResponse:
        """
        Add an asset to a node.

        Args:
          node_slug: A unique identifier for this resource.

          content_fill_rule: Use the content extracted from the child resource to modify the target resource.
              This can be used to populate a node from a asset or link. For example, if you
              wanted to create a node that held the contents of a PDF file, you can upload the
              file with a target node and a fill rule set.

          node_content_fill_target: When NodeContentFillRuleQuery is used, this option must be set in order to
              specify which node will receive content extracted from the source.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not node_slug:
            raise ValueError(f"Expected a non-empty value for `node_slug` but received {node_slug!r}")
        if not asset_id:
            raise ValueError(f"Expected a non-empty value for `asset_id` but received {asset_id!r}")
        return await self._put(
            f"/v1/nodes/{node_slug}/assets/{asset_id}",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {
                        "content_fill_rule": content_fill_rule,
                        "node_content_fill_target": node_content_fill_target,
                    },
                    asset_add_params.AssetAddParams,
                ),
            ),
            cast_to=AssetAddResponse,
        )

    async def remove(
        self,
        asset_id: str,
        *,
        node_slug: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> AssetRemoveResponse:
        """
        Remove an asset from a node.

        Args:
          node_slug: A unique identifier for this resource.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not node_slug:
            raise ValueError(f"Expected a non-empty value for `node_slug` but received {node_slug!r}")
        if not asset_id:
            raise ValueError(f"Expected a non-empty value for `asset_id` but received {asset_id!r}")
        return await self._delete(
            f"/v1/nodes/{node_slug}/assets/{asset_id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=AssetRemoveResponse,
        )


class AssetsResourceWithRawResponse:
    def __init__(self, assets: AssetsResource) -> None:
        self._assets = assets

        self.add = to_raw_response_wrapper(
            assets.add,
        )
        self.remove = to_raw_response_wrapper(
            assets.remove,
        )


class AsyncAssetsResourceWithRawResponse:
    def __init__(self, assets: AsyncAssetsResource) -> None:
        self._assets = assets

        self.add = async_to_raw_response_wrapper(
            assets.add,
        )
        self.remove = async_to_raw_response_wrapper(
            assets.remove,
        )


class AssetsResourceWithStreamingResponse:
    def __init__(self, assets: AssetsResource) -> None:
        self._assets = assets

        self.add = to_streamed_response_wrapper(
            assets.add,
        )
        self.remove = to_streamed_response_wrapper(
            assets.remove,
        )


class AsyncAssetsResourceWithStreamingResponse:
    def __init__(self, assets: AsyncAssetsResource) -> None:
        self._assets = assets

        self.add = async_to_streamed_response_wrapper(
            assets.add,
        )
        self.remove = async_to_streamed_response_wrapper(
            assets.remove,
        )
