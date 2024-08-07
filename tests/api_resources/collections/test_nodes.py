# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from Storyden import Storyden, AsyncStoryden

from Storyden.types.collections import NodeAddResponse, NodeRemoveResponse

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


class TestNodes:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_add(self, client: Storyden) -> None:
        node = client.collections.nodes.add(
            node_id="cc5lnd2s1s4652adtu50",
            collection_id="cc5lnd2s1s4652adtu50",
        )
        assert_matches_type(NodeAddResponse, node, path=["response"])

    @parametrize
    def test_raw_response_add(self, client: Storyden) -> None:
        response = client.collections.nodes.with_raw_response.add(
            node_id="cc5lnd2s1s4652adtu50",
            collection_id="cc5lnd2s1s4652adtu50",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        node = response.parse()
        assert_matches_type(NodeAddResponse, node, path=["response"])

    @parametrize
    def test_streaming_response_add(self, client: Storyden) -> None:
        with client.collections.nodes.with_streaming_response.add(
            node_id="cc5lnd2s1s4652adtu50",
            collection_id="cc5lnd2s1s4652adtu50",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            node = response.parse()
            assert_matches_type(NodeAddResponse, node, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_add(self, client: Storyden) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `collection_id` but received ''"):
            client.collections.nodes.with_raw_response.add(
                node_id="cc5lnd2s1s4652adtu50",
                collection_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `node_id` but received ''"):
            client.collections.nodes.with_raw_response.add(
                node_id="",
                collection_id="cc5lnd2s1s4652adtu50",
            )

    @parametrize
    def test_method_remove(self, client: Storyden) -> None:
        node = client.collections.nodes.remove(
            node_id="cc5lnd2s1s4652adtu50",
            collection_id="cc5lnd2s1s4652adtu50",
        )
        assert_matches_type(NodeRemoveResponse, node, path=["response"])

    @parametrize
    def test_raw_response_remove(self, client: Storyden) -> None:
        response = client.collections.nodes.with_raw_response.remove(
            node_id="cc5lnd2s1s4652adtu50",
            collection_id="cc5lnd2s1s4652adtu50",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        node = response.parse()
        assert_matches_type(NodeRemoveResponse, node, path=["response"])

    @parametrize
    def test_streaming_response_remove(self, client: Storyden) -> None:
        with client.collections.nodes.with_streaming_response.remove(
            node_id="cc5lnd2s1s4652adtu50",
            collection_id="cc5lnd2s1s4652adtu50",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            node = response.parse()
            assert_matches_type(NodeRemoveResponse, node, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_remove(self, client: Storyden) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `collection_id` but received ''"):
            client.collections.nodes.with_raw_response.remove(
                node_id="cc5lnd2s1s4652adtu50",
                collection_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `node_id` but received ''"):
            client.collections.nodes.with_raw_response.remove(
                node_id="",
                collection_id="cc5lnd2s1s4652adtu50",
            )


class TestAsyncNodes:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    async def test_method_add(self, async_client: AsyncStoryden) -> None:
        node = await async_client.collections.nodes.add(
            node_id="cc5lnd2s1s4652adtu50",
            collection_id="cc5lnd2s1s4652adtu50",
        )
        assert_matches_type(NodeAddResponse, node, path=["response"])

    @parametrize
    async def test_raw_response_add(self, async_client: AsyncStoryden) -> None:
        response = await async_client.collections.nodes.with_raw_response.add(
            node_id="cc5lnd2s1s4652adtu50",
            collection_id="cc5lnd2s1s4652adtu50",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        node = await response.parse()
        assert_matches_type(NodeAddResponse, node, path=["response"])

    @parametrize
    async def test_streaming_response_add(self, async_client: AsyncStoryden) -> None:
        async with async_client.collections.nodes.with_streaming_response.add(
            node_id="cc5lnd2s1s4652adtu50",
            collection_id="cc5lnd2s1s4652adtu50",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            node = await response.parse()
            assert_matches_type(NodeAddResponse, node, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_add(self, async_client: AsyncStoryden) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `collection_id` but received ''"):
            await async_client.collections.nodes.with_raw_response.add(
                node_id="cc5lnd2s1s4652adtu50",
                collection_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `node_id` but received ''"):
            await async_client.collections.nodes.with_raw_response.add(
                node_id="",
                collection_id="cc5lnd2s1s4652adtu50",
            )

    @parametrize
    async def test_method_remove(self, async_client: AsyncStoryden) -> None:
        node = await async_client.collections.nodes.remove(
            node_id="cc5lnd2s1s4652adtu50",
            collection_id="cc5lnd2s1s4652adtu50",
        )
        assert_matches_type(NodeRemoveResponse, node, path=["response"])

    @parametrize
    async def test_raw_response_remove(self, async_client: AsyncStoryden) -> None:
        response = await async_client.collections.nodes.with_raw_response.remove(
            node_id="cc5lnd2s1s4652adtu50",
            collection_id="cc5lnd2s1s4652adtu50",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        node = await response.parse()
        assert_matches_type(NodeRemoveResponse, node, path=["response"])

    @parametrize
    async def test_streaming_response_remove(self, async_client: AsyncStoryden) -> None:
        async with async_client.collections.nodes.with_streaming_response.remove(
            node_id="cc5lnd2s1s4652adtu50",
            collection_id="cc5lnd2s1s4652adtu50",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            node = await response.parse()
            assert_matches_type(NodeRemoveResponse, node, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_remove(self, async_client: AsyncStoryden) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `collection_id` but received ''"):
            await async_client.collections.nodes.with_raw_response.remove(
                node_id="cc5lnd2s1s4652adtu50",
                collection_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `node_id` but received ''"):
            await async_client.collections.nodes.with_raw_response.remove(
                node_id="",
                collection_id="cc5lnd2s1s4652adtu50",
            )
