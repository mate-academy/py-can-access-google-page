from unittest import mock
from app.main import can_access_google_page


@mock.patch("app.main.valid_google_url")
@mock.patch("app.main.has_internet_connection")
def test_url_true_and_connection_false(
        mocked_url: bool,
        mocked_check: bool) -> None:
    mocked_url.return_value = True
    mocked_check.return_value = False
    assert can_access_google_page("url") == "Not accessible"


@mock.patch("app.main.valid_google_url")
@mock.patch("app.main.has_internet_connection")
def test_url_false_and_connection_true(
        mocked_url: bool,
        mocked_check: bool) -> None:
    mocked_url.return_value = False
    mocked_check.return_value = True
    assert can_access_google_page("url") == "Not accessible"


@mock.patch("app.main.valid_google_url")
@mock.patch("app.main.has_internet_connection")
def test_valid_url_and_connection_exists(
        mocked_url: bool,
        mocked_check: bool) -> None:
    mocked_url.return_value = True
    mocked_check.return_value = True
    assert can_access_google_page("url") == "Accessible"
