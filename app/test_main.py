from unittest import mock
from app.main import can_access_google_page


@mock.patch("app.main.valid_google_url")
@mock.patch("app.main.has_internet_connection")
def test_can_access_google_page(
        mocked_has_internet: bool,
        mocked_valid_url: bool
) -> None:
    mocked_valid_url.return_value = True
    mocked_has_internet.return_value = True
    result = can_access_google_page("https://www.google.com")
    assert result == "Accessible"

    mocked_has_internet.return_value = True
    mocked_has_internet.return_value = False
    result = can_access_google_page("https://www.google.com")
    assert result == "Not accessible"

    mocked_valid_url.return_value = False
    mocked_has_internet.return_value = True
    result = can_access_google_page("https://www.invalidurl.com")
    assert result == "Not accessible"

    mocked_valid_url.return_value = False
    mocked_has_internet.return_value = False
    result = can_access_google_page("https://www.invalidurl.com")
    assert result == "Not accessible"
