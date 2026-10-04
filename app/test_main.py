from typing import Iterator
from unittest.mock import MagicMock, patch

import pytest

from app import main


@pytest.fixture()
def mocked_valid_google_url() -> Iterator[MagicMock]:
    with patch("app.main.valid_google_url") as mock_test_url:
        yield mock_test_url


@pytest.fixture()
def mocked_has_internet_connection() -> Iterator[MagicMock]:
    with patch("app.main.has_internet_connection") as mock_test_connection:
        yield mock_test_connection


URL = "https://www.google.com"


def test_accessible_when_valid_url_and_connection_exists(
    mocked_valid_google_url: MagicMock,
    mocked_has_internet_connection: MagicMock,
) -> None:
    mocked_valid_google_url.return_value = True
    mocked_has_internet_connection.return_value = True

    assert main.can_access_google_page(URL) == "Accessible"


def test_not_accessible_when_url_is_valid_but_no_connection(
    mocked_valid_google_url: MagicMock,
    mocked_has_internet_connection: MagicMock,
) -> None:
    mocked_valid_google_url.return_value = True
    mocked_has_internet_connection.return_value = False

    assert main.can_access_google_page(URL) == "Not accessible"


def test_not_accessible_when_connection_exists_but_url_is_invalid(
    mocked_valid_google_url: MagicMock,
    mocked_has_internet_connection: MagicMock,
) -> None:
    mocked_valid_google_url.return_value = False
    mocked_has_internet_connection.return_value = True

    assert main.can_access_google_page(URL) == "Not accessible"


def test_not_accessible_when_url_is_invalid_and_no_connection(
    mocked_valid_google_url: MagicMock,
    mocked_has_internet_connection: MagicMock,
) -> None:
    mocked_valid_google_url.return_value = False
    mocked_has_internet_connection.return_value = False

    assert main.can_access_google_page(URL) == "Not accessible"
