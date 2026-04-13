from typing import Generator
from unittest import mock
from unittest.mock import MagicMock

import pytest

from app.main import can_access_google_page

url = "https://www.google.com"


@pytest.fixture
def mocks() -> Generator[tuple[MagicMock, MagicMock], None, None]:
    with (
        mock.patch("app.main.valid_google_url") as mock_url,
        mock.patch("app.main.has_internet_connection") as mock_internet,
    ):
        yield mock_url, mock_internet


def test_accessible(
        mocks: tuple[MagicMock, MagicMock]
) -> None:
    mock_url, mock_internet = mocks
    mock_url.return_value = True
    mock_internet.return_value = True
    assert can_access_google_page(url) == "Accessible"


def test_not_accessible_invalid_url(
        mocks: tuple[MagicMock, MagicMock]
) -> None:
    mock_url, mock_internet = mocks
    mock_url.return_value = False
    mock_internet.return_value = True

    assert can_access_google_page(url) == "Not accessible"


def test_not_accessible_no_internet(
        mocks: tuple[MagicMock, MagicMock]
) -> None:
    mock_url, mock_internet = mocks
    mock_url.return_value = True
    mock_internet.return_value = False

    assert can_access_google_page(url) == "Not accessible"


def test_not_accessible_both_false(
        mocks: tuple[MagicMock, MagicMock]
) -> None:
    mock_url, mock_internet = mocks
    mock_url.return_value = False
    mock_internet.return_value = False

    assert can_access_google_page(url) == "Not accessible"
