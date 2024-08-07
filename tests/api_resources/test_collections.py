# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from Storyden import Storyden, AsyncStoryden

from Storyden.types import (
    CollectionCreateResponse,
    CollectionRetrieveResponse,
    CollectionUpdateResponse,
    CollectionListResponse,
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
from Storyden.types import collection_create_params
from Storyden.types import collection_update_params
from Storyden.types import collection_list_params

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestCollections:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_create(self, client: Storyden) -> None:
        collection = client.collections.create(
            description="description",
            name="name",
        )
        assert_matches_type(CollectionCreateResponse, collection, path=["response"])

    @parametrize
    def test_raw_response_create(self, client: Storyden) -> None:
        response = client.collections.with_raw_response.create(
            description="description",
            name="name",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        collection = response.parse()
        assert_matches_type(CollectionCreateResponse, collection, path=["response"])

    @parametrize
    def test_streaming_response_create(self, client: Storyden) -> None:
        with client.collections.with_streaming_response.create(
            description="description",
            name="name",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            collection = response.parse()
            assert_matches_type(CollectionCreateResponse, collection, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_retrieve(self, client: Storyden) -> None:
        collection = client.collections.retrieve(
            "cc5lnd2s1s4652adtu50",
        )
        assert_matches_type(CollectionRetrieveResponse, collection, path=["response"])

    @parametrize
    def test_raw_response_retrieve(self, client: Storyden) -> None:
        response = client.collections.with_raw_response.retrieve(
            "cc5lnd2s1s4652adtu50",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        collection = response.parse()
        assert_matches_type(CollectionRetrieveResponse, collection, path=["response"])

    @parametrize
    def test_streaming_response_retrieve(self, client: Storyden) -> None:
        with client.collections.with_streaming_response.retrieve(
            "cc5lnd2s1s4652adtu50",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            collection = response.parse()
            assert_matches_type(CollectionRetrieveResponse, collection, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_retrieve(self, client: Storyden) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `collection_id` but received ''"):
            client.collections.with_raw_response.retrieve(
                "",
            )

    @parametrize
    def test_method_update(self, client: Storyden) -> None:
        collection = client.collections.update(
            collection_id="cc5lnd2s1s4652adtu50",
        )
        assert_matches_type(CollectionUpdateResponse, collection, path=["response"])

    @parametrize
    def test_method_update_with_all_params(self, client: Storyden) -> None:
        collection = client.collections.update(
            collection_id="cc5lnd2s1s4652adtu50",
            description="description",
            name="name",
        )
        assert_matches_type(CollectionUpdateResponse, collection, path=["response"])

    @parametrize
    def test_raw_response_update(self, client: Storyden) -> None:
        response = client.collections.with_raw_response.update(
            collection_id="cc5lnd2s1s4652adtu50",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        collection = response.parse()
        assert_matches_type(CollectionUpdateResponse, collection, path=["response"])

    @parametrize
    def test_streaming_response_update(self, client: Storyden) -> None:
        with client.collections.with_streaming_response.update(
            collection_id="cc5lnd2s1s4652adtu50",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            collection = response.parse()
            assert_matches_type(CollectionUpdateResponse, collection, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_update(self, client: Storyden) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `collection_id` but received ''"):
            client.collections.with_raw_response.update(
                collection_id="",
            )

    @parametrize
    def test_method_list(self, client: Storyden) -> None:
        collection = client.collections.list()
        assert_matches_type(CollectionListResponse, collection, path=["response"])

    @parametrize
    def test_method_list_with_all_params(self, client: Storyden) -> None:
        collection = client.collections.list(
            account_handle="Southclaws",
        )
        assert_matches_type(CollectionListResponse, collection, path=["response"])

    @parametrize
    def test_raw_response_list(self, client: Storyden) -> None:
        response = client.collections.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        collection = response.parse()
        assert_matches_type(CollectionListResponse, collection, path=["response"])

    @parametrize
    def test_streaming_response_list(self, client: Storyden) -> None:
        with client.collections.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            collection = response.parse()
            assert_matches_type(CollectionListResponse, collection, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_delete(self, client: Storyden) -> None:
        collection = client.collections.delete(
            "cc5lnd2s1s4652adtu50",
        )
        assert collection is None

    @parametrize
    def test_raw_response_delete(self, client: Storyden) -> None:
        response = client.collections.with_raw_response.delete(
            "cc5lnd2s1s4652adtu50",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        collection = response.parse()
        assert collection is None

    @parametrize
    def test_streaming_response_delete(self, client: Storyden) -> None:
        with client.collections.with_streaming_response.delete(
            "cc5lnd2s1s4652adtu50",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            collection = response.parse()
            assert collection is None

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_delete(self, client: Storyden) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `collection_id` but received ''"):
            client.collections.with_raw_response.delete(
                "",
            )


class TestAsyncCollections:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    async def test_method_create(self, async_client: AsyncStoryden) -> None:
        collection = await async_client.collections.create(
            description="description",
            name="name",
        )
        assert_matches_type(CollectionCreateResponse, collection, path=["response"])

    @parametrize
    async def test_raw_response_create(self, async_client: AsyncStoryden) -> None:
        response = await async_client.collections.with_raw_response.create(
            description="description",
            name="name",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        collection = await response.parse()
        assert_matches_type(CollectionCreateResponse, collection, path=["response"])

    @parametrize
    async def test_streaming_response_create(self, async_client: AsyncStoryden) -> None:
        async with async_client.collections.with_streaming_response.create(
            description="description",
            name="name",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            collection = await response.parse()
            assert_matches_type(CollectionCreateResponse, collection, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_retrieve(self, async_client: AsyncStoryden) -> None:
        collection = await async_client.collections.retrieve(
            "cc5lnd2s1s4652adtu50",
        )
        assert_matches_type(CollectionRetrieveResponse, collection, path=["response"])

    @parametrize
    async def test_raw_response_retrieve(self, async_client: AsyncStoryden) -> None:
        response = await async_client.collections.with_raw_response.retrieve(
            "cc5lnd2s1s4652adtu50",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        collection = await response.parse()
        assert_matches_type(CollectionRetrieveResponse, collection, path=["response"])

    @parametrize
    async def test_streaming_response_retrieve(self, async_client: AsyncStoryden) -> None:
        async with async_client.collections.with_streaming_response.retrieve(
            "cc5lnd2s1s4652adtu50",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            collection = await response.parse()
            assert_matches_type(CollectionRetrieveResponse, collection, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_retrieve(self, async_client: AsyncStoryden) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `collection_id` but received ''"):
            await async_client.collections.with_raw_response.retrieve(
                "",
            )

    @parametrize
    async def test_method_update(self, async_client: AsyncStoryden) -> None:
        collection = await async_client.collections.update(
            collection_id="cc5lnd2s1s4652adtu50",
        )
        assert_matches_type(CollectionUpdateResponse, collection, path=["response"])

    @parametrize
    async def test_method_update_with_all_params(self, async_client: AsyncStoryden) -> None:
        collection = await async_client.collections.update(
            collection_id="cc5lnd2s1s4652adtu50",
            description="description",
            name="name",
        )
        assert_matches_type(CollectionUpdateResponse, collection, path=["response"])

    @parametrize
    async def test_raw_response_update(self, async_client: AsyncStoryden) -> None:
        response = await async_client.collections.with_raw_response.update(
            collection_id="cc5lnd2s1s4652adtu50",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        collection = await response.parse()
        assert_matches_type(CollectionUpdateResponse, collection, path=["response"])

    @parametrize
    async def test_streaming_response_update(self, async_client: AsyncStoryden) -> None:
        async with async_client.collections.with_streaming_response.update(
            collection_id="cc5lnd2s1s4652adtu50",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            collection = await response.parse()
            assert_matches_type(CollectionUpdateResponse, collection, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_update(self, async_client: AsyncStoryden) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `collection_id` but received ''"):
            await async_client.collections.with_raw_response.update(
                collection_id="",
            )

    @parametrize
    async def test_method_list(self, async_client: AsyncStoryden) -> None:
        collection = await async_client.collections.list()
        assert_matches_type(CollectionListResponse, collection, path=["response"])

    @parametrize
    async def test_method_list_with_all_params(self, async_client: AsyncStoryden) -> None:
        collection = await async_client.collections.list(
            account_handle="Southclaws",
        )
        assert_matches_type(CollectionListResponse, collection, path=["response"])

    @parametrize
    async def test_raw_response_list(self, async_client: AsyncStoryden) -> None:
        response = await async_client.collections.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        collection = await response.parse()
        assert_matches_type(CollectionListResponse, collection, path=["response"])

    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncStoryden) -> None:
        async with async_client.collections.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            collection = await response.parse()
            assert_matches_type(CollectionListResponse, collection, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_delete(self, async_client: AsyncStoryden) -> None:
        collection = await async_client.collections.delete(
            "cc5lnd2s1s4652adtu50",
        )
        assert collection is None

    @parametrize
    async def test_raw_response_delete(self, async_client: AsyncStoryden) -> None:
        response = await async_client.collections.with_raw_response.delete(
            "cc5lnd2s1s4652adtu50",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        collection = await response.parse()
        assert collection is None

    @parametrize
    async def test_streaming_response_delete(self, async_client: AsyncStoryden) -> None:
        async with async_client.collections.with_streaming_response.delete(
            "cc5lnd2s1s4652adtu50",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            collection = await response.parse()
            assert collection is None

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_delete(self, async_client: AsyncStoryden) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `collection_id` but received ''"):
            await async_client.collections.with_raw_response.delete(
                "",
            )
