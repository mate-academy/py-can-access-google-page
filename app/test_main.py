import pytest
from unittest.mock import patch
from app.main import can_access_google_page


@pytest.mark.parametrize(
    "valid, internet, result",
    [
        (True, True, "Accessible"),
        (True, False, "Not accessible"),
        (False, True, "Not accessible"),
        (False, False, "Not accessible"),
    ]
)
@patch("app.main.has_internet_connection")
@patch("app.main.valid_google_url")
def test_can_access_google_page(mock_valid_google_url: bool,
                                mock_has_internet_connection: bool,
                                valid: bool,
                                internet: bool, result: str) -> None:
    mock_valid_google_url.return_value = valid
    mock_has_internet_connection.return_value = internet

    assert can_access_google_page("https://google.com") == result
