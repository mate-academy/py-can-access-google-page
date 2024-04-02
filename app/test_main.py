import pytest

from typing import Generator
from unittest.mock import MagicMock, patch

from app.main import can_access_google_page


@pytest.fixture
def mock_valid_google_url() -> Generator[MagicMock, None, None]:
    with patch("app.main.valid_google_url") as mocked_function:
        yield mocked_function


@pytest.fixture
def mock_has_internet_connection() -> Generator[MagicMock, None, None]:
    with patch("app.main.has_internet_connection") as mocked_function:
        yield mocked_function


@pytest.mark.parametrize(
    "valid_url, has_connection, expected_output",
    [
        (True, True, "Accessible"),
        (True, False, "Not accessible"),
        (False, True, "Not accessible"),
        (False, False, "Not accessible"),
    ]
)
def test_cannot_access_if_connection_or_valid_url_is_true(
        mock_valid_google_url: MagicMock,
        mock_has_internet_connection: MagicMock,
        valid_url: bool,
        has_connection: bool,
        expected_output: str
) -> None:
    mock_valid_google_url.return_value = valid_url
    mock_has_internet_connection.return_value = has_connection

    assert can_access_google_page("https://www.google.com/") == expected_output
