# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from Storyden import Storyden, AsyncStoryden

from Storyden.types.nodes import AssetAddResponse, AssetRemoveResponse

from typing import Any, cast

import os
import pytest
import httpx
from typing_extensions import get_args
from typing import Optional
from respx import MockRouter
from Storyden import Storyden, AsyncStoryden
from tests.utils import assert_matches_type
from Storyden.types.nodes import asset_add_params

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestAssets:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_add(self, client: Storyden) -> None:
        asset = client.nodes.assets.add(
            asset_id="asset_id",
            node_slug="cc5lnd2s1s4652adtu50",
        )
        assert_matches_type(AssetAddResponse, asset, path=["response"])

    @parametrize
    def test_method_add_with_all_params(self, client: Storyden) -> None:
        asset = client.nodes.assets.add(
            asset_id="asset_id",
            node_slug="cc5lnd2s1s4652adtu50",
            content_fill_rule="replace",
            node_content_fill_target="cc5lnd2s1s4652adtu50",
        )
        assert_matches_type(AssetAddResponse, asset, path=["response"])

    @parametrize
    def test_raw_response_add(self, client: Storyden) -> None:
        response = client.nodes.assets.with_raw_response.add(
            asset_id="asset_id",
            node_slug="cc5lnd2s1s4652adtu50",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        asset = response.parse()
        assert_matches_type(AssetAddResponse, asset, path=["response"])

    @parametrize
    def test_streaming_response_add(self, client: Storyden) -> None:
        with client.nodes.assets.with_streaming_response.add(
            asset_id="asset_id",
            node_slug="cc5lnd2s1s4652adtu50",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            asset = response.parse()
            assert_matches_type(AssetAddResponse, asset, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_add(self, client: Storyden) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `node_slug` but received ''"):
            client.nodes.assets.with_raw_response.add(
                asset_id="asset_id",
                node_slug="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `asset_id` but received ''"):
            client.nodes.assets.with_raw_response.add(
                asset_id="",
                node_slug="cc5lnd2s1s4652adtu50",
            )

    @parametrize
    def test_method_remove(self, client: Storyden) -> None:
        asset = client.nodes.assets.remove(
            asset_id="asset_id",
            node_slug="cc5lnd2s1s4652adtu50",
        )
        assert_matches_type(AssetRemoveResponse, asset, path=["response"])

    @parametrize
    def test_raw_response_remove(self, client: Storyden) -> None:
        response = client.nodes.assets.with_raw_response.remove(
            asset_id="asset_id",
            node_slug="cc5lnd2s1s4652adtu50",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        asset = response.parse()
        assert_matches_type(AssetRemoveResponse, asset, path=["response"])

    @parametrize
    def test_streaming_response_remove(self, client: Storyden) -> None:
        with client.nodes.assets.with_streaming_response.remove(
            asset_id="asset_id",
            node_slug="cc5lnd2s1s4652adtu50",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            asset = response.parse()
            assert_matches_type(AssetRemoveResponse, asset, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_remove(self, client: Storyden) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `node_slug` but received ''"):
            client.nodes.assets.with_raw_response.remove(
                asset_id="asset_id",
                node_slug="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `asset_id` but received ''"):
            client.nodes.assets.with_raw_response.remove(
                asset_id="",
                node_slug="cc5lnd2s1s4652adtu50",
            )


class TestAsyncAssets:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    async def test_method_add(self, async_client: AsyncStoryden) -> None:
        asset = await async_client.nodes.assets.add(
            asset_id="asset_id",
            node_slug="cc5lnd2s1s4652adtu50",
        )
        assert_matches_type(AssetAddResponse, asset, path=["response"])

    @parametrize
    async def test_method_add_with_all_params(self, async_client: AsyncStoryden) -> None:
        asset = await async_client.nodes.assets.add(
            asset_id="asset_id",
            node_slug="cc5lnd2s1s4652adtu50",
            content_fill_rule="replace",
            node_content_fill_target="cc5lnd2s1s4652adtu50",
        )
        assert_matches_type(AssetAddResponse, asset, path=["response"])

    @parametrize
    async def test_raw_response_add(self, async_client: AsyncStoryden) -> None:
        response = await async_client.nodes.assets.with_raw_response.add(
            asset_id="asset_id",
            node_slug="cc5lnd2s1s4652adtu50",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        asset = await response.parse()
        assert_matches_type(AssetAddResponse, asset, path=["response"])

    @parametrize
    async def test_streaming_response_add(self, async_client: AsyncStoryden) -> None:
        async with async_client.nodes.assets.with_streaming_response.add(
            asset_id="asset_id",
            node_slug="cc5lnd2s1s4652adtu50",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            asset = await response.parse()
            assert_matches_type(AssetAddResponse, asset, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_add(self, async_client: AsyncStoryden) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `node_slug` but received ''"):
            await async_client.nodes.assets.with_raw_response.add(
                asset_id="asset_id",
                node_slug="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `asset_id` but received ''"):
            await async_client.nodes.assets.with_raw_response.add(
                asset_id="",
                node_slug="cc5lnd2s1s4652adtu50",
            )

    @parametrize
    async def test_method_remove(self, async_client: AsyncStoryden) -> None:
        asset = await async_client.nodes.assets.remove(
            asset_id="asset_id",
            node_slug="cc5lnd2s1s4652adtu50",
        )
        assert_matches_type(AssetRemoveResponse, asset, path=["response"])

    @parametrize
    async def test_raw_response_remove(self, async_client: AsyncStoryden) -> None:
        response = await async_client.nodes.assets.with_raw_response.remove(
            asset_id="asset_id",
            node_slug="cc5lnd2s1s4652adtu50",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        asset = await response.parse()
        assert_matches_type(AssetRemoveResponse, asset, path=["response"])

    @parametrize
    async def test_streaming_response_remove(self, async_client: AsyncStoryden) -> None:
        async with async_client.nodes.assets.with_streaming_response.remove(
            asset_id="asset_id",
            node_slug="cc5lnd2s1s4652adtu50",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            asset = await response.parse()
            assert_matches_type(AssetRemoveResponse, asset, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_remove(self, async_client: AsyncStoryden) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `node_slug` but received ''"):
            await async_client.nodes.assets.with_raw_response.remove(
                asset_id="asset_id",
                node_slug="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `asset_id` but received ''"):
            await async_client.nodes.assets.with_raw_response.remove(
                asset_id="",
                node_slug="cc5lnd2s1s4652adtu50",
            )
