# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from .version import VersionResource, AsyncVersionResource

from ..._compat import cached_property

from .openapi import OpenAPIResource, AsyncOpenAPIResource

from .info.info import InfoResource, AsyncInfoResource

import warnings
from typing import TYPE_CHECKING, Optional, Union, List, Dict, Any, Mapping, cast, overload
from typing_extensions import Literal
from ..._utils import extract_files, maybe_transform, required_args, deepcopy_minimal, strip_not_given
from ..._types import NotGiven, Timeout, Headers, NoneType, Query, Body, NOT_GIVEN, FileTypes, BinaryResponseContent
from ..._resource import SyncAPIResource, AsyncAPIResource
from ...types import shared_params
from .version import (
    VersionResource,
    AsyncVersionResource,
    VersionResourceWithRawResponse,
    AsyncVersionResourceWithRawResponse,
    VersionResourceWithStreamingResponse,
    AsyncVersionResourceWithStreamingResponse,
)
from .openapi import (
    OpenAPIResource,
    AsyncOpenAPIResource,
    OpenAPIResourceWithRawResponse,
    AsyncOpenAPIResourceWithRawResponse,
    OpenAPIResourceWithStreamingResponse,
    AsyncOpenAPIResourceWithStreamingResponse,
)
from .info import (
    InfoResource,
    AsyncInfoResource,
    InfoResourceWithRawResponse,
    AsyncInfoResourceWithRawResponse,
    InfoResourceWithStreamingResponse,
    AsyncInfoResourceWithStreamingResponse,
)

__all__ = ["MiscResource", "AsyncMiscResource"]


class MiscResource(SyncAPIResource):
    @cached_property
    def version(self) -> VersionResource:
        return VersionResource(self._client)

    @cached_property
    def openapi(self) -> OpenAPIResource:
        return OpenAPIResource(self._client)

    @cached_property
    def info(self) -> InfoResource:
        return InfoResource(self._client)

    @cached_property
    def with_raw_response(self) -> MiscResourceWithRawResponse:
        return MiscResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> MiscResourceWithStreamingResponse:
        return MiscResourceWithStreamingResponse(self)


class AsyncMiscResource(AsyncAPIResource):
    @cached_property
    def version(self) -> AsyncVersionResource:
        return AsyncVersionResource(self._client)

    @cached_property
    def openapi(self) -> AsyncOpenAPIResource:
        return AsyncOpenAPIResource(self._client)

    @cached_property
    def info(self) -> AsyncInfoResource:
        return AsyncInfoResource(self._client)

    @cached_property
    def with_raw_response(self) -> AsyncMiscResourceWithRawResponse:
        return AsyncMiscResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncMiscResourceWithStreamingResponse:
        return AsyncMiscResourceWithStreamingResponse(self)


class MiscResourceWithRawResponse:
    def __init__(self, misc: MiscResource) -> None:
        self._misc = misc

    @cached_property
    def version(self) -> VersionResourceWithRawResponse:
        return VersionResourceWithRawResponse(self._misc.version)

    @cached_property
    def openapi(self) -> OpenAPIResourceWithRawResponse:
        return OpenAPIResourceWithRawResponse(self._misc.openapi)

    @cached_property
    def info(self) -> InfoResourceWithRawResponse:
        return InfoResourceWithRawResponse(self._misc.info)


class AsyncMiscResourceWithRawResponse:
    def __init__(self, misc: AsyncMiscResource) -> None:
        self._misc = misc

    @cached_property
    def version(self) -> AsyncVersionResourceWithRawResponse:
        return AsyncVersionResourceWithRawResponse(self._misc.version)

    @cached_property
    def openapi(self) -> AsyncOpenAPIResourceWithRawResponse:
        return AsyncOpenAPIResourceWithRawResponse(self._misc.openapi)

    @cached_property
    def info(self) -> AsyncInfoResourceWithRawResponse:
        return AsyncInfoResourceWithRawResponse(self._misc.info)


class MiscResourceWithStreamingResponse:
    def __init__(self, misc: MiscResource) -> None:
        self._misc = misc

    @cached_property
    def version(self) -> VersionResourceWithStreamingResponse:
        return VersionResourceWithStreamingResponse(self._misc.version)

    @cached_property
    def openapi(self) -> OpenAPIResourceWithStreamingResponse:
        return OpenAPIResourceWithStreamingResponse(self._misc.openapi)

    @cached_property
    def info(self) -> InfoResourceWithStreamingResponse:
        return InfoResourceWithStreamingResponse(self._misc.info)


class AsyncMiscResourceWithStreamingResponse:
    def __init__(self, misc: AsyncMiscResource) -> None:
        self._misc = misc

    @cached_property
    def version(self) -> AsyncVersionResourceWithStreamingResponse:
        return AsyncVersionResourceWithStreamingResponse(self._misc.version)

    @cached_property
    def openapi(self) -> AsyncOpenAPIResourceWithStreamingResponse:
        return AsyncOpenAPIResourceWithStreamingResponse(self._misc.openapi)

    @cached_property
    def info(self) -> AsyncInfoResourceWithStreamingResponse:
        return AsyncInfoResourceWithStreamingResponse(self._misc.info)
