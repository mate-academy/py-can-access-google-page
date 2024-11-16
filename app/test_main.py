from unittest.mock import patch, Mock
from app.main import can_access_google_page


@patch("app.main.valid_google_url", return_value=True)
@patch("app.main.has_internet_connection", return_value=True)
def test_can_access_google_page_accessible(
    mock_valid_google_url: Mock, mock_has_internet_connection: Mock
) -> None:
    assert can_access_google_page("https://www.google.com") == "Accessible"


@patch("app.main.valid_google_url", return_value=True)
@patch("app.main.has_internet_connection", return_value=False)
def test_can_access_google_page_accessible_when_internet_is_false() -> None:
    assert can_access_google_page("https://www.google.com") == "Not accessible"


@patch("app.main.valid_google_url", return_value=False)
@patch("app.main.has_internet_connection", return_value=True)
def test_can_access_google_page_accessible_when_url_is_false() -> None:
    assert can_access_google_page("https://www.google.com") == "Not accessible"
