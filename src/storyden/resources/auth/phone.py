# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import httpx

from ..._types import NOT_GIVEN, Body, Query, Headers, NotGiven
from ..._utils import (
    maybe_transform,
    async_maybe_transform,
)
from ..._compat import cached_property
from ..._resource import SyncAPIResource, AsyncAPIResource
from ..._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from ...types.auth import phone_create_params, phone_update_params
from ..._base_client import make_request_options
from ...types.auth.phone_create_response import PhoneCreateResponse
from ...types.auth.phone_update_response import PhoneUpdateResponse

__all__ = ["PhoneResource", "AsyncPhoneResource"]


class PhoneResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> PhoneResourceWithRawResponse:
        return PhoneResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> PhoneResourceWithStreamingResponse:
        return PhoneResourceWithStreamingResponse(self)

    def create(
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
    ) -> PhoneCreateResponse:
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
                phone_create_params.PhoneCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=PhoneCreateResponse,
        )

    def update(
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
    ) -> PhoneUpdateResponse:
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
            body=maybe_transform({"code": code}, phone_update_params.PhoneUpdateParams),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=PhoneUpdateResponse,
        )


class AsyncPhoneResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncPhoneResourceWithRawResponse:
        return AsyncPhoneResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncPhoneResourceWithStreamingResponse:
        return AsyncPhoneResourceWithStreamingResponse(self)

    async def create(
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
    ) -> PhoneCreateResponse:
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
                phone_create_params.PhoneCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=PhoneCreateResponse,
        )

    async def update(
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
    ) -> PhoneUpdateResponse:
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
            body=await async_maybe_transform({"code": code}, phone_update_params.PhoneUpdateParams),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=PhoneUpdateResponse,
        )


class PhoneResourceWithRawResponse:
    def __init__(self, phone: PhoneResource) -> None:
        self._phone = phone

        self.create = to_raw_response_wrapper(
            phone.create,
        )
        self.update = to_raw_response_wrapper(
            phone.update,
        )


class AsyncPhoneResourceWithRawResponse:
    def __init__(self, phone: AsyncPhoneResource) -> None:
        self._phone = phone

        self.create = async_to_raw_response_wrapper(
            phone.create,
        )
        self.update = async_to_raw_response_wrapper(
            phone.update,
        )


class PhoneResourceWithStreamingResponse:
    def __init__(self, phone: PhoneResource) -> None:
        self._phone = phone

        self.create = to_streamed_response_wrapper(
            phone.create,
        )
        self.update = to_streamed_response_wrapper(
            phone.update,
        )


class AsyncPhoneResourceWithStreamingResponse:
    def __init__(self, phone: AsyncPhoneResource) -> None:
        self._phone = phone

        self.create = async_to_streamed_response_wrapper(
            phone.create,
        )
        self.update = async_to_streamed_response_wrapper(
            phone.update,
        )
