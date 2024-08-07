# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import httpx

from .assert_ import AssertResource, AsyncAssertResource

from ...._compat import cached_property

from ....types.auth.webauthn_make_response import WebauthnMakeResponse

from ...._utils import maybe_transform, async_maybe_transform

from ...._base_client import make_request_options

from ...._response import (
    to_raw_response_wrapper,
    async_to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_streamed_response_wrapper,
)

from ....types.auth import webauthn_make_params

import warnings
from typing import TYPE_CHECKING, Optional, Union, List, Dict, Any, Mapping, cast, overload
from typing_extensions import Literal
from ...._utils import extract_files, maybe_transform, required_args, deepcopy_minimal, strip_not_given
from ...._types import NotGiven, Timeout, Headers, NoneType, Query, Body, NOT_GIVEN, FileTypes, BinaryResponseContent
from ...._resource import SyncAPIResource, AsyncAPIResource
from ....types import shared_params
from ....types.auth import webauthn_make_params
from .assert_ import (
    AssertResource,
    AsyncAssertResource,
    AssertResourceWithRawResponse,
    AsyncAssertResourceWithRawResponse,
    AssertResourceWithStreamingResponse,
    AsyncAssertResourceWithStreamingResponse,
)

__all__ = ["WebauthnResource", "AsyncWebauthnResource"]


class WebauthnResource(SyncAPIResource):
    @cached_property
    def assert_(self) -> AssertResource:
        return AssertResource(self._client)

    @cached_property
    def with_raw_response(self) -> WebauthnResourceWithRawResponse:
        return WebauthnResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> WebauthnResourceWithStreamingResponse:
        return WebauthnResourceWithStreamingResponse(self)

    def make(
        self,
        *,
        id: str,
        raw_id: str,
        response: webauthn_make_params.Response,
        type: str,
        authenticator_attachment: str | NotGiven = NOT_GIVEN,
        client_extension_results: object | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> WebauthnMakeResponse:
        """
        Complete WebAuthn registration by creating a new credential.

        Args:
          response: https://www.w3.org/TR/webauthn-2/#authenticatorresponse

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/v1/auth/webauthn/make",
            body=maybe_transform(
                {
                    "id": id,
                    "raw_id": raw_id,
                    "response": response,
                    "type": type,
                    "authenticator_attachment": authenticator_attachment,
                    "client_extension_results": client_extension_results,
                },
                webauthn_make_params.WebauthnMakeParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=WebauthnMakeResponse,
        )


class AsyncWebauthnResource(AsyncAPIResource):
    @cached_property
    def assert_(self) -> AsyncAssertResource:
        return AsyncAssertResource(self._client)

    @cached_property
    def with_raw_response(self) -> AsyncWebauthnResourceWithRawResponse:
        return AsyncWebauthnResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncWebauthnResourceWithStreamingResponse:
        return AsyncWebauthnResourceWithStreamingResponse(self)

    async def make(
        self,
        *,
        id: str,
        raw_id: str,
        response: webauthn_make_params.Response,
        type: str,
        authenticator_attachment: str | NotGiven = NOT_GIVEN,
        client_extension_results: object | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> WebauthnMakeResponse:
        """
        Complete WebAuthn registration by creating a new credential.

        Args:
          response: https://www.w3.org/TR/webauthn-2/#authenticatorresponse

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/v1/auth/webauthn/make",
            body=await async_maybe_transform(
                {
                    "id": id,
                    "raw_id": raw_id,
                    "response": response,
                    "type": type,
                    "authenticator_attachment": authenticator_attachment,
                    "client_extension_results": client_extension_results,
                },
                webauthn_make_params.WebauthnMakeParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=WebauthnMakeResponse,
        )


class WebauthnResourceWithRawResponse:
    def __init__(self, webauthn: WebauthnResource) -> None:
        self._webauthn = webauthn

        self.make = to_raw_response_wrapper(
            webauthn.make,
        )

    @cached_property
    def assert_(self) -> AssertResourceWithRawResponse:
        return AssertResourceWithRawResponse(self._webauthn.assert_)


class AsyncWebauthnResourceWithRawResponse:
    def __init__(self, webauthn: AsyncWebauthnResource) -> None:
        self._webauthn = webauthn

        self.make = async_to_raw_response_wrapper(
            webauthn.make,
        )

    @cached_property
    def assert_(self) -> AsyncAssertResourceWithRawResponse:
        return AsyncAssertResourceWithRawResponse(self._webauthn.assert_)


class WebauthnResourceWithStreamingResponse:
    def __init__(self, webauthn: WebauthnResource) -> None:
        self._webauthn = webauthn

        self.make = to_streamed_response_wrapper(
            webauthn.make,
        )

    @cached_property
    def assert_(self) -> AssertResourceWithStreamingResponse:
        return AssertResourceWithStreamingResponse(self._webauthn.assert_)


class AsyncWebauthnResourceWithStreamingResponse:
    def __init__(self, webauthn: AsyncWebauthnResource) -> None:
        self._webauthn = webauthn

        self.make = async_to_streamed_response_wrapper(
            webauthn.make,
        )

    @cached_property
    def assert_(self) -> AsyncAssertResourceWithStreamingResponse:
        return AsyncAssertResourceWithStreamingResponse(self._webauthn.assert_)
