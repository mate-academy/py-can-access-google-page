from unittest import mock

from app.main import can_access_google_page


@mock.patch("app.main.valid_google_url")
@mock.patch("app.main.has_internet_connection")
def test_valid_url_and_connection_exists(
    has_internet_connection: bool,
    valid_google_url: bool
) -> None:
    valid_google_url.return_value = True
    has_internet_connection.return_value = True
    assert can_access_google_page("https://www.google.com") == "Accessible"


@mock.patch("app.main.valid_google_url")
@mock.patch("app.main.has_internet_connection")
def test_if_only_connection_exists(
    has_internet_connection: bool,
    valid_google_url: bool
) -> None:
    valid_google_url.return_value = False
    has_internet_connection.return_value = True
    assert (
        can_access_google_page("https://httpbin.org/status/404")
        == "Not accessible"
    )


@mock.patch("app.main.valid_google_url")
@mock.patch("app.main.has_internet_connection")
def test_if_only_url_is_valid(
    has_internet_connection: bool,
    valid_google_url: bool
) -> None:
    valid_google_url.return_value = True
    has_internet_connection.return_value = False
    assert can_access_google_page("https://www.google.com") == "Not accessible"


@mock.patch("app.main.valid_google_url")
@mock.patch("app.main.has_internet_connection")
def test_no_connection_and_invalid_url(
    has_internet_connection: bool,
    valid_google_url: bool
) -> None:
    valid_google_url.return_value = False
    has_internet_connection.return_value = False
    assert (
        can_access_google_page("https://httpbin.org/status/404")
        == "Not accessible"
    )
