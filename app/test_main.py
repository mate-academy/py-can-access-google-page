import pytest
from unittest.mock import patch
from app.main import can_access_google_page


@pytest.mark.parametrize(
    "has_internet_mock, valid_url_mock, expected_result",
    [
        (True, True, "Accessible"),
        (True, False, "Not accessible"),
        (False, True, "Not accessible"),
        (False, False, "Not accessible"),
    ],
)
@patch("app.main.has_internet_connection")
@patch("app.main.valid_google_url")
def test_can_access_google_page(
    mock_valid_google_url: bool,
    mock_has_internet_connection: bool,
    has_internet_mock: bool,
    valid_url_mock: bool,
    expected_result: str
) -> None:
    mock_valid_google_url.return_value = valid_url_mock
    mock_has_internet_connection.return_value = has_internet_mock
    result = can_access_google_page("https://www.google.com")
    assert result == expected_result
