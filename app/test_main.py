from unittest import mock
from app.main import can_access_google_page


@mock.patch("app.main.valid_google_url")
@mock.patch("app.main.has_internet_connection")
def test_can_access_google_page(
        mocked_url: bool,
        mocked_internet_connection: bool
) -> None:
    mocked_url.return_value(True)
    mocked_internet_connection.return_value(True)

    result = can_access_google_page("https://www.google.com")
    assert result == "Accessible"

    mocked_url.assert_called()
    mocked_internet_connection.assert_called()
