# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import httpx

from .visibility import VisibilityResource, AsyncVisibilityResource

from ..._compat import cached_property

from .assets import AssetsResource, AsyncAssetsResource

from .children import ChildrenResource, AsyncChildrenResource

from ...types.node_create_response import NodeCreateResponse

from ..._utils import maybe_transform, async_maybe_transform

from ..._base_client import make_request_options

from typing import List, Dict

from typing_extensions import Literal

from ...types.node_retrieve_response import NodeRetrieveResponse

from ...types.node_update_response import NodeUpdateResponse

from ...types.node_list_response import NodeListResponse

from ...types.node_delete_response import NodeDeleteResponse

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
from ...types import node_create_params
from ...types import node_update_params
from ...types import node_list_params
from ...types import node_delete_params
from .visibility import (
    VisibilityResource,
    AsyncVisibilityResource,
    VisibilityResourceWithRawResponse,
    AsyncVisibilityResourceWithRawResponse,
    VisibilityResourceWithStreamingResponse,
    AsyncVisibilityResourceWithStreamingResponse,
)
from .assets import (
    AssetsResource,
    AsyncAssetsResource,
    AssetsResourceWithRawResponse,
    AsyncAssetsResourceWithRawResponse,
    AssetsResourceWithStreamingResponse,
    AsyncAssetsResourceWithStreamingResponse,
)
from .children import (
    ChildrenResource,
    AsyncChildrenResource,
    ChildrenResourceWithRawResponse,
    AsyncChildrenResourceWithRawResponse,
    ChildrenResourceWithStreamingResponse,
    AsyncChildrenResourceWithStreamingResponse,
)

__all__ = ["NodesResource", "AsyncNodesResource"]


