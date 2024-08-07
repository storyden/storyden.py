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
from Storyden.types.misc.info import icon_create_params

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestIcon:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_create(self, client: Storyden) -> None:
        icon = client.misc.info.icon.create(
            body=b"raw file contents",
        )
        assert icon is None

    @parametrize
    def test_raw_response_create(self, client: Storyden) -> None:
        response = client.misc.info.icon.with_raw_response.create(
            body=b"raw file contents",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        icon = response.parse()
        assert icon is None

    @parametrize
    def test_streaming_response_create(self, client: Storyden) -> None:
        with client.misc.info.icon.with_streaming_response.create(
            body=b"raw file contents",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            icon = response.parse()
            assert icon is None

        assert cast(Any, response.is_closed) is True

    @parametrize
    @pytest.mark.respx(base_url=base_url)
    def test_method_retrieve(self, client: Storyden, respx_mock: MockRouter) -> None:
        respx_mock.get("/v1/info/icon/512x512").mock(return_value=httpx.Response(200, json={"foo": "bar"}))
        icon = client.misc.info.icon.retrieve(
            "512x512",
        )
        assert icon.is_closed
        assert icon.json() == {"foo": "bar"}
        assert cast(Any, icon.is_closed) is True
        assert isinstance(icon, BinaryAPIResponse)

    @parametrize
    @pytest.mark.respx(base_url=base_url)
    def test_raw_response_retrieve(self, client: Storyden, respx_mock: MockRouter) -> None:
        respx_mock.get("/v1/info/icon/512x512").mock(return_value=httpx.Response(200, json={"foo": "bar"}))

        icon = client.misc.info.icon.with_raw_response.retrieve(
            "512x512",
        )

        assert icon.is_closed is True
        assert icon.http_request.headers.get("X-Stainless-Lang") == "python"
        assert icon.json() == {"foo": "bar"}
        assert isinstance(icon, BinaryAPIResponse)

    @parametrize
    @pytest.mark.respx(base_url=base_url)
    def test_streaming_response_retrieve(self, client: Storyden, respx_mock: MockRouter) -> None:
        respx_mock.get("/v1/info/icon/512x512").mock(return_value=httpx.Response(200, json={"foo": "bar"}))
        with client.misc.info.icon.with_streaming_response.retrieve(
            "512x512",
        ) as icon:
            assert not icon.is_closed
            assert icon.http_request.headers.get("X-Stainless-Lang") == "python"

            assert icon.json() == {"foo": "bar"}
            assert cast(Any, icon.is_closed) is True
            assert isinstance(icon, StreamedBinaryAPIResponse)

        assert cast(Any, icon.is_closed) is True


class TestAsyncIcon:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    async def test_method_create(self, async_client: AsyncStoryden) -> None:
        icon = await async_client.misc.info.icon.create(
            body=b"raw file contents",
        )
        assert icon is None

    @parametrize
    async def test_raw_response_create(self, async_client: AsyncStoryden) -> None:
        response = await async_client.misc.info.icon.with_raw_response.create(
            body=b"raw file contents",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        icon = await response.parse()
        assert icon is None

    @parametrize
    async def test_streaming_response_create(self, async_client: AsyncStoryden) -> None:
        async with async_client.misc.info.icon.with_streaming_response.create(
            body=b"raw file contents",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            icon = await response.parse()
            assert icon is None

        assert cast(Any, response.is_closed) is True

    @parametrize
    @pytest.mark.respx(base_url=base_url)
    async def test_method_retrieve(self, async_client: AsyncStoryden, respx_mock: MockRouter) -> None:
        respx_mock.get("/v1/info/icon/512x512").mock(return_value=httpx.Response(200, json={"foo": "bar"}))
        icon = await async_client.misc.info.icon.retrieve(
            "512x512",
        )
        assert icon.is_closed
        assert await icon.json() == {"foo": "bar"}
        assert cast(Any, icon.is_closed) is True
        assert isinstance(icon, AsyncBinaryAPIResponse)

    @parametrize
    @pytest.mark.respx(base_url=base_url)
    async def test_raw_response_retrieve(self, async_client: AsyncStoryden, respx_mock: MockRouter) -> None:
        respx_mock.get("/v1/info/icon/512x512").mock(return_value=httpx.Response(200, json={"foo": "bar"}))

        icon = await async_client.misc.info.icon.with_raw_response.retrieve(
            "512x512",
        )

        assert icon.is_closed is True
        assert icon.http_request.headers.get("X-Stainless-Lang") == "python"
        assert await icon.json() == {"foo": "bar"}
        assert isinstance(icon, AsyncBinaryAPIResponse)

    @parametrize
    @pytest.mark.respx(base_url=base_url)
    async def test_streaming_response_retrieve(self, async_client: AsyncStoryden, respx_mock: MockRouter) -> None:
        respx_mock.get("/v1/info/icon/512x512").mock(return_value=httpx.Response(200, json={"foo": "bar"}))
        async with async_client.misc.info.icon.with_streaming_response.retrieve(
            "512x512",
        ) as icon:
            assert not icon.is_closed
            assert icon.http_request.headers.get("X-Stainless-Lang") == "python"

            assert await icon.json() == {"foo": "bar"}
            assert cast(Any, icon.is_closed) is True
            assert isinstance(icon, AsyncStreamedBinaryAPIResponse)

        assert cast(Any, icon.is_closed) is True
