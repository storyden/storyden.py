# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from Storyden import Storyden, AsyncStoryden

from Storyden.types import ProfileRetrieveResponse, ProfileListResponse

from typing import Any, cast

import os
import pytest
import httpx
from typing_extensions import get_args
from typing import Optional
from respx import MockRouter
from Storyden import Storyden, AsyncStoryden
from tests.utils import assert_matches_type
from Storyden.types import profile_list_params

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestProfiles:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_retrieve(self, client: Storyden) -> None:
        profile = client.profiles.retrieve(
            "Southclaws",
        )
        assert_matches_type(ProfileRetrieveResponse, profile, path=["response"])

    @parametrize
    def test_raw_response_retrieve(self, client: Storyden) -> None:
        response = client.profiles.with_raw_response.retrieve(
            "Southclaws",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        profile = response.parse()
        assert_matches_type(ProfileRetrieveResponse, profile, path=["response"])

    @parametrize
    def test_streaming_response_retrieve(self, client: Storyden) -> None:
        with client.profiles.with_streaming_response.retrieve(
            "Southclaws",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            profile = response.parse()
            assert_matches_type(ProfileRetrieveResponse, profile, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_retrieve(self, client: Storyden) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_handle` but received ''"):
            client.profiles.with_raw_response.retrieve(
                "",
            )

    @parametrize
    def test_method_list(self, client: Storyden) -> None:
        profile = client.profiles.list()
        assert_matches_type(ProfileListResponse, profile, path=["response"])

    @parametrize
    def test_method_list_with_all_params(self, client: Storyden) -> None:
        profile = client.profiles.list(
            page="page",
            q="q",
        )
        assert_matches_type(ProfileListResponse, profile, path=["response"])

    @parametrize
    def test_raw_response_list(self, client: Storyden) -> None:
        response = client.profiles.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        profile = response.parse()
        assert_matches_type(ProfileListResponse, profile, path=["response"])

    @parametrize
    def test_streaming_response_list(self, client: Storyden) -> None:
        with client.profiles.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            profile = response.parse()
            assert_matches_type(ProfileListResponse, profile, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncProfiles:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    async def test_method_retrieve(self, async_client: AsyncStoryden) -> None:
        profile = await async_client.profiles.retrieve(
            "Southclaws",
        )
        assert_matches_type(ProfileRetrieveResponse, profile, path=["response"])

    @parametrize
    async def test_raw_response_retrieve(self, async_client: AsyncStoryden) -> None:
        response = await async_client.profiles.with_raw_response.retrieve(
            "Southclaws",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        profile = await response.parse()
        assert_matches_type(ProfileRetrieveResponse, profile, path=["response"])

    @parametrize
    async def test_streaming_response_retrieve(self, async_client: AsyncStoryden) -> None:
        async with async_client.profiles.with_streaming_response.retrieve(
            "Southclaws",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            profile = await response.parse()
            assert_matches_type(ProfileRetrieveResponse, profile, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_retrieve(self, async_client: AsyncStoryden) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_handle` but received ''"):
            await async_client.profiles.with_raw_response.retrieve(
                "",
            )

    @parametrize
    async def test_method_list(self, async_client: AsyncStoryden) -> None:
        profile = await async_client.profiles.list()
        assert_matches_type(ProfileListResponse, profile, path=["response"])

    @parametrize
    async def test_method_list_with_all_params(self, async_client: AsyncStoryden) -> None:
        profile = await async_client.profiles.list(
            page="page",
            q="q",
        )
        assert_matches_type(ProfileListResponse, profile, path=["response"])

    @parametrize
    async def test_raw_response_list(self, async_client: AsyncStoryden) -> None:
        response = await async_client.profiles.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        profile = await response.parse()
        assert_matches_type(ProfileListResponse, profile, path=["response"])

    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncStoryden) -> None:
        async with async_client.profiles.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            profile = await response.parse()
            assert_matches_type(ProfileListResponse, profile, path=["response"])

        assert cast(Any, response.is_closed) is True
