# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import httpx

from ..._compat import cached_property

from ...types.admin.ban_delete_suspended_response import BanDeleteSuspendedResponse

from ..._base_client import make_request_options

from ...types.admin.ban_suspend_response import BanSuspendResponse

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

__all__ = ["BansResource", "AsyncBansResource"]


class BansResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> BansResourceWithRawResponse:
        return BansResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> BansResourceWithStreamingResponse:
        return BansResourceWithStreamingResponse(self)

    def delete_suspended(
        self,
        account_handle: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> BanDeleteSuspendedResponse:
        """
        Given the account is suspended, remove the suspended state.

        Args:
          account_handle: The unique @ handle of an account.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_handle:
            raise ValueError(f"Expected a non-empty value for `account_handle` but received {account_handle!r}")
        return self._delete(
            f"/v1/admin/bans/{account_handle}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=BanDeleteSuspendedResponse,
        )

    def suspend(
        self,
        account_handle: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> BanSuspendResponse:
        """Suspend an account - soft delete.

        This disables the ability for the account
        owner to log in and use the platform. It keeps the account on record for linkage
        to content so UI doesn't break. It does not change anything else about the
        account such as the avatar, name, etc.

        Args:
          account_handle: The unique @ handle of an account.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_handle:
            raise ValueError(f"Expected a non-empty value for `account_handle` but received {account_handle!r}")
        return self._post(
            f"/v1/admin/bans/{account_handle}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=BanSuspendResponse,
        )


class AsyncBansResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncBansResourceWithRawResponse:
        return AsyncBansResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncBansResourceWithStreamingResponse:
        return AsyncBansResourceWithStreamingResponse(self)

    async def delete_suspended(
        self,
        account_handle: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> BanDeleteSuspendedResponse:
        """
        Given the account is suspended, remove the suspended state.

        Args:
          account_handle: The unique @ handle of an account.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_handle:
            raise ValueError(f"Expected a non-empty value for `account_handle` but received {account_handle!r}")
        return await self._delete(
            f"/v1/admin/bans/{account_handle}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=BanDeleteSuspendedResponse,
        )

    async def suspend(
        self,
        account_handle: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> BanSuspendResponse:
        """Suspend an account - soft delete.

        This disables the ability for the account
        owner to log in and use the platform. It keeps the account on record for linkage
        to content so UI doesn't break. It does not change anything else about the
        account such as the avatar, name, etc.

        Args:
          account_handle: The unique @ handle of an account.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_handle:
            raise ValueError(f"Expected a non-empty value for `account_handle` but received {account_handle!r}")
        return await self._post(
            f"/v1/admin/bans/{account_handle}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=BanSuspendResponse,
        )


class BansResourceWithRawResponse:
    def __init__(self, bans: BansResource) -> None:
        self._bans = bans

        self.delete_suspended = to_raw_response_wrapper(
            bans.delete_suspended,
        )
        self.suspend = to_raw_response_wrapper(
            bans.suspend,
        )


class AsyncBansResourceWithRawResponse:
    def __init__(self, bans: AsyncBansResource) -> None:
        self._bans = bans

        self.delete_suspended = async_to_raw_response_wrapper(
            bans.delete_suspended,
        )
        self.suspend = async_to_raw_response_wrapper(
            bans.suspend,
        )


class BansResourceWithStreamingResponse:
    def __init__(self, bans: BansResource) -> None:
        self._bans = bans

        self.delete_suspended = to_streamed_response_wrapper(
            bans.delete_suspended,
        )
        self.suspend = to_streamed_response_wrapper(
            bans.suspend,
        )


class AsyncBansResourceWithStreamingResponse:
    def __init__(self, bans: AsyncBansResource) -> None:
        self._bans = bans

        self.delete_suspended = async_to_streamed_response_wrapper(
            bans.delete_suspended,
        )
        self.suspend = async_to_streamed_response_wrapper(
            bans.suspend,
        )
