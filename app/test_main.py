import pytest
from typing import Any
from unittest import mock

from app.main import can_access_google_page


@pytest.fixture
def mocked_validation() -> Any:
    with mock.patch("app.main.valid_google_url") as mocked_validation:
        yield mocked_validation


@pytest.fixture
def mocked_connection() -> Any:
    with mock.patch("app.main.has_internet_connection") as mocked_connection:
        yield mocked_connection


def test_can_access_google_page_when_validation_and_connection(
        mocked_validation: Any,
        mocked_connection: Any
) -> None:
    mocked_validation.return_value = True
    mocked_connection.return_value = True
    assert can_access_google_page("") == "Accessible", \
        "When validation and connection are true, page should be accessible"


def test_can_access_google_page_when_validation_and_no_connection(
        mocked_validation: Any,
        mocked_connection: Any
) -> None:
    mocked_validation.return_value = True
    mocked_connection.return_value = False
    assert can_access_google_page("") == "Not accessible", \
        ("When validation is true and no connection, "
         "page should not be accessible")


def test_can_access_google_page_when_no_validation_and_connection(
        mocked_validation: Any,
        mocked_connection: Any
) -> None:
    mocked_validation.return_value = False
    mocked_connection.return_value = True
    assert can_access_google_page("") == "Not accessible", \
        ("When no validation and connection is true, "
         "page should not be accessible")


def test_can_access_google_page_when_no_validation_and_no_connection(
        mocked_validation: Any,
        mocked_connection: Any
) -> None:
    mocked_validation.return_value = False
    mocked_connection.return_value = False
    assert can_access_google_page("") == "Not accessible", \
        ("When no validation and no connection are true, "
         "page should not be accessible")
