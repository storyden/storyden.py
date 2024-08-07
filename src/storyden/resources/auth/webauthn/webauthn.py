# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from .make import (
    MakeResource,
    AsyncMakeResource,
    MakeResourceWithRawResponse,
    AsyncMakeResourceWithRawResponse,
    MakeResourceWithStreamingResponse,
    AsyncMakeResourceWithStreamingResponse,
)
from .assert_ import (
    AssertResource,
    AsyncAssertResource,
    AssertResourceWithRawResponse,
    AsyncAssertResourceWithRawResponse,
    AssertResourceWithStreamingResponse,
    AsyncAssertResourceWithStreamingResponse,
)
from ...._compat import cached_property
from ...._resource import SyncAPIResource, AsyncAPIResource

__all__ = ["WebauthnResource", "AsyncWebauthnResource"]


class WebauthnResource(SyncAPIResource):
    @cached_property
    def make(self) -> MakeResource:
        return MakeResource(self._client)

    @cached_property
    def assert_(self) -> AssertResource:
        return AssertResource(self._client)

    @cached_property
    def with_raw_response(self) -> WebauthnResourceWithRawResponse:
        return WebauthnResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> WebauthnResourceWithStreamingResponse:
        return WebauthnResourceWithStreamingResponse(self)


class AsyncWebauthnResource(AsyncAPIResource):
    @cached_property
    def make(self) -> AsyncMakeResource:
        return AsyncMakeResource(self._client)

    @cached_property
    def assert_(self) -> AsyncAssertResource:
        return AsyncAssertResource(self._client)

    @cached_property
    def with_raw_response(self) -> AsyncWebauthnResourceWithRawResponse:
        return AsyncWebauthnResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncWebauthnResourceWithStreamingResponse:
        return AsyncWebauthnResourceWithStreamingResponse(self)


class WebauthnResourceWithRawResponse:
    def __init__(self, webauthn: WebauthnResource) -> None:
        self._webauthn = webauthn

    @cached_property
    def make(self) -> MakeResourceWithRawResponse:
        return MakeResourceWithRawResponse(self._webauthn.make)

    @cached_property
    def assert_(self) -> AssertResourceWithRawResponse:
        return AssertResourceWithRawResponse(self._webauthn.assert_)


class AsyncWebauthnResourceWithRawResponse:
    def __init__(self, webauthn: AsyncWebauthnResource) -> None:
        self._webauthn = webauthn

    @cached_property
    def make(self) -> AsyncMakeResourceWithRawResponse:
        return AsyncMakeResourceWithRawResponse(self._webauthn.make)

    @cached_property
    def assert_(self) -> AsyncAssertResourceWithRawResponse:
        return AsyncAssertResourceWithRawResponse(self._webauthn.assert_)


class WebauthnResourceWithStreamingResponse:
    def __init__(self, webauthn: WebauthnResource) -> None:
        self._webauthn = webauthn

    @cached_property
    def make(self) -> MakeResourceWithStreamingResponse:
        return MakeResourceWithStreamingResponse(self._webauthn.make)

    @cached_property
    def assert_(self) -> AssertResourceWithStreamingResponse:
        return AssertResourceWithStreamingResponse(self._webauthn.assert_)


class AsyncWebauthnResourceWithStreamingResponse:
    def __init__(self, webauthn: AsyncWebauthnResource) -> None:
        self._webauthn = webauthn

    @cached_property
    def make(self) -> AsyncMakeResourceWithStreamingResponse:
        return AsyncMakeResourceWithStreamingResponse(self._webauthn.make)

    @cached_property
    def assert_(self) -> AsyncAssertResourceWithStreamingResponse:
        return AsyncAssertResourceWithStreamingResponse(self._webauthn.assert_)
