# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from storyden import Storyden, AsyncStoryden
from tests.utils import assert_matches_type
from storyden.types.v1.accounts import AuthMethodListResponse, AuthMethodDeleteResponse

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestAuthMethods:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_list(self, client: Storyden) -> None:
        auth_method = client.v1.accounts.auth_methods.list()
        assert_matches_type(AuthMethodListResponse, auth_method, path=["response"])

    @parametrize
    def test_raw_response_list(self, client: Storyden) -> None:
        response = client.v1.accounts.auth_methods.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        auth_method = response.parse()
        assert_matches_type(AuthMethodListResponse, auth_method, path=["response"])

    @parametrize
    def test_streaming_response_list(self, client: Storyden) -> None:
        with client.v1.accounts.auth_methods.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            auth_method = response.parse()
            assert_matches_type(AuthMethodListResponse, auth_method, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_delete(self, client: Storyden) -> None:
        auth_method = client.v1.accounts.auth_methods.delete(
            "auth_method_id",
        )
        assert_matches_type(AuthMethodDeleteResponse, auth_method, path=["response"])

    @parametrize
    def test_raw_response_delete(self, client: Storyden) -> None:
        response = client.v1.accounts.auth_methods.with_raw_response.delete(
            "auth_method_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        auth_method = response.parse()
        assert_matches_type(AuthMethodDeleteResponse, auth_method, path=["response"])

    @parametrize
    def test_streaming_response_delete(self, client: Storyden) -> None:
        with client.v1.accounts.auth_methods.with_streaming_response.delete(
            "auth_method_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            auth_method = response.parse()
            assert_matches_type(AuthMethodDeleteResponse, auth_method, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_delete(self, client: Storyden) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `auth_method_id` but received ''"):
            client.v1.accounts.auth_methods.with_raw_response.delete(
                "",
            )


class TestAsyncAuthMethods:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    async def test_method_list(self, async_client: AsyncStoryden) -> None:
        auth_method = await async_client.v1.accounts.auth_methods.list()
        assert_matches_type(AuthMethodListResponse, auth_method, path=["response"])

    @parametrize
    async def test_raw_response_list(self, async_client: AsyncStoryden) -> None:
        response = await async_client.v1.accounts.auth_methods.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        auth_method = await response.parse()
        assert_matches_type(AuthMethodListResponse, auth_method, path=["response"])

    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncStoryden) -> None:
        async with async_client.v1.accounts.auth_methods.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            auth_method = await response.parse()
            assert_matches_type(AuthMethodListResponse, auth_method, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_delete(self, async_client: AsyncStoryden) -> None:
        auth_method = await async_client.v1.accounts.auth_methods.delete(
            "auth_method_id",
        )
        assert_matches_type(AuthMethodDeleteResponse, auth_method, path=["response"])

    @parametrize
    async def test_raw_response_delete(self, async_client: AsyncStoryden) -> None:
        response = await async_client.v1.accounts.auth_methods.with_raw_response.delete(
            "auth_method_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        auth_method = await response.parse()
        assert_matches_type(AuthMethodDeleteResponse, auth_method, path=["response"])

    @parametrize
    async def test_streaming_response_delete(self, async_client: AsyncStoryden) -> None:
        async with async_client.v1.accounts.auth_methods.with_streaming_response.delete(
            "auth_method_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            auth_method = await response.parse()
            assert_matches_type(AuthMethodDeleteResponse, auth_method, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_delete(self, async_client: AsyncStoryden) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `auth_method_id` but received ''"):
            await async_client.v1.accounts.auth_methods.with_raw_response.delete(
                "",
            )
