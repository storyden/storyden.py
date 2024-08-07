# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from Storyden import Storyden, AsyncStoryden

from typing import Any, cast

import os
import pytest
import httpx
from typing_extensions import get_args
from typing import Optional
from respx import MockRouter
from Storyden import Storyden, AsyncStoryden
from tests.utils import assert_matches_type
from Storyden.types.accounts.self import avatar_create_params

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestAvatar:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_create(self, client: Storyden) -> None:
        avatar = client.accounts.self.avatar.create(
            body=b"raw file contents",
        )
        assert avatar is None

    @parametrize
    def test_raw_response_create(self, client: Storyden) -> None:
        response = client.accounts.self.avatar.with_raw_response.create(
            body=b"raw file contents",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        avatar = response.parse()
        assert avatar is None

    @parametrize
    def test_streaming_response_create(self, client: Storyden) -> None:
        with client.accounts.self.avatar.with_streaming_response.create(
            body=b"raw file contents",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            avatar = response.parse()
            assert avatar is None

        assert cast(Any, response.is_closed) is True


class TestAsyncAvatar:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    async def test_method_create(self, async_client: AsyncStoryden) -> None:
        avatar = await async_client.accounts.self.avatar.create(
            body=b"raw file contents",
        )
        assert avatar is None

    @parametrize
    async def test_raw_response_create(self, async_client: AsyncStoryden) -> None:
        response = await async_client.accounts.self.avatar.with_raw_response.create(
            body=b"raw file contents",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        avatar = await response.parse()
        assert avatar is None

    @parametrize
    async def test_streaming_response_create(self, async_client: AsyncStoryden) -> None:
        async with async_client.accounts.self.avatar.with_streaming_response.create(
            body=b"raw file contents",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            avatar = await response.parse()
            assert avatar is None

        assert cast(Any, response.is_closed) is True
