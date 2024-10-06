from unittest import mock
from app.main import can_access_google_page


@mock.patch("app.main.valid_google_url")
@mock.patch("app.main.has_internet_connection")
def test_can_access_google_page_call_url_and_internet_functions(
        mocked_internet: callable,
        mocked_url: callable,
) -> None:
    can_access_google_page("https://www.google.com/")
    mocked_url.assert_called_once()
    mocked_internet.assert_called_once()
