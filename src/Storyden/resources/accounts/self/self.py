# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from .auth_methods import AuthMethodsResource, AsyncAuthMethodsResource

from ...._compat import cached_property

from .avatar import AvatarResource, AsyncAvatarResource

import warnings
from typing import TYPE_CHECKING, Optional, Union, List, Dict, Any, Mapping, cast, overload
from typing_extensions import Literal
from ...._utils import extract_files, maybe_transform, required_args, deepcopy_minimal, strip_not_given
from ...._types import NotGiven, Timeout, Headers, NoneType, Query, Body, NOT_GIVEN, FileTypes, BinaryResponseContent
from ...._resource import SyncAPIResource, AsyncAPIResource
from ....types import shared_params
from .auth_methods import AuthMethodsResource, AsyncAuthMethodsResource, AuthMethodsResourceWithRawResponse, AsyncAuthMethodsResourceWithRawResponse, AuthMethodsResourceWithStreamingResponse, AsyncAuthMethodsResourceWithStreamingResponse
from .avatar import AvatarResource, AsyncAvatarResource, AvatarResourceWithRawResponse, AsyncAvatarResourceWithRawResponse, AvatarResourceWithStreamingResponse, AsyncAvatarResourceWithStreamingResponse

__all__ = ["SelfResource", "AsyncSelfResource"]

class SelfResource(SyncAPIResource):
    @cached_property
    def auth_methods(self) -> AuthMethodsResource:
        return AuthMethodsResource(self._client)

    @cached_property
    def avatar(self) -> AvatarResource:
        return AvatarResource(self._client)

    @cached_property
    def with_raw_response(self) -> SelfResourceWithRawResponse:
        return SelfResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> SelfResourceWithStreamingResponse:
        return SelfResourceWithStreamingResponse(self)

class AsyncSelfResource(AsyncAPIResource):
    @cached_property
    def auth_methods(self) -> AsyncAuthMethodsResource:
        return AsyncAuthMethodsResource(self._client)

    @cached_property
    def avatar(self) -> AsyncAvatarResource:
        return AsyncAvatarResource(self._client)

    @cached_property
    def with_raw_response(self) -> AsyncSelfResourceWithRawResponse:
        return AsyncSelfResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncSelfResourceWithStreamingResponse:
        return AsyncSelfResourceWithStreamingResponse(self)

class SelfResourceWithRawResponse:
    def __init__(self, self: SelfResource) -> None:
        self._self = self

    @cached_property
    def auth_methods(self) -> AuthMethodsResourceWithRawResponse:
        return AuthMethodsResourceWithRawResponse(self._self.auth_methods)

    @cached_property
    def avatar(self) -> AvatarResourceWithRawResponse:
        return AvatarResourceWithRawResponse(self._self.avatar)

class AsyncSelfResourceWithRawResponse:
    def __init__(self, self: AsyncSelfResource) -> None:
        self._self = self

    @cached_property
    def auth_methods(self) -> AsyncAuthMethodsResourceWithRawResponse:
        return AsyncAuthMethodsResourceWithRawResponse(self._self.auth_methods)

    @cached_property
    def avatar(self) -> AsyncAvatarResourceWithRawResponse:
        return AsyncAvatarResourceWithRawResponse(self._self.avatar)

class SelfResourceWithStreamingResponse:
    def __init__(self, self: SelfResource) -> None:
        self._self = self

    @cached_property
    def auth_methods(self) -> AuthMethodsResourceWithStreamingResponse:
        return AuthMethodsResourceWithStreamingResponse(self._self.auth_methods)

    @cached_property
    def avatar(self) -> AvatarResourceWithStreamingResponse:
        return AvatarResourceWithStreamingResponse(self._self.avatar)

class AsyncSelfResourceWithStreamingResponse:
    def __init__(self, self: AsyncSelfResource) -> None:
        self._self = self

    @cached_property
    def auth_methods(self) -> AsyncAuthMethodsResourceWithStreamingResponse:
        return AsyncAuthMethodsResourceWithStreamingResponse(self._self.auth_methods)

    @cached_property
    def avatar(self) -> AsyncAvatarResourceWithStreamingResponse:
        return AsyncAvatarResourceWithStreamingResponse(self._self.avatar)