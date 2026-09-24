from unittest.mock import patch, MagicMock
from app.main import can_access_google_page


@patch("app.main.has_internet_connection", return_value=True)
@patch("app.main.valid_google_url", return_value=True)
def test_valid_url_and_connection_exists_returns_accessible(
        mock_url: MagicMock,
        mock_internet: MagicMock
) -> None:
    assert can_access_google_page("https://google.com") == "Accessible"


@patch("app.main.has_internet_connection", return_value=False)
@patch("app.main.valid_google_url", return_value=True)
def test_valid_url_and_no_connection_exists_returns_not_accessible(
        mock_url: MagicMock,
        mock_internet: MagicMock
) -> None:
    assert can_access_google_page("https://google.com") == "Not accessible"


@patch("app.main.has_internet_connection", return_value=True)
@patch("app.main.valid_google_url", return_value=False)
def test_invalid_url_and_connection_exists_returns_not_accessible(
        mock_url: MagicMock,
        mock_internet: MagicMock
) -> None:
    assert can_access_google_page("https://google.com") == "Not accessible"


@patch("app.main.has_internet_connection", return_value=False)
@patch("app.main.valid_google_url", return_value=False)
def test_invalid_url_and_no_connection_exists_returns_not_accessible(
        mock_url: MagicMock,
        mock_internet: MagicMock
) -> None:
    assert can_access_google_page("https://google.com") == "Not accessible"
