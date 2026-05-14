from typing import Any
from unittest import mock

import pytest

from app.main import can_access_google_page


@pytest.fixture()
def mocked_valid_google_url() -> Any:
    with mock.patch("app.main.valid_google_url") as mock_valid_url:
        yield mock_valid_url


@pytest.fixture()
def mocked_has_internet_connection() -> Any:
    with mock.patch(
            "app.main.has_internet_connection"
    ) as mock_internet_connection:
        yield mock_internet_connection


@pytest.mark.parametrize(
    "is_url_valid,has_connection,expected_status",
    [
        pytest.param(True, True, "Accessible",
                     id="url_valid_with_internet_connection"),
        pytest.param(True, False, "Not accessible",
                     id="url_valid_wo_internet_connection"),
        pytest.param(False, True, "Not accessible",
                     id="url_invalid_with_internet_connection"),
        pytest.param(False, False, "Not accessible",
                     id="url_invalid_wo_internet_connection"),
    ]
)
def test_can_access_google_page_status(
        mocked_valid_google_url: Any,
        mocked_has_internet_connection: Any,
        is_url_valid: bool,
        has_connection: bool,
        expected_status: str,
) -> None:
    mocked_valid_google_url.return_value = is_url_valid
    mocked_has_internet_connection.return_value = has_connection
    assert can_access_google_page(url="random url") == expected_status
    mocked_has_internet_connection.assert_called_once()
    if has_connection:
        mocked_valid_google_url.assert_called_once_with("random url")
    else:
        mocked_valid_google_url.assert_not_called()
