# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import httpx
import pytest
from respx import MockRouter

from storyden import Storyden, AsyncStoryden
from storyden._response import (
    BinaryAPIResponse,
    AsyncBinaryAPIResponse,
    StreamedBinaryAPIResponse,
    AsyncStreamedBinaryAPIResponse,
)

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestAvatar:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_create(self, client: Storyden) -> None:
        avatar = client.v1.accounts.avatar.create(
            body=b"raw file contents",
        )
        assert avatar is None

    @parametrize
    def test_raw_response_create(self, client: Storyden) -> None:
        response = client.v1.accounts.avatar.with_raw_response.create(
            body=b"raw file contents",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        avatar = response.parse()
        assert avatar is None

    @parametrize
    def test_streaming_response_create(self, client: Storyden) -> None:
        with client.v1.accounts.avatar.with_streaming_response.create(
            body=b"raw file contents",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            avatar = response.parse()
            assert avatar is None

        assert cast(Any, response.is_closed) is True

    @parametrize
    @pytest.mark.respx(base_url=base_url)
    def test_method_retrieve(self, client: Storyden, respx_mock: MockRouter) -> None:
        respx_mock.get("/v1/accounts/southclaws/avatar").mock(return_value=httpx.Response(200, json={"foo": "bar"}))
        avatar = client.v1.accounts.avatar.retrieve(
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

        avatar = client.v1.accounts.avatar.with_raw_response.retrieve(
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
        with client.v1.accounts.avatar.with_streaming_response.retrieve(
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
            client.v1.accounts.avatar.with_raw_response.retrieve(
                "",
            )


class TestAsyncAvatar:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    async def test_method_create(self, async_client: AsyncStoryden) -> None:
        avatar = await async_client.v1.accounts.avatar.create(
            body=b"raw file contents",
        )
        assert avatar is None

    @parametrize
    async def test_raw_response_create(self, async_client: AsyncStoryden) -> None:
        response = await async_client.v1.accounts.avatar.with_raw_response.create(
            body=b"raw file contents",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        avatar = await response.parse()
        assert avatar is None

    @parametrize
    async def test_streaming_response_create(self, async_client: AsyncStoryden) -> None:
        async with async_client.v1.accounts.avatar.with_streaming_response.create(
            body=b"raw file contents",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            avatar = await response.parse()
            assert avatar is None

        assert cast(Any, response.is_closed) is True

    @parametrize
    @pytest.mark.respx(base_url=base_url)
    async def test_method_retrieve(self, async_client: AsyncStoryden, respx_mock: MockRouter) -> None:
        respx_mock.get("/v1/accounts/southclaws/avatar").mock(return_value=httpx.Response(200, json={"foo": "bar"}))
        avatar = await async_client.v1.accounts.avatar.retrieve(
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

        avatar = await async_client.v1.accounts.avatar.with_raw_response.retrieve(
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
        async with async_client.v1.accounts.avatar.with_streaming_response.retrieve(
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
            await async_client.v1.accounts.avatar.with_raw_response.retrieve(
                "",
            )
