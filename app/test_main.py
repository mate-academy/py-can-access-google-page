import pytest
from unittest import mock
from app.main import can_access_google_page


@pytest.fixture()
def mocked_valid_google_url() -> mock:
    with mock.patch("app.main.valid_google_url") as mocked_valid_url:
        yield mocked_valid_url


@pytest.fixture()
def mocked_has_internet_connection() -> mock:
    with mock.patch("app.main.has_internet_connection") \
            as mocked_has_internet:
        yield mocked_has_internet


def test_should_return_accessible_when_time_and_url_are_good(
        mocked_valid_google_url,
        mocked_has_internet_connection
) -> None:
    mocked_has_internet_connection.return_value = True
    mocked_valid_google_url.return_value = True
    assert can_access_google_page("www.test_url") == "Accessible"


def test_should_return_not_accessible_when_time_and_url_are_bad(
        mocked_valid_google_url,
        mocked_has_internet_connection
) -> None:
    mocked_has_internet_connection.return_value = False
    mocked_valid_google_url.return_value = False
    assert can_access_google_page("www.test_url") == "Not accessible"


def test_should_return_not_accessible_when_time_good_and_url_bad(
        mocked_valid_google_url,
        mocked_has_internet_connection
) -> None:
    mocked_has_internet_connection.return_value = False
    mocked_valid_google_url.return_value = True
    assert can_access_google_page("www.test_url") == "Not accessible"


def test_should_return_not_accessible_when_time_bad_and_url_good(
        mocked_valid_google_url,
        mocked_has_internet_connection
) -> None:
    mocked_has_internet_connection.return_value = True
    mocked_valid_google_url.return_value = False
    assert can_access_google_page("www.test_url") == "Not accessible"
