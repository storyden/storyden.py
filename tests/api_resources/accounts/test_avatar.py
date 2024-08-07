# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from Storyden import Storyden, AsyncStoryden

from typing import Any, cast

from Storyden._response import (
    BinaryAPIResponse,
    StreamedBinaryAPIResponse,
    AsyncBinaryAPIResponse,
    AsyncStreamedBinaryAPIResponse,
)

import os
import pytest
import httpx
from typing_extensions import get_args
from typing import Optional
from respx import MockRouter
from Storyden import Storyden, AsyncStoryden
from tests.utils import assert_matches_type

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestAvatar:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    @pytest.mark.respx(base_url=base_url)
    def test_method_retrieve(self, client: Storyden, respx_mock: MockRouter) -> None:
        respx_mock.get("/v1/accounts/southclaws/avatar").mock(return_value=httpx.Response(200, json={"foo": "bar"}))
        avatar = client.accounts.avatar.retrieve(
            "Southclaws",
        )
        assert avatar.is_closed
        assert avatar.json() == {"foo": "bar"}
        assert cast(Any, avatar.is_closed) is True
        assert isinstance(avatar, BinaryAPIResponse)

    @parametrize
    @pytest.mark.respx(base_url=base_url)
    def test_raw_response_retrieve(self, client: Storyden, respx_mock: MockRouter) -> None:
        respx_mock.get("/v1/accounts/southclaws/avatar").mock(return_value=httpx.Response(200, json={"foo": "bar"}))

        avatar = client.accounts.avatar.with_raw_response.retrieve(
            "Southclaws",
        )

        assert avatar.is_closed is True
        assert avatar.http_request.headers.get("X-Stainless-Lang") == "python"
        assert avatar.json() == {"foo": "bar"}
        assert isinstance(avatar, BinaryAPIResponse)

    @parametrize
    @pytest.mark.respx(base_url=base_url)
    def test_streaming_response_retrieve(self, client: Storyden, respx_mock: MockRouter) -> None:
        respx_mock.get("/v1/accounts/southclaws/avatar").mock(return_value=httpx.Response(200, json={"foo": "bar"}))
        with client.accounts.avatar.with_streaming_response.retrieve(
            "Southclaws",
        ) as avatar:
            assert not avatar.is_closed
            assert avatar.http_request.headers.get("X-Stainless-Lang") == "python"

            assert avatar.json() == {"foo": "bar"}
            assert cast(Any, avatar.is_closed) is True
            assert isinstance(avatar, StreamedBinaryAPIResponse)

        assert cast(Any, avatar.is_closed) is True

    @parametrize
    @pytest.mark.respx(base_url=base_url)
    def test_path_params_retrieve(self, client: Storyden) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_handle` but received ''"):
            client.accounts.avatar.with_raw_response.retrieve(
                "",
            )


class TestAsyncAvatar:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    @pytest.mark.respx(base_url=base_url)
    async def test_method_retrieve(self, async_client: AsyncStoryden, respx_mock: MockRouter) -> None:
        respx_mock.get("/v1/accounts/southclaws/avatar").mock(return_value=httpx.Response(200, json={"foo": "bar"}))
        avatar = await async_client.accounts.avatar.retrieve(
            "Southclaws",
        )
        assert avatar.is_closed
        assert await avatar.json() == {"foo": "bar"}
        assert cast(Any, avatar.is_closed) is True
        assert isinstance(avatar, AsyncBinaryAPIResponse)

    @parametrize
    @pytest.mark.respx(base_url=base_url)
    async def test_raw_response_retrieve(self, async_client: AsyncStoryden, respx_mock: MockRouter) -> None:
        respx_mock.get("/v1/accounts/southclaws/avatar").mock(return_value=httpx.Response(200, json={"foo": "bar"}))

        avatar = await async_client.accounts.avatar.with_raw_response.retrieve(
            "Southclaws",
        )

        assert avatar.is_closed is True
        assert avatar.http_request.headers.get("X-Stainless-Lang") == "python"
        assert await avatar.json() == {"foo": "bar"}
        assert isinstance(avatar, AsyncBinaryAPIResponse)

    @parametrize
    @pytest.mark.respx(base_url=base_url)
    async def test_streaming_response_retrieve(self, async_client: AsyncStoryden, respx_mock: MockRouter) -> None:
        respx_mock.get("/v1/accounts/southclaws/avatar").mock(return_value=httpx.Response(200, json={"foo": "bar"}))
        async with async_client.accounts.avatar.with_streaming_response.retrieve(
            "Southclaws",
        ) as avatar:
            assert not avatar.is_closed
            assert avatar.http_request.headers.get("X-Stainless-Lang") == "python"

            assert await avatar.json() == {"foo": "bar"}
            assert cast(Any, avatar.is_closed) is True
            assert isinstance(avatar, AsyncStreamedBinaryAPIResponse)

        assert cast(Any, avatar.is_closed) is True

    @parametrize
    @pytest.mark.respx(base_url=base_url)
    async def test_path_params_retrieve(self, async_client: AsyncStoryden) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_handle` but received ''"):
            await async_client.accounts.avatar.with_raw_response.retrieve(
                "",
            )