class NodesResource(SyncAPIResource):
    @cached_property
    def visibility(self) -> VisibilityResource:
        return VisibilityResource(self._client)

    @cached_property
    def assets(self) -> AssetsResource:
        return AssetsResource(self._client)

    @cached_property
    def children(self) -> ChildrenResource:
        return ChildrenResource(self._client)

    @cached_property
    def with_raw_response(self) -> NodesResourceWithRawResponse:
        return NodesResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> NodesResourceWithStreamingResponse:
        return NodesResourceWithStreamingResponse(self)

    def create(
        self,
        *,
        name: str,
        asset_ids: List[str] | NotGiven = NOT_GIVEN,
        asset_sources: List[str] | NotGiven = NOT_GIVEN,
        content: str | NotGiven = NOT_GIVEN,
        meta: Dict[str, object] | NotGiven = NOT_GIVEN,
        parent: str | NotGiven = NOT_GIVEN,
        slug: str | NotGiven = NOT_GIVEN,
        url: str | NotGiven = NOT_GIVEN,
        visibility: Literal["draft", "unlisted", "review", "published"] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> NodeCreateResponse:
        """
        Create a node for curating structured knowledge together.

        Args:
          content: The body text of a post within a thread. The type is either a string or an
              object, depending on what was used during creation. Strings can be used for
              basic plain text or markdown content and objects are used for more complex types
              such as Slate.js editor documents.

          meta: Arbitrary metadata for the resource.

          parent: A URL-safe slug for uniquely identifying resources.

          slug: A URL-safe slug for uniquely identifying resources.

          url: A web address

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/v1/nodes",
            body=maybe_transform(
                {
                    "name": name,
                    "asset_ids": asset_ids,
                    "asset_sources": asset_sources,
                    "content": content,
                    "meta": meta,
                    "parent": parent,
                    "slug": slug,
                    "url": url,
                    "visibility": visibility,
                },
                node_create_params.NodeCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NodeCreateResponse,
        )

    def retrieve(
        self,
        node_slug: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> NodeRetrieveResponse:
        """
        Get a node by its URL slug.

        Args:
          node_slug: A unique identifier for this resource.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not node_slug:
            raise ValueError(f"Expected a non-empty value for `node_slug` but received {node_slug!r}")
        return self._get(
            f"/v1/nodes/{node_slug}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NodeRetrieveResponse,
        )

    def update(
        self,
        node_slug: str,
        *,
        asset_ids: List[str] | NotGiven = NOT_GIVEN,
        asset_sources: List[str] | NotGiven = NOT_GIVEN,
        content: str | NotGiven = NOT_GIVEN,
        meta: Dict[str, object] | NotGiven = NOT_GIVEN,
        name: str | NotGiven = NOT_GIVEN,
        parent: str | NotGiven = NOT_GIVEN,
        slug: str | NotGiven = NOT_GIVEN,
        url: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> NodeUpdateResponse:
        """
        Update a node.

        Args:
          node_slug: A unique identifier for this resource.

          content: The body text of a post within a thread. The type is either a string or an
              object, depending on what was used during creation. Strings can be used for
              basic plain text or markdown content and objects are used for more complex types
              such as Slate.js editor documents.

          meta: Arbitrary metadata for the resource.

          parent: A URL-safe slug for uniquely identifying resources.

          slug: A URL-safe slug for uniquely identifying resources.

          url: A web address

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not node_slug:
            raise ValueError(f"Expected a non-empty value for `node_slug` but received {node_slug!r}")
        return self._patch(
            f"/v1/nodes/{node_slug}",
            body=maybe_transform(
                {
                    "asset_ids": asset_ids,
                    "asset_sources": asset_sources,
                    "content": content,
                    "meta": meta,
                    "name": name,
                    "parent": parent,
                    "slug": slug,
                    "url": url,
                },
                node_update_params.NodeUpdateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NodeUpdateResponse,
        )

    def list(
        self,
        *,
        author: str | NotGiven = NOT_GIVEN,
        depth: str | NotGiven = NOT_GIVEN,
        node_id: str | NotGiven = NOT_GIVEN,
        page: str | NotGiven = NOT_GIVEN,
        q: str | NotGiven = NOT_GIVEN,
        visibility: List[Literal["draft", "unlisted", "review", "published"]] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> NodeListResponse:
        """List nodes using the given filters.

        Can be used to get a full tree.

        Args:
          author: Show only results owned by this account.

          depth: When set to a positive value, the nodes in the response will include all child
              nodes up to the specified depth. When set to zero, then if the request includes
              a node ID only that node will be returned, otherwise only top-level (root) nodes
              will be returned.

          node_id: List this node and all child nodes.

          page: Pagination query parameters.

          q: Search query string.

          visibility: Filter nodes with specific visibility values. Note that by default, only
              published nodes are returned. When 'draft' is specified, only drafts owned by
              the requesting account are included. When 'review' is specified, the request
              will fail if the requesting account is not an administrator.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get(
            "/v1/nodes",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "author": author,
                        "depth": depth,
                        "node_id": node_id,
                        "page": page,
                        "q": q,
                        "visibility": visibility,
                    },
                    node_list_params.NodeListParams,
                ),
            ),
            cast_to=NodeListResponse,
        )

    def delete(
        self,
        node_slug: str,
        *,
        target_node: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> NodeDeleteResponse:
        """
        Delete a node and move all children to its parent or root.

        Args:
          node_slug: A unique identifier for this resource.

          target_node: If set, child nodes will be moved to the target node. If not set, child nodes
              will be moved to the root.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not node_slug:
            raise ValueError(f"Expected a non-empty value for `node_slug` but received {node_slug!r}")
        return self._delete(
            f"/v1/nodes/{node_slug}",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform({"target_node": target_node}, node_delete_params.NodeDeleteParams),
            ),
            cast_to=NodeDeleteResponse,
        )


class AsyncNodesResource(AsyncAPIResource):
    @cached_property
    def visibility(self) -> AsyncVisibilityResource:
        return AsyncVisibilityResource(self._client)

    @cached_property
    def assets(self) -> AsyncAssetsResource:
        return AsyncAssetsResource(self._client)

    @cached_property
    def children(self) -> AsyncChildrenResource:
        return AsyncChildrenResource(self._client)

    @cached_property
    def with_raw_response(self) -> AsyncNodesResourceWithRawResponse:
        return AsyncNodesResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncNodesResourceWithStreamingResponse:
        return AsyncNodesResourceWithStreamingResponse(self)

    async def create(
        self,
        *,
        name: str,
        asset_ids: List[str] | NotGiven = NOT_GIVEN,
        asset_sources: List[str] | NotGiven = NOT_GIVEN,
        content: str | NotGiven = NOT_GIVEN,
        meta: Dict[str, object] | NotGiven = NOT_GIVEN,
        parent: str | NotGiven = NOT_GIVEN,
        slug: str | NotGiven = NOT_GIVEN,
        url: str | NotGiven = NOT_GIVEN,
        visibility: Literal["draft", "unlisted", "review", "published"] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> NodeCreateResponse:
        """
        Create a node for curating structured knowledge together.

        Args:
          content: The body text of a post within a thread. The type is either a string or an
              object, depending on what was used during creation. Strings can be used for
              basic plain text or markdown content and objects are used for more complex types
              such as Slate.js editor documents.

          meta: Arbitrary metadata for the resource.

          parent: A URL-safe slug for uniquely identifying resources.

          slug: A URL-safe slug for uniquely identifying resources.

          url: A web address

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/v1/nodes",
            body=await async_maybe_transform(
                {
                    "name": name,
                    "asset_ids": asset_ids,
                    "asset_sources": asset_sources,
                    "content": content,
                    "meta": meta,
                    "parent": parent,
                    "slug": slug,
                    "url": url,
                    "visibility": visibility,
                },
                node_create_params.NodeCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NodeCreateResponse,
        )

    async def retrieve(
        self,
        node_slug: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> NodeRetrieveResponse:
        """
        Get a node by its URL slug.

        Args:
          node_slug: A unique identifier for this resource.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not node_slug:
            raise ValueError(f"Expected a non-empty value for `node_slug` but received {node_slug!r}")
        return await self._get(
            f"/v1/nodes/{node_slug}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NodeRetrieveResponse,
        )

    async def update(
        self,
        node_slug: str,
        *,
        asset_ids: List[str] | NotGiven = NOT_GIVEN,
        asset_sources: List[str] | NotGiven = NOT_GIVEN,
        content: str | NotGiven = NOT_GIVEN,
        meta: Dict[str, object] | NotGiven = NOT_GIVEN,
        name: str | NotGiven = NOT_GIVEN,
        parent: str | NotGiven = NOT_GIVEN,
        slug: str | NotGiven = NOT_GIVEN,
        url: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> NodeUpdateResponse:
        """
        Update a node.

        Args:
          node_slug: A unique identifier for this resource.

          content: The body text of a post within a thread. The type is either a string or an
              object, depending on what was used during creation. Strings can be used for
              basic plain text or markdown content and objects are used for more complex types
              such as Slate.js editor documents.

          meta: Arbitrary metadata for the resource.

          parent: A URL-safe slug for uniquely identifying resources.

          slug: A URL-safe slug for uniquely identifying resources.

          url: A web address

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not node_slug:
            raise ValueError(f"Expected a non-empty value for `node_slug` but received {node_slug!r}")
        return await self._patch(
            f"/v1/nodes/{node_slug}",
            body=await async_maybe_transform(
                {
                    "asset_ids": asset_ids,
                    "asset_sources": asset_sources,
                    "content": content,
                    "meta": meta,
                    "name": name,
                    "parent": parent,
                    "slug": slug,
                    "url": url,
                },
                node_update_params.NodeUpdateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NodeUpdateResponse,
        )

    async def list(
        self,
        *,
        author: str | NotGiven = NOT_GIVEN,
        depth: str | NotGiven = NOT_GIVEN,
        node_id: str | NotGiven = NOT_GIVEN,
        page: str | NotGiven = NOT_GIVEN,
        q: str | NotGiven = NOT_GIVEN,
        visibility: List[Literal["draft", "unlisted", "review", "published"]] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> NodeListResponse:
        """List nodes using the given filters.

        Can be used to get a full tree.

        Args:
          author: Show only results owned by this account.

          depth: When set to a positive value, the nodes in the response will include all child
              nodes up to the specified depth. When set to zero, then if the request includes
              a node ID only that node will be returned, otherwise only top-level (root) nodes
              will be returned.

          node_id: List this node and all child nodes.

          page: Pagination query parameters.

          q: Search query string.

          visibility: Filter nodes with specific visibility values. Note that by default, only
              published nodes are returned. When 'draft' is specified, only drafts owned by
              the requesting account are included. When 'review' is specified, the request
              will fail if the requesting account is not an administrator.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._get(
            "/v1/nodes",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {
                        "author": author,
                        "depth": depth,
                        "node_id": node_id,
                        "page": page,
                        "q": q,
                        "visibility": visibility,
                    },
                    node_list_params.NodeListParams,
                ),
            ),
            cast_to=NodeListResponse,
        )

    async def delete(
        self,
        node_slug: str,
        *,
        target_node: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> NodeDeleteResponse:
        """
        Delete a node and move all children to its parent or root.

        Args:
          node_slug: A unique identifier for this resource.

          target_node: If set, child nodes will be moved to the target node. If not set, child nodes
              will be moved to the root.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not node_slug:
            raise ValueError(f"Expected a non-empty value for `node_slug` but received {node_slug!r}")
        return await self._delete(
            f"/v1/nodes/{node_slug}",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform({"target_node": target_node}, node_delete_params.NodeDeleteParams),
            ),
            cast_to=NodeDeleteResponse,
        )


class NodesResourceWithRawResponse:
    def __init__(self, nodes: NodesResource) -> None:
        self._nodes = nodes

        self.create = to_raw_response_wrapper(
            nodes.create,
        )
        self.retrieve = to_raw_response_wrapper(
            nodes.retrieve,
        )
        self.update = to_raw_response_wrapper(
            nodes.update,
        )
        self.list = to_raw_response_wrapper(
            nodes.list,
        )
        self.delete = to_raw_response_wrapper(
            nodes.delete,
        )

    @cached_property
    def visibility(self) -> VisibilityResourceWithRawResponse:
        return VisibilityResourceWithRawResponse(self._nodes.visibility)

    @cached_property
    def assets(self) -> AssetsResourceWithRawResponse:
        return AssetsResourceWithRawResponse(self._nodes.assets)

    @cached_property
    def children(self) -> ChildrenResourceWithRawResponse:
        return ChildrenResourceWithRawResponse(self._nodes.children)


class AsyncNodesResourceWithRawResponse:
    def __init__(self, nodes: AsyncNodesResource) -> None:
        self._nodes = nodes

        self.create = async_to_raw_response_wrapper(
            nodes.create,
        )
        self.retrieve = async_to_raw_response_wrapper(
            nodes.retrieve,
        )
        self.update = async_to_raw_response_wrapper(
            nodes.update,
        )
        self.list = async_to_raw_response_wrapper(
            nodes.list,
        )
        self.delete = async_to_raw_response_wrapper(
            nodes.delete,
        )

    @cached_property
    def visibility(self) -> AsyncVisibilityResourceWithRawResponse:
        return AsyncVisibilityResourceWithRawResponse(self._nodes.visibility)

    @cached_property
    def assets(self) -> AsyncAssetsResourceWithRawResponse:
        return AsyncAssetsResourceWithRawResponse(self._nodes.assets)

    @cached_property
    def children(self) -> AsyncChildrenResourceWithRawResponse:
        return AsyncChildrenResourceWithRawResponse(self._nodes.children)


class NodesResourceWithStreamingResponse:
    def __init__(self, nodes: NodesResource) -> None:
        self._nodes = nodes

        self.create = to_streamed_response_wrapper(
            nodes.create,
        )
        self.retrieve = to_streamed_response_wrapper(
            nodes.retrieve,
        )
        self.update = to_streamed_response_wrapper(
            nodes.update,
        )
        self.list = to_streamed_response_wrapper(
            nodes.list,
        )
        self.delete = to_streamed_response_wrapper(
            nodes.delete,
        )

    @cached_property
    def visibility(self) -> VisibilityResourceWithStreamingResponse:
        return VisibilityResourceWithStreamingResponse(self._nodes.visibility)

    @cached_property
    def assets(self) -> AssetsResourceWithStreamingResponse:
        return AssetsResourceWithStreamingResponse(self._nodes.assets)

    @cached_property
    def children(self) -> ChildrenResourceWithStreamingResponse:
        return ChildrenResourceWithStreamingResponse(self._nodes.children)


class AsyncNodesResourceWithStreamingResponse:
    def __init__(self, nodes: AsyncNodesResource) -> None:
        self._nodes = nodes

        self.create = async_to_streamed_response_wrapper(
            nodes.create,
        )
        self.retrieve = async_to_streamed_response_wrapper(
            nodes.retrieve,
        )
        self.update = async_to_streamed_response_wrapper(
            nodes.update,
        )
        self.list = async_to_streamed_response_wrapper(
            nodes.list,
        )
        self.delete = async_to_streamed_response_wrapper(
            nodes.delete,
        )

    @cached_property
    def visibility(self) -> AsyncVisibilityResourceWithStreamingResponse:
        return AsyncVisibilityResourceWithStreamingResponse(self._nodes.visibility)

    @cached_property
    def assets(self) -> AsyncAssetsResourceWithStreamingResponse:
        return AsyncAssetsResourceWithStreamingResponse(self._nodes.assets)

    @cached_property
    def children(self) -> AsyncChildrenResourceWithStreamingResponse:
        return AsyncChildrenResourceWithStreamingResponse(self._nodes.children)
