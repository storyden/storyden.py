# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import httpx

from ..types import link_list_params, link_create_params
from .._types import NOT_GIVEN, Body, Query, Headers, NotGiven
from .._utils import (
    maybe_transform,
    async_maybe_transform,
)
from .._compat import cached_property
from .._resource import SyncAPIResource, AsyncAPIResource
from .._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from .._base_client import make_request_options
from ..types.link_list_response import LinkListResponse
from ..types.link_create_response import LinkCreateResponse
from ..types.link_retrieve_response import LinkRetrieveResponse

__all__ = ["LinksResource", "AsyncLinksResource"]


class LinksResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> LinksResourceWithRawResponse:
        return LinksResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> LinksResourceWithStreamingResponse:
        return LinksResourceWithStreamingResponse(self)

    def create(
        self,
        *,
        url: str,
        description: str | NotGiven = NOT_GIVEN,
        title: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> LinkCreateResponse:
        """Add a link to the community bookmarks.

        This will also scrape the content at the
        site the link points to, if possible. If the submitted link is an invalid link
        for whatever reason (invalid URL structure or page is dead) then the API will
        fail. The metadata for the link is indexed on success.

        If the submitted link already exists it will be an idempotent operation, unless
        the body contains additional metadata. In these cases, the link's metadata will
        be updated with the new metadata and the URL is unchanged.

        When a link is submitted, it is first "cleaned" to remove any fragments.

        Args:
          url: A web address

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/v1/links",
            body=maybe_transform(
                {
                    "url": url,
                    "description": description,
                    "title": title,
                },
                link_create_params.LinkCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=LinkCreateResponse,
        )

    def retrieve(
        self,
        link_slug: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> LinkRetrieveResponse:
        """Get the details for a specific link.

        Such as where it's been posted, which
        resources it's linked to and how many times it's been opened.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not link_slug:
            raise ValueError(f"Expected a non-empty value for `link_slug` but received {link_slug!r}")
        return self._get(
            f"/v1/links/{link_slug}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=LinkRetrieveResponse,
        )

    def list(
        self,
        *,
        page: str | NotGiven = NOT_GIVEN,
        q: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> LinkListResponse:
        """
        List all links using the filtering options.

        Args:
          page: Pagination query parameters.

          q: Search query string.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get(
            "/v1/links",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "page": page,
                        "q": q,
                    },
                    link_list_params.LinkListParams,
                ),
            ),
            cast_to=LinkListResponse,
        )


class AsyncLinksResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncLinksResourceWithRawResponse:
        return AsyncLinksResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncLinksResourceWithStreamingResponse:
        return AsyncLinksResourceWithStreamingResponse(self)

    async def create(
        self,
        *,
        url: str,
        description: str | NotGiven = NOT_GIVEN,
        title: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> LinkCreateResponse:
        """Add a link to the community bookmarks.

        This will also scrape the content at the
        site the link points to, if possible. If the submitted link is an invalid link
        for whatever reason (invalid URL structure or page is dead) then the API will
        fail. The metadata for the link is indexed on success.

        If the submitted link already exists it will be an idempotent operation, unless
        the body contains additional metadata. In these cases, the link's metadata will
        be updated with the new metadata and the URL is unchanged.

        When a link is submitted, it is first "cleaned" to remove any fragments.

        Args:
          url: A web address

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/v1/links",
            body=await async_maybe_transform(
                {
                    "url": url,
                    "description": description,
                    "title": title,
                },
                link_create_params.LinkCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=LinkCreateResponse,
        )

    async def retrieve(
        self,
        link_slug: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> LinkRetrieveResponse:
        """Get the details for a specific link.

        Such as where it's been posted, which
        resources it's linked to and how many times it's been opened.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not link_slug:
            raise ValueError(f"Expected a non-empty value for `link_slug` but received {link_slug!r}")
        return await self._get(
            f"/v1/links/{link_slug}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=LinkRetrieveResponse,
        )

    async def list(
        self,
        *,
        page: str | NotGiven = NOT_GIVEN,
        q: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> LinkListResponse:
        """
        List all links using the filtering options.

        Args:
          page: Pagination query parameters.

          q: Search query string.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._get(
            "/v1/links",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {
                        "page": page,
                        "q": q,
                    },
                    link_list_params.LinkListParams,
                ),
            ),
            cast_to=LinkListResponse,
        )


class LinksResourceWithRawResponse:
    def __init__(self, links: LinksResource) -> None:
        self._links = links

        self.create = to_raw_response_wrapper(
            links.create,
        )
        self.retrieve = to_raw_response_wrapper(
            links.retrieve,
        )
        self.list = to_raw_response_wrapper(
            links.list,
        )


class AsyncLinksResourceWithRawResponse:
    def __init__(self, links: AsyncLinksResource) -> None:
        self._links = links

        self.create = async_to_raw_response_wrapper(
            links.create,
        )
        self.retrieve = async_to_raw_response_wrapper(
            links.retrieve,
        )
        self.list = async_to_raw_response_wrapper(
            links.list,
        )


class LinksResourceWithStreamingResponse:
    def __init__(self, links: LinksResource) -> None:
        self._links = links

        self.create = to_streamed_response_wrapper(
            links.create,
        )
        self.retrieve = to_streamed_response_wrapper(
            links.retrieve,
        )
        self.list = to_streamed_response_wrapper(
            links.list,
        )


class AsyncLinksResourceWithStreamingResponse:
    def __init__(self, links: AsyncLinksResource) -> None:
        self._links = links

        self.create = async_to_streamed_response_wrapper(
            links.create,
        )
        self.retrieve = async_to_streamed_response_wrapper(
            links.retrieve,
        )
        self.list = async_to_streamed_response_wrapper(
            links.list,
        )
