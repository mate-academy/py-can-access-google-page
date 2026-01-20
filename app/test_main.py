from unittest import mock
from unittest.mock import MagicMock

from app.main import can_access_google_page

url = "http://google.com/"


@mock.patch("app.main.has_internet_connection")
@mock.patch("app.main.valid_google_url")
def test_when_only_valid_url_returned_false(
        mock_valid_url: MagicMock,
        mock_has_internet: MagicMock
) -> None:
    mock_valid_url.return_value = False
    mock_has_internet.return_value = True

    result = can_access_google_page(url)
    assert result == "Not accessible"


@mock.patch("app.main.has_internet_connection")
@mock.patch("app.main.valid_google_url")
def test_when_only_internet_connection_returned_true(
        mock_valid_url: MagicMock,
        mock_has_internet: MagicMock
) -> None:
    mock_valid_url.return_value = True
    mock_has_internet.return_value = False

    result = can_access_google_page(url)
    assert result == "Not accessible"


@mock.patch("app.main.has_internet_connection")
@mock.patch("app.main.valid_google_url")
def test_valid_url_and_connection_exists(
        mock_valid_url: MagicMock,
        mock_has_internet: MagicMock
) -> None:
    mock_valid_url.return_value = True
    mock_has_internet.return_value = True

    result = can_access_google_page(url)
    assert result == "Accessible"
