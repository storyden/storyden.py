# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from storyden import Storyden, AsyncStoryden
from tests.utils import assert_matches_type
from storyden.types.auth import PhoneCreateResponse, PhoneUpdateResponse

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestPhone:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_create(self, client: Storyden) -> None:
        phone = client.auth.phone.create(
            identifier="southclaws",
            phone_number="phone_number",
        )
        assert_matches_type(PhoneCreateResponse, phone, path=["response"])

    @parametrize
    def test_raw_response_create(self, client: Storyden) -> None:
        response = client.auth.phone.with_raw_response.create(
            identifier="southclaws",
            phone_number="phone_number",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        phone = response.parse()
        assert_matches_type(PhoneCreateResponse, phone, path=["response"])

    @parametrize
    def test_streaming_response_create(self, client: Storyden) -> None:
        with client.auth.phone.with_streaming_response.create(
            identifier="southclaws",
            phone_number="phone_number",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            phone = response.parse()
            assert_matches_type(PhoneCreateResponse, phone, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_update(self, client: Storyden) -> None:
        phone = client.auth.phone.update(
            account_handle="southclaws",
            code="code",
        )
        assert_matches_type(PhoneUpdateResponse, phone, path=["response"])

    @parametrize
    def test_raw_response_update(self, client: Storyden) -> None:
        response = client.auth.phone.with_raw_response.update(
            account_handle="southclaws",
            code="code",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        phone = response.parse()
        assert_matches_type(PhoneUpdateResponse, phone, path=["response"])

    @parametrize
    def test_streaming_response_update(self, client: Storyden) -> None:
        with client.auth.phone.with_streaming_response.update(
            account_handle="southclaws",
            code="code",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            phone = response.parse()
            assert_matches_type(PhoneUpdateResponse, phone, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_update(self, client: Storyden) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_handle` but received ''"):
            client.auth.phone.with_raw_response.update(
                account_handle="",
                code="code",
            )


class TestAsyncPhone:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    async def test_method_create(self, async_client: AsyncStoryden) -> None:
        phone = await async_client.auth.phone.create(
            identifier="southclaws",
            phone_number="phone_number",
        )
        assert_matches_type(PhoneCreateResponse, phone, path=["response"])

    @parametrize
    async def test_raw_response_create(self, async_client: AsyncStoryden) -> None:
        response = await async_client.auth.phone.with_raw_response.create(
            identifier="southclaws",
            phone_number="phone_number",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        phone = await response.parse()
        assert_matches_type(PhoneCreateResponse, phone, path=["response"])

    @parametrize
    async def test_streaming_response_create(self, async_client: AsyncStoryden) -> None:
        async with async_client.auth.phone.with_streaming_response.create(
            identifier="southclaws",
            phone_number="phone_number",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            phone = await response.parse()
            assert_matches_type(PhoneCreateResponse, phone, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_update(self, async_client: AsyncStoryden) -> None:
        phone = await async_client.auth.phone.update(
            account_handle="southclaws",
            code="code",
        )
        assert_matches_type(PhoneUpdateResponse, phone, path=["response"])

    @parametrize
    async def test_raw_response_update(self, async_client: AsyncStoryden) -> None:
        response = await async_client.auth.phone.with_raw_response.update(
            account_handle="southclaws",
            code="code",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        phone = await response.parse()
        assert_matches_type(PhoneUpdateResponse, phone, path=["response"])

    @parametrize
    async def test_streaming_response_update(self, async_client: AsyncStoryden) -> None:
        async with async_client.auth.phone.with_streaming_response.update(
            account_handle="southclaws",
            code="code",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            phone = await response.parse()
            assert_matches_type(PhoneUpdateResponse, phone, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_update(self, async_client: AsyncStoryden) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_handle` but received ''"):
            await async_client.auth.phone.with_raw_response.update(
                account_handle="",
                code="code",
            )
