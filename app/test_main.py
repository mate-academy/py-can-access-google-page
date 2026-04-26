from unittest.mock import patch, Mock
from app.main import can_access_google_page


@patch("app.main.valid_google_url", return_value=True)
@patch("app.main.has_internet_connection", return_value=True)
def test_accessible(mock_internet: Mock, mock_url: Mock) -> None:
    result = can_access_google_page("https://google.com")
    assert result == "Accessible"


@patch("app.main.valid_google_url", return_value=False)
@patch("app.main.has_internet_connection", return_value=True)
def test_not_accessible_invalid_url(
        mock_internet: Mock, mock_url: Mock
) -> None:
    result = can_access_google_page("https://bad.com")
    assert result == "Not accessible"


@patch("app.main.valid_google_url", return_value=True)
@patch("app.main.has_internet_connection", return_value=False)
def test_not_accessible_no_internet(
        mock_internet: Mock, mock_url: Mock
) -> None:
    result = can_access_google_page("https://google.com")
    assert result == "Not accessible"


@patch("app.main.valid_google_url", return_value=False)
@patch("app.main.has_internet_connection", return_value=False)
def test_not_accessible_both_fail(
        mock_internet: Mock, mock_url: Mock
) -> None:
    result = can_access_google_page("https://bad.com")
    assert result == "Not accessible"
