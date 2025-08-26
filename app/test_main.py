from unittest import mock
from app.main import can_access_google_page


def test_can_access_google_page() -> None:
    with (mock.patch("app.main.valid_google_url") as valid_url,
          mock.patch("app.main.has_internet_connection") as internet_connect):

        url = "https://www.google.com/"
        assert can_access_google_page(url) == "Accessible"
        internet_connect.assert_called_once()
        valid_url.assert_called_once_with(url)
