# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from storyden import Storyden, AsyncStoryden
from tests.utils import assert_matches_type
from storyden.types.v1.admin import BanCreateResponse, BanDeleteResponse

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestBans:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_create(self, client: Storyden) -> None:
        ban = client.v1.admin.bans.create(
            "Southclaws",
        )
        assert_matches_type(BanCreateResponse, ban, path=["response"])

    @parametrize
    def test_raw_response_create(self, client: Storyden) -> None:
        response = client.v1.admin.bans.with_raw_response.create(
            "Southclaws",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        ban = response.parse()
        assert_matches_type(BanCreateResponse, ban, path=["response"])

    @parametrize
    def test_streaming_response_create(self, client: Storyden) -> None:
        with client.v1.admin.bans.with_streaming_response.create(
            "Southclaws",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            ban = response.parse()
            assert_matches_type(BanCreateResponse, ban, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_create(self, client: Storyden) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_handle` but received ''"):
            client.v1.admin.bans.with_raw_response.create(
                "",
            )

    @parametrize
    def test_method_delete(self, client: Storyden) -> None:
        ban = client.v1.admin.bans.delete(
            "Southclaws",
        )
        assert_matches_type(BanDeleteResponse, ban, path=["response"])

    @parametrize
    def test_raw_response_delete(self, client: Storyden) -> None:
        response = client.v1.admin.bans.with_raw_response.delete(
            "Southclaws",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        ban = response.parse()
        assert_matches_type(BanDeleteResponse, ban, path=["response"])

    @parametrize
    def test_streaming_response_delete(self, client: Storyden) -> None:
        with client.v1.admin.bans.with_streaming_response.delete(
            "Southclaws",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            ban = response.parse()
            assert_matches_type(BanDeleteResponse, ban, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_delete(self, client: Storyden) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_handle` but received ''"):
            client.v1.admin.bans.with_raw_response.delete(
                "",
            )


class TestAsyncBans:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    async def test_method_create(self, async_client: AsyncStoryden) -> None:
        ban = await async_client.v1.admin.bans.create(
            "Southclaws",
        )
        assert_matches_type(BanCreateResponse, ban, path=["response"])

    @parametrize
    async def test_raw_response_create(self, async_client: AsyncStoryden) -> None:
        response = await async_client.v1.admin.bans.with_raw_response.create(
            "Southclaws",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        ban = await response.parse()
        assert_matches_type(BanCreateResponse, ban, path=["response"])

    @parametrize
    async def test_streaming_response_create(self, async_client: AsyncStoryden) -> None:
        async with async_client.v1.admin.bans.with_streaming_response.create(
            "Southclaws",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            ban = await response.parse()
            assert_matches_type(BanCreateResponse, ban, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_create(self, async_client: AsyncStoryden) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_handle` but received ''"):
            await async_client.v1.admin.bans.with_raw_response.create(
                "",
            )

    @parametrize
    async def test_method_delete(self, async_client: AsyncStoryden) -> None:
        ban = await async_client.v1.admin.bans.delete(
            "Southclaws",
        )
        assert_matches_type(BanDeleteResponse, ban, path=["response"])

    @parametrize
    async def test_raw_response_delete(self, async_client: AsyncStoryden) -> None:
        response = await async_client.v1.admin.bans.with_raw_response.delete(
            "Southclaws",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        ban = await response.parse()
        assert_matches_type(BanDeleteResponse, ban, path=["response"])

    @parametrize
    async def test_streaming_response_delete(self, async_client: AsyncStoryden) -> None:
        async with async_client.v1.admin.bans.with_streaming_response.delete(
            "Southclaws",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            ban = await response.parse()
            assert_matches_type(BanDeleteResponse, ban, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_delete(self, async_client: AsyncStoryden) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_handle` but received ''"):
            await async_client.v1.admin.bans.with_raw_response.delete(
                "",
            )
