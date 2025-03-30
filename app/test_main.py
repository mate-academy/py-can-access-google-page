import pytest
from unittest.mock import patch, MagicMock

from app.main import can_access_google_page


@pytest.mark.parametrize(
    "valid_url_mock, internet_mock, expected_output",
    [
        (True, True, "Accessible"),
        (False, True, "Not accessible"),
        (True, False, "Not accessible"),
        (False, False, "Not accessible"),
    ]
)
@patch("app.main.valid_google_url")
@patch("app.main.has_internet_connection")
def test_can_access_google_page(mock_internet: MagicMock,
                                mock_valid_url: MagicMock,
                                valid_url_mock: bool,
                                internet_mock: bool,
                                expected_output: str) -> None:

    mock_valid_url.return_value = valid_url_mock
    mock_internet.return_value = internet_mock

    assert can_access_google_page("https://www.google.com") == expected_output
