from unittest import mock
from app.main import can_access_google_page


def test_can_access_google_page() -> None:
    with (mock.patch("app.main.has_internet_connection")
          as mock_internet_connection,
          mock.patch("app.main.valid_google_url") as mock_valid_url):

        can_access_google_page("https://www.youtube.com/")
        mock_internet_connection.assert_called_once()
        mock_valid_url.assert_called_once_with("https://www.youtube.com/")

    assert can_access_google_page("https://www.youtube.com/") == "Accessible"