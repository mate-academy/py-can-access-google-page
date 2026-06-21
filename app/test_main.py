from unittest import mock
from unittest.mock import MagicMock
from app.main import can_access_google_page


@mock.patch("app.main.valid_google_url")
@mock.patch("app.main.has_internet_connection")
def test_can_access_google_page_with_valid_url_and_internet(
    mock_valid_google_url: MagicMock,
    mock_has_internet_connection: MagicMock
) -> None:
    mock_valid_google_url.return_value = True
    mock_has_internet_connection.return_value = True

    assert can_access_google_page(
        "google.com"
    ) == "Accessible"


@mock.patch("app.main.valid_google_url")
@mock.patch("app.main.has_internet_connection")
def test_can_access_google_page_with_invalid_url_and_valid_connection(
    mock_valid_google_url: MagicMock,
    mock_has_internet_connection: MagicMock
) -> None:
    mock_valid_google_url.return_value = False
    mock_has_internet_connection.return_value = True

    assert can_access_google_page(
        "google.com"
    ) == "Not accessible"


@mock.patch("app.main.valid_google_url")
@mock.patch("app.main.has_internet_connection")
def test_can_access_google_page_with_valid_url_and_invalid_connection(
    mock_valid_google_url: MagicMock,
    mock_has_internet_connection: MagicMock
) -> None:
    mock_valid_google_url.return_value = True
    mock_has_internet_connection.return_value = False

    assert can_access_google_page(
        "google.com"
    ) == "Not accessible"


@mock.patch("app.main.valid_google_url")
@mock.patch("app.main.has_internet_connection")
def test_can_access_google_page_with_invalid_url_and_invalid_connection(
    mock_valid_google_url: MagicMock,
    mock_has_internet_connection: MagicMock
) -> None:
    mock_valid_google_url.return_value = False
    mock_has_internet_connection.return_value = False

    assert can_access_google_page(
        "google.com"
    ) == "Not accessible"
