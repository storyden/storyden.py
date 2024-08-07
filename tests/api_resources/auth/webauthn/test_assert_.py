# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from Storyden import Storyden, AsyncStoryden

from Storyden.types.auth.webauthn import AssertStartResponse

from typing import Any, cast

import os
import pytest
import httpx
from typing_extensions import get_args
from typing import Optional
from respx import MockRouter
from Storyden import Storyden, AsyncStoryden
from tests.utils import assert_matches_type

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestAssert:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_start(self, client: Storyden) -> None:
        assert_ = client.auth.webauthn.assert_.start(
            "Southclaws",
        )
        assert_matches_type(AssertStartResponse, assert_, path=["response"])

    @parametrize
    def test_raw_response_start(self, client: Storyden) -> None:
        response = client.auth.webauthn.assert_.with_raw_response.start(
            "Southclaws",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        assert_ = response.parse()
        assert_matches_type(AssertStartResponse, assert_, path=["response"])

    @parametrize
    def test_streaming_response_start(self, client: Storyden) -> None:
        with client.auth.webauthn.assert_.with_streaming_response.start(
            "Southclaws",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            assert_ = response.parse()
            assert_matches_type(AssertStartResponse, assert_, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_start(self, client: Storyden) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_handle` but received ''"):
            client.auth.webauthn.assert_.with_raw_response.start(
                "",
            )


class TestAsyncAssert:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    async def test_method_start(self, async_client: AsyncStoryden) -> None:
        assert_ = await async_client.auth.webauthn.assert_.start(
            "Southclaws",
        )
        assert_matches_type(AssertStartResponse, assert_, path=["response"])

    @parametrize
    async def test_raw_response_start(self, async_client: AsyncStoryden) -> None:
        response = await async_client.auth.webauthn.assert_.with_raw_response.start(
            "Southclaws",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        assert_ = await response.parse()
        assert_matches_type(AssertStartResponse, assert_, path=["response"])

    @parametrize
    async def test_streaming_response_start(self, async_client: AsyncStoryden) -> None:
        async with async_client.auth.webauthn.assert_.with_streaming_response.start(
            "Southclaws",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            assert_ = await response.parse()
            assert_matches_type(AssertStartResponse, assert_, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_start(self, async_client: AsyncStoryden) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_handle` but received ''"):
            await async_client.auth.webauthn.assert_.with_raw_response.start(
                "",
            )
