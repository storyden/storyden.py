# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from Storyden import Storyden, AsyncStoryden

from Storyden.types import PostUpdateResponse, PostSearchResponse

from typing import Any, cast

import os
import pytest
import httpx
from typing_extensions import get_args
from typing import Optional
from respx import MockRouter
from Storyden import Storyden, AsyncStoryden
from tests.utils import assert_matches_type
from Storyden.types import post_update_params
from Storyden.types import post_search_params

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestPosts:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_update(self, client: Storyden) -> None:
        post = client.posts.update(
            post_id="cc5lnd2s1s4652adtu50",
        )
        assert_matches_type(PostUpdateResponse, post, path=["response"])

    @parametrize
    def test_method_update_with_all_params(self, client: Storyden) -> None:
        post = client.posts.update(
            post_id="cc5lnd2s1s4652adtu50",
            body="body",
            meta={"foo": "bar"},
            url="url",
        )
        assert_matches_type(PostUpdateResponse, post, path=["response"])

    @parametrize
    def test_raw_response_update(self, client: Storyden) -> None:
        response = client.posts.with_raw_response.update(
            post_id="cc5lnd2s1s4652adtu50",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        post = response.parse()
        assert_matches_type(PostUpdateResponse, post, path=["response"])

    @parametrize
    def test_streaming_response_update(self, client: Storyden) -> None:
        with client.posts.with_streaming_response.update(
            post_id="cc5lnd2s1s4652adtu50",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            post = response.parse()
            assert_matches_type(PostUpdateResponse, post, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_update(self, client: Storyden) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `post_id` but received ''"):
            client.posts.with_raw_response.update(
                post_id="",
            )

    @parametrize
    def test_method_delete(self, client: Storyden) -> None:
        post = client.posts.delete(
            "cc5lnd2s1s4652adtu50",
        )
        assert post is None

    @parametrize
    def test_raw_response_delete(self, client: Storyden) -> None:
        response = client.posts.with_raw_response.delete(
            "cc5lnd2s1s4652adtu50",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        post = response.parse()
        assert post is None

    @parametrize
    def test_streaming_response_delete(self, client: Storyden) -> None:
        with client.posts.with_streaming_response.delete(
            "cc5lnd2s1s4652adtu50",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            post = response.parse()
            assert post is None

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_delete(self, client: Storyden) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `post_id` but received ''"):
            client.posts.with_raw_response.delete(
                "",
            )

    @parametrize
    def test_method_search(self, client: Storyden) -> None:
        post = client.posts.search()
        assert_matches_type(PostSearchResponse, post, path=["response"])

    @parametrize
    def test_method_search_with_all_params(self, client: Storyden) -> None:
        post = client.posts.search(
            author="Southclaws",
            body="body",
            kind=["post", "thread"],
        )
        assert_matches_type(PostSearchResponse, post, path=["response"])

    @parametrize
    def test_raw_response_search(self, client: Storyden) -> None:
        response = client.posts.with_raw_response.search()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        post = response.parse()
        assert_matches_type(PostSearchResponse, post, path=["response"])

    @parametrize
    def test_streaming_response_search(self, client: Storyden) -> None:
        with client.posts.with_streaming_response.search() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            post = response.parse()
            assert_matches_type(PostSearchResponse, post, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncPosts:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    async def test_method_update(self, async_client: AsyncStoryden) -> None:
        post = await async_client.posts.update(
            post_id="cc5lnd2s1s4652adtu50",
        )
        assert_matches_type(PostUpdateResponse, post, path=["response"])

    @parametrize
    async def test_method_update_with_all_params(self, async_client: AsyncStoryden) -> None:
        post = await async_client.posts.update(
            post_id="cc5lnd2s1s4652adtu50",
            body="body",
            meta={"foo": "bar"},
            url="url",
        )
        assert_matches_type(PostUpdateResponse, post, path=["response"])

    @parametrize
    async def test_raw_response_update(self, async_client: AsyncStoryden) -> None:
        response = await async_client.posts.with_raw_response.update(
            post_id="cc5lnd2s1s4652adtu50",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        post = await response.parse()
        assert_matches_type(PostUpdateResponse, post, path=["response"])

    @parametrize
    async def test_streaming_response_update(self, async_client: AsyncStoryden) -> None:
        async with async_client.posts.with_streaming_response.update(
            post_id="cc5lnd2s1s4652adtu50",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            post = await response.parse()
            assert_matches_type(PostUpdateResponse, post, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_update(self, async_client: AsyncStoryden) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `post_id` but received ''"):
            await async_client.posts.with_raw_response.update(
                post_id="",
            )

    @parametrize
    async def test_method_delete(self, async_client: AsyncStoryden) -> None:
        post = await async_client.posts.delete(
            "cc5lnd2s1s4652adtu50",
        )
        assert post is None

    @parametrize
    async def test_raw_response_delete(self, async_client: AsyncStoryden) -> None:
        response = await async_client.posts.with_raw_response.delete(
            "cc5lnd2s1s4652adtu50",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        post = await response.parse()
        assert post is None

    @parametrize
    async def test_streaming_response_delete(self, async_client: AsyncStoryden) -> None:
        async with async_client.posts.with_streaming_response.delete(
            "cc5lnd2s1s4652adtu50",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            post = await response.parse()
            assert post is None

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_delete(self, async_client: AsyncStoryden) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `post_id` but received ''"):
            await async_client.posts.with_raw_response.delete(
                "",
            )

    @parametrize
    async def test_method_search(self, async_client: AsyncStoryden) -> None:
        post = await async_client.posts.search()
        assert_matches_type(PostSearchResponse, post, path=["response"])

    @parametrize
    async def test_method_search_with_all_params(self, async_client: AsyncStoryden) -> None:
        post = await async_client.posts.search(
            author="Southclaws",
            body="body",
            kind=["post", "thread"],
        )
        assert_matches_type(PostSearchResponse, post, path=["response"])

    @parametrize
    async def test_raw_response_search(self, async_client: AsyncStoryden) -> None:
        response = await async_client.posts.with_raw_response.search()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        post = await response.parse()
        assert_matches_type(PostSearchResponse, post, path=["response"])

    @parametrize
    async def test_streaming_response_search(self, async_client: AsyncStoryden) -> None:
        async with async_client.posts.with_streaming_response.search() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            post = await response.parse()
            assert_matches_type(PostSearchResponse, post, path=["response"])

        assert cast(Any, response.is_closed) is True
