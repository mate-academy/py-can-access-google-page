from unittest import mock

from app.main import can_access_google_page


@mock.patch("app.main.has_internet_connection")
@mock.patch("app.main.valid_google_url")
def test_can_access_google_page(
        has_connection: mock.MagicMock,
        valid_url: mock.MagicMock
) -> None:
    res = can_access_google_page("https://www.google.com")
    valid_url.assert_called_once()
    has_connection.assert_called_once()
    assert res
