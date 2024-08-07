# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import httpx

from ..._compat import cached_property

from ...types.auth.phone_complete_response import PhoneCompleteResponse

from ..._utils import maybe_transform, async_maybe_transform

from ..._base_client import make_request_options

from ...types.auth.phone_start_response import PhoneStartResponse

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
from ...types.auth import phone_complete_params
from ...types.auth import phone_start_params

__all__ = ["PhoneResource", "AsyncPhoneResource"]


class PhoneResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> PhoneResourceWithRawResponse:
        return PhoneResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> PhoneResourceWithStreamingResponse:
        return PhoneResourceWithStreamingResponse(self)

    def complete(
        self,
        account_handle: str,
        *,
        code: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> PhoneCompleteResponse:
        """
        Complete the phone number authentication flow by submitting the one-time code
        that was sent to the user's phone.

        Args:
          account_handle: The unique @ handle of an account.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_handle:
            raise ValueError(f"Expected a non-empty value for `account_handle` but received {account_handle!r}")
        return self._put(
            f"/v1/auth/phone/{account_handle}",
            body=maybe_transform({"code": code}, phone_complete_params.PhoneCompleteParams),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=PhoneCompleteResponse,
        )

    def start(
        self,
        *,
        identifier: str,
        phone_number: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> PhoneStartResponse:
        """Start the authentication flow with a phone number.

        The handler will send a
        one-time code to the provided phone number which must then be sent to the other
        phone endpoint to verify the number and validate the account.

        Args:
          identifier: The desired username to link to the phone number.

          phone_number: The phone number to receive the one-time code on.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/v1/auth/phone",
            body=maybe_transform(
                {
                    "identifier": identifier,
                    "phone_number": phone_number,
                },
                phone_start_params.PhoneStartParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=PhoneStartResponse,
        )


class AsyncPhoneResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncPhoneResourceWithRawResponse:
        return AsyncPhoneResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncPhoneResourceWithStreamingResponse:
        return AsyncPhoneResourceWithStreamingResponse(self)

    async def complete(
        self,
        account_handle: str,
        *,
        code: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> PhoneCompleteResponse:
        """
        Complete the phone number authentication flow by submitting the one-time code
        that was sent to the user's phone.

        Args:
          account_handle: The unique @ handle of an account.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_handle:
            raise ValueError(f"Expected a non-empty value for `account_handle` but received {account_handle!r}")
        return await self._put(
            f"/v1/auth/phone/{account_handle}",
            body=await async_maybe_transform({"code": code}, phone_complete_params.PhoneCompleteParams),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=PhoneCompleteResponse,
        )

    async def start(
        self,
        *,
        identifier: str,
        phone_number: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> PhoneStartResponse:
        """Start the authentication flow with a phone number.

        The handler will send a
        one-time code to the provided phone number which must then be sent to the other
        phone endpoint to verify the number and validate the account.

        Args:
          identifier: The desired username to link to the phone number.

          phone_number: The phone number to receive the one-time code on.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/v1/auth/phone",
            body=await async_maybe_transform(
                {
                    "identifier": identifier,
                    "phone_number": phone_number,
                },
                phone_start_params.PhoneStartParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=PhoneStartResponse,
        )


class PhoneResourceWithRawResponse:
    def __init__(self, phone: PhoneResource) -> None:
        self._phone = phone

        self.complete = to_raw_response_wrapper(
            phone.complete,
        )
        self.start = to_raw_response_wrapper(
            phone.start,
        )


class AsyncPhoneResourceWithRawResponse:
    def __init__(self, phone: AsyncPhoneResource) -> None:
        self._phone = phone

        self.complete = async_to_raw_response_wrapper(
            phone.complete,
        )
        self.start = async_to_raw_response_wrapper(
            phone.start,
        )


class PhoneResourceWithStreamingResponse:
    def __init__(self, phone: PhoneResource) -> None:
        self._phone = phone

        self.complete = to_streamed_response_wrapper(
            phone.complete,
        )
        self.start = to_streamed_response_wrapper(
            phone.start,
        )


class AsyncPhoneResourceWithStreamingResponse:
    def __init__(self, phone: AsyncPhoneResource) -> None:
        self._phone = phone

        self.complete = async_to_streamed_response_wrapper(
            phone.complete,
        )
        self.start = async_to_streamed_response_wrapper(
            phone.start,
        )
