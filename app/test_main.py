from unittest import mock
from app.main import can_access_google_page
import pytest


@pytest.fixture()
def mocked_current_time() -> None:
    with mock.patch("app.main.datetime") as mock_current_time:
        yield mock_current_time


@mock.patch("app.main.valid_google_url")
@mock.patch("app.main.has_internet_connection")
def test_should_return_accessible_when_all_funcs_return_true(
        mocked_valid_google_url: mock,
        mocked_has_internet_connection: mock
) -> None:
    mocked_valid_google_url.return_value = True
    mocked_has_internet_connection.return_value = True
    assert can_access_google_page("http://www.google.com") == "Accessible"


@mock.patch("app.main.valid_google_url")
@mock.patch("app.main.has_internet_connection")
def test_should_return_not_accessible_when_valid_googl_funcs_return_false(
        mocked_valid_google_url: mock,
        mocked_has_internet_connection: mock
) -> None:
    mocked_valid_google_url.return_value = False
    mocked_has_internet_connection.return_value = True
    assert can_access_google_page("http://www.google.com") == "Not accessible"


@mock.patch("app.main.valid_google_url")
@mock.patch("app.main.has_internet_connection")
def test_should_return_not_accessible_when_has_internet_return_false(
        mocked_valid_google_url: mock,
        mocked_has_internet_connection: mock
) -> None:
    mocked_valid_google_url.return_value = True
    mocked_has_internet_connection.return_value = False
    assert can_access_google_page("http://www.google.com") == "Not accessible"


@mock.patch("app.main.valid_google_url")
@mock.patch("app.main.has_internet_connection")
def test_should_return_not_accessible_when_all_funcs_return_false(
        mocked_valid_google_url: mock,
        mocked_has_internet_connection: mock
) -> None:
    mocked_valid_google_url.return_value = False
    mocked_has_internet_connection.return_value = False
    assert can_access_google_page("http://www.google.com") == "Not accessible"
