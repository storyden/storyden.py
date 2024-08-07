# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import httpx
import pytest
from respx import MockRouter

from storyden import Storyden, AsyncStoryden
from tests.utils import assert_matches_type
from storyden.types import AssetCreateResponse
from storyden._response import (
    BinaryAPIResponse,
    AsyncBinaryAPIResponse,
    StreamedBinaryAPIResponse,
    AsyncStreamedBinaryAPIResponse,
)

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestAssets:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_create(self, client: Storyden) -> None:
        asset = client.assets.create(
            body=b"raw file contents",
        )
        assert_matches_type(AssetCreateResponse, asset, path=["response"])

    @parametrize
    def test_method_create_with_all_params(self, client: Storyden) -> None:
        asset = client.assets.create(
            body=b"raw file contents",
            content_fill_rule="replace",
            filename="filename",
            node_content_fill_target="cc5lnd2s1s4652adtu50",
        )
        assert_matches_type(AssetCreateResponse, asset, path=["response"])

    @parametrize
    def test_raw_response_create(self, client: Storyden) -> None:
        response = client.assets.with_raw_response.create(
            body=b"raw file contents",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        asset = response.parse()
        assert_matches_type(AssetCreateResponse, asset, path=["response"])

    @parametrize
    def test_streaming_response_create(self, client: Storyden) -> None:
        with client.assets.with_streaming_response.create(
            body=b"raw file contents",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            asset = response.parse()
            assert_matches_type(AssetCreateResponse, asset, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    @pytest.mark.respx(base_url=base_url)
    def test_method_retrieve(self, client: Storyden, respx_mock: MockRouter) -> None:
        respx_mock.get("/v1/assets/asset_filename").mock(return_value=httpx.Response(200, json={"foo": "bar"}))
        asset = client.assets.retrieve(
            "asset_filename",
        )
        assert asset.is_closed
        assert asset.json() == {"foo": "bar"}
        assert cast(Any, asset.is_closed) is True
        assert isinstance(asset, BinaryAPIResponse)

    @parametrize
    @pytest.mark.respx(base_url=base_url)
    def test_raw_response_retrieve(self, client: Storyden, respx_mock: MockRouter) -> None:
        respx_mock.get("/v1/assets/asset_filename").mock(return_value=httpx.Response(200, json={"foo": "bar"}))

        asset = client.assets.with_raw_response.retrieve(
            "asset_filename",
        )

        assert asset.is_closed is True
        assert asset.http_request.headers.get("X-Stainless-Lang") == "python"
        assert asset.json() == {"foo": "bar"}
        assert isinstance(asset, BinaryAPIResponse)

    @parametrize
    @pytest.mark.respx(base_url=base_url)
    def test_streaming_response_retrieve(self, client: Storyden, respx_mock: MockRouter) -> None:
        respx_mock.get("/v1/assets/asset_filename").mock(return_value=httpx.Response(200, json={"foo": "bar"}))
        with client.assets.with_streaming_response.retrieve(
            "asset_filename",
        ) as asset:
            assert not asset.is_closed
            assert asset.http_request.headers.get("X-Stainless-Lang") == "python"

            assert asset.json() == {"foo": "bar"}
            assert cast(Any, asset.is_closed) is True
            assert isinstance(asset, StreamedBinaryAPIResponse)

        assert cast(Any, asset.is_closed) is True

    @parametrize
    @pytest.mark.respx(base_url=base_url)
    def test_path_params_retrieve(self, client: Storyden) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `asset_filename` but received ''"):
            client.assets.with_raw_response.retrieve(
                "",
            )


class TestAsyncAssets:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    async def test_method_create(self, async_client: AsyncStoryden) -> None:
        asset = await async_client.assets.create(
            body=b"raw file contents",
        )
        assert_matches_type(AssetCreateResponse, asset, path=["response"])

    @parametrize
    async def test_method_create_with_all_params(self, async_client: AsyncStoryden) -> None:
        asset = await async_client.assets.create(
            body=b"raw file contents",
            content_fill_rule="replace",
            filename="filename",
            node_content_fill_target="cc5lnd2s1s4652adtu50",
        )
        assert_matches_type(AssetCreateResponse, asset, path=["response"])

    @parametrize
    async def test_raw_response_create(self, async_client: AsyncStoryden) -> None:
        response = await async_client.assets.with_raw_response.create(
            body=b"raw file contents",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        asset = await response.parse()
        assert_matches_type(AssetCreateResponse, asset, path=["response"])

    @parametrize
    async def test_streaming_response_create(self, async_client: AsyncStoryden) -> None:
        async with async_client.assets.with_streaming_response.create(
            body=b"raw file contents",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            asset = await response.parse()
            assert_matches_type(AssetCreateResponse, asset, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    @pytest.mark.respx(base_url=base_url)
    async def test_method_retrieve(self, async_client: AsyncStoryden, respx_mock: MockRouter) -> None:
        respx_mock.get("/v1/assets/asset_filename").mock(return_value=httpx.Response(200, json={"foo": "bar"}))
        asset = await async_client.assets.retrieve(
            "asset_filename",
        )
        assert asset.is_closed
        assert await asset.json() == {"foo": "bar"}
        assert cast(Any, asset.is_closed) is True
        assert isinstance(asset, AsyncBinaryAPIResponse)

    @parametrize
    @pytest.mark.respx(base_url=base_url)
    async def test_raw_response_retrieve(self, async_client: AsyncStoryden, respx_mock: MockRouter) -> None:
        respx_mock.get("/v1/assets/asset_filename").mock(return_value=httpx.Response(200, json={"foo": "bar"}))

        asset = await async_client.assets.with_raw_response.retrieve(
            "asset_filename",
        )

        assert asset.is_closed is True
        assert asset.http_request.headers.get("X-Stainless-Lang") == "python"
        assert await asset.json() == {"foo": "bar"}
        assert isinstance(asset, AsyncBinaryAPIResponse)

    @parametrize
    @pytest.mark.respx(base_url=base_url)
    async def test_streaming_response_retrieve(self, async_client: AsyncStoryden, respx_mock: MockRouter) -> None:
        respx_mock.get("/v1/assets/asset_filename").mock(return_value=httpx.Response(200, json={"foo": "bar"}))
        async with async_client.assets.with_streaming_response.retrieve(
            "asset_filename",
        ) as asset:
            assert not asset.is_closed
            assert asset.http_request.headers.get("X-Stainless-Lang") == "python"

            assert await asset.json() == {"foo": "bar"}
            assert cast(Any, asset.is_closed) is True
            assert isinstance(asset, AsyncStreamedBinaryAPIResponse)

        assert cast(Any, asset.is_closed) is True

    @parametrize
    @pytest.mark.respx(base_url=base_url)
    async def test_path_params_retrieve(self, async_client: AsyncStoryden) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `asset_filename` but received ''"):
            await async_client.assets.with_raw_response.retrieve(
                "",
            )
