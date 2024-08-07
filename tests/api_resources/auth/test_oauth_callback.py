# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from storyden import Storyden, AsyncStoryden
from tests.utils import assert_matches_type
from storyden.types.auth import OAuthCallbackCreateResponse

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestOAuthCallback:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_create(self, client: Storyden) -> None:
        oauth_callback = client.auth.oauth_callback.create(
            oauth_provider="twitter",
            code="code",
            state="state",
        )
        assert_matches_type(OAuthCallbackCreateResponse, oauth_callback, path=["response"])

    @parametrize
    def test_raw_response_create(self, client: Storyden) -> None:
        response = client.auth.oauth_callback.with_raw_response.create(
            oauth_provider="twitter",
            code="code",
            state="state",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        oauth_callback = response.parse()
        assert_matches_type(OAuthCallbackCreateResponse, oauth_callback, path=["response"])

    @parametrize
    def test_streaming_response_create(self, client: Storyden) -> None:
        with client.auth.oauth_callback.with_streaming_response.create(
            oauth_provider="twitter",
            code="code",
            state="state",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            oauth_callback = response.parse()
            assert_matches_type(OAuthCallbackCreateResponse, oauth_callback, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_create(self, client: Storyden) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `oauth_provider` but received ''"):
            client.auth.oauth_callback.with_raw_response.create(
                oauth_provider="",
                code="code",
                state="state",
            )


class TestAsyncOAuthCallback:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    async def test_method_create(self, async_client: AsyncStoryden) -> None:
        oauth_callback = await async_client.auth.oauth_callback.create(
            oauth_provider="twitter",
            code="code",
            state="state",
        )
        assert_matches_type(OAuthCallbackCreateResponse, oauth_callback, path=["response"])

    @parametrize
    async def test_raw_response_create(self, async_client: AsyncStoryden) -> None:
        response = await async_client.auth.oauth_callback.with_raw_response.create(
            oauth_provider="twitter",
            code="code",
            state="state",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        oauth_callback = await response.parse()
        assert_matches_type(OAuthCallbackCreateResponse, oauth_callback, path=["response"])

    @parametrize
    async def test_streaming_response_create(self, async_client: AsyncStoryden) -> None:
        async with async_client.auth.oauth_callback.with_streaming_response.create(
            oauth_provider="twitter",
            code="code",
            state="state",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            oauth_callback = await response.parse()
            assert_matches_type(OAuthCallbackCreateResponse, oauth_callback, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_create(self, async_client: AsyncStoryden) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `oauth_provider` but received ''"):
            await async_client.auth.oauth_callback.with_raw_response.create(
                oauth_provider="",
                code="code",
                state="state",
            )
