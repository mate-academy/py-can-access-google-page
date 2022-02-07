from unittest import mock

from app.main import can_access_google_page


@mock.patch("app.main.has_internet_connection")
@mock.patch("app.main.valid_google_url")
def test_connection_is_good_url_is_good(
        mocked_has_internet_connection,
        mocked_valid_google_url
):
    mocked_has_internet_connection.return_value = True
    mocked_valid_google_url.return_value = True

    assert can_access_google_page(
        'https://www.youtube.com/') == "Accessible"


@mock.patch("app.main.has_internet_connection")
@mock.patch("app.main.valid_google_url")
def test_connection_is_good_url_is_bad(
        mocked_has_internet_connection,
        mocked_valid_google_url
):
    mocked_has_internet_connection.return_value = True
    mocked_valid_google_url.return_value = False

    assert can_access_google_page(
        'https://www.youtube.com/') == "Not accessible"


@mock.patch("app.main.has_internet_connection")
@mock.patch("app.main.valid_google_url")
def test_connection_is_bad_url_is_good(
        mocked_has_internet_connection,
        mocked_valid_google_url
):
    mocked_has_internet_connection.return_value = False
    mocked_valid_google_url.return_value = True

    assert can_access_google_page(
        'https://www.youtube.com/') == "Not accessible"


@mock.patch("app.main.has_internet_connection")
@mock.patch("app.main.valid_google_url")
def test_connection_is_bad_url_is_bad(
        mocked_has_internet_connection,
        mocked_valid_google_url
):
    mocked_has_internet_connection.return_value = False
    mocked_valid_google_url.return_value = False

    assert can_access_google_page(
        'https://www.youtube.com/') == "Not accessible"
