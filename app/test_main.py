from typing import Any
import pytest
from unittest import mock
from app.main import can_access_google_page


@pytest.fixture()
def mock_valid_url() -> Any:
    with mock.patch("app.main.valid_google_url") as valid_url:
        yield valid_url


@pytest.fixture()
def mock_has_internet_connection() -> Any:
    with mock.patch("app.main.has_internet_connection") as mock_connection:
        yield mock_connection


@pytest.mark.parametrize(
    "is_connection, is_valid_url, expected_result",
    [
        (False, False, "Not accessible"),
        (True, False, "Not accessible"),
        (False, True, "Not accessible"),
        (True, True, "Accessible")
    ]
)
def test_can_access_google_page(
        mock_valid_url: Any,
        mock_has_internet_connection: Any,
        is_connection: bool,
        is_valid_url: bool,
        expected_result: str
) -> None:
    mock_valid_url.return_value = is_valid_url
    mock_has_internet_connection.return_value = is_connection
    assert can_access_google_page("") == expected_result


def test_valid_google_url_has_been_started(
        mock_valid_url: Any,
        mock_has_internet_connection: Any) -> None:
    can_access_google_page("")
    mock_valid_url.assert_called_once()


def test_has_internet_connection_has_been_started(
        mock_has_internet_connection: Any,
        mock_valid_url: Any) -> None:
    can_access_google_page("")
    mock_has_internet_connection.assert_called_once()
