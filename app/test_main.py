from unittest.mock import patch, MagicMock
from app.main import can_access_google_page


@patch("app.main.valid_google_url", return_value=True)
@patch("app.main.has_internet_connection", return_value=True)
def test_can_access_google_page_accessible(
        mock_conn: MagicMock,
        mock_valid: MagicMock
) -> None:
    assert can_access_google_page("https://google.com") == "Accessible"


@patch("app.main.valid_google_url", return_value=False)
@patch("app.main.has_internet_connection", return_value=True)
def test_can_access_google_page_invalid_url(
        mock_conn: MagicMock,
        mock_valid: MagicMock
) -> None:
    assert can_access_google_page("https://wrong.com") == "Not accessible"


@patch("app.main.valid_google_url", return_value=True)
@patch("app.main.has_internet_connection", return_value=False)
def test_can_access_google_page_no_internet(
        mock_conn: MagicMock,
        mock_valid: MagicMock
) -> None:
    assert can_access_google_page("https://google.com") == "Not accessible"


@patch("app.main.valid_google_url", return_value=False)
@patch("app.main.has_internet_connection", return_value=False)
def test_can_access_google_page_no_internet_and_invalid_url(
        mock_conn: MagicMock,
        mock_valid: MagicMock
) -> None:
    assert can_access_google_page("https://wrong.com") == "Not accessible"
