from unittest import mock
from app.main import can_access_google_page


@mock.patch("app.main.valid_google_url")
@mock.patch("app.main.has_internet_connection")
def test_return_accessible(
        valid_google_url: callable,
        has_internet_connection: callable) -> None:
    valid_google_url.value = True
    has_internet_connection.value = True
    assert can_access_google_page("http://google.com") == "Accessible"


@mock.patch("app.main.valid_google_url")
@mock.patch("app.main.has_internet_connection")
def test_return_not_accessible_one(
        valid_google_url: callable,
        has_internet_connection: callable) -> None:
    valid_google_url.return_value = False
    has_internet_connection.return_value = True
    assert can_access_google_page("http://google.com") == "Not accessible"


@mock.patch("app.main.valid_google_url")
@mock.patch("app.main.has_internet_connection")
def test_return_not_accessible_two(
        valid_google_url: callable,
        has_internet_connection: callable) -> None:
    valid_google_url.return_value = True
    has_internet_connection.return_value = False
    assert can_access_google_page("http://google.com") == "Not accessible"


@mock.patch("app.main.valid_google_url")
@mock.patch("app.main.has_internet_connection")
def test_return_not_accessible_three(
        valid_google_url: callable,
        has_internet_connection: callable) -> None:
    valid_google_url.return_value = False
    has_internet_connection.return_value = False
    assert can_access_google_page("http://google.com") == "Not accessible"
