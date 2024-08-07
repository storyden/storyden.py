# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from Storyden import Storyden, AsyncStoryden

from Storyden.types import (
    NodeCreateResponse,
    NodeRetrieveResponse,
    NodeUpdateResponse,
    NodeListResponse,
    NodeDeleteResponse,
)

from typing import Any, cast

import os
import pytest
import httpx
from typing_extensions import get_args
from typing import Optional
from respx import MockRouter
from Storyden import Storyden, AsyncStoryden
from tests.utils import assert_matches_type
from Storyden.types import node_create_params
from Storyden.types import node_update_params
from Storyden.types import node_list_params
from Storyden.types import node_delete_params

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestNodes:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_create(self, client: Storyden) -> None:
        node = client.nodes.create(
            name="name",
        )
        assert_matches_type(NodeCreateResponse, node, path=["response"])

    @parametrize
    def test_method_create_with_all_params(self, client: Storyden) -> None:
        node = client.nodes.create(
            name="name",
            asset_ids=["cc5lnd2s1s4652adtu50", "cc5lnd2s1s4652adtu50", "cc5lnd2s1s4652adtu50"],
            asset_sources=["string", "string", "string"],
            content="content",
            meta={"foo": "bar"},
            parent="parent",
            slug="slug",
            url="url",
            visibility="draft",
        )
        assert_matches_type(NodeCreateResponse, node, path=["response"])

    @parametrize
    def test_raw_response_create(self, client: Storyden) -> None:
        response = client.nodes.with_raw_response.create(
            name="name",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        node = response.parse()
        assert_matches_type(NodeCreateResponse, node, path=["response"])

    @parametrize
    def test_streaming_response_create(self, client: Storyden) -> None:
        with client.nodes.with_streaming_response.create(
            name="name",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            node = response.parse()
            assert_matches_type(NodeCreateResponse, node, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_retrieve(self, client: Storyden) -> None:
        node = client.nodes.retrieve(
            "cc5lnd2s1s4652adtu50",
        )
        assert_matches_type(NodeRetrieveResponse, node, path=["response"])

    @parametrize
    def test_raw_response_retrieve(self, client: Storyden) -> None:
        response = client.nodes.with_raw_response.retrieve(
            "cc5lnd2s1s4652adtu50",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        node = response.parse()
        assert_matches_type(NodeRetrieveResponse, node, path=["response"])

    @parametrize
    def test_streaming_response_retrieve(self, client: Storyden) -> None:
        with client.nodes.with_streaming_response.retrieve(
            "cc5lnd2s1s4652adtu50",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            node = response.parse()
            assert_matches_type(NodeRetrieveResponse, node, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_retrieve(self, client: Storyden) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `node_slug` but received ''"):
            client.nodes.with_raw_response.retrieve(
                "",
            )

    @parametrize
    def test_method_update(self, client: Storyden) -> None:
        node = client.nodes.update(
            node_slug="cc5lnd2s1s4652adtu50",
        )
        assert_matches_type(NodeUpdateResponse, node, path=["response"])

    @parametrize
    def test_method_update_with_all_params(self, client: Storyden) -> None:
        node = client.nodes.update(
            node_slug="cc5lnd2s1s4652adtu50",
            asset_ids=["cc5lnd2s1s4652adtu50", "cc5lnd2s1s4652adtu50", "cc5lnd2s1s4652adtu50"],
            asset_sources=["string", "string", "string"],
            content="content",
            meta={"foo": "bar"},
            name="name",
            parent="parent",
            slug="slug",
            url="url",
        )
        assert_matches_type(NodeUpdateResponse, node, path=["response"])

    @parametrize
    def test_raw_response_update(self, client: Storyden) -> None:
        response = client.nodes.with_raw_response.update(
            node_slug="cc5lnd2s1s4652adtu50",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        node = response.parse()
        assert_matches_type(NodeUpdateResponse, node, path=["response"])

    @parametrize
    def test_streaming_response_update(self, client: Storyden) -> None:
        with client.nodes.with_streaming_response.update(
            node_slug="cc5lnd2s1s4652adtu50",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            node = response.parse()
            assert_matches_type(NodeUpdateResponse, node, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_update(self, client: Storyden) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `node_slug` but received ''"):
            client.nodes.with_raw_response.update(
                node_slug="",
            )

    @parametrize
    def test_method_list(self, client: Storyden) -> None:
        node = client.nodes.list()
        assert_matches_type(NodeListResponse, node, path=["response"])

    @parametrize
    def test_method_list_with_all_params(self, client: Storyden) -> None:
        node = client.nodes.list(
            author="Southclaws",
            depth="depth",
            node_id="cc5lnd2s1s4652adtu50",
            page="page",
            q="q",
            visibility=["draft", "unlisted", "review"],
        )
        assert_matches_type(NodeListResponse, node, path=["response"])

    @parametrize
    def test_raw_response_list(self, client: Storyden) -> None:
        response = client.nodes.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        node = response.parse()
        assert_matches_type(NodeListResponse, node, path=["response"])

    @parametrize
    def test_streaming_response_list(self, client: Storyden) -> None:
        with client.nodes.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            node = response.parse()
            assert_matches_type(NodeListResponse, node, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_delete(self, client: Storyden) -> None:
        node = client.nodes.delete(
            node_slug="cc5lnd2s1s4652adtu50",
        )
        assert_matches_type(NodeDeleteResponse, node, path=["response"])

    @parametrize
    def test_method_delete_with_all_params(self, client: Storyden) -> None:
        node = client.nodes.delete(
            node_slug="cc5lnd2s1s4652adtu50",
            target_node="target_node",
        )
        assert_matches_type(NodeDeleteResponse, node, path=["response"])

    @parametrize
    def test_raw_response_delete(self, client: Storyden) -> None:
        response = client.nodes.with_raw_response.delete(
            node_slug="cc5lnd2s1s4652adtu50",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        node = response.parse()
        assert_matches_type(NodeDeleteResponse, node, path=["response"])

    @parametrize
    def test_streaming_response_delete(self, client: Storyden) -> None:
        with client.nodes.with_streaming_response.delete(
            node_slug="cc5lnd2s1s4652adtu50",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            node = response.parse()
            assert_matches_type(NodeDeleteResponse, node, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_delete(self, client: Storyden) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `node_slug` but received ''"):
            client.nodes.with_raw_response.delete(
                node_slug="",
            )


class TestAsyncNodes:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    async def test_method_create(self, async_client: AsyncStoryden) -> None:
        node = await async_client.nodes.create(
            name="name",
        )
        assert_matches_type(NodeCreateResponse, node, path=["response"])

    @parametrize
    async def test_method_create_with_all_params(self, async_client: AsyncStoryden) -> None:
        node = await async_client.nodes.create(
            name="name",
            asset_ids=["cc5lnd2s1s4652adtu50", "cc5lnd2s1s4652adtu50", "cc5lnd2s1s4652adtu50"],
            asset_sources=["string", "string", "string"],
            content="content",
            meta={"foo": "bar"},
            parent="parent",
            slug="slug",
            url="url",
            visibility="draft",
        )
        assert_matches_type(NodeCreateResponse, node, path=["response"])

    @parametrize
    async def test_raw_response_create(self, async_client: AsyncStoryden) -> None:
        response = await async_client.nodes.with_raw_response.create(
            name="name",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        node = await response.parse()
        assert_matches_type(NodeCreateResponse, node, path=["response"])

    @parametrize
    async def test_streaming_response_create(self, async_client: AsyncStoryden) -> None:
        async with async_client.nodes.with_streaming_response.create(
            name="name",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            node = await response.parse()
            assert_matches_type(NodeCreateResponse, node, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_retrieve(self, async_client: AsyncStoryden) -> None:
        node = await async_client.nodes.retrieve(
            "cc5lnd2s1s4652adtu50",
        )
        assert_matches_type(NodeRetrieveResponse, node, path=["response"])

    @parametrize
    async def test_raw_response_retrieve(self, async_client: AsyncStoryden) -> None:
        response = await async_client.nodes.with_raw_response.retrieve(
            "cc5lnd2s1s4652adtu50",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        node = await response.parse()
        assert_matches_type(NodeRetrieveResponse, node, path=["response"])

    @parametrize
    async def test_streaming_response_retrieve(self, async_client: AsyncStoryden) -> None:
        async with async_client.nodes.with_streaming_response.retrieve(
            "cc5lnd2s1s4652adtu50",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            node = await response.parse()
            assert_matches_type(NodeRetrieveResponse, node, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_retrieve(self, async_client: AsyncStoryden) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `node_slug` but received ''"):
            await async_client.nodes.with_raw_response.retrieve(
                "",
            )

    @parametrize
    async def test_method_update(self, async_client: AsyncStoryden) -> None:
        node = await async_client.nodes.update(
            node_slug="cc5lnd2s1s4652adtu50",
        )
        assert_matches_type(NodeUpdateResponse, node, path=["response"])

    @parametrize
    async def test_method_update_with_all_params(self, async_client: AsyncStoryden) -> None:
        node = await async_client.nodes.update(
            node_slug="cc5lnd2s1s4652adtu50",
            asset_ids=["cc5lnd2s1s4652adtu50", "cc5lnd2s1s4652adtu50", "cc5lnd2s1s4652adtu50"],
            asset_sources=["string", "string", "string"],
            content="content",
            meta={"foo": "bar"},
            name="name",
            parent="parent",
            slug="slug",
            url="url",
        )
        assert_matches_type(NodeUpdateResponse, node, path=["response"])

    @parametrize
    async def test_raw_response_update(self, async_client: AsyncStoryden) -> None:
        response = await async_client.nodes.with_raw_response.update(
            node_slug="cc5lnd2s1s4652adtu50",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        node = await response.parse()
        assert_matches_type(NodeUpdateResponse, node, path=["response"])

    @parametrize
    async def test_streaming_response_update(self, async_client: AsyncStoryden) -> None:
        async with async_client.nodes.with_streaming_response.update(
            node_slug="cc5lnd2s1s4652adtu50",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            node = await response.parse()
            assert_matches_type(NodeUpdateResponse, node, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_update(self, async_client: AsyncStoryden) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `node_slug` but received ''"):
            await async_client.nodes.with_raw_response.update(
                node_slug="",
            )

    @parametrize
    async def test_method_list(self, async_client: AsyncStoryden) -> None:
        node = await async_client.nodes.list()
        assert_matches_type(NodeListResponse, node, path=["response"])

    @parametrize
    async def test_method_list_with_all_params(self, async_client: AsyncStoryden) -> None:
        node = await async_client.nodes.list(
            author="Southclaws",
            depth="depth",
            node_id="cc5lnd2s1s4652adtu50",
            page="page",
            q="q",
            visibility=["draft", "unlisted", "review"],
        )
        assert_matches_type(NodeListResponse, node, path=["response"])

    @parametrize
    async def test_raw_response_list(self, async_client: AsyncStoryden) -> None:
        response = await async_client.nodes.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        node = await response.parse()
        assert_matches_type(NodeListResponse, node, path=["response"])

    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncStoryden) -> None:
        async with async_client.nodes.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            node = await response.parse()
            assert_matches_type(NodeListResponse, node, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_delete(self, async_client: AsyncStoryden) -> None:
        node = await async_client.nodes.delete(
            node_slug="cc5lnd2s1s4652adtu50",
        )
        assert_matches_type(NodeDeleteResponse, node, path=["response"])

    @parametrize
    async def test_method_delete_with_all_params(self, async_client: AsyncStoryden) -> None:
        node = await async_client.nodes.delete(
            node_slug="cc5lnd2s1s4652adtu50",
            target_node="target_node",
        )
        assert_matches_type(NodeDeleteResponse, node, path=["response"])

    @parametrize
    async def test_raw_response_delete(self, async_client: AsyncStoryden) -> None:
        response = await async_client.nodes.with_raw_response.delete(
            node_slug="cc5lnd2s1s4652adtu50",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        node = await response.parse()
        assert_matches_type(NodeDeleteResponse, node, path=["response"])

    @parametrize
    async def test_streaming_response_delete(self, async_client: AsyncStoryden) -> None:
        async with async_client.nodes.with_streaming_response.delete(
            node_slug="cc5lnd2s1s4652adtu50",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            node = await response.parse()
            assert_matches_type(NodeDeleteResponse, node, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_delete(self, async_client: AsyncStoryden) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `node_slug` but received ''"):
            await async_client.nodes.with_raw_response.delete(
                node_slug="",
            )
