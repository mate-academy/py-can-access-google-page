from unittest.mock import patch
from app.main import can_access_google_page


def test_can_access_google_page() -> None:
    url = "google.com"

    with (patch("app.main.has_internet_connection") as mock,
          patch("app.main.valid_google_url") as valid_url):

        can_access_google_page(url)
        mock.assert_called_once()
        valid_url.assert_called_once_with(url)
