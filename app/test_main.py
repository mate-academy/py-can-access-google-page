from typing import Generator, Tuple
from unittest import mock

import pytest
from app.main import can_access_google_page


@pytest.fixture
def mock_connection_and_url() -> Generator[
    Tuple[mock.Mock, mock.Mock], None, None
]:
    with (mock.patch("app.main.has_internet_connection") as mock_connection,
         mock.patch("app.main.valid_google_url") as mock_url):
        yield mock_connection, mock_url


def test_valid_url_and_connection_exists(
    mock_connection_and_url: Tuple[mock.Mock, mock.Mock]
) -> None:
    mock_connection, mock_url = mock_connection_and_url
    mock_connection.return_value = True
    mock_url.return_value = True

    assert can_access_google_page("https://www.google.com") == "Accessible"

    mock_connection.assert_called_once()
    mock_url.assert_called_once_with("https://www.google.com")


def test_invalid_connection_exists(
    mock_connection_and_url: Tuple[mock.Mock, mock.Mock]
) -> None:
    mock_connection, mock_url = mock_connection_and_url
    mock_connection.return_value = False
    mock_url.return_value = True

    assert can_access_google_page("https://www.google.com") == "Not accessible"

    mock_connection.assert_called_once()
    mock_url.assert_not_called()


def test_invalid_url_exists(
    mock_connection_and_url: Tuple[mock.Mock, mock.Mock]
) -> None:
    mock_connection, mock_url = mock_connection_and_url
    mock_connection.return_value = True
    mock_url.return_value = False

    assert (
        can_access_google_page("https://www.google.comm") == "Not accessible"
    )

    mock_connection.assert_called_once()
    mock_url.assert_called_once_with("https://www.google.comm")
