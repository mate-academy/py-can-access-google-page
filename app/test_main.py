from app.main import can_access_google_page
from unittest import mock


@mock.patch("app.main.valid_google_url")
def test_valid_google_url(mocked_valid_google_url: bool) -> None:
    mocked_valid_google_url.return_value = False
    assert can_access_google_page(url="123") == "Not accessible"


@mock.patch("app.main.has_internet_connection")
def test_has_internet_connection(mocked_has_internet_connection: bool) -> None:
    mocked_has_internet_connection.return_value = False
    assert can_access_google_page(url="123") == "Not accessible"
