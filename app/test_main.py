from unittest import mock
from unittest.mock import Mock

from app.main import can_access_google_page


@mock.patch("app.main.valid_google_url")
@mock.patch("app.main.has_internet_connection")
def test_can_access_google_page_if_valid_url_and_has_internet_connection(
        valid_google_url: Mock,
        has_internet_connection: Mock
) -> None:
    valid_google_url.return_value = True
    has_internet_connection.return_value = True
    assert can_access_google_page("some_url") == "Accessible"


@mock.patch("app.main.valid_google_url")
@mock.patch("app.main.has_internet_connection")
def test_cant_access_google_page_if_not_valid_url_and_has_internet_connection(
        valid_google_url: Mock,
        has_internet_connection: Mock
) -> None:
    valid_google_url.return_value = False
    has_internet_connection.return_value = True
    assert can_access_google_page("some_url") == "Not accessible"


@mock.patch("app.main.valid_google_url")
@mock.patch("app.main.has_internet_connection")
def test_cant_access_google_page_if_not_valid_url_and_no_internet_connection(
        valid_google_url: Mock,
        has_internet_connection: Mock
) -> None:
    valid_google_url.return_value = False
    has_internet_connection.return_value = False
    assert can_access_google_page("some_url") == "Not accessible"


@mock.patch("app.main.valid_google_url")
@mock.patch("app.main.has_internet_connection")
def test_cant_access_google_page_if_valid_url_and_no_internet_connection(
        valid_google_url: Mock,
        has_internet_connection: Mock
) -> None:
    valid_google_url.return_value = True
    has_internet_connection.return_value = False
    assert can_access_google_page("some_url") == "Not accessible"
