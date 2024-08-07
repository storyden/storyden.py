# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from storyden import Storyden, AsyncStoryden
from tests.utils import assert_matches_type
from storyden.types import (
    ThreadListResponse,
    ThreadCreateResponse,
    ThreadPublishChangesResponse,
    ThreadRetrieveInformationResponse,
)

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestThreads:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_create(self, client: Storyden) -> None:
        thread = client.threads.create(
            body="body",
            category="cc5lnd2s1s4652adtu50",
            title="Hello world!",
            visibility="draft",
        )
        assert_matches_type(ThreadCreateResponse, thread, path=["response"])

    @parametrize
    def test_method_create_with_all_params(self, client: Storyden) -> None:
        thread = client.threads.create(
            body="body",
            category="cc5lnd2s1s4652adtu50",
            title="Hello world!",
            visibility="draft",
            meta={"foo": "bar"},
            tags=["cc5lnd2s1s4652adtu50", "cc5lnd2s1s4652adtu50", "cc5lnd2s1s4652adtu50"],
            url="url",
        )
        assert_matches_type(ThreadCreateResponse, thread, path=["response"])

    @parametrize
    def test_raw_response_create(self, client: Storyden) -> None:
        response = client.threads.with_raw_response.create(
            body="body",
            category="cc5lnd2s1s4652adtu50",
            title="Hello world!",
            visibility="draft",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        thread = response.parse()
        assert_matches_type(ThreadCreateResponse, thread, path=["response"])

    @parametrize
    def test_streaming_response_create(self, client: Storyden) -> None:
        with client.threads.with_streaming_response.create(
            body="body",
            category="cc5lnd2s1s4652adtu50",
            title="Hello world!",
            visibility="draft",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            thread = response.parse()
            assert_matches_type(ThreadCreateResponse, thread, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_list(self, client: Storyden) -> None:
        thread = client.threads.list()
        assert_matches_type(ThreadListResponse, thread, path=["response"])

    @parametrize
    def test_method_list_with_all_params(self, client: Storyden) -> None:
        thread = client.threads.list(
            author="Southclaws",
            categories=["string", "string", "string"],
            page="page",
            q="q",
            tags=["cc5lnd2s1s4652adtu50", "cc5lnd2s1s4652adtu50", "cc5lnd2s1s4652adtu50"],
        )
        assert_matches_type(ThreadListResponse, thread, path=["response"])

    @parametrize
    def test_raw_response_list(self, client: Storyden) -> None:
        response = client.threads.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        thread = response.parse()
        assert_matches_type(ThreadListResponse, thread, path=["response"])

    @parametrize
    def test_streaming_response_list(self, client: Storyden) -> None:
        with client.threads.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            thread = response.parse()
            assert_matches_type(ThreadListResponse, thread, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_archive(self, client: Storyden) -> None:
        thread = client.threads.archive(
            "cc5lnd2s1s4652adtu50-top-10-movies-thread",
        )
        assert thread is None

    @parametrize
    def test_raw_response_archive(self, client: Storyden) -> None:
        response = client.threads.with_raw_response.archive(
            "cc5lnd2s1s4652adtu50-top-10-movies-thread",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        thread = response.parse()
        assert thread is None

    @parametrize
    def test_streaming_response_archive(self, client: Storyden) -> None:
        with client.threads.with_streaming_response.archive(
            "cc5lnd2s1s4652adtu50-top-10-movies-thread",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            thread = response.parse()
            assert thread is None

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_archive(self, client: Storyden) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `thread_mark` but received ''"):
            client.threads.with_raw_response.archive(
                "",
            )

    @parametrize
    def test_method_publish_changes(self, client: Storyden) -> None:
        thread = client.threads.publish_changes(
            thread_mark="cc5lnd2s1s4652adtu50-top-10-movies-thread",
        )
        assert_matches_type(ThreadPublishChangesResponse, thread, path=["response"])

    @parametrize
    def test_method_publish_changes_with_all_params(self, client: Storyden) -> None:
        thread = client.threads.publish_changes(
            thread_mark="cc5lnd2s1s4652adtu50-top-10-movies-thread",
            body="body",
            category="cc5lnd2s1s4652adtu50",
            meta={"foo": "bar"},
            tags=["cc5lnd2s1s4652adtu50", "cc5lnd2s1s4652adtu50", "cc5lnd2s1s4652adtu50"],
            title="Hello world!",
            url="url",
            visibility="draft",
        )
        assert_matches_type(ThreadPublishChangesResponse, thread, path=["response"])

    @parametrize
    def test_raw_response_publish_changes(self, client: Storyden) -> None:
        response = client.threads.with_raw_response.publish_changes(
            thread_mark="cc5lnd2s1s4652adtu50-top-10-movies-thread",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        thread = response.parse()
        assert_matches_type(ThreadPublishChangesResponse, thread, path=["response"])

    @parametrize
    def test_streaming_response_publish_changes(self, client: Storyden) -> None:
        with client.threads.with_streaming_response.publish_changes(
            thread_mark="cc5lnd2s1s4652adtu50-top-10-movies-thread",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            thread = response.parse()
            assert_matches_type(ThreadPublishChangesResponse, thread, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_publish_changes(self, client: Storyden) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `thread_mark` but received ''"):
            client.threads.with_raw_response.publish_changes(
                thread_mark="",
            )

    @parametrize
    def test_method_retrieve_information(self, client: Storyden) -> None:
        thread = client.threads.retrieve_information(
            "cc5lnd2s1s4652adtu50-top-10-movies-thread",
        )
        assert_matches_type(ThreadRetrieveInformationResponse, thread, path=["response"])

    @parametrize
    def test_raw_response_retrieve_information(self, client: Storyden) -> None:
        response = client.threads.with_raw_response.retrieve_information(
            "cc5lnd2s1s4652adtu50-top-10-movies-thread",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        thread = response.parse()
        assert_matches_type(ThreadRetrieveInformationResponse, thread, path=["response"])

    @parametrize
    def test_streaming_response_retrieve_information(self, client: Storyden) -> None:
        with client.threads.with_streaming_response.retrieve_information(
            "cc5lnd2s1s4652adtu50-top-10-movies-thread",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            thread = response.parse()
            assert_matches_type(ThreadRetrieveInformationResponse, thread, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_retrieve_information(self, client: Storyden) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `thread_mark` but received ''"):
            client.threads.with_raw_response.retrieve_information(
                "",
            )


class TestAsyncThreads:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    async def test_method_create(self, async_client: AsyncStoryden) -> None:
        thread = await async_client.threads.create(
            body="body",
            category="cc5lnd2s1s4652adtu50",
            title="Hello world!",
            visibility="draft",
        )
        assert_matches_type(ThreadCreateResponse, thread, path=["response"])

    @parametrize
    async def test_method_create_with_all_params(self, async_client: AsyncStoryden) -> None:
        thread = await async_client.threads.create(
            body="body",
            category="cc5lnd2s1s4652adtu50",
            title="Hello world!",
            visibility="draft",
            meta={"foo": "bar"},
            tags=["cc5lnd2s1s4652adtu50", "cc5lnd2s1s4652adtu50", "cc5lnd2s1s4652adtu50"],
            url="url",
        )
        assert_matches_type(ThreadCreateResponse, thread, path=["response"])

    @parametrize
    async def test_raw_response_create(self, async_client: AsyncStoryden) -> None:
        response = await async_client.threads.with_raw_response.create(
            body="body",
            category="cc5lnd2s1s4652adtu50",
            title="Hello world!",
            visibility="draft",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        thread = await response.parse()
        assert_matches_type(ThreadCreateResponse, thread, path=["response"])

    @parametrize
    async def test_streaming_response_create(self, async_client: AsyncStoryden) -> None:
        async with async_client.threads.with_streaming_response.create(
            body="body",
            category="cc5lnd2s1s4652adtu50",
            title="Hello world!",
            visibility="draft",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            thread = await response.parse()
            assert_matches_type(ThreadCreateResponse, thread, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_list(self, async_client: AsyncStoryden) -> None:
        thread = await async_client.threads.list()
        assert_matches_type(ThreadListResponse, thread, path=["response"])

    @parametrize
    async def test_method_list_with_all_params(self, async_client: AsyncStoryden) -> None:
        thread = await async_client.threads.list(
            author="Southclaws",
            categories=["string", "string", "string"],
            page="page",
            q="q",
            tags=["cc5lnd2s1s4652adtu50", "cc5lnd2s1s4652adtu50", "cc5lnd2s1s4652adtu50"],
        )
        assert_matches_type(ThreadListResponse, thread, path=["response"])

    @parametrize
    async def test_raw_response_list(self, async_client: AsyncStoryden) -> None:
        response = await async_client.threads.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        thread = await response.parse()
        assert_matches_type(ThreadListResponse, thread, path=["response"])

    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncStoryden) -> None:
        async with async_client.threads.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            thread = await response.parse()
            assert_matches_type(ThreadListResponse, thread, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_archive(self, async_client: AsyncStoryden) -> None:
        thread = await async_client.threads.archive(
            "cc5lnd2s1s4652adtu50-top-10-movies-thread",
        )
        assert thread is None

    @parametrize
    async def test_raw_response_archive(self, async_client: AsyncStoryden) -> None:
        response = await async_client.threads.with_raw_response.archive(
            "cc5lnd2s1s4652adtu50-top-10-movies-thread",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        thread = await response.parse()
        assert thread is None

    @parametrize
    async def test_streaming_response_archive(self, async_client: AsyncStoryden) -> None:
        async with async_client.threads.with_streaming_response.archive(
            "cc5lnd2s1s4652adtu50-top-10-movies-thread",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            thread = await response.parse()
            assert thread is None

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_archive(self, async_client: AsyncStoryden) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `thread_mark` but received ''"):
            await async_client.threads.with_raw_response.archive(
                "",
            )

    @parametrize
    async def test_method_publish_changes(self, async_client: AsyncStoryden) -> None:
        thread = await async_client.threads.publish_changes(
            thread_mark="cc5lnd2s1s4652adtu50-top-10-movies-thread",
        )
        assert_matches_type(ThreadPublishChangesResponse, thread, path=["response"])

    @parametrize
    async def test_method_publish_changes_with_all_params(self, async_client: AsyncStoryden) -> None:
        thread = await async_client.threads.publish_changes(
            thread_mark="cc5lnd2s1s4652adtu50-top-10-movies-thread",
            body="body",
            category="cc5lnd2s1s4652adtu50",
            meta={"foo": "bar"},
            tags=["cc5lnd2s1s4652adtu50", "cc5lnd2s1s4652adtu50", "cc5lnd2s1s4652adtu50"],
            title="Hello world!",
            url="url",
            visibility="draft",
        )
        assert_matches_type(ThreadPublishChangesResponse, thread, path=["response"])

    @parametrize
    async def test_raw_response_publish_changes(self, async_client: AsyncStoryden) -> None:
        response = await async_client.threads.with_raw_response.publish_changes(
            thread_mark="cc5lnd2s1s4652adtu50-top-10-movies-thread",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        thread = await response.parse()
        assert_matches_type(ThreadPublishChangesResponse, thread, path=["response"])

    @parametrize
    async def test_streaming_response_publish_changes(self, async_client: AsyncStoryden) -> None:
        async with async_client.threads.with_streaming_response.publish_changes(
            thread_mark="cc5lnd2s1s4652adtu50-top-10-movies-thread",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            thread = await response.parse()
            assert_matches_type(ThreadPublishChangesResponse, thread, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_publish_changes(self, async_client: AsyncStoryden) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `thread_mark` but received ''"):
            await async_client.threads.with_raw_response.publish_changes(
                thread_mark="",
            )

    @parametrize
    async def test_method_retrieve_information(self, async_client: AsyncStoryden) -> None:
        thread = await async_client.threads.retrieve_information(
            "cc5lnd2s1s4652adtu50-top-10-movies-thread",
        )
        assert_matches_type(ThreadRetrieveInformationResponse, thread, path=["response"])

    @parametrize
    async def test_raw_response_retrieve_information(self, async_client: AsyncStoryden) -> None:
        response = await async_client.threads.with_raw_response.retrieve_information(
            "cc5lnd2s1s4652adtu50-top-10-movies-thread",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        thread = await response.parse()
        assert_matches_type(ThreadRetrieveInformationResponse, thread, path=["response"])

    @parametrize
    async def test_streaming_response_retrieve_information(self, async_client: AsyncStoryden) -> None:
        async with async_client.threads.with_streaming_response.retrieve_information(
            "cc5lnd2s1s4652adtu50-top-10-movies-thread",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            thread = await response.parse()
            assert_matches_type(ThreadRetrieveInformationResponse, thread, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_retrieve_information(self, async_client: AsyncStoryden) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `thread_mark` but received ''"):
            await async_client.threads.with_raw_response.retrieve_information(
                "",
            )
