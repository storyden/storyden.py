# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import httpx

from .._compat import cached_property

from ..types.asset_create_response import AssetCreateResponse

from .._utils import maybe_transform, async_maybe_transform

from .._base_client import make_request_options

from .._types import FileTypes

from typing_extensions import Literal

from .._response import (
    BinaryAPIResponse,
    AsyncBinaryAPIResponse,
    to_raw_response_wrapper,
    to_custom_raw_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_custom_raw_response_wrapper,
    to_streamed_response_wrapper,
    to_custom_streamed_response_wrapper,
    StreamedBinaryAPIResponse,
    async_to_streamed_response_wrapper,
    async_to_custom_streamed_response_wrapper,
    AsyncStreamedBinaryAPIResponse,
)

import warnings
from typing import TYPE_CHECKING, Optional, Union, List, Dict, Any, Mapping, cast, overload
from typing_extensions import Literal
from .._utils import extract_files, maybe_transform, required_args, deepcopy_minimal, strip_not_given
from .._types import NotGiven, Timeout, Headers, NoneType, Query, Body, NOT_GIVEN, FileTypes, BinaryResponseContent
from .._resource import SyncAPIResource, AsyncAPIResource
from ..types import shared_params
from ..types import asset_create_params

__all__ = ["AssetsResource", "AsyncAssetsResource"]


class AssetsResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AssetsResourceWithRawResponse:
        return AssetsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AssetsResourceWithStreamingResponse:
        return AssetsResourceWithStreamingResponse(self)

    def create(
        self,
        *,
        body: FileTypes,
        content_fill_rule: Literal["replace"] | NotGiven = NOT_GIVEN,
        filename: str | NotGiven = NOT_GIVEN,
        node_content_fill_target: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> AssetCreateResponse:
        """
        Upload and process a media file.

        Args:
          content_fill_rule: Use the content extracted from the child resource to modify the target resource.
              This can be used to populate a node from a asset or link. For example, if you
              wanted to create a node that held the contents of a PDF file, you can upload the
              file with a target node and a fill rule set.

          filename: The client-provided file name for the asset.

          node_content_fill_target: When NodeContentFillRuleQuery is used, this option must be set in order to
              specify which node will receive content extracted from the source.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/v1/assets",
            body=maybe_transform(body, asset_create_params.AssetCreateParams),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "content_fill_rule": content_fill_rule,
                        "filename": filename,
                        "node_content_fill_target": node_content_fill_target,
                    },
                    asset_create_params.AssetCreateParams,
                ),
            ),
            cast_to=AssetCreateResponse,
        )

    def retrieve(
        self,
        asset_filename: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> BinaryAPIResponse:
        """
        Download an asset by its ID.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not asset_filename:
            raise ValueError(f"Expected a non-empty value for `asset_filename` but received {asset_filename!r}")
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return self._get(
            f"/v1/assets/{asset_filename}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=BinaryAPIResponse,
        )


class AsyncAssetsResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncAssetsResourceWithRawResponse:
        return AsyncAssetsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncAssetsResourceWithStreamingResponse:
        return AsyncAssetsResourceWithStreamingResponse(self)

    async def create(
        self,
        *,
        body: FileTypes,
        content_fill_rule: Literal["replace"] | NotGiven = NOT_GIVEN,
        filename: str | NotGiven = NOT_GIVEN,
        node_content_fill_target: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> AssetCreateResponse:
        """
        Upload and process a media file.

        Args:
          content_fill_rule: Use the content extracted from the child resource to modify the target resource.
              This can be used to populate a node from a asset or link. For example, if you
              wanted to create a node that held the contents of a PDF file, you can upload the
              file with a target node and a fill rule set.

          filename: The client-provided file name for the asset.

          node_content_fill_target: When NodeContentFillRuleQuery is used, this option must be set in order to
              specify which node will receive content extracted from the source.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/v1/assets",
            body=await async_maybe_transform(body, asset_create_params.AssetCreateParams),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {
                        "content_fill_rule": content_fill_rule,
                        "filename": filename,
                        "node_content_fill_target": node_content_fill_target,
                    },
                    asset_create_params.AssetCreateParams,
                ),
            ),
            cast_to=AssetCreateResponse,
        )

    async def retrieve(
        self,
        asset_filename: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> AsyncBinaryAPIResponse:
        """
        Download an asset by its ID.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not asset_filename:
            raise ValueError(f"Expected a non-empty value for `asset_filename` but received {asset_filename!r}")
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return await self._get(
            f"/v1/assets/{asset_filename}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=AsyncBinaryAPIResponse,
        )


class AssetsResourceWithRawResponse:
    def __init__(self, assets: AssetsResource) -> None:
        self._assets = assets

        self.create = to_raw_response_wrapper(
            assets.create,
        )
        self.retrieve = to_custom_raw_response_wrapper(
            assets.retrieve,
            BinaryAPIResponse,
        )


class AsyncAssetsResourceWithRawResponse:
    def __init__(self, assets: AsyncAssetsResource) -> None:
        self._assets = assets

        self.create = async_to_raw_response_wrapper(
            assets.create,
        )
        self.retrieve = async_to_custom_raw_response_wrapper(
            assets.retrieve,
            AsyncBinaryAPIResponse,
        )


class AssetsResourceWithStreamingResponse:
    def __init__(self, assets: AssetsResource) -> None:
        self._assets = assets

        self.create = to_streamed_response_wrapper(
            assets.create,
        )
        self.retrieve = to_custom_streamed_response_wrapper(
            assets.retrieve,
            StreamedBinaryAPIResponse,
        )


class AsyncAssetsResourceWithStreamingResponse:
    def __init__(self, assets: AsyncAssetsResource) -> None:
        self._assets = assets

        self.create = async_to_streamed_response_wrapper(
            assets.create,
        )
        self.retrieve = async_to_custom_streamed_response_wrapper(
            assets.retrieve,
            AsyncStreamedBinaryAPIResponse,
        )
