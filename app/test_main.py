from typing import Any
import pytest
from unittest import mock
from app.main import can_access_google_page


@pytest.fixture()
def mock_valid_url() -> Any:
    with mock.patch("app.main.valid_google_url") as mocked_url:
        yield mocked_url


@pytest.fixture()
def mock_has_internet_connection() -> Any:
    with mock.patch("app.main.has_internet_connection") as mocked_internet:
        yield mocked_internet


@pytest.mark.parametrize(
    "is_connection, is_valid_url, expected_result",
    [
        (True, True, "Accessible"),
        (False, False, "Not accessible"),
        (True, False, "Not accessible"),
        (False, True, "Not accessible"),

    ]
)
def test_can_access_google_page(
        mock_valid_url: Any,
        mock_has_internet_connection: Any,
        is_connection: bool,
        is_valid_url: bool,
        expected_result: str
) -> None:
    mock_valid_url.return_value = is_valid_url
    mock_has_internet_connection.return_value = is_connection
    assert can_access_google_page("") == expected_result
