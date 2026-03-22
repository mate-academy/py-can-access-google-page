from unittest import mock
from app.main import can_access_google_page


@mock.patch("app.main.has_internet_connection")
@mock.patch("app.main.valid_google_url")
def test_valid_and_connection_return_accessible(
        mock_valid: str,
        mock_connection: str
) -> None:
    mock_valid.return_value = True
    mock_connection.return_value = True
    result = can_access_google_page("https://www.google.com")
    assert result == "Accessible"


@mock.patch("app.main.has_internet_connection")
@mock.patch("app.main.valid_google_url")
def test_invalid_return_not_accessible(
        mock_valid: str,
        mock_connection: str
) -> None:
    mock_valid.return_value = False
    mock_connection.return_value = True
    assert can_access_google_page("bad url") == "Not accessible"


@mock.patch("app.main.has_internet_connection")
@mock.patch("app.main.valid_google_url")
def test_no_connection_returns_not_accessible(
        mock_valid: str,
        mock_connection: str
) -> None:
    mock_valid.return_value = True
    mock_connection.return_value = False
    assert can_access_google_page("https://www.google.com") == "Not accessible"
