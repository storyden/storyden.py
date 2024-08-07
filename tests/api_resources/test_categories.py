# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from storyden import Storyden, AsyncStoryden
from tests.utils import assert_matches_type
from storyden.types import (
    CategoryListResponse,
    CategoryUpdateResponse,
    CategoryUpdateOrderResponse,
)

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestCategories:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_update(self, client: Storyden) -> None:
        category = client.categories.update(
            category_id="cc5lnd2s1s4652adtu50",
        )
        assert_matches_type(CategoryUpdateResponse, category, path=["response"])

    @parametrize
    def test_method_update_with_all_params(self, client: Storyden) -> None:
        category = client.categories.update(
            category_id="cc5lnd2s1s4652adtu50",
            admin=True,
            colour="colour",
            description="description",
            meta={"foo": "bar"},
            name="name",
            slug="slug",
        )
        assert_matches_type(CategoryUpdateResponse, category, path=["response"])

    @parametrize
    def test_raw_response_update(self, client: Storyden) -> None:
        response = client.categories.with_raw_response.update(
            category_id="cc5lnd2s1s4652adtu50",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        category = response.parse()
        assert_matches_type(CategoryUpdateResponse, category, path=["response"])

    @parametrize
    def test_streaming_response_update(self, client: Storyden) -> None:
        with client.categories.with_streaming_response.update(
            category_id="cc5lnd2s1s4652adtu50",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            category = response.parse()
            assert_matches_type(CategoryUpdateResponse, category, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_update(self, client: Storyden) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `category_id` but received ''"):
            client.categories.with_raw_response.update(
                category_id="",
            )

    @parametrize
    def test_method_list(self, client: Storyden) -> None:
        category = client.categories.list()
        assert_matches_type(CategoryListResponse, category, path=["response"])

    @parametrize
    def test_raw_response_list(self, client: Storyden) -> None:
        response = client.categories.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        category = response.parse()
        assert_matches_type(CategoryListResponse, category, path=["response"])

    @parametrize
    def test_streaming_response_list(self, client: Storyden) -> None:
        with client.categories.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            category = response.parse()
            assert_matches_type(CategoryListResponse, category, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_update_order(self, client: Storyden) -> None:
        category = client.categories.update_order(
            body=["cc5lnd2s1s4652adtu50", "cc5lnd2s1s4652adtu50", "cc5lnd2s1s4652adtu50"],
        )
        assert_matches_type(CategoryUpdateOrderResponse, category, path=["response"])

    @parametrize
    def test_raw_response_update_order(self, client: Storyden) -> None:
        response = client.categories.with_raw_response.update_order(
            body=["cc5lnd2s1s4652adtu50", "cc5lnd2s1s4652adtu50", "cc5lnd2s1s4652adtu50"],
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        category = response.parse()
        assert_matches_type(CategoryUpdateOrderResponse, category, path=["response"])

    @parametrize
    def test_streaming_response_update_order(self, client: Storyden) -> None:
        with client.categories.with_streaming_response.update_order(
            body=["cc5lnd2s1s4652adtu50", "cc5lnd2s1s4652adtu50", "cc5lnd2s1s4652adtu50"],
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            category = response.parse()
            assert_matches_type(CategoryUpdateOrderResponse, category, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncCategories:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    async def test_method_update(self, async_client: AsyncStoryden) -> None:
        category = await async_client.categories.update(
            category_id="cc5lnd2s1s4652adtu50",
        )
        assert_matches_type(CategoryUpdateResponse, category, path=["response"])

    @parametrize
    async def test_method_update_with_all_params(self, async_client: AsyncStoryden) -> None:
        category = await async_client.categories.update(
            category_id="cc5lnd2s1s4652adtu50",
            admin=True,
            colour="colour",
            description="description",
            meta={"foo": "bar"},
            name="name",
            slug="slug",
        )
        assert_matches_type(CategoryUpdateResponse, category, path=["response"])

    @parametrize
    async def test_raw_response_update(self, async_client: AsyncStoryden) -> None:
        response = await async_client.categories.with_raw_response.update(
            category_id="cc5lnd2s1s4652adtu50",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        category = await response.parse()
        assert_matches_type(CategoryUpdateResponse, category, path=["response"])

    @parametrize
    async def test_streaming_response_update(self, async_client: AsyncStoryden) -> None:
        async with async_client.categories.with_streaming_response.update(
            category_id="cc5lnd2s1s4652adtu50",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            category = await response.parse()
            assert_matches_type(CategoryUpdateResponse, category, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_update(self, async_client: AsyncStoryden) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `category_id` but received ''"):
            await async_client.categories.with_raw_response.update(
                category_id="",
            )

    @parametrize
    async def test_method_list(self, async_client: AsyncStoryden) -> None:
        category = await async_client.categories.list()
        assert_matches_type(CategoryListResponse, category, path=["response"])

    @parametrize
    async def test_raw_response_list(self, async_client: AsyncStoryden) -> None:
        response = await async_client.categories.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        category = await response.parse()
        assert_matches_type(CategoryListResponse, category, path=["response"])

    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncStoryden) -> None:
        async with async_client.categories.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            category = await response.parse()
            assert_matches_type(CategoryListResponse, category, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_update_order(self, async_client: AsyncStoryden) -> None:
        category = await async_client.categories.update_order(
            body=["cc5lnd2s1s4652adtu50", "cc5lnd2s1s4652adtu50", "cc5lnd2s1s4652adtu50"],
        )
        assert_matches_type(CategoryUpdateOrderResponse, category, path=["response"])

    @parametrize
    async def test_raw_response_update_order(self, async_client: AsyncStoryden) -> None:
        response = await async_client.categories.with_raw_response.update_order(
            body=["cc5lnd2s1s4652adtu50", "cc5lnd2s1s4652adtu50", "cc5lnd2s1s4652adtu50"],
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        category = await response.parse()
        assert_matches_type(CategoryUpdateOrderResponse, category, path=["response"])

    @parametrize
    async def test_streaming_response_update_order(self, async_client: AsyncStoryden) -> None:
        async with async_client.categories.with_streaming_response.update_order(
            body=["cc5lnd2s1s4652adtu50", "cc5lnd2s1s4652adtu50", "cc5lnd2s1s4652adtu50"],
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            category = await response.parse()
            assert_matches_type(CategoryUpdateOrderResponse, category, path=["response"])

        assert cast(Any, response.is_closed) is True
