from unittest import mock

from app.main import can_access_google_page


@mock.patch("app.main.valid_google_url")
@mock.patch("app.main.has_internet_connection")
def test_access_google_page_with_connect_and_valid_url(
        mocked_valid_url: mock,
        mocked_connection: mock
) -> None:
    mocked_valid_url.return_value = True
    mocked_connection.return_value = True
    assert can_access_google_page("https://www.google.com") == "Accessible"


@mock.patch("app.main.valid_google_url")
@mock.patch("app.main.has_internet_connection")
def test_access_google_page_with_connect_and_invalid_url(
        mocked_valid_url: mock,
        mocked_connection: mock
) -> None:
    mocked_valid_url.return_value = False
    mocked_connection.return_value = True
    assert can_access_google_page("https://www.google.com") == "Not accessible"


@mock.patch("app.main.valid_google_url")
@mock.patch("app.main.has_internet_connection")
def test_access_google_page_with_no_connect_and_valid_url(
        mocked_valid_url: mock,
        mocked_connection: mock
) -> None:
    mocked_valid_url.return_value = True
    mocked_connection.return_value = False
    assert can_access_google_page("https://www.google.com") == "Not accessible"


@mock.patch("app.main.valid_google_url")
@mock.patch("app.main.has_internet_connection")
def test_access_google_page_with_no_connect_and_invalid_url(
        mocked_valid_url: mock,
        mocked_connection: mock
) -> None:
    mocked_valid_url.return_value = False
    mocked_connection.return_value = False
    assert can_access_google_page("https://www.google.com") == "Not accessible"
