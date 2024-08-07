# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, Union, Mapping
from typing_extensions import Self, override

import httpx

from . import resources, _exceptions
from ._qs import Querystring
from ._types import (
    NOT_GIVEN,
    Omit,
    Timeout,
    NotGiven,
    Transport,
    ProxiesTypes,
    RequestOptions,
)
from ._utils import (
    is_given,
    get_async_library,
)
from ._version import __version__
from ._streaming import Stream as Stream, AsyncStream as AsyncStream
from ._exceptions import StorydenError, APIStatusError
from ._base_client import (
    DEFAULT_MAX_RETRIES,
    SyncAPIClient,
    AsyncAPIClient,
)

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
    version: resources.VersionResource
    openapi_json: resources.OpenAPIJsonResource
    v1: resources.V1Resource
    auth: resources.AuthResource
    categories: resources.CategoriesResource
    threads: resources.ThreadsResource
    posts: resources.PostsResource
    assets: resources.AssetsResource
    collections: resources.CollectionsResource
    links: resources.LinksResource
    datagraph: resources.DatagraphResource
    with_raw_response: StorydenWithRawResponse
    with_streaming_response: StorydenWithStreamedResponse

    # client options
    storyden_session: str
    storyden_webauthn_session: str

    def __init__(
        self,
        *,
        storyden_session: str | None = None,
        storyden_webauthn_session: str | None = None,
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
        """Construct a new synchronous Storyden client instance.

        This automatically infers the following arguments from their corresponding environment variables if they are not provided:
        - `storyden_session` from `STORYDEN_STORYDEN_SESSION`
        - `storyden_webauthn_session` from `STORYDEN_STORYDEN_WEBAUTHN_SESSION`
        """
        if storyden_session is None:
            storyden_session = os.environ.get("STORYDEN_STORYDEN_SESSION")
        if storyden_session is None:
            raise StorydenError(
                "The storyden_session client option must be set either by passing storyden_session to the client or by setting the STORYDEN_STORYDEN_SESSION environment variable"
            )
        self.storyden_session = storyden_session

        if storyden_webauthn_session is None:
            storyden_webauthn_session = os.environ.get("STORYDEN_STORYDEN_WEBAUTHN_SESSION")
        if storyden_webauthn_session is None:
            raise StorydenError(
                "The storyden_webauthn_session client option must be set either by passing storyden_webauthn_session to the client or by setting the STORYDEN_STORYDEN_WEBAUTHN_SESSION environment variable"
            )
        self.storyden_webauthn_session = storyden_webauthn_session

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

        self.version = resources.VersionResource(self)
        self.openapi_json = resources.OpenAPIJsonResource(self)
        self.v1 = resources.V1Resource(self)
        self.auth = resources.AuthResource(self)
        self.categories = resources.CategoriesResource(self)
        self.threads = resources.ThreadsResource(self)
        self.posts = resources.PostsResource(self)
        self.assets = resources.AssetsResource(self)
        self.collections = resources.CollectionsResource(self)
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
    def auth_headers(self) -> dict[str, str]:
        if self._browser:
            return self._browser
        if self._webauthn:
            return self._webauthn
        return {}

    @property
    def _browser(self) -> dict[str, str]:
        storyden_session = self.storyden_session
        return {"storyden-session": storyden_session}

    @property
    def _webauthn(self) -> dict[str, str]:
        storyden_webauthn_session = self.storyden_webauthn_session
        return {"storyden-webauthn-session": storyden_webauthn_session}

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
        storyden_session: str | None = None,
        storyden_webauthn_session: str | None = None,
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
            storyden_session=storyden_session or self.storyden_session,
            storyden_webauthn_session=storyden_webauthn_session or self.storyden_webauthn_session,
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
    version: resources.AsyncVersionResource
    openapi_json: resources.AsyncOpenAPIJsonResource
    v1: resources.AsyncV1Resource
    auth: resources.AsyncAuthResource
    categories: resources.AsyncCategoriesResource
    threads: resources.AsyncThreadsResource
    posts: resources.AsyncPostsResource
    assets: resources.AsyncAssetsResource
    collections: resources.AsyncCollectionsResource
    links: resources.AsyncLinksResource
    datagraph: resources.AsyncDatagraphResource
    with_raw_response: AsyncStorydenWithRawResponse
    with_streaming_response: AsyncStorydenWithStreamedResponse

    # client options
    storyden_session: str
    storyden_webauthn_session: str

    def __init__(
        self,
        *,
        storyden_session: str | None = None,
        storyden_webauthn_session: str | None = None,
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
        """Construct a new async Storyden client instance.

        This automatically infers the following arguments from their corresponding environment variables if they are not provided:
        - `storyden_session` from `STORYDEN_STORYDEN_SESSION`
        - `storyden_webauthn_session` from `STORYDEN_STORYDEN_WEBAUTHN_SESSION`
        """
        if storyden_session is None:
            storyden_session = os.environ.get("STORYDEN_STORYDEN_SESSION")
        if storyden_session is None:
            raise StorydenError(
                "The storyden_session client option must be set either by passing storyden_session to the client or by setting the STORYDEN_STORYDEN_SESSION environment variable"
            )
        self.storyden_session = storyden_session

        if storyden_webauthn_session is None:
            storyden_webauthn_session = os.environ.get("STORYDEN_STORYDEN_WEBAUTHN_SESSION")
        if storyden_webauthn_session is None:
            raise StorydenError(
                "The storyden_webauthn_session client option must be set either by passing storyden_webauthn_session to the client or by setting the STORYDEN_STORYDEN_WEBAUTHN_SESSION environment variable"
            )
        self.storyden_webauthn_session = storyden_webauthn_session

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

        self.version = resources.AsyncVersionResource(self)
        self.openapi_json = resources.AsyncOpenAPIJsonResource(self)
        self.v1 = resources.AsyncV1Resource(self)
        self.auth = resources.AsyncAuthResource(self)
        self.categories = resources.AsyncCategoriesResource(self)
        self.threads = resources.AsyncThreadsResource(self)
        self.posts = resources.AsyncPostsResource(self)
        self.assets = resources.AsyncAssetsResource(self)
        self.collections = resources.AsyncCollectionsResource(self)
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
    def auth_headers(self) -> dict[str, str]:
        if self._browser:
            return self._browser
        if self._webauthn:
            return self._webauthn
        return {}

    @property
    def _browser(self) -> dict[str, str]:
        storyden_session = self.storyden_session
        return {"storyden-session": storyden_session}

    @property
    def _webauthn(self) -> dict[str, str]:
        storyden_webauthn_session = self.storyden_webauthn_session
        return {"storyden-webauthn-session": storyden_webauthn_session}

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
        storyden_session: str | None = None,
        storyden_webauthn_session: str | None = None,
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
            storyden_session=storyden_session or self.storyden_session,
            storyden_webauthn_session=storyden_webauthn_session or self.storyden_webauthn_session,
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
        self.version = resources.VersionResourceWithRawResponse(client.version)
        self.openapi_json = resources.OpenAPIJsonResourceWithRawResponse(client.openapi_json)
        self.v1 = resources.V1ResourceWithRawResponse(client.v1)
        self.auth = resources.AuthResourceWithRawResponse(client.auth)
        self.categories = resources.CategoriesResourceWithRawResponse(client.categories)
        self.threads = resources.ThreadsResourceWithRawResponse(client.threads)
        self.posts = resources.PostsResourceWithRawResponse(client.posts)
        self.assets = resources.AssetsResourceWithRawResponse(client.assets)
        self.collections = resources.CollectionsResourceWithRawResponse(client.collections)
        self.links = resources.LinksResourceWithRawResponse(client.links)
        self.datagraph = resources.DatagraphResourceWithRawResponse(client.datagraph)


class AsyncStorydenWithRawResponse:
    def __init__(self, client: AsyncStoryden) -> None:
        self.version = resources.AsyncVersionResourceWithRawResponse(client.version)
        self.openapi_json = resources.AsyncOpenAPIJsonResourceWithRawResponse(client.openapi_json)
        self.v1 = resources.AsyncV1ResourceWithRawResponse(client.v1)
        self.auth = resources.AsyncAuthResourceWithRawResponse(client.auth)
        self.categories = resources.AsyncCategoriesResourceWithRawResponse(client.categories)
        self.threads = resources.AsyncThreadsResourceWithRawResponse(client.threads)
        self.posts = resources.AsyncPostsResourceWithRawResponse(client.posts)
        self.assets = resources.AsyncAssetsResourceWithRawResponse(client.assets)
        self.collections = resources.AsyncCollectionsResourceWithRawResponse(client.collections)
        self.links = resources.AsyncLinksResourceWithRawResponse(client.links)
        self.datagraph = resources.AsyncDatagraphResourceWithRawResponse(client.datagraph)


class StorydenWithStreamedResponse:
    def __init__(self, client: Storyden) -> None:
        self.version = resources.VersionResourceWithStreamingResponse(client.version)
        self.openapi_json = resources.OpenAPIJsonResourceWithStreamingResponse(client.openapi_json)
        self.v1 = resources.V1ResourceWithStreamingResponse(client.v1)
        self.auth = resources.AuthResourceWithStreamingResponse(client.auth)
        self.categories = resources.CategoriesResourceWithStreamingResponse(client.categories)
        self.threads = resources.ThreadsResourceWithStreamingResponse(client.threads)
        self.posts = resources.PostsResourceWithStreamingResponse(client.posts)
        self.assets = resources.AssetsResourceWithStreamingResponse(client.assets)
        self.collections = resources.CollectionsResourceWithStreamingResponse(client.collections)
        self.links = resources.LinksResourceWithStreamingResponse(client.links)
        self.datagraph = resources.DatagraphResourceWithStreamingResponse(client.datagraph)


class AsyncStorydenWithStreamedResponse:
    def __init__(self, client: AsyncStoryden) -> None:
        self.version = resources.AsyncVersionResourceWithStreamingResponse(client.version)
        self.openapi_json = resources.AsyncOpenAPIJsonResourceWithStreamingResponse(client.openapi_json)
        self.v1 = resources.AsyncV1ResourceWithStreamingResponse(client.v1)
        self.auth = resources.AsyncAuthResourceWithStreamingResponse(client.auth)
        self.categories = resources.AsyncCategoriesResourceWithStreamingResponse(client.categories)
        self.threads = resources.AsyncThreadsResourceWithStreamingResponse(client.threads)
        self.posts = resources.AsyncPostsResourceWithStreamingResponse(client.posts)
        self.assets = resources.AsyncAssetsResourceWithStreamingResponse(client.assets)
        self.collections = resources.AsyncCollectionsResourceWithStreamingResponse(client.collections)
        self.links = resources.AsyncLinksResourceWithStreamingResponse(client.links)
        self.datagraph = resources.AsyncDatagraphResourceWithStreamingResponse(client.datagraph)


Client = Storyden

AsyncClient = AsyncStoryden
