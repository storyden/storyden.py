# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from storyden import Storyden, AsyncStoryden
from tests.utils import assert_matches_type
from storyden.types.v1 import AccountUpdateResponse, AccountRetrieveResponse

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestAccounts:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_retrieve(self, client: Storyden) -> None:
        account = client.v1.accounts.retrieve()
        assert_matches_type(AccountRetrieveResponse, account, path=["response"])

    @parametrize
    def test_raw_response_retrieve(self, client: Storyden) -> None:
        response = client.v1.accounts.with_raw_response.retrieve()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        account = response.parse()
        assert_matches_type(AccountRetrieveResponse, account, path=["response"])

    @parametrize
    def test_streaming_response_retrieve(self, client: Storyden) -> None:
        with client.v1.accounts.with_streaming_response.retrieve() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            account = response.parse()
            assert_matches_type(AccountRetrieveResponse, account, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_update(self, client: Storyden) -> None:
        account = client.v1.accounts.update()
        assert_matches_type(AccountUpdateResponse, account, path=["response"])

    @parametrize
    def test_method_update_with_all_params(self, client: Storyden) -> None:
        account = client.v1.accounts.update(
            bio="<body><p>hi, my name is</p><p>southclaws</p></body>",
            handle="Southclaws",
            interests=["cc5lnd2s1s4652adtu50", "cc5lnd2s1s4652adtu50", "cc5lnd2s1s4652adtu50"],
            links=[
                {
                    "text": "text",
                    "url": "url",
                },
                {
                    "text": "text",
                    "url": "url",
                },
                {
                    "text": "text",
                    "url": "url",
                },
            ],
            meta={"foo": "bar"},
            name="Barnaby Keene",
        )
        assert_matches_type(AccountUpdateResponse, account, path=["response"])

    @parametrize
    def test_raw_response_update(self, client: Storyden) -> None:
        response = client.v1.accounts.with_raw_response.update()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        account = response.parse()
        assert_matches_type(AccountUpdateResponse, account, path=["response"])

    @parametrize
    def test_streaming_response_update(self, client: Storyden) -> None:
        with client.v1.accounts.with_streaming_response.update() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            account = response.parse()
            assert_matches_type(AccountUpdateResponse, account, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncAccounts:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    async def test_method_retrieve(self, async_client: AsyncStoryden) -> None:
        account = await async_client.v1.accounts.retrieve()
        assert_matches_type(AccountRetrieveResponse, account, path=["response"])

    @parametrize
    async def test_raw_response_retrieve(self, async_client: AsyncStoryden) -> None:
        response = await async_client.v1.accounts.with_raw_response.retrieve()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        account = await response.parse()
        assert_matches_type(AccountRetrieveResponse, account, path=["response"])

    @parametrize
    async def test_streaming_response_retrieve(self, async_client: AsyncStoryden) -> None:
        async with async_client.v1.accounts.with_streaming_response.retrieve() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            account = await response.parse()
            assert_matches_type(AccountRetrieveResponse, account, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_update(self, async_client: AsyncStoryden) -> None:
        account = await async_client.v1.accounts.update()
        assert_matches_type(AccountUpdateResponse, account, path=["response"])

    @parametrize
    async def test_method_update_with_all_params(self, async_client: AsyncStoryden) -> None:
        account = await async_client.v1.accounts.update(
            bio="<body><p>hi, my name is</p><p>southclaws</p></body>",
            handle="Southclaws",
            interests=["cc5lnd2s1s4652adtu50", "cc5lnd2s1s4652adtu50", "cc5lnd2s1s4652adtu50"],
            links=[
                {
                    "text": "text",
                    "url": "url",
                },
                {
                    "text": "text",
                    "url": "url",
                },
                {
                    "text": "text",
                    "url": "url",
                },
            ],
            meta={"foo": "bar"},
            name="Barnaby Keene",
        )
        assert_matches_type(AccountUpdateResponse, account, path=["response"])

    @parametrize
    async def test_raw_response_update(self, async_client: AsyncStoryden) -> None:
        response = await async_client.v1.accounts.with_raw_response.update()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        account = await response.parse()
        assert_matches_type(AccountUpdateResponse, account, path=["response"])

    @parametrize
    async def test_streaming_response_update(self, async_client: AsyncStoryden) -> None:
        async with async_client.v1.accounts.with_streaming_response.update() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            account = await response.parse()
            assert_matches_type(AccountUpdateResponse, account, path=["response"])

        assert cast(Any, response.is_closed) is True
