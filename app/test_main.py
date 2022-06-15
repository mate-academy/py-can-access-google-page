from unittest import mock

from app.main import can_access_google_page


@mock.patch("app.main.valid_google_url")
@mock.patch("app.main.has_internet_connection")
def test_can_access_google_page_correctly(
        mocked_validation,
        mocked_connection
):
    url = "https://www.google.com/"
    mocked_connection.return_value = True
    mocked_validation.return_value = True
    assert can_access_google_page(url) == "Accessible"


@mock.patch("app.main.valid_google_url")
@mock.patch("app.main.has_internet_connection")
def test_can_access_google_page_has_no_internet_connection(
        mocked_validation,
        mocked_connection
):
    url = "https://www.google.com/"
    mocked_connection.return_value = False
    mocked_validation.return_value = True
    assert can_access_google_page(url) == "Not accessible"


@mock.patch("app.main.valid_google_url")
@mock.patch("app.main.has_internet_connection")
def test_can_access_google_page_url_is_not_valid(
        mocked_validation,
        mocked_connection
):
    url = "https://www.google.com/"
    mocked_connection.return_value = True
    mocked_validation.return_value = False
    assert can_access_google_page(url) == "Not accessible"
