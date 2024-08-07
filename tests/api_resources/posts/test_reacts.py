# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from Storyden import Storyden, AsyncStoryden

from Storyden.types.posts import ReactUpdateResponse

from typing import Any, cast

import os
import pytest
import httpx
from typing_extensions import get_args
from typing import Optional
from respx import MockRouter
from Storyden import Storyden, AsyncStoryden
from tests.utils import assert_matches_type
from Storyden.types.posts import react_update_params

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestReacts:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_update(self, client: Storyden) -> None:
        react = client.posts.reacts.update(
            post_id="cc5lnd2s1s4652adtu50",
        )
        assert_matches_type(ReactUpdateResponse, react, path=["response"])

    @parametrize
    def test_method_update_with_all_params(self, client: Storyden) -> None:
        react = client.posts.reacts.update(
            post_id="cc5lnd2s1s4652adtu50",
            emoji="emoji",
        )
        assert_matches_type(ReactUpdateResponse, react, path=["response"])

    @parametrize
    def test_raw_response_update(self, client: Storyden) -> None:
        response = client.posts.reacts.with_raw_response.update(
            post_id="cc5lnd2s1s4652adtu50",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        react = response.parse()
        assert_matches_type(ReactUpdateResponse, react, path=["response"])

    @parametrize
    def test_streaming_response_update(self, client: Storyden) -> None:
        with client.posts.reacts.with_streaming_response.update(
            post_id="cc5lnd2s1s4652adtu50",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            react = response.parse()
            assert_matches_type(ReactUpdateResponse, react, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_update(self, client: Storyden) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `post_id` but received ''"):
            client.posts.reacts.with_raw_response.update(
                post_id="",
            )


class TestAsyncReacts:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    async def test_method_update(self, async_client: AsyncStoryden) -> None:
        react = await async_client.posts.reacts.update(
            post_id="cc5lnd2s1s4652adtu50",
        )
        assert_matches_type(ReactUpdateResponse, react, path=["response"])

    @parametrize
    async def test_method_update_with_all_params(self, async_client: AsyncStoryden) -> None:
        react = await async_client.posts.reacts.update(
            post_id="cc5lnd2s1s4652adtu50",
            emoji="emoji",
        )
        assert_matches_type(ReactUpdateResponse, react, path=["response"])

    @parametrize
    async def test_raw_response_update(self, async_client: AsyncStoryden) -> None:
        response = await async_client.posts.reacts.with_raw_response.update(
            post_id="cc5lnd2s1s4652adtu50",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        react = await response.parse()
        assert_matches_type(ReactUpdateResponse, react, path=["response"])

    @parametrize
    async def test_streaming_response_update(self, async_client: AsyncStoryden) -> None:
        async with async_client.posts.reacts.with_streaming_response.update(
            post_id="cc5lnd2s1s4652adtu50",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            react = await response.parse()
            assert_matches_type(ReactUpdateResponse, react, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_update(self, async_client: AsyncStoryden) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `post_id` but received ''"):
            await async_client.posts.reacts.with_raw_response.update(
                post_id="",
            )
