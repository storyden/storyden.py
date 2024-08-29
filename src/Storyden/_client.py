# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import httpx

import os

from ._streaming import AsyncStream as AsyncStream, Stream as Stream

from typing_extensions import override, Self

from typing import Any

from ._exceptions import APIStatusError

from ._utils import get_async_library

from . import _exceptions

import os
import asyncio
import warnings
from typing import Optional, Union, Dict, Any, Mapping, overload, cast
from typing_extensions import Literal

import httpx

from ._version import __version__
from ._qs import Querystring
from ._utils import (
    extract_files,
    maybe_transform,
    required_args,
    deepcopy_minimal,
    maybe_coerce_integer,
    maybe_coerce_float,
    maybe_coerce_boolean,
    is_given,
)
from ._types import (
    Omit,
    NotGiven,
    Timeout,
    Transport,
    ProxiesTypes,
    RequestOptions,
    Headers,
    NoneType,
    Query,
    Body,
    NOT_GIVEN,
)
from ._base_client import (
    DEFAULT_CONNECTION_LIMITS,
    DEFAULT_TIMEOUT,
    DEFAULT_MAX_RETRIES,
    ResponseT,
    SyncHttpxClientWrapper,
    AsyncHttpxClientWrapper,
    SyncAPIClient,
    AsyncAPIClient,
    make_request_options,
)
from . import resources

__all__ = [
    "Timeout",
    "Transport",
    "ProxiesTypes",
    "RequestOptions",
    "resources",
    "Storyden",
    "AsyncStoryden",
    "Client",
    "AsyncClient",
]


class Storyden(SyncAPIClient):
    misc: resources.MiscResource
    admin: resources.AdminResource
    auth: resources.AuthResource
    accounts: resources.AccountsResource
    profiles: resources.ProfilesResource
    categories: resources.CategoriesResource
    threads: resources.ThreadsResource
    posts: resources.PostsResource
    assets: resources.AssetsResource
    collections: resources.CollectionsResource
    nodes: resources.NodesResource
    links: resources.LinksResource
    datagraph: resources.DatagraphResource
    with_raw_response: StorydenWithRawResponse
    with_streaming_response: StorydenWithStreamedResponse

    # client options

    def __init__(
        self,
        *,
        base_url: str | httpx.URL | None = None,
        timeout: Union[float, Timeout, None, NotGiven] = NOT_GIVEN,
        max_retries: int = DEFAULT_MAX_RETRIES,
        default_headers: Mapping[str, str] | None = None,
        default_query: Mapping[str, object] | None = None,
        # Configure a custom httpx client.
        # We provide a `DefaultHttpxClient` class that you can pass to retain the default values we use for `limits`, `timeout` & `follow_redirects`.
        # See the [httpx documentation](https://www.python-httpx.org/api/#client) for more details.
        http_client: httpx.Client | None = None,
        # Enable or disable schema validation for data returned by the API.
        # When enabled an error APIResponseValidationError is raised
        # if the API responds with invalid data for the expected schema.
        #
        # This parameter may be removed or changed in the future.
        # If you rely on this feature, please open a GitHub issue
        # outlining your use-case to help us decide if it should be
        # part of our public interface in the future.
        _strict_response_validation: bool = False,
    ) -> None:
        """Construct a new synchronous Storyden client instance."""
        if base_url is None:
            base_url = os.environ.get("STORYDEN_BASE_URL")
        if base_url is None:
            base_url = f"/api"

        super().__init__(
            version=__version__,
            base_url=base_url,
            max_retries=max_retries,
            timeout=timeout,
            http_client=http_client,
            custom_headers=default_headers,
            custom_query=default_query,
            _strict_response_validation=_strict_response_validation,
        )

        self.misc = resources.MiscResource(self)
        self.admin = resources.AdminResource(self)
        self.auth = resources.AuthResource(self)
        self.accounts = resources.AccountsResource(self)
        self.profiles = resources.ProfilesResource(self)
        self.categories = resources.CategoriesResource(self)
        self.threads = resources.ThreadsResource(self)
        self.posts = resources.PostsResource(self)
        self.assets = resources.AssetsResource(self)
        self.collections = resources.CollectionsResource(self)
        self.nodes = resources.NodesResource(self)
        self.links = resources.LinksResource(self)
        self.datagraph = resources.DatagraphResource(self)
        self.with_raw_response = StorydenWithRawResponse(self)
        self.with_streaming_response = StorydenWithStreamedResponse(self)

    @property
    @override
    def qs(self) -> Querystring:
        return Querystring(array_format="comma")

    @property
    @override
    def default_headers(self) -> dict[str, str | Omit]:
        return {
            **super().default_headers,
            "X-Stainless-Async": "false",
            **self._custom_headers,
        }

    def copy(
        self,
        *,
        base_url: str | httpx.URL | None = None,
        timeout: float | Timeout | None | NotGiven = NOT_GIVEN,
        http_client: httpx.Client | None = None,
        max_retries: int | NotGiven = NOT_GIVEN,
        default_headers: Mapping[str, str] | None = None,
        set_default_headers: Mapping[str, str] | None = None,
        default_query: Mapping[str, object] | None = None,
        set_default_query: Mapping[str, object] | None = None,
        _extra_kwargs: Mapping[str, Any] = {},
    ) -> Self:
        """
        Create a new client instance re-using the same options given to the current client with optional overriding.
        """
        if default_headers is not None and set_default_headers is not None:
            raise ValueError("The `default_headers` and `set_default_headers` arguments are mutually exclusive")

        if default_query is not None and set_default_query is not None:
            raise ValueError("The `default_query` and `set_default_query` arguments are mutually exclusive")

        headers = self._custom_headers
        if default_headers is not None:
            headers = {**headers, **default_headers}
        elif set_default_headers is not None:
            headers = set_default_headers

        params = self._custom_query
        if default_query is not None:
            params = {**params, **default_query}
        elif set_default_query is not None:
            params = set_default_query

        http_client = http_client or self._client
        return self.__class__(
            base_url=base_url or self.base_url,
            timeout=self.timeout if isinstance(timeout, NotGiven) else timeout,
            http_client=http_client,
            max_retries=max_retries if is_given(max_retries) else self.max_retries,
            default_headers=headers,
            default_query=params,
            **_extra_kwargs,
        )

    # Alias for `copy` for nicer inline usage, e.g.
    # client.with_options(timeout=10).foo.create(...)
    with_options = copy

    @override
    def _make_status_error(
        self,
        err_msg: str,
        *,
        body: object,
        response: httpx.Response,
    ) -> APIStatusError:
        if response.status_code == 400:
            return _exceptions.BadRequestError(err_msg, response=response, body=body)

        if response.status_code == 401:
            return _exceptions.AuthenticationError(err_msg, response=response, body=body)

        if response.status_code == 403:
            return _exceptions.PermissionDeniedError(err_msg, response=response, body=body)

        if response.status_code == 404:
            return _exceptions.NotFoundError(err_msg, response=response, body=body)

        if response.status_code == 409:
            return _exceptions.ConflictError(err_msg, response=response, body=body)

        if response.status_code == 422:
            return _exceptions.UnprocessableEntityError(err_msg, response=response, body=body)

        if response.status_code == 429:
            return _exceptions.RateLimitError(err_msg, response=response, body=body)

        if response.status_code >= 500:
            return _exceptions.InternalServerError(err_msg, response=response, body=body)
        return APIStatusError(err_msg, response=response, body=body)


