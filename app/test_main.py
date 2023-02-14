import pytest

from typing import Callable
from unittest import mock

from app.main import can_access_google_page


@pytest.fixture()
def mock_google_url() -> None:
    with mock.patch(
            "app.main.valid_google_url"
    ) as mock_test_url:
        yield mock_test_url


@pytest.fixture()
def mock_internet_connection() -> None:
    with mock.patch(
            "app.main.has_internet_connection"
    ) as mock_test_connection:
        yield mock_test_connection


@pytest.mark.parametrize(
    "url, answer, mock_google_url_value, mock_internet_connection_value",
    [
        ("www.googl.com", "Not accessible", True, False),
        ("www.googl.com", "Not accessible", False, True),
        ("www.googl.com", "Not accessible", False, False),
        ("www.googl.com", "Accessible", True, True),
    ]
)
def test_can_access_google_page(
        mock_google_url: Callable,
        mock_internet_connection: Callable,
        url: str,
        answer: str,
        mock_google_url_value: bool,
        mock_internet_connection_value: bool
) -> None:
    mock_google_url.return_value = mock_google_url_value
    mock_internet_connection.return_value = mock_internet_connection_value
    assert can_access_google_page(url) == answer
