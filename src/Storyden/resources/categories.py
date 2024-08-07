# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import httpx

from .._compat import cached_property

from ..types.category_create_response import CategoryCreateResponse

from .._utils import maybe_transform, async_maybe_transform

from .._base_client import make_request_options

from typing import Dict

from ..types.category_update_response import CategoryUpdateResponse

from ..types.category_list_response import CategoryListResponse

from .._response import (
    to_raw_response_wrapper,
    async_to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_streamed_response_wrapper,
)

import warnings
from typing import TYPE_CHECKING, Optional, Union, List, Dict, Any, Mapping, cast, overload
from typing_extensions import Literal
from .._utils import extract_files, maybe_transform, required_args, deepcopy_minimal, strip_not_given
from .._types import NotGiven, Timeout, Headers, NoneType, Query, Body, NOT_GIVEN, FileTypes, BinaryResponseContent
from .._resource import SyncAPIResource, AsyncAPIResource
from ..types import shared_params
from ..types import category_create_params
from ..types import category_update_params

__all__ = ["CategoriesResource", "AsyncCategoriesResource"]


class CategoriesResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> CategoriesResourceWithRawResponse:
        return CategoriesResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> CategoriesResourceWithStreamingResponse:
        return CategoriesResourceWithStreamingResponse(self)

    def create(
        self,
        *,
        admin: bool,
        colour: str,
        description: str,
        name: str,
        meta: Dict[str, object] | NotGiven = NOT_GIVEN,
        slug: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> CategoryCreateResponse:
        """
        Create a category for organising posts.

        Args:
          name: A category's user-facing name.

          meta: Arbitrary metadata for the resource.

          slug: A category's URL-safe slug.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/v1/categories",
            body=maybe_transform(
                {
                    "admin": admin,
                    "colour": colour,
                    "description": description,
                    "name": name,
                    "meta": meta,
                    "slug": slug,
                },
                category_create_params.CategoryCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=CategoryCreateResponse,
        )

    def update(
        self,
        category_id: str,
        *,
        admin: bool | NotGiven = NOT_GIVEN,
        colour: str | NotGiven = NOT_GIVEN,
        description: str | NotGiven = NOT_GIVEN,
        meta: Dict[str, object] | NotGiven = NOT_GIVEN,
        name: str | NotGiven = NOT_GIVEN,
        slug: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> CategoryUpdateResponse:
        """
        Create a category for organising posts.

        Args:
          category_id: A unique identifier for this resource.

          meta: Arbitrary metadata for the resource.

          name: A category's user-facing name.

          slug: A category's URL-safe slug.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not category_id:
            raise ValueError(f"Expected a non-empty value for `category_id` but received {category_id!r}")
        return self._patch(
            f"/v1/categories/{category_id}",
            body=maybe_transform(
                {
                    "admin": admin,
                    "colour": colour,
                    "description": description,
                    "meta": meta,
                    "name": name,
                    "slug": slug,
                },
                category_update_params.CategoryUpdateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=CategoryUpdateResponse,
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
    ) -> CategoryListResponse:
        """Get a list of all categories on the site."""
        return self._get(
            "/v1/categories",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=CategoryListResponse,
        )


class AsyncCategoriesResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncCategoriesResourceWithRawResponse:
        return AsyncCategoriesResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncCategoriesResourceWithStreamingResponse:
        return AsyncCategoriesResourceWithStreamingResponse(self)

    async def create(
        self,
        *,
        admin: bool,
        colour: str,
        description: str,
        name: str,
        meta: Dict[str, object] | NotGiven = NOT_GIVEN,
        slug: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> CategoryCreateResponse:
        """
        Create a category for organising posts.

        Args:
          name: A category's user-facing name.

          meta: Arbitrary metadata for the resource.

          slug: A category's URL-safe slug.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/v1/categories",
            body=await async_maybe_transform(
                {
                    "admin": admin,
                    "colour": colour,
                    "description": description,
                    "name": name,
                    "meta": meta,
                    "slug": slug,
                },
                category_create_params.CategoryCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=CategoryCreateResponse,
        )

    async def update(
        self,
        category_id: str,
        *,
        admin: bool | NotGiven = NOT_GIVEN,
        colour: str | NotGiven = NOT_GIVEN,
        description: str | NotGiven = NOT_GIVEN,
        meta: Dict[str, object] | NotGiven = NOT_GIVEN,
        name: str | NotGiven = NOT_GIVEN,
        slug: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> CategoryUpdateResponse:
        """
        Create a category for organising posts.

        Args:
          category_id: A unique identifier for this resource.

          meta: Arbitrary metadata for the resource.

          name: A category's user-facing name.

          slug: A category's URL-safe slug.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not category_id:
            raise ValueError(f"Expected a non-empty value for `category_id` but received {category_id!r}")
        return await self._patch(
            f"/v1/categories/{category_id}",
            body=await async_maybe_transform(
                {
                    "admin": admin,
                    "colour": colour,
                    "description": description,
                    "meta": meta,
                    "name": name,
                    "slug": slug,
                },
                category_update_params.CategoryUpdateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=CategoryUpdateResponse,
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
    ) -> CategoryListResponse:
        """Get a list of all categories on the site."""
        return await self._get(
            "/v1/categories",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=CategoryListResponse,
        )


class CategoriesResourceWithRawResponse:
    def __init__(self, categories: CategoriesResource) -> None:
        self._categories = categories

        self.create = to_raw_response_wrapper(
            categories.create,
        )
        self.update = to_raw_response_wrapper(
            categories.update,
        )
        self.list = to_raw_response_wrapper(
            categories.list,
        )


class AsyncCategoriesResourceWithRawResponse:
    def __init__(self, categories: AsyncCategoriesResource) -> None:
        self._categories = categories

        self.create = async_to_raw_response_wrapper(
            categories.create,
        )
        self.update = async_to_raw_response_wrapper(
            categories.update,
        )
        self.list = async_to_raw_response_wrapper(
            categories.list,
        )


class CategoriesResourceWithStreamingResponse:
    def __init__(self, categories: CategoriesResource) -> None:
        self._categories = categories

        self.create = to_streamed_response_wrapper(
            categories.create,
        )
        self.update = to_streamed_response_wrapper(
            categories.update,
        )
        self.list = to_streamed_response_wrapper(
            categories.list,
        )


class AsyncCategoriesResourceWithStreamingResponse:
    def __init__(self, categories: AsyncCategoriesResource) -> None:
        self._categories = categories

        self.create = async_to_streamed_response_wrapper(
            categories.create,
        )
        self.update = async_to_streamed_response_wrapper(
            categories.update,
        )
        self.list = async_to_streamed_response_wrapper(
            categories.list,
        )
