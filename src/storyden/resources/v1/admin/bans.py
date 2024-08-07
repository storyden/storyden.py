# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import httpx

from ...._types import NOT_GIVEN, Body, Query, Headers, NotGiven
from ...._compat import cached_property
from ...._resource import SyncAPIResource, AsyncAPIResource
from ...._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from ...._base_client import make_request_options
from ....types.v1.admin.ban_create_response import BanCreateResponse
from ....types.v1.admin.ban_delete_response import BanDeleteResponse

__all__ = ["BansResource", "AsyncBansResource"]


class BansResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> BansResourceWithRawResponse:
        return BansResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> BansResourceWithStreamingResponse:
        return BansResourceWithStreamingResponse(self)

    def create(
        self,
        account_handle: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> BanCreateResponse:
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
            cast_to=BanCreateResponse,
        )

    def delete(
        self,
        account_handle: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> BanDeleteResponse:
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
            cast_to=BanDeleteResponse,
        )


class AsyncBansResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncBansResourceWithRawResponse:
        return AsyncBansResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncBansResourceWithStreamingResponse:
        return AsyncBansResourceWithStreamingResponse(self)

    async def create(
        self,
        account_handle: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> BanCreateResponse:
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
            cast_to=BanCreateResponse,
        )

    async def delete(
        self,
        account_handle: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> BanDeleteResponse:
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
            cast_to=BanDeleteResponse,
        )


class BansResourceWithRawResponse:
    def __init__(self, bans: BansResource) -> None:
        self._bans = bans

        self.create = to_raw_response_wrapper(
            bans.create,
        )
        self.delete = to_raw_response_wrapper(
            bans.delete,
        )


class AsyncBansResourceWithRawResponse:
    def __init__(self, bans: AsyncBansResource) -> None:
        self._bans = bans

        self.create = async_to_raw_response_wrapper(
            bans.create,
        )
        self.delete = async_to_raw_response_wrapper(
            bans.delete,
        )


class BansResourceWithStreamingResponse:
    def __init__(self, bans: BansResource) -> None:
        self._bans = bans

        self.create = to_streamed_response_wrapper(
            bans.create,
        )
        self.delete = to_streamed_response_wrapper(
            bans.delete,
        )


class AsyncBansResourceWithStreamingResponse:
    def __init__(self, bans: AsyncBansResource) -> None:
        self._bans = bans

        self.create = async_to_streamed_response_wrapper(
            bans.create,
        )
        self.delete = async_to_streamed_response_wrapper(
            bans.delete,
        )
