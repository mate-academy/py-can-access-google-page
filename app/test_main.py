from unittest import mock

from app.main import can_access_google_page


def test_can_access_google_page_when_url_is_valid_and_connection_exists() \
        -> None:
    with mock.patch("app.main.valid_google_url", return_value=True):
        with mock.patch("app.main.has_internet_connection", return_value=True):
            result = can_access_google_page("http://google.com")
            assert result == "Accessible"


def test_can_access_google_page_when_url_is_valid_but_no_connection() -> None:
    with mock.patch("app.main.valid_google_url", return_value=True):
        with mock.patch("app.main.has_internet_connection",
                        return_value=False):
            result = can_access_google_page("http://google.com")
            assert result == "Not accessible"


def test_can_access_google_page_when_url_is_invalid() -> None:
    with mock.patch("app.main.valid_google_url", return_value=False):
        result = can_access_google_page("http://google.com")
        assert result == "Not accessible"