class AsyncStoryden(AsyncAPIClient):
    misc: resources.AsyncMiscResource
    admin: resources.AsyncAdminResource
    auth: resources.AsyncAuthResource
    accounts: resources.AsyncAccountsResource
    profiles: resources.AsyncProfilesResource
    categories: resources.AsyncCategoriesResource
    threads: resources.AsyncThreadsResource
    posts: resources.AsyncPostsResource
    assets: resources.AsyncAssetsResource
    collections: resources.AsyncCollectionsResource
    nodes: resources.AsyncNodesResource
    links: resources.AsyncLinksResource
    datagraph: resources.AsyncDatagraphResource
    with_raw_response: AsyncStorydenWithRawResponse
    with_streaming_response: AsyncStorydenWithStreamedResponse

    # client options

    def __init__(
        self,
        *,
        base_url: str | httpx.URL | None = None,
        timeout: Union[float, Timeout, None, NotGiven] = NOT_GIVEN,
        max_retries: int = DEFAULT_MAX_RETRIES,
        default_headers: Mapping[str, str] | None = None,
        default_query: Mapping[str, object] | None = None,
        # Configure a custom httpx client.
        # We provide a `DefaultAsyncHttpxClient` class that you can pass to retain the default values we use for `limits`, `timeout` & `follow_redirects`.
        # See the [httpx documentation](https://www.python-httpx.org/api/#asyncclient) for more details.
        http_client: httpx.AsyncClient | None = None,
        # Enable or disable schema validation for data returned by the API.
        # When enabled an error APIResponseValidationError is raised
        # if the API responds with invalid data for the expected schema.
        #
        # This parameter may be removed or changed in the future.
        # If you rely on this feature, please open a GitHub issue
        # outlining your use-case to help us decide if it should be
        # part of our public interface in the future.
        _strict_response_validation: bool = False,
    ) -> None:
        """Construct a new async Storyden client instance."""
        if base_url is None:
            base_url = os.environ.get("STORYDEN_BASE_URL")
        if base_url is None:
            base_url = f"/api"

        super().__init__(
            version=__version__,
            base_url=base_url,
            max_retries=max_retries,
            timeout=timeout,
            http_client=http_client,
            custom_headers=default_headers,
            custom_query=default_query,
            _strict_response_validation=_strict_response_validation,
        )

        self.misc = resources.AsyncMiscResource(self)
        self.admin = resources.AsyncAdminResource(self)
        self.auth = resources.AsyncAuthResource(self)
        self.accounts = resources.AsyncAccountsResource(self)
        self.profiles = resources.AsyncProfilesResource(self)
        self.categories = resources.AsyncCategoriesResource(self)
        self.threads = resources.AsyncThreadsResource(self)
        self.posts = resources.AsyncPostsResource(self)
        self.assets = resources.AsyncAssetsResource(self)
        self.collections = resources.AsyncCollectionsResource(self)
        self.nodes = resources.AsyncNodesResource(self)
        self.links = resources.AsyncLinksResource(self)
        self.datagraph = resources.AsyncDatagraphResource(self)
        self.with_raw_response = AsyncStorydenWithRawResponse(self)
        self.with_streaming_response = AsyncStorydenWithStreamedResponse(self)

    @property
    @override
    def qs(self) -> Querystring:
        return Querystring(array_format="comma")

    @property
    @override
    def default_headers(self) -> dict[str, str | Omit]:
        return {
            **super().default_headers,
            "X-Stainless-Async": f"async:{get_async_library()}",
            **self._custom_headers,
        }

    def copy(
        self,
        *,
        base_url: str | httpx.URL | None = None,
        timeout: float | Timeout | None | NotGiven = NOT_GIVEN,
        http_client: httpx.AsyncClient | None = None,
        max_retries: int | NotGiven = NOT_GIVEN,
        default_headers: Mapping[str, str] | None = None,
        set_default_headers: Mapping[str, str] | None = None,
        default_query: Mapping[str, object] | None = None,
        set_default_query: Mapping[str, object] | None = None,
        _extra_kwargs: Mapping[str, Any] = {},
    ) -> Self:
        """
        Create a new client instance re-using the same options given to the current client with optional overriding.
        """
        if default_headers is not None and set_default_headers is not None:
            raise ValueError("The `default_headers` and `set_default_headers` arguments are mutually exclusive")

        if default_query is not None and set_default_query is not None:
            raise ValueError("The `default_query` and `set_default_query` arguments are mutually exclusive")

        headers = self._custom_headers
        if default_headers is not None:
            headers = {**headers, **default_headers}
        elif set_default_headers is not None:
            headers = set_default_headers

        params = self._custom_query
        if default_query is not None:
            params = {**params, **default_query}
        elif set_default_query is not None:
            params = set_default_query

        http_client = http_client or self._client
        return self.__class__(
            base_url=base_url or self.base_url,
            timeout=self.timeout if isinstance(timeout, NotGiven) else timeout,
            http_client=http_client,
            max_retries=max_retries if is_given(max_retries) else self.max_retries,
            default_headers=headers,
            default_query=params,
            **_extra_kwargs,
        )

    # Alias for `copy` for nicer inline usage, e.g.
    # client.with_options(timeout=10).foo.create(...)
    with_options = copy

    @override
    def _make_status_error(
        self,
        err_msg: str,
        *,
        body: object,
        response: httpx.Response,
    ) -> APIStatusError:
        if response.status_code == 400:
            return _exceptions.BadRequestError(err_msg, response=response, body=body)

        if response.status_code == 401:
            return _exceptions.AuthenticationError(err_msg, response=response, body=body)

        if response.status_code == 403:
            return _exceptions.PermissionDeniedError(err_msg, response=response, body=body)

        if response.status_code == 404:
            return _exceptions.NotFoundError(err_msg, response=response, body=body)

        if response.status_code == 409:
            return _exceptions.ConflictError(err_msg, response=response, body=body)

        if response.status_code == 422:
            return _exceptions.UnprocessableEntityError(err_msg, response=response, body=body)

        if response.status_code == 429:
            return _exceptions.RateLimitError(err_msg, response=response, body=body)

        if response.status_code >= 500:
            return _exceptions.InternalServerError(err_msg, response=response, body=body)
        return APIStatusError(err_msg, response=response, body=body)


