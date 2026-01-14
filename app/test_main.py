from unittest import mock
from .main import can_access_google_page


def test_can_access_google_page_accessible() -> None:
    with mock.patch("app.main.has_internet_connection",
                    return_value=True), \
         mock.patch("app.main.valid_google_url",
                    return_value=True):

        result = can_access_google_page("https://www.google.com")

        assert result == "Accessible"
