# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from storyden import Storyden, AsyncStoryden
from tests.utils import assert_matches_type
from storyden.types.auth.webauthn import AssertCreateResponse, AssertRetrieveResponse

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestAssert:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_create(self, client: Storyden) -> None:
        assert_ = client.auth.webauthn.assert_.create(
            id="id",
            raw_id="rawId",
            response={"client_data_json": "clientDataJSON"},
            type="type",
        )
        assert_matches_type(AssertCreateResponse, assert_, path=["response"])

    @parametrize
    def test_method_create_with_all_params(self, client: Storyden) -> None:
        assert_ = client.auth.webauthn.assert_.create(
            id="id",
            raw_id="rawId",
            response={
                "client_data_json": "clientDataJSON",
                "attestation_object": "attestationObject",
                "transports": ["string", "string", "string"],
                "authenticator_data": "authenticatorData",
                "signature": "signature",
                "user_handle": "userHandle",
            },
            type="type",
            authenticator_attachment="authenticatorAttachment",
            client_extension_results={},
        )
        assert_matches_type(AssertCreateResponse, assert_, path=["response"])

    @parametrize
    def test_raw_response_create(self, client: Storyden) -> None:
        response = client.auth.webauthn.assert_.with_raw_response.create(
            id="id",
            raw_id="rawId",
            response={"client_data_json": "clientDataJSON"},
            type="type",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        assert_ = response.parse()
        assert_matches_type(AssertCreateResponse, assert_, path=["response"])

    @parametrize
    def test_streaming_response_create(self, client: Storyden) -> None:
        with client.auth.webauthn.assert_.with_streaming_response.create(
            id="id",
            raw_id="rawId",
            response={"client_data_json": "clientDataJSON"},
            type="type",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            assert_ = response.parse()
            assert_matches_type(AssertCreateResponse, assert_, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_retrieve(self, client: Storyden) -> None:
        assert_ = client.auth.webauthn.assert_.retrieve(
            "Southclaws",
        )
        assert_matches_type(AssertRetrieveResponse, assert_, path=["response"])

    @parametrize
    def test_raw_response_retrieve(self, client: Storyden) -> None:
        response = client.auth.webauthn.assert_.with_raw_response.retrieve(
            "Southclaws",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        assert_ = response.parse()
        assert_matches_type(AssertRetrieveResponse, assert_, path=["response"])

    @parametrize
    def test_streaming_response_retrieve(self, client: Storyden) -> None:
        with client.auth.webauthn.assert_.with_streaming_response.retrieve(
            "Southclaws",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            assert_ = response.parse()
            assert_matches_type(AssertRetrieveResponse, assert_, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_retrieve(self, client: Storyden) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_handle` but received ''"):
            client.auth.webauthn.assert_.with_raw_response.retrieve(
                "",
            )


class TestAsyncAssert:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    async def test_method_create(self, async_client: AsyncStoryden) -> None:
        assert_ = await async_client.auth.webauthn.assert_.create(
            id="id",
            raw_id="rawId",
            response={"client_data_json": "clientDataJSON"},
            type="type",
        )
        assert_matches_type(AssertCreateResponse, assert_, path=["response"])

    @parametrize
    async def test_method_create_with_all_params(self, async_client: AsyncStoryden) -> None:
        assert_ = await async_client.auth.webauthn.assert_.create(
            id="id",
            raw_id="rawId",
            response={
                "client_data_json": "clientDataJSON",
                "attestation_object": "attestationObject",
                "transports": ["string", "string", "string"],
                "authenticator_data": "authenticatorData",
                "signature": "signature",
                "user_handle": "userHandle",
            },
            type="type",
            authenticator_attachment="authenticatorAttachment",
            client_extension_results={},
        )
        assert_matches_type(AssertCreateResponse, assert_, path=["response"])

    @parametrize
    async def test_raw_response_create(self, async_client: AsyncStoryden) -> None:
        response = await async_client.auth.webauthn.assert_.with_raw_response.create(
            id="id",
            raw_id="rawId",
            response={"client_data_json": "clientDataJSON"},
            type="type",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        assert_ = await response.parse()
        assert_matches_type(AssertCreateResponse, assert_, path=["response"])

    @parametrize
    async def test_streaming_response_create(self, async_client: AsyncStoryden) -> None:
        async with async_client.auth.webauthn.assert_.with_streaming_response.create(
            id="id",
            raw_id="rawId",
            response={"client_data_json": "clientDataJSON"},
            type="type",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            assert_ = await response.parse()
            assert_matches_type(AssertCreateResponse, assert_, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_retrieve(self, async_client: AsyncStoryden) -> None:
        assert_ = await async_client.auth.webauthn.assert_.retrieve(
            "Southclaws",
        )
        assert_matches_type(AssertRetrieveResponse, assert_, path=["response"])

    @parametrize
    async def test_raw_response_retrieve(self, async_client: AsyncStoryden) -> None:
        response = await async_client.auth.webauthn.assert_.with_raw_response.retrieve(
            "Southclaws",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        assert_ = await response.parse()
        assert_matches_type(AssertRetrieveResponse, assert_, path=["response"])

    @parametrize
    async def test_streaming_response_retrieve(self, async_client: AsyncStoryden) -> None:
        async with async_client.auth.webauthn.assert_.with_streaming_response.retrieve(
            "Southclaws",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            assert_ = await response.parse()
            assert_matches_type(AssertRetrieveResponse, assert_, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_retrieve(self, async_client: AsyncStoryden) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_handle` but received ''"):
            await async_client.auth.webauthn.assert_.with_raw_response.retrieve(
                "",
            )
