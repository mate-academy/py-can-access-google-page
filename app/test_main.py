from unittest import mock

import pytest

from app.main import can_access_google_page


@pytest.fixture()
def mocked_valid_url() -> None:
    with mock.patch("app.main.valid_google_url") as to_valid:
        yield to_valid


@pytest.fixture()
def mocked_connection() -> None:
    with mock.patch("app.main.has_internet_connection") as have_internet:
        yield have_internet


def test_should_return_accessible_if_both_true(
        mocked_valid_url: mock,
        mocked_connection: mock
) -> None:
    mocked_valid_url.return_value = True
    mocked_connection.return_value = True
    assert can_access_google_page("https://mate.academy/") == "Accessible"


def test_should_return_not_accessible_if_valid_false(
        mocked_valid_url: mock,
        mocked_connection: mock
) -> None:
    mocked_valid_url.return_value = False
    mocked_connection.return_value = True
    assert can_access_google_page("https://mate.academy/") == "Not accessible"


def test_should_return_not_accessible_if_connection_false(
        mocked_valid_url: mock,
        mocked_connection: mock
) -> None:
    mocked_valid_url.return_value = True
    mocked_connection.return_value = False
    assert can_access_google_page("https://mate.academy/") == "Not accessible"
