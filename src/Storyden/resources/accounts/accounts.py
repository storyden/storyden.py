# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import httpx

from .self.self import SelfResource, AsyncSelfResource

from ..._compat import cached_property

from .avatar import AvatarResource, AsyncAvatarResource

from ...types.account_update_response import AccountUpdateResponse

from ..._utils import maybe_transform, async_maybe_transform

from ..._base_client import make_request_options

from typing import List, Iterable, Dict

from ...types.account_list_response import AccountListResponse

from ..._response import (
    to_raw_response_wrapper,
    async_to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_streamed_response_wrapper,
)

from ...types import account_update_params

import warnings
from typing import TYPE_CHECKING, Optional, Union, List, Dict, Any, Mapping, cast, overload
from typing_extensions import Literal
from ..._utils import extract_files, maybe_transform, required_args, deepcopy_minimal, strip_not_given
from ..._types import NotGiven, Timeout, Headers, NoneType, Query, Body, NOT_GIVEN, FileTypes, BinaryResponseContent
from ..._resource import SyncAPIResource, AsyncAPIResource
from ...types import shared_params
from ...types import account_update_params
from .self import (
    SelfResource,
    AsyncSelfResource,
    SelfResourceWithRawResponse,
    AsyncSelfResourceWithRawResponse,
    SelfResourceWithStreamingResponse,
    AsyncSelfResourceWithStreamingResponse,
)
from .avatar import (
    AvatarResource,
    AsyncAvatarResource,
    AvatarResourceWithRawResponse,
    AsyncAvatarResourceWithRawResponse,
    AvatarResourceWithStreamingResponse,
    AsyncAvatarResourceWithStreamingResponse,
)

__all__ = ["AccountsResource", "AsyncAccountsResource"]


class AccountsResource(SyncAPIResource):
    @cached_property
    def self(self) -> SelfResource:
        return SelfResource(self._client)

    @cached_property
    def avatar(self) -> AvatarResource:
        return AvatarResource(self._client)

    @cached_property
    def with_raw_response(self) -> AccountsResourceWithRawResponse:
        return AccountsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AccountsResourceWithStreamingResponse:
        return AccountsResourceWithStreamingResponse(self)

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

    def list(
        self,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> AccountListResponse:
        """Get the information for the currently authenticated account."""
        return self._get(
            "/v1/accounts",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=AccountListResponse,
        )


class AsyncAccountsResource(AsyncAPIResource):
    @cached_property
    def self(self) -> AsyncSelfResource:
        return AsyncSelfResource(self._client)

    @cached_property
    def avatar(self) -> AsyncAvatarResource:
        return AsyncAvatarResource(self._client)

    @cached_property
    def with_raw_response(self) -> AsyncAccountsResourceWithRawResponse:
        return AsyncAccountsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncAccountsResourceWithStreamingResponse:
        return AsyncAccountsResourceWithStreamingResponse(self)

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

    async def list(
        self,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> AccountListResponse:
        """Get the information for the currently authenticated account."""
        return await self._get(
            "/v1/accounts",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=AccountListResponse,
        )


class AccountsResourceWithRawResponse:
    def __init__(self, accounts: AccountsResource) -> None:
        self._accounts = accounts

        self.update = to_raw_response_wrapper(
            accounts.update,
        )
        self.list = to_raw_response_wrapper(
            accounts.list,
        )

    @cached_property
    def self(self) -> SelfResourceWithRawResponse:
        return SelfResourceWithRawResponse(self._accounts.self)

    @cached_property
    def avatar(self) -> AvatarResourceWithRawResponse:
        return AvatarResourceWithRawResponse(self._accounts.avatar)


class AsyncAccountsResourceWithRawResponse:
    def __init__(self, accounts: AsyncAccountsResource) -> None:
        self._accounts = accounts

        self.update = async_to_raw_response_wrapper(
            accounts.update,
        )
        self.list = async_to_raw_response_wrapper(
            accounts.list,
        )

    @cached_property
    def self(self) -> AsyncSelfResourceWithRawResponse:
        return AsyncSelfResourceWithRawResponse(self._accounts.self)

    @cached_property
    def avatar(self) -> AsyncAvatarResourceWithRawResponse:
        return AsyncAvatarResourceWithRawResponse(self._accounts.avatar)


class AccountsResourceWithStreamingResponse:
    def __init__(self, accounts: AccountsResource) -> None:
        self._accounts = accounts

        self.update = to_streamed_response_wrapper(
            accounts.update,
        )
        self.list = to_streamed_response_wrapper(
            accounts.list,
        )

    @cached_property
    def self(self) -> SelfResourceWithStreamingResponse:
        return SelfResourceWithStreamingResponse(self._accounts.self)

    @cached_property
    def avatar(self) -> AvatarResourceWithStreamingResponse:
        return AvatarResourceWithStreamingResponse(self._accounts.avatar)


class AsyncAccountsResourceWithStreamingResponse:
    def __init__(self, accounts: AsyncAccountsResource) -> None:
        self._accounts = accounts

        self.update = async_to_streamed_response_wrapper(
            accounts.update,
        )
        self.list = async_to_streamed_response_wrapper(
            accounts.list,
        )

    @cached_property
    def self(self) -> AsyncSelfResourceWithStreamingResponse:
        return AsyncSelfResourceWithStreamingResponse(self._accounts.self)

    @cached_property
    def avatar(self) -> AsyncAvatarResourceWithStreamingResponse:
        return AsyncAvatarResourceWithStreamingResponse(self._accounts.avatar)
