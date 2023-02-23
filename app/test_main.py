from unittest import mock

from app.main import can_access_google_page


@mock.patch("app.main.valid_google_url")
@mock.patch("app.main.has_internet_connection")
def test_valid_url_when_connection_does_not_exists(
        valid_google_url: bool,
        has_internet_connection: bool
) -> None:
    valid_google_url.return_value = True
    has_internet_connection.return_value = False

    assert can_access_google_page("google.com") == "Not accessible"


@mock.patch("app.main.valid_google_url")
@mock.patch("app.main.has_internet_connection")
def test_valid_url_when_connection_exists(
        valid_google_url: bool,
        has_internet_connection: bool
) -> None:
    valid_google_url.return_value = False
    has_internet_connection.return_value = True

    assert can_access_google_page("google.com") == "Not accessible"
