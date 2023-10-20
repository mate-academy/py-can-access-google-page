from unittest.mock import patch
from app.main import can_access_google_page


@patch("app.main.valid_google_url", return_value=True)
@patch("app.main.has_internet_connection", return_value=True)
def test_can_access_google_page(
        mock_has_internet_connection: bool,
        mock_valid_google_url: bool
) -> None:
    assert can_access_google_page("https://www.google.com") == "Accessible"

    mock_has_internet_connection.return_value = False
    assert can_access_google_page("https://www.google.com") == "Not accessible"

    mock_valid_google_url.return_value = False
    assert can_access_google_page("https://invalidurl.com") == "Not accessible"
