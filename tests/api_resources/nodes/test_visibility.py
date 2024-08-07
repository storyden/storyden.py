# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from Storyden import Storyden, AsyncStoryden

from Storyden.types.nodes import VisibilityUpdateResponse

from typing import Any, cast

import os
import pytest
import httpx
from typing_extensions import get_args
from typing import Optional
from respx import MockRouter
from Storyden import Storyden, AsyncStoryden
from tests.utils import assert_matches_type
from Storyden.types.nodes import visibility_update_params

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestVisibility:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_update(self, client: Storyden) -> None:
        visibility = client.nodes.visibility.update(
            node_slug="cc5lnd2s1s4652adtu50",
            visibility="draft",
        )
        assert_matches_type(VisibilityUpdateResponse, visibility, path=["response"])

    @parametrize
    def test_raw_response_update(self, client: Storyden) -> None:
        response = client.nodes.visibility.with_raw_response.update(
            node_slug="cc5lnd2s1s4652adtu50",
            visibility="draft",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        visibility = response.parse()
        assert_matches_type(VisibilityUpdateResponse, visibility, path=["response"])

    @parametrize
    def test_streaming_response_update(self, client: Storyden) -> None:
        with client.nodes.visibility.with_streaming_response.update(
            node_slug="cc5lnd2s1s4652adtu50",
            visibility="draft",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            visibility = response.parse()
            assert_matches_type(VisibilityUpdateResponse, visibility, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_update(self, client: Storyden) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `node_slug` but received ''"):
            client.nodes.visibility.with_raw_response.update(
                node_slug="",
                visibility="draft",
            )


class TestAsyncVisibility:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    async def test_method_update(self, async_client: AsyncStoryden) -> None:
        visibility = await async_client.nodes.visibility.update(
            node_slug="cc5lnd2s1s4652adtu50",
            visibility="draft",
        )
        assert_matches_type(VisibilityUpdateResponse, visibility, path=["response"])

    @parametrize
    async def test_raw_response_update(self, async_client: AsyncStoryden) -> None:
        response = await async_client.nodes.visibility.with_raw_response.update(
            node_slug="cc5lnd2s1s4652adtu50",
            visibility="draft",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        visibility = await response.parse()
        assert_matches_type(VisibilityUpdateResponse, visibility, path=["response"])

    @parametrize
    async def test_streaming_response_update(self, async_client: AsyncStoryden) -> None:
        async with async_client.nodes.visibility.with_streaming_response.update(
            node_slug="cc5lnd2s1s4652adtu50",
            visibility="draft",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            visibility = await response.parse()
            assert_matches_type(VisibilityUpdateResponse, visibility, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_update(self, async_client: AsyncStoryden) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `node_slug` but received ''"):
            await async_client.nodes.visibility.with_raw_response.update(
                node_slug="",
                visibility="draft",
            )
