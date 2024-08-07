# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from Storyden import Storyden, AsyncStoryden

from Storyden.types.nodes import ChildRemoveParentResponse, ChildSetParentResponse

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


class TestChildren:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_remove_parent(self, client: Storyden) -> None:
        child = client.nodes.children.remove_parent(
            node_slug_child="cc5lnd2s1s4652adtu50",
            node_slug="cc5lnd2s1s4652adtu50",
        )
        assert_matches_type(ChildRemoveParentResponse, child, path=["response"])

    @parametrize
    def test_raw_response_remove_parent(self, client: Storyden) -> None:
        response = client.nodes.children.with_raw_response.remove_parent(
            node_slug_child="cc5lnd2s1s4652adtu50",
            node_slug="cc5lnd2s1s4652adtu50",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        child = response.parse()
        assert_matches_type(ChildRemoveParentResponse, child, path=["response"])

    @parametrize
    def test_streaming_response_remove_parent(self, client: Storyden) -> None:
        with client.nodes.children.with_streaming_response.remove_parent(
            node_slug_child="cc5lnd2s1s4652adtu50",
            node_slug="cc5lnd2s1s4652adtu50",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            child = response.parse()
            assert_matches_type(ChildRemoveParentResponse, child, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_remove_parent(self, client: Storyden) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `node_slug` but received ''"):
            client.nodes.children.with_raw_response.remove_parent(
                node_slug_child="cc5lnd2s1s4652adtu50",
                node_slug="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `node_slug_child` but received ''"):
            client.nodes.children.with_raw_response.remove_parent(
                node_slug_child="",
                node_slug="cc5lnd2s1s4652adtu50",
            )

    @parametrize
    def test_method_set_parent(self, client: Storyden) -> None:
        child = client.nodes.children.set_parent(
            node_slug_child="cc5lnd2s1s4652adtu50",
            node_slug="cc5lnd2s1s4652adtu50",
        )
        assert_matches_type(ChildSetParentResponse, child, path=["response"])

    @parametrize
    def test_raw_response_set_parent(self, client: Storyden) -> None:
        response = client.nodes.children.with_raw_response.set_parent(
            node_slug_child="cc5lnd2s1s4652adtu50",
            node_slug="cc5lnd2s1s4652adtu50",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        child = response.parse()
        assert_matches_type(ChildSetParentResponse, child, path=["response"])

    @parametrize
    def test_streaming_response_set_parent(self, client: Storyden) -> None:
        with client.nodes.children.with_streaming_response.set_parent(
            node_slug_child="cc5lnd2s1s4652adtu50",
            node_slug="cc5lnd2s1s4652adtu50",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            child = response.parse()
            assert_matches_type(ChildSetParentResponse, child, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_set_parent(self, client: Storyden) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `node_slug` but received ''"):
            client.nodes.children.with_raw_response.set_parent(
                node_slug_child="cc5lnd2s1s4652adtu50",
                node_slug="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `node_slug_child` but received ''"):
            client.nodes.children.with_raw_response.set_parent(
                node_slug_child="",
                node_slug="cc5lnd2s1s4652adtu50",
            )


class TestAsyncChildren:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    async def test_method_remove_parent(self, async_client: AsyncStoryden) -> None:
        child = await async_client.nodes.children.remove_parent(
            node_slug_child="cc5lnd2s1s4652adtu50",
            node_slug="cc5lnd2s1s4652adtu50",
        )
        assert_matches_type(ChildRemoveParentResponse, child, path=["response"])

    @parametrize
    async def test_raw_response_remove_parent(self, async_client: AsyncStoryden) -> None:
        response = await async_client.nodes.children.with_raw_response.remove_parent(
            node_slug_child="cc5lnd2s1s4652adtu50",
            node_slug="cc5lnd2s1s4652adtu50",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        child = await response.parse()
        assert_matches_type(ChildRemoveParentResponse, child, path=["response"])

    @parametrize
    async def test_streaming_response_remove_parent(self, async_client: AsyncStoryden) -> None:
        async with async_client.nodes.children.with_streaming_response.remove_parent(
            node_slug_child="cc5lnd2s1s4652adtu50",
            node_slug="cc5lnd2s1s4652adtu50",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            child = await response.parse()
            assert_matches_type(ChildRemoveParentResponse, child, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_remove_parent(self, async_client: AsyncStoryden) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `node_slug` but received ''"):
            await async_client.nodes.children.with_raw_response.remove_parent(
                node_slug_child="cc5lnd2s1s4652adtu50",
                node_slug="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `node_slug_child` but received ''"):
            await async_client.nodes.children.with_raw_response.remove_parent(
                node_slug_child="",
                node_slug="cc5lnd2s1s4652adtu50",
            )

    @parametrize
    async def test_method_set_parent(self, async_client: AsyncStoryden) -> None:
        child = await async_client.nodes.children.set_parent(
            node_slug_child="cc5lnd2s1s4652adtu50",
            node_slug="cc5lnd2s1s4652adtu50",
        )
        assert_matches_type(ChildSetParentResponse, child, path=["response"])

    @parametrize
    async def test_raw_response_set_parent(self, async_client: AsyncStoryden) -> None:
        response = await async_client.nodes.children.with_raw_response.set_parent(
            node_slug_child="cc5lnd2s1s4652adtu50",
            node_slug="cc5lnd2s1s4652adtu50",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        child = await response.parse()
        assert_matches_type(ChildSetParentResponse, child, path=["response"])

    @parametrize
    async def test_streaming_response_set_parent(self, async_client: AsyncStoryden) -> None:
        async with async_client.nodes.children.with_streaming_response.set_parent(
            node_slug_child="cc5lnd2s1s4652adtu50",
            node_slug="cc5lnd2s1s4652adtu50",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            child = await response.parse()
            assert_matches_type(ChildSetParentResponse, child, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_set_parent(self, async_client: AsyncStoryden) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `node_slug` but received ''"):
            await async_client.nodes.children.with_raw_response.set_parent(
                node_slug_child="cc5lnd2s1s4652adtu50",
                node_slug="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `node_slug_child` but received ''"):
            await async_client.nodes.children.with_raw_response.set_parent(
                node_slug_child="",
                node_slug="cc5lnd2s1s4652adtu50",
            )
