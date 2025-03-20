from unittest import mock
from app.main import can_access_google_page


@mock.patch("app.main.valid_google_url")
@mock.patch("app.main.has_internet_connection")
def test_can_access_google_page_uses_suport_functions_correct(
        moked_internet: mock.MagicMock,
        moked_valid: mock.MagicMock) -> None:

    can_access_google_page("https://someUrl.com")
    moked_internet.assert_called_once()
    moked_valid.assert_called_once_with("https://someUrl.com")


@mock.patch("app.main.valid_google_url")
@mock.patch("app.main.has_internet_connection")
def test_can_access_google_page_without_internet(
        moked_internet: mock.MagicMock,
        moked_valid: mock.MagicMock) -> None:
    moked_internet.return_value = False
    assert can_access_google_page("https://someUrl.com") == "Not accessible"


@mock.patch("app.main.valid_google_url")
@mock.patch("app.main.has_internet_connection")
def test_can_access_google_page_invalid_url(
        moked_internet: mock.MagicMock,
        moked_valid: mock.MagicMock) -> None:
    moked_valid.return_value = False
    assert can_access_google_page("https://someUrl.com") == "Not accessible"


@mock.patch("app.main.valid_google_url")
@mock.patch("app.main.has_internet_connection")
def test_can_access_google_page_basic_case(
        moked_internet: mock.MagicMock,
        moked_valid: mock.MagicMock) -> None:
    moked_valid.return_value = True
    moked_internet.return_value = True
    assert can_access_google_page("https://someUrl.com") == "Accessible"
