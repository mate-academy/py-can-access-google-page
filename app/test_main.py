from unittest import mock
from app.main import can_access_google_page

URL = "https://www.google.com/"


@mock.patch("app.main.has_internet_connection")
def test_can_access_google_page_ok_time(
        mocked_has_connection: mock
) -> None:
    mocked_has_connection.return_value = True
    assert can_access_google_page(URL) == "Accessible"


@mock.patch("app.main.has_internet_connection")
def test_can_access_google_page_wrong_time(
        mocked_has_connection: mock
) -> None:
    mocked_has_connection.return_value = False
    assert can_access_google_page(URL) == "Not accessible"
    assert mocked_has_connection.has_been_called_once()


@mock.patch("app.main.has_internet_connection")
@mock.patch("app.main.valid_google_url")
def test_can_access_google_page(mocked_valid_google_url: mock,
                                mocked_has_connection: mock) -> None:
    mocked_has_connection.return_value = True
    mocked_valid_google_url.return_value = True
    assert can_access_google_page(URL) == "Accessible"
    assert mocked_valid_google_url.has_been_called_once_with(URL)


@mock.patch("app.main.has_internet_connection")
@mock.patch("app.main.valid_google_url")
def test_can_access_google_page_wrong_response(
        mocked_valid_google_url: mock,
        mocked_has_connection: mock
) -> None:

    mocked_has_connection.return_value = True
    mocked_valid_google_url.return_value = False
    assert can_access_google_page(URL) == "Not accessible"
