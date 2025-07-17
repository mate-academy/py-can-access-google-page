from unittest import mock
from unittest.mock import MagicMock
from app.main import can_access_google_page


@mock.patch("app.main.valid_google_url", return_value=True)
@mock.patch("app.main.has_internet_connection", return_value=True)
def test_valid_url_has_internet_connection(
        mock_internet: MagicMock,
        mock_valid_url: MagicMock
) -> None:
    result = can_access_google_page("www.google.com")
    assert result == "Accessible"


@mock.patch("app.main.valid_google_url", return_value=False)
@mock.patch("app.main.has_internet_connection", return_value=True)
def test_cannot_access_with_invalid_google_url(
        mock_internet: MagicMock,
        mock_valid_url: MagicMock
) -> None:
    result = can_access_google_page("www.google.com")
    assert result == "Not accessible"


@mock.patch("app.main.valid_google_url", return_value=True)
@mock.patch("app.main.has_internet_connection", return_value=False)
def test_cannot_access_without_internet_connection(
        mock_internet: MagicMock,
        mock_valid_url: MagicMock
) -> None:
    result = can_access_google_page("www.google.com")
    assert result == "Not accessible"
