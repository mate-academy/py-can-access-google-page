import pytest
from unittest import mock
from typing import Callable


from app.main import can_access_google_page


@pytest.fixture
def mocked_validator_func() -> Callable:
    with mock.patch("app.main.valid_google_url") as mocked_validator:
        yield mocked_validator


@pytest.fixture
def mocked_connection_check_func() -> Callable:
    with mock.patch("app.main.has_internet_connection")\
            as mocked_connection_checker:
        yield mocked_connection_checker


def test_access_with_valid_responses(
        mocked_validator_func: Callable,
        mocked_connection_check_func: Callable
) -> None:
    mocked_validator_func.return_value = True
    mocked_connection_check_func.return_value = True
    assert can_access_google_page("test.url") == "Accessible"


def test_access_with_invalid_url(
        mocked_validator_func: Callable,
        mocked_connection_check_func: Callable
) -> None:
    mocked_validator_func.return_value = False
    mocked_connection_check_func.return_value = True
    assert can_access_google_page("test.url") == "Not accessible"


def test_access_with_no_connection(
        mocked_validator_func: Callable,
        mocked_connection_check_func: Callable
) -> None:
    mocked_validator_func.return_value = True
    mocked_connection_check_func.return_value = False
    assert can_access_google_page("test.url") == "Not accessible"


def test_access_with_invalid_responses(
        mocked_validator_func: Callable,
        mocked_connection_check_func: Callable
) -> None:
    mocked_validator_func.return_value = False
    mocked_validator_func.return_value = False
    assert can_access_google_page("test.url") == "Not accessible"
