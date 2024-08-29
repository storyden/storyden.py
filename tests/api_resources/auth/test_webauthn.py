# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from Storyden import Storyden, AsyncStoryden

from Storyden.types.auth import WebauthnMakeResponse

from typing import Any, cast

import os
import pytest
import httpx
from typing_extensions import get_args
from typing import Optional
from respx import MockRouter
from Storyden import Storyden, AsyncStoryden
from tests.utils import assert_matches_type
from Storyden.types.auth import webauthn_make_params

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestWebauthn:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_make(self, client: Storyden) -> None:
        webauthn = client.auth.webauthn.make(
            id="id",
            raw_id="rawId",
            response={"client_data_json": "clientDataJSON"},
            type="type",
        )
        assert_matches_type(WebauthnMakeResponse, webauthn, path=["response"])

    @parametrize
    def test_method_make_with_all_params(self, client: Storyden) -> None:
        webauthn = client.auth.webauthn.make(
            id="id",
            raw_id="rawId",
            response={
                "client_data_json": "clientDataJSON",
                "attestation_object": "attestationObject",
                "authenticator_data": "authenticatorData",
                "signature": "signature",
                "transports": ["string", "string", "string"],
                "user_handle": "userHandle",
            },
            type="type",
            authenticator_attachment="authenticatorAttachment",
            client_extension_results={},
        )
        assert_matches_type(WebauthnMakeResponse, webauthn, path=["response"])

    @parametrize
    def test_raw_response_make(self, client: Storyden) -> None:
        response = client.auth.webauthn.with_raw_response.make(
            id="id",
            raw_id="rawId",
            response={"client_data_json": "clientDataJSON"},
            type="type",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        webauthn = response.parse()
        assert_matches_type(WebauthnMakeResponse, webauthn, path=["response"])

    @parametrize
    def test_streaming_response_make(self, client: Storyden) -> None:
        with client.auth.webauthn.with_streaming_response.make(
            id="id",
            raw_id="rawId",
            response={"client_data_json": "clientDataJSON"},
            type="type",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            webauthn = response.parse()
            assert_matches_type(WebauthnMakeResponse, webauthn, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncWebauthn:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    async def test_method_make(self, async_client: AsyncStoryden) -> None:
        webauthn = await async_client.auth.webauthn.make(
            id="id",
            raw_id="rawId",
            response={"client_data_json": "clientDataJSON"},
            type="type",
        )
        assert_matches_type(WebauthnMakeResponse, webauthn, path=["response"])

    @parametrize
    async def test_method_make_with_all_params(self, async_client: AsyncStoryden) -> None:
        webauthn = await async_client.auth.webauthn.make(
            id="id",
            raw_id="rawId",
            response={
                "client_data_json": "clientDataJSON",
                "attestation_object": "attestationObject",
                "authenticator_data": "authenticatorData",
                "signature": "signature",
                "transports": ["string", "string", "string"],
                "user_handle": "userHandle",
            },
            type="type",
            authenticator_attachment="authenticatorAttachment",
            client_extension_results={},
        )
        assert_matches_type(WebauthnMakeResponse, webauthn, path=["response"])

    @parametrize
    async def test_raw_response_make(self, async_client: AsyncStoryden) -> None:
        response = await async_client.auth.webauthn.with_raw_response.make(
            id="id",
            raw_id="rawId",
            response={"client_data_json": "clientDataJSON"},
            type="type",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        webauthn = await response.parse()
        assert_matches_type(WebauthnMakeResponse, webauthn, path=["response"])

    @parametrize
    async def test_streaming_response_make(self, async_client: AsyncStoryden) -> None:
        async with async_client.auth.webauthn.with_streaming_response.make(
            id="id",
            raw_id="rawId",
            response={"client_data_json": "clientDataJSON"},
            type="type",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            webauthn = await response.parse()
            assert_matches_type(WebauthnMakeResponse, webauthn, path=["response"])

        assert cast(Any, response.is_closed) is True
