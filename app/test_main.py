from unittest import mock
from unittest.mock import MagicMock
from app.main import can_access_google_page


@mock.patch("app.main.valid_google_url")
@mock.patch("app.main.has_internet_connection")
def test_if_valid_url_and_has_connection(
        mock_has_internet_connection: MagicMock,
        mock_valid_google_url: MagicMock
) -> None:
    mock_has_internet_connection.return_value = True
    mock_valid_google_url.return_value = True
    assert (can_access_google_page("https://www.google.de/?hl=de")
            == "Accessible")


@mock.patch("app.main.valid_google_url")
@mock.patch("app.main.has_internet_connection")
def test_if_valid_url_and_has_not_connection(
        mock_has_internet_connection: MagicMock,
        mock_valid_google_url: MagicMock
) -> None:
    mock_has_internet_connection.return_value = False
    mock_valid_google_url.return_value = True
    assert (can_access_google_page("https://www.google.de/?hl=de")
            == "Not accessible")


@mock.patch("app.main.valid_google_url")
@mock.patch("app.main.has_internet_connection")
def test_if_invalid_url_and_has_not_connection(
        mock_has_internet_connection: MagicMock,
        mock_valid_google_url: MagicMock
) -> None:
    mock_has_internet_connection.return_value = False
    mock_valid_google_url.return_value = False
    assert (can_access_google_page("https://www.google.de/?hl=de")
            == "Not accessible")


@mock.patch("app.main.valid_google_url")
@mock.patch("app.main.has_internet_connection")
def test_if_invalid_url_and_has_connection(
        mock_has_internet_connection: MagicMock,
        mock_valid_google_url: MagicMock
) -> None:
    mock_has_internet_connection.return_value = True
    mock_valid_google_url.return_value = False
    assert (can_access_google_page("https://www.google.de/?hl=de")
            == "Not accessible")
