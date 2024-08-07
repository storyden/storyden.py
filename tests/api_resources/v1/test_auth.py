# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from storyden import Storyden, AsyncStoryden
from tests.utils import assert_matches_type
from storyden.types.v1 import AuthListResponse, AuthPasswordSignupResponse

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestAuth:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_list(self, client: Storyden) -> None:
        auth = client.v1.auth.list()
        assert_matches_type(AuthListResponse, auth, path=["response"])

    @parametrize
    def test_raw_response_list(self, client: Storyden) -> None:
        response = client.v1.auth.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        auth = response.parse()
        assert_matches_type(AuthListResponse, auth, path=["response"])

    @parametrize
    def test_streaming_response_list(self, client: Storyden) -> None:
        with client.v1.auth.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            auth = response.parse()
            assert_matches_type(AuthListResponse, auth, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_logout(self, client: Storyden) -> None:
        auth = client.v1.auth.logout()
        assert auth is None

    @parametrize
    def test_raw_response_logout(self, client: Storyden) -> None:
        response = client.v1.auth.with_raw_response.logout()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        auth = response.parse()
        assert auth is None

    @parametrize
    def test_streaming_response_logout(self, client: Storyden) -> None:
        with client.v1.auth.with_streaming_response.logout() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            auth = response.parse()
            assert auth is None

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_password_signup(self, client: Storyden) -> None:
        auth = client.v1.auth.password_signup(
            token="password",
            identifier="odin",
        )
        assert_matches_type(AuthPasswordSignupResponse, auth, path=["response"])

    @parametrize
    def test_raw_response_password_signup(self, client: Storyden) -> None:
        response = client.v1.auth.with_raw_response.password_signup(
            token="password",
            identifier="odin",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        auth = response.parse()
        assert_matches_type(AuthPasswordSignupResponse, auth, path=["response"])

    @parametrize
    def test_streaming_response_password_signup(self, client: Storyden) -> None:
        with client.v1.auth.with_streaming_response.password_signup(
            token="password",
            identifier="odin",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            auth = response.parse()
            assert_matches_type(AuthPasswordSignupResponse, auth, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncAuth:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    async def test_method_list(self, async_client: AsyncStoryden) -> None:
        auth = await async_client.v1.auth.list()
        assert_matches_type(AuthListResponse, auth, path=["response"])

    @parametrize
    async def test_raw_response_list(self, async_client: AsyncStoryden) -> None:
        response = await async_client.v1.auth.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        auth = await response.parse()
        assert_matches_type(AuthListResponse, auth, path=["response"])

    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncStoryden) -> None:
        async with async_client.v1.auth.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            auth = await response.parse()
            assert_matches_type(AuthListResponse, auth, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_logout(self, async_client: AsyncStoryden) -> None:
        auth = await async_client.v1.auth.logout()
        assert auth is None

    @parametrize
    async def test_raw_response_logout(self, async_client: AsyncStoryden) -> None:
        response = await async_client.v1.auth.with_raw_response.logout()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        auth = await response.parse()
        assert auth is None

    @parametrize
    async def test_streaming_response_logout(self, async_client: AsyncStoryden) -> None:
        async with async_client.v1.auth.with_streaming_response.logout() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            auth = await response.parse()
            assert auth is None

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_password_signup(self, async_client: AsyncStoryden) -> None:
        auth = await async_client.v1.auth.password_signup(
            token="password",
            identifier="odin",
        )
        assert_matches_type(AuthPasswordSignupResponse, auth, path=["response"])

    @parametrize
    async def test_raw_response_password_signup(self, async_client: AsyncStoryden) -> None:
        response = await async_client.v1.auth.with_raw_response.password_signup(
            token="password",
            identifier="odin",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        auth = await response.parse()
        assert_matches_type(AuthPasswordSignupResponse, auth, path=["response"])

    @parametrize
    async def test_streaming_response_password_signup(self, async_client: AsyncStoryden) -> None:
        async with async_client.v1.auth.with_streaming_response.password_signup(
            token="password",
            identifier="odin",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            auth = await response.parse()
            assert_matches_type(AuthPasswordSignupResponse, auth, path=["response"])

        assert cast(Any, response.is_closed) is True
