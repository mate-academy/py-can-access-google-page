from collections.abc import Generator
from typing import Any
from unittest import mock
from unittest.mock import MagicMock

import pytest

from app.main import can_access_google_page


@pytest.fixture()
def has_internet_connection_mocked() -> Generator[MagicMock, Any, Any]:
    with mock.patch("app.main.has_internet_connection") as internet_mock:
        internet_mock.return_value = True
        yield internet_mock


@pytest.fixture()
def valid_google_url_mocked() -> Generator[MagicMock, Any, Any]:
    with mock.patch("app.main.valid_google_url") as valid_url_mock:
        valid_url_mock.return_value = True
        yield valid_url_mock


def test_with_valid_url_and_internet(
    valid_google_url_mocked: MagicMock,
    has_internet_connection_mocked: MagicMock,
) -> None:
    assert can_access_google_page("https://example.com") == "Accessible"


def test_with_invalid_url_and_internet(
    valid_google_url_mocked: MagicMock,
    has_internet_connection_mocked: MagicMock,
) -> None:
    valid_google_url_mocked.return_value = False
    assert can_access_google_page("https://example.com") == "Not accessible"


def test_with_valid_url_and_no_internet(
    valid_google_url_mocked: MagicMock,
    has_internet_connection_mocked: MagicMock,
) -> None:
    has_internet_connection_mocked.return_value = False
    assert can_access_google_page("https://example.com") == "Not accessible"
