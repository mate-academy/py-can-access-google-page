from unittest import mock
from unittest.mock import MagicMock

from app.main import can_access_google_page


test_url = "https://google.com"


@mock.patch("app.main.valid_google_url")
@mock.patch("app.main.has_internet_connection")
def test_can_access_google_page_when_connection_and_url_are_valid(
        mock_has_internet_connection: MagicMock,
        mock_valid_google_url: MagicMock
) -> None:
    mock_valid_google_url.return_value = True
    mock_has_internet_connection.return_value = True
    assert can_access_google_page(test_url) == "Accessible"
    mock_valid_google_url.assert_called_once_with(test_url)


@mock.patch("app.main.valid_google_url")
@mock.patch("app.main.has_internet_connection")
def test_not_accessible_when_url_is_invalid(
        mock_has_internet_connection: MagicMock,
        mock_valid_google_url: MagicMock
) -> None:
    mock_valid_google_url.return_value = False
    mock_has_internet_connection.return_value = True
    assert can_access_google_page(test_url) == "Not accessible"
    mock_valid_google_url.assert_called_once_with(test_url)


@mock.patch("app.main.valid_google_url")
@mock.patch("app.main.has_internet_connection")
def test_not_accessible_when_no_internet_connection(
        mock_has_internet_connection: MagicMock,
        mock_valid_google_url: MagicMock
) -> None:
    mock_valid_google_url.return_value = True
    mock_has_internet_connection.return_value = False
    assert can_access_google_page(test_url) == "Not accessible"

    mock_valid_google_url.assert_not_called()
    mock_has_internet_connection.assert_called_once()


@mock.patch("app.main.valid_google_url")
@mock.patch("app.main.has_internet_connection")
def test_not_accessible_when_no_connection_and_invalid_url(
        mock_has_internet_connection: MagicMock,
        mock_valid_google_url: MagicMock
) -> None:
    mock_valid_google_url.return_value = False
    mock_has_internet_connection.return_value = False
    assert can_access_google_page(test_url) == "Not accessible"

    mock_valid_google_url.assert_not_called()
    mock_has_internet_connection.assert_called_once()
