# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import httpx

from ...._compat import cached_property

from ....types.auth.webauthn.assert_start_response import AssertStartResponse

from ...._base_client import make_request_options

from ...._response import (
    to_raw_response_wrapper,
    async_to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_streamed_response_wrapper,
)

import warnings
from typing import TYPE_CHECKING, Optional, Union, List, Dict, Any, Mapping, cast, overload
from typing_extensions import Literal
from ...._utils import extract_files, maybe_transform, required_args, deepcopy_minimal, strip_not_given
from ...._types import NotGiven, Timeout, Headers, NoneType, Query, Body, NOT_GIVEN, FileTypes, BinaryResponseContent
from ...._resource import SyncAPIResource, AsyncAPIResource
from ....types import shared_params

__all__ = ["AssertResource", "AsyncAssertResource"]


class AssertResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AssertResourceWithRawResponse:
        return AssertResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AssertResourceWithStreamingResponse:
        return AssertResourceWithStreamingResponse(self)

    def start(
        self,
        account_handle: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> AssertStartResponse:
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
            cast_to=AssertStartResponse,
        )


class AsyncAssertResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncAssertResourceWithRawResponse:
        return AsyncAssertResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncAssertResourceWithStreamingResponse:
        return AsyncAssertResourceWithStreamingResponse(self)

    async def start(
        self,
        account_handle: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> AssertStartResponse:
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
            cast_to=AssertStartResponse,
        )


class AssertResourceWithRawResponse:
    def __init__(self, assert_: AssertResource) -> None:
        self._assert_ = assert_

        self.start = to_raw_response_wrapper(
            assert_.start,
        )


class AsyncAssertResourceWithRawResponse:
    def __init__(self, assert_: AsyncAssertResource) -> None:
        self._assert_ = assert_

        self.start = async_to_raw_response_wrapper(
            assert_.start,
        )


class AssertResourceWithStreamingResponse:
    def __init__(self, assert_: AssertResource) -> None:
        self._assert_ = assert_

        self.start = to_streamed_response_wrapper(
            assert_.start,
        )


class AsyncAssertResourceWithStreamingResponse:
    def __init__(self, assert_: AsyncAssertResource) -> None:
        self._assert_ = assert_

        self.start = async_to_streamed_response_wrapper(
            assert_.start,
        )
