from unittest import mock
from app.main import can_access_google_page


def test_can_access_google_page() -> None:
    url = "https://example.com"

    with (mock.patch("app.main.valid_google_url") as valid_url,
          mock.patch("app.main.has_internet_connection") as has_connection):
        valid_url.return_value = True
        has_connection.return_value = True

        result = can_access_google_page(url)

        valid_url.assert_called_once_with(url)
        has_connection.assert_called_once()

        assert result == "Accessible"
