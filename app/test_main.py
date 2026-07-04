from unittest import mock
from app.main import can_access_google_page


@mock.patch("app.main.has_internet_connection")
@mock.patch("app.main.valid_google_url")
def test_can_access_google_page(mocked_url: str,
                                mocked_internet: None) -> None:
    mocked_url.return_value = True
    mocked_internet.return_value = True
    result = can_access_google_page("https://google.com")
    assert result == "Accessible"
    mocked_url.assert_called_once_with("https://google.com")
