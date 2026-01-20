from unittest import mock

from app.main import can_access_google_page


@mock.patch("app.main.valid_google_url")
@mock.patch("app.main.has_internet_connection")
def test_access_google_page_valid_url_true_and_connection_true(
        mocked_connection: object,
        mocked_url: object
) -> None:
    mocked_connection.return_value = True
    mocked_url.return_value = True
    assert can_access_google_page("www.google.com") == "Accessible"


@mock.patch("app.main.valid_google_url")
@mock.patch("app.main.has_internet_connection")
def test_access_google_page_valid_url_true_and_connection_false(
        mocked_connection: object,
        mocked_url: object
) -> None:
    mocked_connection.return_value = False
    mocked_url.return_value = True
    assert can_access_google_page("www.google.com") == "Not accessible"


@mock.patch("app.main.valid_google_url")
@mock.patch("app.main.has_internet_connection")
def test_access_google_page_valid_url_false_and_connection_true(
        mocked_connection: object,
        mocked_url: object
) -> None:
    mocked_connection.return_value = True
    mocked_url.return_value = False
    assert can_access_google_page("www.google.com") == "Not accessible"
