from typing import Callable
from unittest import mock

import pytest

from app.main import can_access_google_page


@pytest.fixture()
def mock_valid_url() -> None:
    with mock.patch("app.main.valid_google_url") as mocked_url:
        yield mocked_url


@pytest.fixture()
def mock_internet_connection() -> None:
    with mock.patch("app.main.has_internet_connection") as mocked_connection:
        yield mocked_connection


def test_with_correct_date(
        mock_internet_connection: Callable,
        mock_valid_url: Callable
) -> None:
    mock_internet_connection.return_value = True
    mock_valid_url.return_value = True
    result = can_access_google_page("https://some_page.ma")
    assert result == "Accessible"


def test_with_wrong_url(
        mock_internet_connection: Callable,
        mock_valid_url: Callable
) -> None:
    mock_internet_connection.return_value = True
    mock_valid_url.return_value = False
    result = can_access_google_page("https://some_page.ma")
    assert result == "Not accessible"


def test_without_internet_connection(
        mock_internet_connection: Callable,
        mock_valid_url: Callable
) -> None:
    mock_internet_connection.return_value = False
    mock_valid_url.return_value = True
    result = can_access_google_page("https://some_page.ma")
    assert result == "Not accessible"


def test_without_internet_with_wrong_url(
        mock_internet_connection: Callable,
        mock_valid_url: Callable
) -> None:
    mock_internet_connection.return_value = False
    mock_valid_url.return_value = False
    result = can_access_google_page("https://some_page.ma")
    assert result == "Not accessible"
