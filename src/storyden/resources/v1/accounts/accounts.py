# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict, List, Iterable

import httpx

from .avatar import (
    AvatarResource,
    AsyncAvatarResource,
    AvatarResourceWithRawResponse,
    AsyncAvatarResourceWithRawResponse,
    AvatarResourceWithStreamingResponse,
    AsyncAvatarResourceWithStreamingResponse,
)
from ...._types import NOT_GIVEN, Body, Query, Headers, NotGiven
from ...._utils import (
    maybe_transform,
    async_maybe_transform,
)
from ...._compat import cached_property
from ....types.v1 import account_update_params
from ...._resource import SyncAPIResource, AsyncAPIResource
from ...._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from .auth_methods import (
    AuthMethodsResource,
    AsyncAuthMethodsResource,
    AuthMethodsResourceWithRawResponse,
    AsyncAuthMethodsResourceWithRawResponse,
    AuthMethodsResourceWithStreamingResponse,
    AsyncAuthMethodsResourceWithStreamingResponse,
)
from ...._base_client import make_request_options
from ....types.v1.account_update_response import AccountUpdateResponse
from ....types.v1.account_retrieve_response import AccountRetrieveResponse

__all__ = ["AccountsResource", "AsyncAccountsResource"]


class AccountsResource(SyncAPIResource):
    @cached_property
    def auth_methods(self) -> AuthMethodsResource:
        return AuthMethodsResource(self._client)

    @cached_property
    def avatar(self) -> AvatarResource:
        return AvatarResource(self._client)

    @cached_property
    def with_raw_response(self) -> AccountsResourceWithRawResponse:
        return AccountsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AccountsResourceWithStreamingResponse:
        return AccountsResourceWithStreamingResponse(self)

    def retrieve(
        self,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> AccountRetrieveResponse:
        """Get the information for the currently authenticated account."""
        return self._get(
            "/v1/accounts",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=AccountRetrieveResponse,
        )

    def update(
        self,
        *,
        bio: str | NotGiven = NOT_GIVEN,
        handle: str | NotGiven = NOT_GIVEN,
        interests: List[str] | NotGiven = NOT_GIVEN,
        links: Iterable[account_update_params.Link] | NotGiven = NOT_GIVEN,
        meta: Dict[str, object] | NotGiven = NOT_GIVEN,
        name: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> AccountUpdateResponse:
        """
        Update the information for the currently authenticated account.

        Args:
          bio: The rich-text bio for an account's public profile.

          handle: The unique @ handle of an account.

          interests: A list of tags IDs.

          meta: Arbitrary metadata for the resource.

          name: The account owners display name.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._patch(
            "/v1/accounts",
            body=maybe_transform(
                {
                    "bio": bio,
                    "handle": handle,
                    "interests": interests,
                    "links": links,
                    "meta": meta,
                    "name": name,
                },
                account_update_params.AccountUpdateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=AccountUpdateResponse,
        )


class AsyncAccountsResource(AsyncAPIResource):
    @cached_property
    def auth_methods(self) -> AsyncAuthMethodsResource:
        return AsyncAuthMethodsResource(self._client)

    @cached_property
    def avatar(self) -> AsyncAvatarResource:
        return AsyncAvatarResource(self._client)

    @cached_property
    def with_raw_response(self) -> AsyncAccountsResourceWithRawResponse:
        return AsyncAccountsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncAccountsResourceWithStreamingResponse:
        return AsyncAccountsResourceWithStreamingResponse(self)

    async def retrieve(
        self,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> AccountRetrieveResponse:
        """Get the information for the currently authenticated account."""
        return await self._get(
            "/v1/accounts",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=AccountRetrieveResponse,
        )

    async def update(
        self,
        *,
        bio: str | NotGiven = NOT_GIVEN,
        handle: str | NotGiven = NOT_GIVEN,
        interests: List[str] | NotGiven = NOT_GIVEN,
        links: Iterable[account_update_params.Link] | NotGiven = NOT_GIVEN,
        meta: Dict[str, object] | NotGiven = NOT_GIVEN,
        name: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> AccountUpdateResponse:
        """
        Update the information for the currently authenticated account.

        Args:
          bio: The rich-text bio for an account's public profile.

          handle: The unique @ handle of an account.

          interests: A list of tags IDs.

          meta: Arbitrary metadata for the resource.

          name: The account owners display name.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._patch(
            "/v1/accounts",
            body=await async_maybe_transform(
                {
                    "bio": bio,
                    "handle": handle,
                    "interests": interests,
                    "links": links,
                    "meta": meta,
                    "name": name,
                },
                account_update_params.AccountUpdateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=AccountUpdateResponse,
        )


class AccountsResourceWithRawResponse:
    def __init__(self, accounts: AccountsResource) -> None:
        self._accounts = accounts

        self.retrieve = to_raw_response_wrapper(
            accounts.retrieve,
        )
        self.update = to_raw_response_wrapper(
            accounts.update,
        )

    @cached_property
    def auth_methods(self) -> AuthMethodsResourceWithRawResponse:
        return AuthMethodsResourceWithRawResponse(self._accounts.auth_methods)

    @cached_property
    def avatar(self) -> AvatarResourceWithRawResponse:
        return AvatarResourceWithRawResponse(self._accounts.avatar)


class AsyncAccountsResourceWithRawResponse:
    def __init__(self, accounts: AsyncAccountsResource) -> None:
        self._accounts = accounts

        self.retrieve = async_to_raw_response_wrapper(
            accounts.retrieve,
        )
        self.update = async_to_raw_response_wrapper(
            accounts.update,
        )

    @cached_property
    def auth_methods(self) -> AsyncAuthMethodsResourceWithRawResponse:
        return AsyncAuthMethodsResourceWithRawResponse(self._accounts.auth_methods)

    @cached_property
    def avatar(self) -> AsyncAvatarResourceWithRawResponse:
        return AsyncAvatarResourceWithRawResponse(self._accounts.avatar)


class AccountsResourceWithStreamingResponse:
    def __init__(self, accounts: AccountsResource) -> None:
        self._accounts = accounts

        self.retrieve = to_streamed_response_wrapper(
            accounts.retrieve,
        )
        self.update = to_streamed_response_wrapper(
            accounts.update,
        )

    @cached_property
    def auth_methods(self) -> AuthMethodsResourceWithStreamingResponse:
        return AuthMethodsResourceWithStreamingResponse(self._accounts.auth_methods)

    @cached_property
    def avatar(self) -> AvatarResourceWithStreamingResponse:
        return AvatarResourceWithStreamingResponse(self._accounts.avatar)


class AsyncAccountsResourceWithStreamingResponse:
    def __init__(self, accounts: AsyncAccountsResource) -> None:
        self._accounts = accounts

        self.retrieve = async_to_streamed_response_wrapper(
            accounts.retrieve,
        )
        self.update = async_to_streamed_response_wrapper(
            accounts.update,
        )

    @cached_property
    def auth_methods(self) -> AsyncAuthMethodsResourceWithStreamingResponse:
        return AsyncAuthMethodsResourceWithStreamingResponse(self._accounts.auth_methods)

    @cached_property
    def avatar(self) -> AsyncAvatarResourceWithStreamingResponse:
        return AsyncAvatarResourceWithStreamingResponse(self._accounts.avatar)
