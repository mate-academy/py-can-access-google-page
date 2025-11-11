from unittest import mock
from unittest.mock import MagicMock

from app.main import can_access_google_page


test_url = "https://google.com"


@mock.patch("app.main.valid_google_url")
@mock.patch("app.main.has_internet_connection")
def test_when_both_true(
        mock_has_internet_connection: MagicMock,
        mock_valid_google_url: MagicMock
) -> None:
    mock_valid_google_url.return_value = True
    mock_has_internet_connection.return_value = True
    assert can_access_google_page(test_url) == "Accessible"
    mock_valid_google_url.assert_called_once_with(test_url)


@mock.patch("app.main.valid_google_url")
@mock.patch("app.main.has_internet_connection")
def test_when_valid_url_false(
        mock_has_internet_connection: MagicMock,
        mock_valid_google_url: MagicMock
) -> None:
    mock_valid_google_url.return_value = False
    mock_has_internet_connection.return_value = True
    assert can_access_google_page(test_url) == "Not accessible"
    mock_valid_google_url.assert_called_once_with(test_url)


@mock.patch("app.main.valid_google_url")
@mock.patch("app.main.has_internet_connection")
def test_when_connection_false(
        mock_has_internet_connection: MagicMock,
        mock_valid_google_url: MagicMock
) -> None:
    mock_valid_google_url.return_value = True
    mock_has_internet_connection.return_value = False
    assert can_access_google_page(test_url) == "Not accessible"


@mock.patch("app.main.valid_google_url")
@mock.patch("app.main.has_internet_connection")
def test_when_both_false(
        mock_has_internet_connection: MagicMock,
        mock_valid_google_url: MagicMock
) -> None:
    mock_valid_google_url.return_value = False
    mock_has_internet_connection.return_value = False
    assert can_access_google_page(test_url) == "Not accessible"
