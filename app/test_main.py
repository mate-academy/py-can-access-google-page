from unittest.mock import patch, MagicMock

import pytest

from app.main import can_access_google_page


@pytest.fixture()
def google_url() -> str:
    return "https://www.google.com/"


@patch("app.main.valid_google_url")
@patch("app.main.has_internet_connection")
def test_valid_url_and_connection_exists(
        mock_valid_url: MagicMock,
        mock_has_internet: MagicMock,
        google_url: str
) -> None:
    mock_valid_url.return_value = True
    mock_has_internet.return_value = True

    assert can_access_google_page(google_url) == "Accessible"


@patch("app.main.valid_google_url")
@patch("app.main.has_internet_connection")
def test_invalid_url_and_connection_exists(
        mock_valid_url: MagicMock,
        mock_has_internet: MagicMock,
        google_url: str
) -> None:
    mock_valid_url.return_value = False
    mock_has_internet.return_value = True

    assert can_access_google_page(google_url) == "Not accessible"


@patch("app.main.valid_google_url")
@patch("app.main.has_internet_connection")
def test_valid_url_and_no_connection_exists(
        mock_valid_url: MagicMock,
        mock_has_internet: MagicMock,
        google_url: str
) -> None:
    mock_valid_url.return_value = True
    mock_has_internet.return_value = False

    assert can_access_google_page(google_url) == "Not accessible"


@patch("app.main.valid_google_url")
@patch("app.main.has_internet_connection")
def test_invalid_url_and_no_connection_exists(
        mock_valid_url: MagicMock,
        mock_has_internet: MagicMock,
        google_url: str
) -> None:
    mock_valid_url.return_value = False
    mock_has_internet.return_value = False

    assert can_access_google_page(google_url) == "Not accessible"
