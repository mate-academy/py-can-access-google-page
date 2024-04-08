import pytest
from unittest import mock
from unittest.mock import MagicMock
from app.main import can_access_google_page


@pytest.fixture
def mock_has_internet_connection() -> MagicMock:
    with mock.patch("app.main.has_internet_connection") as mock_conn:
        yield mock_conn


@pytest.fixture
def mock_valid_google_url() -> MagicMock:
    with mock.patch("app.main.valid_google_url") as mock_url:
        yield mock_url


@pytest.mark.parametrize(
    "has_internet_connection, valid_google_url, expected_result",
    [
        (True, True, "Accessible"),
        (True, False, "Not accessible"),
        (False, True, "Not accessible"),
        (False, False, "Not accessible"),
    ],
    ids=[
        "Access granted with internet and valid URL",
        "Access denied without valid URL",
        "Access denied without internet connection",
        "Access denied without internet connection and valid URL",
    ]
)
def test_can_access_google_page(
        mock_has_internet_connection: MagicMock,
        mock_valid_google_url: MagicMock,
        has_internet_connection: bool,
        valid_google_url: bool,
        expected_result: str
) -> None:
    mock_has_internet_connection.return_value = has_internet_connection
    mock_valid_google_url.return_value = valid_google_url

    result = can_access_google_page("https://www.google.com")
    assert result == expected_result

    mock_has_internet_connection.assert_called_once()
    if has_internet_connection:
        mock_valid_google_url.assert_called_once()
    else:
        mock_valid_google_url.assert_not_called()
