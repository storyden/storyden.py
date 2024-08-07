# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from Storyden import Storyden, AsyncStoryden

from Storyden.types import LinkCreateResponse, LinkRetrieveResponse, LinkListResponse

from typing import Any, cast

import os
import pytest
import httpx
from typing_extensions import get_args
from typing import Optional
from respx import MockRouter
from Storyden import Storyden, AsyncStoryden
from tests.utils import assert_matches_type
from Storyden.types import link_create_params
from Storyden.types import link_list_params

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestLinks:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_create(self, client: Storyden) -> None:
        link = client.links.create(
            url="url",
        )
        assert_matches_type(LinkCreateResponse, link, path=["response"])

    @parametrize
    def test_method_create_with_all_params(self, client: Storyden) -> None:
        link = client.links.create(
            url="url",
            description="The Open Graph protocol enables any web page to become a rich object in a social graph.",
            title="The Open Graph Protocol",
        )
        assert_matches_type(LinkCreateResponse, link, path=["response"])

    @parametrize
    def test_raw_response_create(self, client: Storyden) -> None:
        response = client.links.with_raw_response.create(
            url="url",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        link = response.parse()
        assert_matches_type(LinkCreateResponse, link, path=["response"])

    @parametrize
    def test_streaming_response_create(self, client: Storyden) -> None:
        with client.links.with_streaming_response.create(
            url="url",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            link = response.parse()
            assert_matches_type(LinkCreateResponse, link, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_retrieve(self, client: Storyden) -> None:
        link = client.links.retrieve(
            "link_slug",
        )
        assert_matches_type(LinkRetrieveResponse, link, path=["response"])

    @parametrize
    def test_raw_response_retrieve(self, client: Storyden) -> None:
        response = client.links.with_raw_response.retrieve(
            "link_slug",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        link = response.parse()
        assert_matches_type(LinkRetrieveResponse, link, path=["response"])

    @parametrize
    def test_streaming_response_retrieve(self, client: Storyden) -> None:
        with client.links.with_streaming_response.retrieve(
            "link_slug",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            link = response.parse()
            assert_matches_type(LinkRetrieveResponse, link, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_retrieve(self, client: Storyden) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `link_slug` but received ''"):
            client.links.with_raw_response.retrieve(
                "",
            )

    @parametrize
    def test_method_list(self, client: Storyden) -> None:
        link = client.links.list()
        assert_matches_type(LinkListResponse, link, path=["response"])

    @parametrize
    def test_method_list_with_all_params(self, client: Storyden) -> None:
        link = client.links.list(
            page="page",
            q="q",
        )
        assert_matches_type(LinkListResponse, link, path=["response"])

    @parametrize
    def test_raw_response_list(self, client: Storyden) -> None:
        response = client.links.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        link = response.parse()
        assert_matches_type(LinkListResponse, link, path=["response"])

    @parametrize
    def test_streaming_response_list(self, client: Storyden) -> None:
        with client.links.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            link = response.parse()
            assert_matches_type(LinkListResponse, link, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncLinks:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    async def test_method_create(self, async_client: AsyncStoryden) -> None:
        link = await async_client.links.create(
            url="url",
        )
        assert_matches_type(LinkCreateResponse, link, path=["response"])

    @parametrize
    async def test_method_create_with_all_params(self, async_client: AsyncStoryden) -> None:
        link = await async_client.links.create(
            url="url",
            description="The Open Graph protocol enables any web page to become a rich object in a social graph.",
            title="The Open Graph Protocol",
        )
        assert_matches_type(LinkCreateResponse, link, path=["response"])

    @parametrize
    async def test_raw_response_create(self, async_client: AsyncStoryden) -> None:
        response = await async_client.links.with_raw_response.create(
            url="url",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        link = await response.parse()
        assert_matches_type(LinkCreateResponse, link, path=["response"])

    @parametrize
    async def test_streaming_response_create(self, async_client: AsyncStoryden) -> None:
        async with async_client.links.with_streaming_response.create(
            url="url",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            link = await response.parse()
            assert_matches_type(LinkCreateResponse, link, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_retrieve(self, async_client: AsyncStoryden) -> None:
        link = await async_client.links.retrieve(
            "link_slug",
        )
        assert_matches_type(LinkRetrieveResponse, link, path=["response"])

    @parametrize
    async def test_raw_response_retrieve(self, async_client: AsyncStoryden) -> None:
        response = await async_client.links.with_raw_response.retrieve(
            "link_slug",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        link = await response.parse()
        assert_matches_type(LinkRetrieveResponse, link, path=["response"])

    @parametrize
    async def test_streaming_response_retrieve(self, async_client: AsyncStoryden) -> None:
        async with async_client.links.with_streaming_response.retrieve(
            "link_slug",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            link = await response.parse()
            assert_matches_type(LinkRetrieveResponse, link, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_retrieve(self, async_client: AsyncStoryden) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `link_slug` but received ''"):
            await async_client.links.with_raw_response.retrieve(
                "",
            )

    @parametrize
    async def test_method_list(self, async_client: AsyncStoryden) -> None:
        link = await async_client.links.list()
        assert_matches_type(LinkListResponse, link, path=["response"])

    @parametrize
    async def test_method_list_with_all_params(self, async_client: AsyncStoryden) -> None:
        link = await async_client.links.list(
            page="page",
            q="q",
        )
        assert_matches_type(LinkListResponse, link, path=["response"])

    @parametrize
    async def test_raw_response_list(self, async_client: AsyncStoryden) -> None:
        response = await async_client.links.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        link = await response.parse()
        assert_matches_type(LinkListResponse, link, path=["response"])

    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncStoryden) -> None:
        async with async_client.links.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            link = await response.parse()
            assert_matches_type(LinkListResponse, link, path=["response"])

        assert cast(Any, response.is_closed) is True
