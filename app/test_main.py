from unittest import mock

from app.main import can_access_google_page


@mock.patch("app.main.valid_google_url")
@mock.patch("app.main.has_internet_connection")
def test_can_access_google_page(
        mocked_url: mock.MagicMock,
        mocked_connection: mock.MagicMock) -> None:
    mocked_connection.return_value = True
    mocked_url.return_value = True
    assert can_access_google_page("http://google.com") == True
