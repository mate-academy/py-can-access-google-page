import pytest
from unittest import mock
from app.main import can_access_google_page


@pytest.fixture()
def mock_google_url() -> None:
    with mock.patch("app.main.valid_google_url") as url_mocked:
        yield url_mocked


@pytest.fixture()
def mock_internet_connection() -> None:
    with mock.patch("app.main.has_internet_connection") as connection_mocked:
        yield connection_mocked


def test_access_url(
        mock_google_url: bool, mock_internet_connection: bool
) -> None:
    mock_google_url.return_value = True
    mock_internet_connection.return_value = True
    assert can_access_google_page("https://mail.google.com/") == "Accessible"


def test_has_no_internet_connection(
    mock_google_url: bool, mock_internet_connection: bool
) -> None:
    mock_google_url.return_value = True
    mock_internet_connection.return_value = False
    assert can_access_google_page(
        "https://mail.google.com/"
    ) == "Not accessible"


def test_url_is_invalid(
        mock_google_url: bool, mock_internet_connection: bool
) -> None:
    mock_google_url.return_value = False
    mock_internet_connection.return_value = True
    assert can_access_google_page(
        "https://mail.google.com/"
    ) == "Not accessible"


def test_url_is_invalid_and_connection_is_lost(
        mock_google_url: bool, mock_internet_connection: bool
) -> None:
    mock_google_url.return_value = False
    mock_internet_connection.return_value = False
    assert can_access_google_page(
        "https://mail.google.com/"
    ) == "Not accessible"

