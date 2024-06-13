from typing import Callable

from app.main import can_access_google_page
from unittest import mock

import pytest


@pytest.fixture
def url() -> str:
    return "https://google.com"


@pytest.fixture
def mock_internet_connection() -> mock.MagicMock:
    with mock.patch("app.main.has_internet_connection") as mock_connection:
        yield mock_connection


@pytest.fixture
def mock_valid_google_url() -> mock.MagicMock:
    with mock.patch("app.main.valid_google_url") as mock_valid_url:
        yield mock_valid_url


@pytest.mark.parametrize(
    "connection_return,valid_url_return,expected_result",
    [
        (True, False, "Not accessible"),
        (False, True, "Not accessible"),
        (False, False, "Not accessible"),
        (True, True, "Accessible")
    ],
    ids=[
        "can't access only with connection",
        "can't access only with valid url",
        "can't access with no connection and valid url",
        "can access with connection and valid url"
    ]
)
def test_should_access_google_page(
        mock_internet_connection: Callable,
        mock_valid_google_url: Callable,
        connection_return: bool,
        valid_url_return: bool,
        expected_result: str,
        url: str) -> None:
    mock_internet_connection.return_value = connection_return
    mock_valid_google_url.return_value = valid_url_return
    assert can_access_google_page(url) == expected_result
