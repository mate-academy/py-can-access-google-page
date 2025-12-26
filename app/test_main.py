from unittest import mock
from typing import Any
import pytest

from app.main import can_access_google_page


@pytest.fixture()
def mock_valid_google_url() -> Any:
    with mock.patch("app.main.valid_google_url") as mock_valid_google_url:
        yield mock_valid_google_url


@pytest.fixture()
def mock_has_internet_connection() -> Any:
    with mock.patch(
        "app.main.has_internet_connection"
    ) as mock_has_internet_connection:
        yield mock_has_internet_connection


def test_can_access_google_page_when_all_valid(
    mock_valid_google_url: Any,
    mock_has_internet_connection: Any
) -> None:
    mock_valid_google_url.return_value = True
    mock_has_internet_connection.return_value = True
    assert can_access_google_page("https://www.google.com/") == "Accessible"


def test_can_access_google_page_when_only_valid_google_url(
    mock_valid_google_url: Any,
    mock_has_internet_connection: Any
) -> None:
    mock_valid_google_url.return_value = True
    mock_has_internet_connection.return_value = False
    assert can_access_google_page(
        "https://www.google.com/"
    ) == "Not accessible"


def test_can_access_google_page_when_only_valid_has_internet_connection(
    mock_valid_google_url: Any,
    mock_has_internet_connection: Any
) -> None:
    mock_valid_google_url.return_value = False
    mock_has_internet_connection.return_value = True
    assert can_access_google_page(
        "https://www.google.com/"
    ) == "Not accessible"


def test_can_access_google_page_when_only_all_invalid(
    mock_valid_google_url: Any,
    mock_has_internet_connection: Any
) -> None:
    mock_valid_google_url.return_value = False
    mock_has_internet_connection.return_value = False
    assert can_access_google_page(
        "https://www.google.com/"
    ) == "Not accessible"
