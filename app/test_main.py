from unittest import mock
from app.main import can_access_google_page


@mock.patch("app.main.has_internet_connection")
@mock.patch("app.main.valid_google_url")
def test_should_accessible_if_url_is_valid_and_connection_exists(
        mocked_response: bool, mocked_time: bool) -> None:
    mocked_response.return_value = True
    mocked_time.return_value = True
    assert can_access_google_page("https://mate.academy/") == "Accessible"


@mock.patch("app.main.has_internet_connection")
@mock.patch("app.main.valid_google_url")
def test_should_not_accessible_if_url_is_valid_and_connection_not_exists(
        mocked_response: bool, mocked_time: bool) -> None:
    mocked_response.return_value = True
    mocked_time.return_value = False
    assert can_access_google_page("https://mate.academy/") == "Not accessible"


@mock.patch("app.main.has_internet_connection")
@mock.patch("app.main.valid_google_url")
def test_should_not_accessible_if_url_is_not_valid_and_connection_exists(
        mocked_response: bool, mocked_time: bool) -> None:
    mocked_response.return_value = False
    mocked_time.return_value = True
    assert can_access_google_page("https://mate.academy/") == "Not accessible"


@mock.patch("app.main.has_internet_connection")
@mock.patch("app.main.valid_google_url")
def test_should_not_accessible_if_url_is_not_valid_and_connection_not_exists(
        mocked_response: bool, mocked_time: bool) -> None:
    mocked_response.return_value = False
    mocked_time.return_value = False
    assert can_access_google_page("https://mate.academy/") == "Not accessible"
