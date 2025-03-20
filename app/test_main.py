from typing import Callable

import pytest
from unittest import mock

from app.main import can_access_google_page


@pytest.fixture()
def mock_valid_google() -> Callable:
    with mock.patch("app.main.valid_google_url") as valid_mock:
        yield valid_mock


@pytest.fixture
def mock_has_internet() -> Callable:
    with mock.patch("app.main.has_internet_connection") as internet_mock:
        yield internet_mock


@pytest.mark.parametrize(
    "valid_google,has_internet,result_connection",
    [
        (True, True, "Accessible"),
        (True, False, "Not accessible"),
        (False, False, "Not accessible"),
        (False, True, "Not accessible"),
    ],
    ids=[
        "Accessible when "
        "internet connection and google validation - True",
        "Not accessible when "
        "internet connection - True but google validation - False",
        "Not accessible when "
        "internet connection and google validation False",
        "Not accessible when "
        "internet connection False and google validation True"
    ]
)
def test_if_can_access_google_page_works_correctly(
    mock_valid_google: mock.MagicMock,
    mock_has_internet: mock.MagicMock,
    valid_google: bool,
    has_internet: bool,
    result_connection: str
) -> None:
    mock_valid_google.return_value = valid_google
    mock_has_internet.return_value = has_internet
    assert can_access_google_page("some_url") == result_connection
