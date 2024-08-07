# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import httpx

from .bans import BansResource, AsyncBansResource

from ..._compat import cached_property

from ...types.admin_update_response import AdminUpdateResponse

from ..._utils import maybe_transform, async_maybe_transform

from ..._base_client import make_request_options

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
from ...types import admin_update_params
from .bans import (
    BansResource,
    AsyncBansResource,
    BansResourceWithRawResponse,
    AsyncBansResourceWithRawResponse,
    BansResourceWithStreamingResponse,
    AsyncBansResourceWithStreamingResponse,
)

__all__ = ["AdminResource", "AsyncAdminResource"]


class AdminResource(SyncAPIResource):
    @cached_property
    def bans(self) -> BansResource:
        return BansResource(self._client)

    @cached_property
    def with_raw_response(self) -> AdminResourceWithRawResponse:
        return AdminResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AdminResourceWithStreamingResponse:
        return AdminResourceWithStreamingResponse(self)

    def update(
        self,
        *,
        accent_colour: str | NotGiven = NOT_GIVEN,
        description: str | NotGiven = NOT_GIVEN,
        title: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> AdminUpdateResponse:
        """
        Update non-env configuration settings for installation.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._patch(
            "/v1/admin",
            body=maybe_transform(
                {
                    "accent_colour": accent_colour,
                    "description": description,
                    "title": title,
                },
                admin_update_params.AdminUpdateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=AdminUpdateResponse,
        )


class AsyncAdminResource(AsyncAPIResource):
    @cached_property
    def bans(self) -> AsyncBansResource:
        return AsyncBansResource(self._client)

    @cached_property
    def with_raw_response(self) -> AsyncAdminResourceWithRawResponse:
        return AsyncAdminResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncAdminResourceWithStreamingResponse:
        return AsyncAdminResourceWithStreamingResponse(self)

    async def update(
        self,
        *,
        accent_colour: str | NotGiven = NOT_GIVEN,
        description: str | NotGiven = NOT_GIVEN,
        title: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> AdminUpdateResponse:
        """
        Update non-env configuration settings for installation.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._patch(
            "/v1/admin",
            body=await async_maybe_transform(
                {
                    "accent_colour": accent_colour,
                    "description": description,
                    "title": title,
                },
                admin_update_params.AdminUpdateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=AdminUpdateResponse,
        )


class AdminResourceWithRawResponse:
    def __init__(self, admin: AdminResource) -> None:
        self._admin = admin

        self.update = to_raw_response_wrapper(
            admin.update,
        )

    @cached_property
    def bans(self) -> BansResourceWithRawResponse:
        return BansResourceWithRawResponse(self._admin.bans)


class AsyncAdminResourceWithRawResponse:
    def __init__(self, admin: AsyncAdminResource) -> None:
        self._admin = admin

        self.update = async_to_raw_response_wrapper(
            admin.update,
        )

    @cached_property
    def bans(self) -> AsyncBansResourceWithRawResponse:
        return AsyncBansResourceWithRawResponse(self._admin.bans)


class AdminResourceWithStreamingResponse:
    def __init__(self, admin: AdminResource) -> None:
        self._admin = admin

        self.update = to_streamed_response_wrapper(
            admin.update,
        )

    @cached_property
    def bans(self) -> BansResourceWithStreamingResponse:
        return BansResourceWithStreamingResponse(self._admin.bans)


class AsyncAdminResourceWithStreamingResponse:
    def __init__(self, admin: AsyncAdminResource) -> None:
        self._admin = admin

        self.update = async_to_streamed_response_wrapper(
            admin.update,
        )

    @cached_property
    def bans(self) -> AsyncBansResourceWithStreamingResponse:
        return AsyncBansResourceWithStreamingResponse(self._admin.bans)
