from app.main import can_access_google_page
from unittest import mock


@mock.patch("app.main.has_internet_connection")
@mock.patch("app.main.valid_google_url")
def test_can_access_google_page(valid_google_url: bool,
                                has_internet_connection: bool) -> None:
    has_internet_connection.return_value = True
    valid_google_url.return_value = True
    assert can_access_google_page("https://google.com") == "Accessible"


@mock.patch("app.main.has_internet_connection")
@mock.patch("app.main.valid_google_url")
def test_can_access_without_internet(valid_google_url: bool,
                                     has_internet_connection: bool) -> None:
    has_internet_connection.return_value = False
    valid_google_url.return_value = True
    assert can_access_google_page("https://google.com") == "Not accessible"


@mock.patch("app.main.has_internet_connection")
@mock.patch("app.main.valid_google_url")
def test_can_access_url_is_error(valid_google_url: bool,
                                 has_internet_connection: bool) -> None:
    has_internet_connection.return_value = True
    valid_google_url.return_value = False
    assert can_access_google_page("https://google.com") == "Not accessible"
