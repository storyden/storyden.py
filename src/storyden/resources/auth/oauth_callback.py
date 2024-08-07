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
from ...types.auth import oauth_callback_create_params
from ..._base_client import make_request_options
from ...types.auth.oauth_callback_create_response import OAuthCallbackCreateResponse

__all__ = ["OAuthCallbackResource", "AsyncOAuthCallbackResource"]


class OAuthCallbackResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> OAuthCallbackResourceWithRawResponse:
        return OAuthCallbackResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> OAuthCallbackResourceWithStreamingResponse:
        return OAuthCallbackResourceWithStreamingResponse(self)

    def create(
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
    ) -> OAuthCallbackCreateResponse:
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
                oauth_callback_create_params.OAuthCallbackCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=OAuthCallbackCreateResponse,
        )


class AsyncOAuthCallbackResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncOAuthCallbackResourceWithRawResponse:
        return AsyncOAuthCallbackResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncOAuthCallbackResourceWithStreamingResponse:
        return AsyncOAuthCallbackResourceWithStreamingResponse(self)

    async def create(
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
    ) -> OAuthCallbackCreateResponse:
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
                oauth_callback_create_params.OAuthCallbackCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=OAuthCallbackCreateResponse,
        )


class OAuthCallbackResourceWithRawResponse:
    def __init__(self, oauth_callback: OAuthCallbackResource) -> None:
        self._oauth_callback = oauth_callback

        self.create = to_raw_response_wrapper(
            oauth_callback.create,
        )


class AsyncOAuthCallbackResourceWithRawResponse:
    def __init__(self, oauth_callback: AsyncOAuthCallbackResource) -> None:
        self._oauth_callback = oauth_callback

        self.create = async_to_raw_response_wrapper(
            oauth_callback.create,
        )


class OAuthCallbackResourceWithStreamingResponse:
    def __init__(self, oauth_callback: OAuthCallbackResource) -> None:
        self._oauth_callback = oauth_callback

        self.create = to_streamed_response_wrapper(
            oauth_callback.create,
        )


class AsyncOAuthCallbackResourceWithStreamingResponse:
    def __init__(self, oauth_callback: AsyncOAuthCallbackResource) -> None:
        self._oauth_callback = oauth_callback

        self.create = async_to_streamed_response_wrapper(
            oauth_callback.create,
        )
