# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from storyden import Storyden, AsyncStoryden
from tests.utils import assert_matches_type
from storyden.types.v1 import CategoryCreateResponse

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestCategories:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_create(self, client: Storyden) -> None:
        category = client.v1.categories.create(
            admin=True,
            colour="colour",
            description="description",
            name="name",
        )
        assert_matches_type(CategoryCreateResponse, category, path=["response"])

    @parametrize
    def test_method_create_with_all_params(self, client: Storyden) -> None:
        category = client.v1.categories.create(
            admin=True,
            colour="colour",
            description="description",
            name="name",
            meta={"foo": "bar"},
            slug="slug",
        )
        assert_matches_type(CategoryCreateResponse, category, path=["response"])

    @parametrize
    def test_raw_response_create(self, client: Storyden) -> None:
        response = client.v1.categories.with_raw_response.create(
            admin=True,
            colour="colour",
            description="description",
            name="name",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        category = response.parse()
        assert_matches_type(CategoryCreateResponse, category, path=["response"])

    @parametrize
    def test_streaming_response_create(self, client: Storyden) -> None:
        with client.v1.categories.with_streaming_response.create(
            admin=True,
            colour="colour",
            description="description",
            name="name",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            category = response.parse()
            assert_matches_type(CategoryCreateResponse, category, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncCategories:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    async def test_method_create(self, async_client: AsyncStoryden) -> None:
        category = await async_client.v1.categories.create(
            admin=True,
            colour="colour",
            description="description",
            name="name",
        )
        assert_matches_type(CategoryCreateResponse, category, path=["response"])

    @parametrize
    async def test_method_create_with_all_params(self, async_client: AsyncStoryden) -> None:
        category = await async_client.v1.categories.create(
            admin=True,
            colour="colour",
            description="description",
            name="name",
            meta={"foo": "bar"},
            slug="slug",
        )
        assert_matches_type(CategoryCreateResponse, category, path=["response"])

    @parametrize
    async def test_raw_response_create(self, async_client: AsyncStoryden) -> None:
        response = await async_client.v1.categories.with_raw_response.create(
            admin=True,
            colour="colour",
            description="description",
            name="name",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        category = await response.parse()
        assert_matches_type(CategoryCreateResponse, category, path=["response"])

    @parametrize
    async def test_streaming_response_create(self, async_client: AsyncStoryden) -> None:
        async with async_client.v1.categories.with_streaming_response.create(
            admin=True,
            colour="colour",
            description="description",
            name="name",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            category = await response.parse()
            assert_matches_type(CategoryCreateResponse, category, path=["response"])

        assert cast(Any, response.is_closed) is True
