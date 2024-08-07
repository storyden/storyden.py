# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import httpx

from ...._types import NOT_GIVEN, Body, Query, Headers, NotGiven
from ...._utils import (
    maybe_transform,
    async_maybe_transform,
)
from ...._compat import cached_property
from ...._resource import SyncAPIResource, AsyncAPIResource
from ...._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from ...._base_client import make_request_options
from ....types.auth.webauthn import assert_create_params
from ....types.auth.webauthn.assert_create_response import AssertCreateResponse
from ....types.auth.webauthn.assert_retrieve_response import AssertRetrieveResponse

__all__ = ["AssertResource", "AsyncAssertResource"]


class AssertResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AssertResourceWithRawResponse:
        return AssertResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AssertResourceWithStreamingResponse:
        return AssertResourceWithStreamingResponse(self)

    def create(
        self,
        *,
        id: str,
        raw_id: str,
        response: assert_create_params.Response,
        type: str,
        authenticator_attachment: str | NotGiven = NOT_GIVEN,
        client_extension_results: object | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> AssertCreateResponse:
        """
        Complete the credential assertion and sign in to an account.

        Args:
          response: https://www.w3.org/TR/webauthn-2/#authenticatorresponse

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/v1/auth/webauthn/assert",
            body=maybe_transform(
                {
                    "id": id,
                    "raw_id": raw_id,
                    "response": response,
                    "type": type,
                    "authenticator_attachment": authenticator_attachment,
                    "client_extension_results": client_extension_results,
                },
                assert_create_params.AssertCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=AssertCreateResponse,
        )

    def retrieve(
        self,
        account_handle: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> AssertRetrieveResponse:
        """
        Start the WebAuthn assertion for an existing account.

        Args:
          account_handle: The unique @ handle of an account.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_handle:
            raise ValueError(f"Expected a non-empty value for `account_handle` but received {account_handle!r}")
        return self._get(
            f"/v1/auth/webauthn/assert/{account_handle}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=AssertRetrieveResponse,
        )


class AsyncAssertResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncAssertResourceWithRawResponse:
        return AsyncAssertResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncAssertResourceWithStreamingResponse:
        return AsyncAssertResourceWithStreamingResponse(self)

    async def create(
        self,
        *,
        id: str,
        raw_id: str,
        response: assert_create_params.Response,
        type: str,
        authenticator_attachment: str | NotGiven = NOT_GIVEN,
        client_extension_results: object | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> AssertCreateResponse:
        """
        Complete the credential assertion and sign in to an account.

        Args:
          response: https://www.w3.org/TR/webauthn-2/#authenticatorresponse

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/v1/auth/webauthn/assert",
            body=await async_maybe_transform(
                {
                    "id": id,
                    "raw_id": raw_id,
                    "response": response,
                    "type": type,
                    "authenticator_attachment": authenticator_attachment,
                    "client_extension_results": client_extension_results,
                },
                assert_create_params.AssertCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=AssertCreateResponse,
        )

    async def retrieve(
        self,
        account_handle: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> AssertRetrieveResponse:
        """
        Start the WebAuthn assertion for an existing account.

        Args:
          account_handle: The unique @ handle of an account.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_handle:
            raise ValueError(f"Expected a non-empty value for `account_handle` but received {account_handle!r}")
        return await self._get(
            f"/v1/auth/webauthn/assert/{account_handle}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=AssertRetrieveResponse,
        )


class AssertResourceWithRawResponse:
    def __init__(self, assert_: AssertResource) -> None:
        self._assert_ = assert_

        self.create = to_raw_response_wrapper(
            assert_.create,
        )
        self.retrieve = to_raw_response_wrapper(
            assert_.retrieve,
        )


class AsyncAssertResourceWithRawResponse:
    def __init__(self, assert_: AsyncAssertResource) -> None:
        self._assert_ = assert_

        self.create = async_to_raw_response_wrapper(
            assert_.create,
        )
        self.retrieve = async_to_raw_response_wrapper(
            assert_.retrieve,
        )


class AssertResourceWithStreamingResponse:
    def __init__(self, assert_: AssertResource) -> None:
        self._assert_ = assert_

        self.create = to_streamed_response_wrapper(
            assert_.create,
        )
        self.retrieve = to_streamed_response_wrapper(
            assert_.retrieve,
        )


class AsyncAssertResourceWithStreamingResponse:
    def __init__(self, assert_: AsyncAssertResource) -> None:
        self._assert_ = assert_

        self.create = async_to_streamed_response_wrapper(
            assert_.create,
        )
        self.retrieve = async_to_streamed_response_wrapper(
            assert_.retrieve,
        )
