from unittest import mock

from app.main import can_access_google_page


@mock.patch("app.main.has_internet_connection")
def test_has_internet_connection_call(mocked: mock.MagicMock) -> None:
    can_access_google_page("https://www.google.com/webhp?client=firefox-b-d")
    mocked.assert_called_once()


@mock.patch("app.main.valid_google_url")
def test_have_valid_google_url(mocked: mock.MagicMock) -> None:
    can_access_google_page("https://www.google.com/webhp?client=firefox-b-d")
    mocked.assert_called_once_with(
        "https://www.google.com/webhp?client=firefox-b-d"
    )
