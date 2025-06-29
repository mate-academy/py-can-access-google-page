from unittest import mock

from app.main import can_access_google_page


def test_can_access_google_page() -> None:
    url = "https://docs.python.org/3/library/unittest.mock.html"

    with mock.patch("app.main.has_internet_connection") as mocked_connection:
        can_access_google_page(url)
        mocked_connection.assert_called_once()
    with mock.patch("app.main.valid_google_url") as mocked_valid_url:
        can_access_google_page(url)
        mocked_valid_url.assert_called_once_with(url)
    assert can_access_google_page(url) == "Accessible"
