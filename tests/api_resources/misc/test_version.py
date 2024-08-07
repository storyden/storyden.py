# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from Storyden import Storyden, AsyncStoryden

from Storyden.types.misc import VersionRetrieveResponse

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


class TestVersion:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_retrieve(self, client: Storyden) -> None:
        version = client.misc.version.retrieve()
        assert_matches_type(str, version, path=["response"])

    @parametrize
    def test_raw_response_retrieve(self, client: Storyden) -> None:
        response = client.misc.version.with_raw_response.retrieve()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        version = response.parse()
        assert_matches_type(str, version, path=["response"])

    @parametrize
    def test_streaming_response_retrieve(self, client: Storyden) -> None:
        with client.misc.version.with_streaming_response.retrieve() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            version = response.parse()
            assert_matches_type(str, version, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncVersion:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    async def test_method_retrieve(self, async_client: AsyncStoryden) -> None:
        version = await async_client.misc.version.retrieve()
        assert_matches_type(str, version, path=["response"])

    @parametrize
    async def test_raw_response_retrieve(self, async_client: AsyncStoryden) -> None:
        response = await async_client.misc.version.with_raw_response.retrieve()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        version = await response.parse()
        assert_matches_type(str, version, path=["response"])

    @parametrize
    async def test_streaming_response_retrieve(self, async_client: AsyncStoryden) -> None:
        async with async_client.misc.version.with_streaming_response.retrieve() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            version = await response.parse()
            assert_matches_type(str, version, path=["response"])

        assert cast(Any, response.is_closed) is True