class StorydenWithRawResponse:
    def __init__(self, client: Storyden) -> None:
        self.misc = resources.MiscResourceWithRawResponse(client.misc)
        self.admin = resources.AdminResourceWithRawResponse(client.admin)
        self.auth = resources.AuthResourceWithRawResponse(client.auth)
        self.accounts = resources.AccountsResourceWithRawResponse(client.accounts)
        self.profiles = resources.ProfilesResourceWithRawResponse(client.profiles)
        self.categories = resources.CategoriesResourceWithRawResponse(client.categories)
        self.threads = resources.ThreadsResourceWithRawResponse(client.threads)
        self.posts = resources.PostsResourceWithRawResponse(client.posts)
        self.assets = resources.AssetsResourceWithRawResponse(client.assets)
        self.collections = resources.CollectionsResourceWithRawResponse(client.collections)
        self.nodes = resources.NodesResourceWithRawResponse(client.nodes)
        self.links = resources.LinksResourceWithRawResponse(client.links)
        self.datagraph = resources.DatagraphResourceWithRawResponse(client.datagraph)


class AsyncStorydenWithRawResponse:
    def __init__(self, client: AsyncStoryden) -> None:
        self.misc = resources.AsyncMiscResourceWithRawResponse(client.misc)
        self.admin = resources.AsyncAdminResourceWithRawResponse(client.admin)
        self.auth = resources.AsyncAuthResourceWithRawResponse(client.auth)
        self.accounts = resources.AsyncAccountsResourceWithRawResponse(client.accounts)
        self.profiles = resources.AsyncProfilesResourceWithRawResponse(client.profiles)
        self.categories = resources.AsyncCategoriesResourceWithRawResponse(client.categories)
        self.threads = resources.AsyncThreadsResourceWithRawResponse(client.threads)
        self.posts = resources.AsyncPostsResourceWithRawResponse(client.posts)
        self.assets = resources.AsyncAssetsResourceWithRawResponse(client.assets)
        self.collections = resources.AsyncCollectionsResourceWithRawResponse(client.collections)
        self.nodes = resources.AsyncNodesResourceWithRawResponse(client.nodes)
        self.links = resources.AsyncLinksResourceWithRawResponse(client.links)
        self.datagraph = resources.AsyncDatagraphResourceWithRawResponse(client.datagraph)


