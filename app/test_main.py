from unittest import mock

from app.main import can_access_google_page


@mock.patch("app.main.valid_google_url")
@mock.patch("app.main.has_internet_connection")
def test_valid_url_and_connection_exists(
        mocked_valid_google_url: mock.MagicMock,
        mocked_has_internet_connection: mock.MagicMock
) -> None:
    can_access_google_page(mocked_valid_google_url)
    mocked_valid_google_url.assert_called_once()
    mocked_has_internet_connection.assert_called_once()
    assert mocked_valid_google_url
    assert mocked_has_internet_connection
