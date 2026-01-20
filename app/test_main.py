from typing import Any

from unittest import mock
import pytest

from app.main import can_access_google_page


@pytest.fixture()
def mock_valid_url() -> Any:
    with mock.patch("app.main.valid_google_url") as mock_func:
        yield mock_func


@pytest.fixture()
def mock_connection() -> Any:
    with mock.patch("app.main.has_internet_connection") as mock_func:
        yield mock_func


def test_valid_url_and_connection_exists(
        mock_valid_url: Any,
        mock_connection: Any
) -> None:

    mock_connection.return_value = True
    mock_valid_url.return_value = True
    assert can_access_google_page("url") == "Accessible"


def test_invalid_url_and_connection_exists(
        mock_valid_url: Any,
        mock_connection: Any
) -> None:

    mock_connection.return_value = True
    mock_valid_url.return_value = False
    assert can_access_google_page("url") == "Not accessible"


def test_valid_url_and_connection_not_exists(
        mock_valid_url: Any,
        mock_connection: Any
) -> None:

    mock_connection.return_value = False
    mock_valid_url.return_value = True
    assert can_access_google_page("url") == "Not accessible"