class StorydenWithStreamedResponse:
    def __init__(self, client: Storyden) -> None:
        self.misc = resources.MiscResourceWithStreamingResponse(client.misc)
        self.admin = resources.AdminResourceWithStreamingResponse(client.admin)
        self.auth = resources.AuthResourceWithStreamingResponse(client.auth)
        self.accounts = resources.AccountsResourceWithStreamingResponse(client.accounts)
        self.profiles = resources.ProfilesResourceWithStreamingResponse(client.profiles)
        self.categories = resources.CategoriesResourceWithStreamingResponse(client.categories)
        self.threads = resources.ThreadsResourceWithStreamingResponse(client.threads)
        self.posts = resources.PostsResourceWithStreamingResponse(client.posts)
        self.assets = resources.AssetsResourceWithStreamingResponse(client.assets)
        self.collections = resources.CollectionsResourceWithStreamingResponse(client.collections)
        self.nodes = resources.NodesResourceWithStreamingResponse(client.nodes)
        self.links = resources.LinksResourceWithStreamingResponse(client.links)
        self.datagraph = resources.DatagraphResourceWithStreamingResponse(client.datagraph)


class AsyncStorydenWithStreamedResponse:
    def __init__(self, client: AsyncStoryden) -> None:
        self.misc = resources.AsyncMiscResourceWithStreamingResponse(client.misc)
        self.admin = resources.AsyncAdminResourceWithStreamingResponse(client.admin)
        self.auth = resources.AsyncAuthResourceWithStreamingResponse(client.auth)
        self.accounts = resources.AsyncAccountsResourceWithStreamingResponse(client.accounts)
        self.profiles = resources.AsyncProfilesResourceWithStreamingResponse(client.profiles)
        self.categories = resources.AsyncCategoriesResourceWithStreamingResponse(client.categories)
        self.threads = resources.AsyncThreadsResourceWithStreamingResponse(client.threads)
        self.posts = resources.AsyncPostsResourceWithStreamingResponse(client.posts)
        self.assets = resources.AsyncAssetsResourceWithStreamingResponse(client.assets)
        self.collections = resources.AsyncCollectionsResourceWithStreamingResponse(client.collections)
        self.nodes = resources.AsyncNodesResourceWithStreamingResponse(client.nodes)
        self.links = resources.AsyncLinksResourceWithStreamingResponse(client.links)
        self.datagraph = resources.AsyncDatagraphResourceWithStreamingResponse(client.datagraph)


Client = Storyden

AsyncClient = AsyncStoryden
