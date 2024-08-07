# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from Storyden import Storyden, AsyncStoryden

from Storyden.types.auth import EmailSigninResponse, EmailSignupResponse, EmailVerifyResponse

from typing import Any, cast

import os
import pytest
import httpx
from typing_extensions import get_args
from typing import Optional
from respx import MockRouter
from Storyden import Storyden, AsyncStoryden
from tests.utils import assert_matches_type
from Storyden.types.auth import email_signin_params
from Storyden.types.auth import email_signup_params
from Storyden.types.auth import email_verify_params

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestEmail:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_signin(self, client: Storyden) -> None:
        email = client.auth.email.signin(
            email="hello@storyden.org",
        )
        assert_matches_type(EmailSigninResponse, email, path=["response"])

    @parametrize
    def test_method_signin_with_all_params(self, client: Storyden) -> None:
        email = client.auth.email.signin(
            email="hello@storyden.org",
            handle="Southclaws",
        )
        assert_matches_type(EmailSigninResponse, email, path=["response"])

    @parametrize
    def test_raw_response_signin(self, client: Storyden) -> None:
        response = client.auth.email.with_raw_response.signin(
            email="hello@storyden.org",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        email = response.parse()
        assert_matches_type(EmailSigninResponse, email, path=["response"])

    @parametrize
    def test_streaming_response_signin(self, client: Storyden) -> None:
        with client.auth.email.with_streaming_response.signin(
            email="hello@storyden.org",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            email = response.parse()
            assert_matches_type(EmailSigninResponse, email, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_signup(self, client: Storyden) -> None:
        email = client.auth.email.signup(
            email="hello@storyden.org",
        )
        assert_matches_type(EmailSignupResponse, email, path=["response"])

    @parametrize
    def test_method_signup_with_all_params(self, client: Storyden) -> None:
        email = client.auth.email.signup(
            email="hello@storyden.org",
            handle="Southclaws",
        )
        assert_matches_type(EmailSignupResponse, email, path=["response"])

    @parametrize
    def test_raw_response_signup(self, client: Storyden) -> None:
        response = client.auth.email.with_raw_response.signup(
            email="hello@storyden.org",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        email = response.parse()
        assert_matches_type(EmailSignupResponse, email, path=["response"])

    @parametrize
    def test_streaming_response_signup(self, client: Storyden) -> None:
        with client.auth.email.with_streaming_response.signup(
            email="hello@storyden.org",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            email = response.parse()
            assert_matches_type(EmailSignupResponse, email, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_verify(self, client: Storyden) -> None:
        email = client.auth.email.verify(
            code="728562",
            email="email",
        )
        assert_matches_type(EmailVerifyResponse, email, path=["response"])

    @parametrize
    def test_raw_response_verify(self, client: Storyden) -> None:
        response = client.auth.email.with_raw_response.verify(
            code="728562",
            email="email",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        email = response.parse()
        assert_matches_type(EmailVerifyResponse, email, path=["response"])

    @parametrize
    def test_streaming_response_verify(self, client: Storyden) -> None:
        with client.auth.email.with_streaming_response.verify(
            code="728562",
            email="email",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            email = response.parse()
            assert_matches_type(EmailVerifyResponse, email, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncEmail:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    async def test_method_signin(self, async_client: AsyncStoryden) -> None:
        email = await async_client.auth.email.signin(
            email="hello@storyden.org",
        )
        assert_matches_type(EmailSigninResponse, email, path=["response"])

    @parametrize
    async def test_method_signin_with_all_params(self, async_client: AsyncStoryden) -> None:
        email = await async_client.auth.email.signin(
            email="hello@storyden.org",
            handle="Southclaws",
        )
        assert_matches_type(EmailSigninResponse, email, path=["response"])

    @parametrize
    async def test_raw_response_signin(self, async_client: AsyncStoryden) -> None:
        response = await async_client.auth.email.with_raw_response.signin(
            email="hello@storyden.org",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        email = await response.parse()
        assert_matches_type(EmailSigninResponse, email, path=["response"])

    @parametrize
    async def test_streaming_response_signin(self, async_client: AsyncStoryden) -> None:
        async with async_client.auth.email.with_streaming_response.signin(
            email="hello@storyden.org",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            email = await response.parse()
            assert_matches_type(EmailSigninResponse, email, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_signup(self, async_client: AsyncStoryden) -> None:
        email = await async_client.auth.email.signup(
            email="hello@storyden.org",
        )
        assert_matches_type(EmailSignupResponse, email, path=["response"])

    @parametrize
    async def test_method_signup_with_all_params(self, async_client: AsyncStoryden) -> None:
        email = await async_client.auth.email.signup(
            email="hello@storyden.org",
            handle="Southclaws",
        )
        assert_matches_type(EmailSignupResponse, email, path=["response"])

    @parametrize
    async def test_raw_response_signup(self, async_client: AsyncStoryden) -> None:
        response = await async_client.auth.email.with_raw_response.signup(
            email="hello@storyden.org",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        email = await response.parse()
        assert_matches_type(EmailSignupResponse, email, path=["response"])

    @parametrize
    async def test_streaming_response_signup(self, async_client: AsyncStoryden) -> None:
        async with async_client.auth.email.with_streaming_response.signup(
            email="hello@storyden.org",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            email = await response.parse()
            assert_matches_type(EmailSignupResponse, email, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_verify(self, async_client: AsyncStoryden) -> None:
        email = await async_client.auth.email.verify(
            code="728562",
            email="email",
        )
        assert_matches_type(EmailVerifyResponse, email, path=["response"])

    @parametrize
    async def test_raw_response_verify(self, async_client: AsyncStoryden) -> None:
        response = await async_client.auth.email.with_raw_response.verify(
            code="728562",
            email="email",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        email = await response.parse()
        assert_matches_type(EmailVerifyResponse, email, path=["response"])

    @parametrize
    async def test_streaming_response_verify(self, async_client: AsyncStoryden) -> None:
        async with async_client.auth.email.with_streaming_response.verify(
            code="728562",
            email="email",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            email = await response.parse()
            assert_matches_type(EmailVerifyResponse, email, path=["response"])

        assert cast(Any, response.is_closed) is True
