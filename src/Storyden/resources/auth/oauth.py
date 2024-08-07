# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import httpx

from ..._compat import cached_property

from ...types.auth.oauth_callback_response import OAuthCallbackResponse

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
from ...types.auth import oauth_callback_params

__all__ = ["OAuthResource", "AsyncOAuthResource"]


class OAuthResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> OAuthResourceWithRawResponse:
        return OAuthResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> OAuthResourceWithStreamingResponse:
        return OAuthResourceWithStreamingResponse(self)

    def callback(
        self,
        oauth_provider: str,
        *,
        code: str,
        state: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> OAuthCallbackResponse:
        """
        OAuth2 callback.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not oauth_provider:
            raise ValueError(f"Expected a non-empty value for `oauth_provider` but received {oauth_provider!r}")
        return self._post(
            f"/v1/auth/oauth/{oauth_provider}/callback",
            body=maybe_transform(
                {
                    "code": code,
                    "state": state,
                },
                oauth_callback_params.OAuthCallbackParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=OAuthCallbackResponse,
        )


class AsyncOAuthResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncOAuthResourceWithRawResponse:
        return AsyncOAuthResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncOAuthResourceWithStreamingResponse:
        return AsyncOAuthResourceWithStreamingResponse(self)

    async def callback(
        self,
        oauth_provider: str,
        *,
        code: str,
        state: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> OAuthCallbackResponse:
        """
        OAuth2 callback.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not oauth_provider:
            raise ValueError(f"Expected a non-empty value for `oauth_provider` but received {oauth_provider!r}")
        return await self._post(
            f"/v1/auth/oauth/{oauth_provider}/callback",
            body=await async_maybe_transform(
                {
                    "code": code,
                    "state": state,
                },
                oauth_callback_params.OAuthCallbackParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=OAuthCallbackResponse,
        )


class OAuthResourceWithRawResponse:
    def __init__(self, oauth: OAuthResource) -> None:
        self._oauth = oauth

        self.callback = to_raw_response_wrapper(
            oauth.callback,
        )


class AsyncOAuthResourceWithRawResponse:
    def __init__(self, oauth: AsyncOAuthResource) -> None:
        self._oauth = oauth

        self.callback = async_to_raw_response_wrapper(
            oauth.callback,
        )


class OAuthResourceWithStreamingResponse:
    def __init__(self, oauth: OAuthResource) -> None:
        self._oauth = oauth

        self.callback = to_streamed_response_wrapper(
            oauth.callback,
        )


class AsyncOAuthResourceWithStreamingResponse:
    def __init__(self, oauth: AsyncOAuthResource) -> None:
        self._oauth = oauth

        self.callback = async_to_streamed_response_wrapper(
            oauth.callback,
        )
