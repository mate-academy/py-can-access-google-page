from unittest import mock

from app.main import can_access_google_page


def call_function_has_internet_connection() -> bool:
    with mock.patch("app.main.has_internet_connection") as mocked_connection:
        can_access_google_page("https://google.com")
        return mocked_connection.called


def call_function_valid_google_url() -> bool:
    with mock.patch("app.main.valid_google_url") as mocked_valid_url:
        can_access_google_page("https://google.com")
        return mocked_valid_url.called


def test_can_access_google_page_with_internet_and_valid_url() -> None:
    if (call_function_has_internet_connection()
            and call_function_valid_google_url()):
        can_access_google_page_should_equal = "Accessible"
    else:
        can_access_google_page_should_equal = "Not accessible"
    assert (can_access_google_page("https://google.com")
            is can_access_google_page_should_equal)
