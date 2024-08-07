# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from Storyden import Storyden, AsyncStoryden

from Storyden.types.auth import (
    PasswordCreateResponse,
    PasswordUpdateResponse,
    PasswordSigninResponse,
    PasswordSignupResponse,
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
from Storyden.types.auth import password_create_params
from Storyden.types.auth import password_update_params
from Storyden.types.auth import password_signin_params
from Storyden.types.auth import password_signup_params

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestPassword:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_create(self, client: Storyden) -> None:
        password = client.auth.password.create(
            password="password123",
        )
        assert_matches_type(PasswordCreateResponse, password, path=["response"])

    @parametrize
    def test_raw_response_create(self, client: Storyden) -> None:
        response = client.auth.password.with_raw_response.create(
            password="password123",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        password = response.parse()
        assert_matches_type(PasswordCreateResponse, password, path=["response"])

    @parametrize
    def test_streaming_response_create(self, client: Storyden) -> None:
        with client.auth.password.with_streaming_response.create(
            password="password123",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            password = response.parse()
            assert_matches_type(PasswordCreateResponse, password, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_update(self, client: Storyden) -> None:
        password = client.auth.password.update(
            new="password456",
            old="password123",
        )
        assert_matches_type(PasswordUpdateResponse, password, path=["response"])

    @parametrize
    def test_raw_response_update(self, client: Storyden) -> None:
        response = client.auth.password.with_raw_response.update(
            new="password456",
            old="password123",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        password = response.parse()
        assert_matches_type(PasswordUpdateResponse, password, path=["response"])

    @parametrize
    def test_streaming_response_update(self, client: Storyden) -> None:
        with client.auth.password.with_streaming_response.update(
            new="password456",
            old="password123",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            password = response.parse()
            assert_matches_type(PasswordUpdateResponse, password, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_signin(self, client: Storyden) -> None:
        password = client.auth.password.signin(
            token="password",
            identifier="odin",
        )
        assert_matches_type(PasswordSigninResponse, password, path=["response"])

    @parametrize
    def test_raw_response_signin(self, client: Storyden) -> None:
        response = client.auth.password.with_raw_response.signin(
            token="password",
            identifier="odin",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        password = response.parse()
        assert_matches_type(PasswordSigninResponse, password, path=["response"])

    @parametrize
    def test_streaming_response_signin(self, client: Storyden) -> None:
        with client.auth.password.with_streaming_response.signin(
            token="password",
            identifier="odin",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            password = response.parse()
            assert_matches_type(PasswordSigninResponse, password, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_signup(self, client: Storyden) -> None:
        password = client.auth.password.signup(
            token="password",
            identifier="odin",
        )
        assert_matches_type(PasswordSignupResponse, password, path=["response"])

    @parametrize
    def test_raw_response_signup(self, client: Storyden) -> None:
        response = client.auth.password.with_raw_response.signup(
            token="password",
            identifier="odin",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        password = response.parse()
        assert_matches_type(PasswordSignupResponse, password, path=["response"])

    @parametrize
    def test_streaming_response_signup(self, client: Storyden) -> None:
        with client.auth.password.with_streaming_response.signup(
            token="password",
            identifier="odin",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            password = response.parse()
            assert_matches_type(PasswordSignupResponse, password, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncPassword:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    async def test_method_create(self, async_client: AsyncStoryden) -> None:
        password = await async_client.auth.password.create(
            password="password123",
        )
        assert_matches_type(PasswordCreateResponse, password, path=["response"])

    @parametrize
    async def test_raw_response_create(self, async_client: AsyncStoryden) -> None:
        response = await async_client.auth.password.with_raw_response.create(
            password="password123",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        password = await response.parse()
        assert_matches_type(PasswordCreateResponse, password, path=["response"])

    @parametrize
    async def test_streaming_response_create(self, async_client: AsyncStoryden) -> None:
        async with async_client.auth.password.with_streaming_response.create(
            password="password123",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            password = await response.parse()
            assert_matches_type(PasswordCreateResponse, password, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_update(self, async_client: AsyncStoryden) -> None:
        password = await async_client.auth.password.update(
            new="password456",
            old="password123",
        )
        assert_matches_type(PasswordUpdateResponse, password, path=["response"])

    @parametrize
    async def test_raw_response_update(self, async_client: AsyncStoryden) -> None:
        response = await async_client.auth.password.with_raw_response.update(
            new="password456",
            old="password123",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        password = await response.parse()
        assert_matches_type(PasswordUpdateResponse, password, path=["response"])

    @parametrize
    async def test_streaming_response_update(self, async_client: AsyncStoryden) -> None:
        async with async_client.auth.password.with_streaming_response.update(
            new="password456",
            old="password123",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            password = await response.parse()
            assert_matches_type(PasswordUpdateResponse, password, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_signin(self, async_client: AsyncStoryden) -> None:
        password = await async_client.auth.password.signin(
            token="password",
            identifier="odin",
        )
        assert_matches_type(PasswordSigninResponse, password, path=["response"])

    @parametrize
    async def test_raw_response_signin(self, async_client: AsyncStoryden) -> None:
        response = await async_client.auth.password.with_raw_response.signin(
            token="password",
            identifier="odin",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        password = await response.parse()
        assert_matches_type(PasswordSigninResponse, password, path=["response"])

    @parametrize
    async def test_streaming_response_signin(self, async_client: AsyncStoryden) -> None:
        async with async_client.auth.password.with_streaming_response.signin(
            token="password",
            identifier="odin",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            password = await response.parse()
            assert_matches_type(PasswordSigninResponse, password, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_signup(self, async_client: AsyncStoryden) -> None:
        password = await async_client.auth.password.signup(
            token="password",
            identifier="odin",
        )
        assert_matches_type(PasswordSignupResponse, password, path=["response"])

    @parametrize
    async def test_raw_response_signup(self, async_client: AsyncStoryden) -> None:
        response = await async_client.auth.password.with_raw_response.signup(
            token="password",
            identifier="odin",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        password = await response.parse()
        assert_matches_type(PasswordSignupResponse, password, path=["response"])

    @parametrize
    async def test_streaming_response_signup(self, async_client: AsyncStoryden) -> None:
        async with async_client.auth.password.with_streaming_response.signup(
            token="password",
            identifier="odin",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            password = await response.parse()
            assert_matches_type(PasswordSignupResponse, password, path=["response"])

        assert cast(Any, response.is_closed) is True
