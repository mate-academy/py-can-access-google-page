from app.main import can_access_google_page
import pytest
from unittest import mock
from typing import Callable


@pytest.fixture()
def mocked_valid_google_url() -> Callable:
    with mock.patch(
            "app.main.valid_google_url"
    ) as mocked_validator_url:
        yield mocked_validator_url


@pytest.fixture()
def mocked_has_internet_connection() -> Callable:
    with mock.patch(
            "app.main.has_internet_connection"
    ) as mocked_has_internet:
        yield mocked_has_internet


def test_url_valid(
        mocked_valid_google_url: Callable,
        mocked_has_internet_connection: Callable
) -> None:
    mocked_valid_google_url.return_value = True
    mocked_has_internet_connection.return_value = False
    assert can_access_google_page(
        "https://www.google.com/"
    ) == "Not accessible"


def test_url_invalid_only_connection(
        mocked_valid_google_url: Callable,
        mocked_has_internet_connection: Callable
) -> None:
    mocked_valid_google_url.return_value = False
    mocked_has_internet_connection.return_value = True
    assert can_access_google_page(
        "https://www.google1.com/"
    ) == "Not accessible"
