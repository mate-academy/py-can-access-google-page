from unittest import mock
from app.main import (
    can_access_google_page)


@mock.patch("app.main.has_internet_connection")
@mock.patch("app.main.valid_google_url")
def test_access_google_page(mocked_url: str, mocked_connection: str) -> None:
    mocked_connection.return_value = True
    mocked_url.return_value = True
    assert can_access_google_page("https://www.google.com") == "Accessible"

    mocked_connection.return_value = False
    mocked_url.return_value = True
    assert can_access_google_page("https://www.google.com") == "Not accessible"

    mocked_connection.return_value = True
    mocked_url.return_value = False
    assert can_access_google_page("https://www.google.com") == "Not accessible"

    mocked_connection.return_value = False
    mocked_url.return_value = False
    assert (can_access_google_page
            ("https://invalid-url.com") == "Not accessible")
