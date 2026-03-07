from unittest import mock
from app.main import can_access_google_page


def test_return_not_accessible_when_url_not_valid() -> None:
    with (mock.patch("app.main.valid_google_url") as mocked_url,
          mock.patch("app.main.has_internet_connection") as mocked_connection):
        can_access_google_page("url")
        mocked_url.assert_called_once()
        mocked_connection.assert_called_once()
    assert can_access_google_page("url") == "Not accessible"


def test_return_accessible_when_url_valid() -> None:
    with (mock.patch("app.main.valid_google_url") as mocked_url,
          mock.patch("app.main.has_internet_connection") as mocked_connection):
        can_access_google_page("https://www.google.com/")
        mocked_url.assert_called_once()
        mocked_connection.assert_called_once()
    assert can_access_google_page("https://www.google.com/") == "Accessible"
