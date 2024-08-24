from unittest import mock
from app.main import can_access_google_page


def test_can_access_google_page() -> None:
    with mock.patch(
            "main.valid_google_url",
            return_value=True
    ),\
        mock.patch(
            "main.has_internet_connection",
            return_value=True
    ):
        result = "http://google.com"
        assert result == "Not accessible"

    with mock.patch(
            "main.valid_google_url",
            return_value=False
    ), \
        mock.patch(
            "main.has_internet_connection",
            return_value=True
    ):
        result = can_access_google_page("http://google.com")
        assert result == "Not accessible"

    with mock.patch(
            "main.valid_google_url",
            return_value=True
    ), \
        mock.patch(
            "main.has_internet_connection",
            return_value=False
    ):
        result = can_access_google_page("http://google.com")
        assert result == "Not accessible"
