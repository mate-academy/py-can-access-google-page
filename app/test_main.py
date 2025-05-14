from unittest.mock import patch, MagicMock

from app.main import can_access_google_page


@patch("app.main.valid_google_url")
@patch("app.main.has_internet_connection")
def test_can_access_google_page(has_internet_connection: MagicMock,
                                valid_google_url: MagicMock) -> None:
    url = "https://www.google.com"

    has_internet_connection.return_value = True
    valid_google_url.return_value = True
    assert can_access_google_page(url) == "Accessible"

    has_internet_connection.return_value = False
    valid_google_url.return_value = True
    assert can_access_google_page(url) == "Not accessible"

    has_internet_connection.return_value = True
    valid_google_url.return_value = False
    assert can_access_google_page(url) == "Not accessible"
