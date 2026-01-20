from unittest import mock

import pytest

from app.main import can_access_google_page


@pytest.fixture
def mocked_validator():
    with mock.patch(
            "app.main.valid_google_url",
            return_value=True
    ) as mocked_validation:
        yield mocked_validation


@pytest.fixture
def mocked_connection():
    with mock.patch(
            "app.main.has_internet_connection",
            return_value=True
    ) as mocked_connection:
        yield mocked_connection


def test_should_call_has_internet_connection(
        mocked_validator,
        mocked_connection
):
    can_access_google_page("www.google.com")

    mocked_connection.assert_called_once()


def test_should_call_valid_google_url_with_arg(
        mocked_validator,
        mocked_connection
):
    can_access_google_page("www.google.com")

    mocked_validator.assert_called_once_with("www.google.com")


def test_should_return_accessible_if_validation_and_connection(
        mocked_validator,
        mocked_connection
):
    assert can_access_google_page("www.google.com") == "Accessible"


def test_should_return_not_accessible_if_connection_fail(
        mocked_validator,
        mocked_connection
):
    mocked_connection.return_value = False

    assert can_access_google_page("www.google.com") == "Not accessible"


def test_should_return_not_accessible_if_validation_fail(
        mocked_validator,
        mocked_connection
):
    mocked_validator.return_value = False

    assert can_access_google_page("www.google.com") == "Not accessible"


def test_should_return_not_accessible_if_validation_and_connection_failed(
        mocked_validator,
        mocked_connection
):
    mocked_validator.return_value = False
    mocked_connection.return_value = False

    assert can_access_google_page("www.google.com") == "Not accessible"
