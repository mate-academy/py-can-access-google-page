from unittest import mock
import pytest
from typing import Any

from app.main import can_access_google_page


@pytest.fixture()
def mocked_connection() -> Any:
    with mock.patch("app.main.has_internet_connection") as mock_connection:
        yield mock_connection


@pytest.fixture()
def mocked_validity() -> Any:
    with mock.patch("app.main.valid_google_url") as mock_validity:
        yield mock_validity


@pytest.mark.parametrize(
    "url_check, time_check, expected",
    [
        (True, True, "Accessible"),
        (True, False, "Not accessible"),
    ],
    ids=[
        "all checks true",
        "url check false"
    ]
)
def test_access_verified_with_good_connectivity(
    mocked_connection: Any,
    mocked_validity: Any,
    url_check: bool,
    time_check: bool,
    expected: str
) -> None:
    url = "test"
    mocked_connection.return_value = url_check
    mocked_validity.return_value = time_check

    assert (
        can_access_google_page(url) == expected
    ), f"Function should return: {expected}"
    mocked_connection.assert_called_once()
    mocked_validity.assert_called_once_with(url)


@pytest.mark.parametrize(
    "url_check, time_check, expected",
    [
        (False, True, "Not accessible"),
    ],
    ids=[
        "connectivity check false",
    ]
)
def test_access_verified_without_connectivity(
    mocked_connection: Any,
    mocked_validity: Any,
    url_check: bool,
    time_check: bool,
    expected: str
) -> None:
    url = "test"
    mocked_connection.return_value = url_check
    mocked_validity.return_value = time_check

    assert (
        can_access_google_page(url) == expected
    ), f"Function should return: {expected}"
    mocked_connection.assert_called_once()
    # when no connection, python won't go for valid_google_url check
