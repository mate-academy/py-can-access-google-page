from unittest import mock

from app.main import can_access_google_page


@mock.patch("app.main.valid_google_url")
@mock.patch("app.main.has_internet_connection")
def test_can_access_google_page_accessible(
        mocked_has_internet: str,
        mocked_valid_url: str) -> None:
    mocked_valid_url.return_value = True
    mocked_has_internet.return_value = True

    result = can_access_google_page("https://google.com")

    assert result == "Accessible"


@mock.patch("app.main.valid_google_url")
@mock.patch("app.main.has_internet_connection")
def test_can_access_google_page_not_accessible(
        mocked_has_internet: str,
        mocked_valid_url: str) -> None:
    mocked_valid_url.return_value = False
    mocked_has_internet.return_value = True

    result = can_access_google_page("https://notgoogle.com")
    assert result == "Not accessible"
