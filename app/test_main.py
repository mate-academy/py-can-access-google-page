from unittest import mock

from app.main import can_access_google_page


@mock.patch("app.main.valid_google_url")
@mock.patch("app.main.has_internet_connection")
def test_can_access_google_page_calls_required_functions(
        mocked_has_internet_connection: mock.MagicMock,
        mocked_valid_google_url: mock.MagicMock
) -> None:
    can_access_google_page("https")
    mocked_has_internet_connection.assert_called_once()
    mocked_valid_google_url.assert_called_once_with("https")
