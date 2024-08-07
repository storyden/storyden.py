# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from Storyden import Storyden, AsyncStoryden

from Storyden.types.admin import BanDeleteSuspendedResponse, BanSuspendResponse

from typing import Any, cast

import os
import pytest
import httpx
from typing_extensions import get_args
from typing import Optional
from respx import MockRouter
from Storyden import Storyden, AsyncStoryden
from tests.utils import assert_matches_type

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestBans:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_delete_suspended(self, client: Storyden) -> None:
        ban = client.admin.bans.delete_suspended(
            "Southclaws",
        )
        assert_matches_type(BanDeleteSuspendedResponse, ban, path=["response"])

    @parametrize
    def test_raw_response_delete_suspended(self, client: Storyden) -> None:
        response = client.admin.bans.with_raw_response.delete_suspended(
            "Southclaws",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        ban = response.parse()
        assert_matches_type(BanDeleteSuspendedResponse, ban, path=["response"])

    @parametrize
    def test_streaming_response_delete_suspended(self, client: Storyden) -> None:
        with client.admin.bans.with_streaming_response.delete_suspended(
            "Southclaws",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            ban = response.parse()
            assert_matches_type(BanDeleteSuspendedResponse, ban, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_delete_suspended(self, client: Storyden) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_handle` but received ''"):
            client.admin.bans.with_raw_response.delete_suspended(
                "",
            )

    @parametrize
    def test_method_suspend(self, client: Storyden) -> None:
        ban = client.admin.bans.suspend(
            "Southclaws",
        )
        assert_matches_type(BanSuspendResponse, ban, path=["response"])

    @parametrize
    def test_raw_response_suspend(self, client: Storyden) -> None:
        response = client.admin.bans.with_raw_response.suspend(
            "Southclaws",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        ban = response.parse()
        assert_matches_type(BanSuspendResponse, ban, path=["response"])

    @parametrize
    def test_streaming_response_suspend(self, client: Storyden) -> None:
        with client.admin.bans.with_streaming_response.suspend(
            "Southclaws",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            ban = response.parse()
            assert_matches_type(BanSuspendResponse, ban, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_suspend(self, client: Storyden) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_handle` but received ''"):
            client.admin.bans.with_raw_response.suspend(
                "",
            )


class TestAsyncBans:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    async def test_method_delete_suspended(self, async_client: AsyncStoryden) -> None:
        ban = await async_client.admin.bans.delete_suspended(
            "Southclaws",
        )
        assert_matches_type(BanDeleteSuspendedResponse, ban, path=["response"])

    @parametrize
    async def test_raw_response_delete_suspended(self, async_client: AsyncStoryden) -> None:
        response = await async_client.admin.bans.with_raw_response.delete_suspended(
            "Southclaws",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        ban = await response.parse()
        assert_matches_type(BanDeleteSuspendedResponse, ban, path=["response"])

    @parametrize
    async def test_streaming_response_delete_suspended(self, async_client: AsyncStoryden) -> None:
        async with async_client.admin.bans.with_streaming_response.delete_suspended(
            "Southclaws",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            ban = await response.parse()
            assert_matches_type(BanDeleteSuspendedResponse, ban, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_delete_suspended(self, async_client: AsyncStoryden) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_handle` but received ''"):
            await async_client.admin.bans.with_raw_response.delete_suspended(
                "",
            )

    @parametrize
    async def test_method_suspend(self, async_client: AsyncStoryden) -> None:
        ban = await async_client.admin.bans.suspend(
            "Southclaws",
        )
        assert_matches_type(BanSuspendResponse, ban, path=["response"])

    @parametrize
    async def test_raw_response_suspend(self, async_client: AsyncStoryden) -> None:
        response = await async_client.admin.bans.with_raw_response.suspend(
            "Southclaws",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        ban = await response.parse()
        assert_matches_type(BanSuspendResponse, ban, path=["response"])

    @parametrize
    async def test_streaming_response_suspend(self, async_client: AsyncStoryden) -> None:
        async with async_client.admin.bans.with_streaming_response.suspend(
            "Southclaws",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            ban = await response.parse()
            assert_matches_type(BanSuspendResponse, ban, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_suspend(self, async_client: AsyncStoryden) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_handle` but received ''"):
            await async_client.admin.bans.with_raw_response.suspend(
                "",
            )
