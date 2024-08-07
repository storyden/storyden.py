# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from Storyden import Storyden, AsyncStoryden

from Storyden.types.auth import EmailPasswordSigninResponse, EmailPasswordSignupResponse

from typing import Any, cast

import os
import pytest
import httpx
from typing_extensions import get_args
from typing import Optional
from respx import MockRouter
from Storyden import Storyden, AsyncStoryden
from tests.utils import assert_matches_type
from Storyden.types.auth import email_password_signin_params
from Storyden.types.auth import email_password_signup_params

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestEmailPassword:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_signin(self, client: Storyden) -> None:
        email_password = client.auth.email_password.signin(
            email="hello@storyden.org",
            password="password",
        )
        assert_matches_type(EmailPasswordSigninResponse, email_password, path=["response"])

    @parametrize
    def test_method_signin_with_all_params(self, client: Storyden) -> None:
        email_password = client.auth.email_password.signin(
            email="hello@storyden.org",
            password="password",
            handle="Southclaws",
        )
        assert_matches_type(EmailPasswordSigninResponse, email_password, path=["response"])

    @parametrize
    def test_raw_response_signin(self, client: Storyden) -> None:
        response = client.auth.email_password.with_raw_response.signin(
            email="hello@storyden.org",
            password="password",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        email_password = response.parse()
        assert_matches_type(EmailPasswordSigninResponse, email_password, path=["response"])

    @parametrize
    def test_streaming_response_signin(self, client: Storyden) -> None:
        with client.auth.email_password.with_streaming_response.signin(
            email="hello@storyden.org",
            password="password",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            email_password = response.parse()
            assert_matches_type(EmailPasswordSigninResponse, email_password, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_signup(self, client: Storyden) -> None:
        email_password = client.auth.email_password.signup(
            email="hello@storyden.org",
            password="password",
        )
        assert_matches_type(EmailPasswordSignupResponse, email_password, path=["response"])

    @parametrize
    def test_method_signup_with_all_params(self, client: Storyden) -> None:
        email_password = client.auth.email_password.signup(
            email="hello@storyden.org",
            password="password",
            handle="Southclaws",
        )
        assert_matches_type(EmailPasswordSignupResponse, email_password, path=["response"])

    @parametrize
    def test_raw_response_signup(self, client: Storyden) -> None:
        response = client.auth.email_password.with_raw_response.signup(
            email="hello@storyden.org",
            password="password",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        email_password = response.parse()
        assert_matches_type(EmailPasswordSignupResponse, email_password, path=["response"])

    @parametrize
    def test_streaming_response_signup(self, client: Storyden) -> None:
        with client.auth.email_password.with_streaming_response.signup(
            email="hello@storyden.org",
            password="password",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            email_password = response.parse()
            assert_matches_type(EmailPasswordSignupResponse, email_password, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncEmailPassword:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    async def test_method_signin(self, async_client: AsyncStoryden) -> None:
        email_password = await async_client.auth.email_password.signin(
            email="hello@storyden.org",
            password="password",
        )
        assert_matches_type(EmailPasswordSigninResponse, email_password, path=["response"])

    @parametrize
    async def test_method_signin_with_all_params(self, async_client: AsyncStoryden) -> None:
        email_password = await async_client.auth.email_password.signin(
            email="hello@storyden.org",
            password="password",
            handle="Southclaws",
        )
        assert_matches_type(EmailPasswordSigninResponse, email_password, path=["response"])

    @parametrize
    async def test_raw_response_signin(self, async_client: AsyncStoryden) -> None:
        response = await async_client.auth.email_password.with_raw_response.signin(
            email="hello@storyden.org",
            password="password",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        email_password = await response.parse()
        assert_matches_type(EmailPasswordSigninResponse, email_password, path=["response"])

    @parametrize
    async def test_streaming_response_signin(self, async_client: AsyncStoryden) -> None:
        async with async_client.auth.email_password.with_streaming_response.signin(
            email="hello@storyden.org",
            password="password",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            email_password = await response.parse()
            assert_matches_type(EmailPasswordSigninResponse, email_password, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_signup(self, async_client: AsyncStoryden) -> None:
        email_password = await async_client.auth.email_password.signup(
            email="hello@storyden.org",
            password="password",
        )
        assert_matches_type(EmailPasswordSignupResponse, email_password, path=["response"])

    @parametrize
    async def test_method_signup_with_all_params(self, async_client: AsyncStoryden) -> None:
        email_password = await async_client.auth.email_password.signup(
            email="hello@storyden.org",
            password="password",
            handle="Southclaws",
        )
        assert_matches_type(EmailPasswordSignupResponse, email_password, path=["response"])

    @parametrize
    async def test_raw_response_signup(self, async_client: AsyncStoryden) -> None:
        response = await async_client.auth.email_password.with_raw_response.signup(
            email="hello@storyden.org",
            password="password",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        email_password = await response.parse()
        assert_matches_type(EmailPasswordSignupResponse, email_password, path=["response"])

    @parametrize
    async def test_streaming_response_signup(self, async_client: AsyncStoryden) -> None:
        async with async_client.auth.email_password.with_streaming_response.signup(
            email="hello@storyden.org",
            password="password",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            email_password = await response.parse()
            assert_matches_type(EmailPasswordSignupResponse, email_password, path=["response"])

        assert cast(Any, response.is_closed) is True
