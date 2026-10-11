import pytest
from unittest.mock import patch, MagicMock
import app.main


@pytest.mark.parametrize(
    "valid_url, has_internet, expected",
    [
        (True, True, "Accessible"),
        (True, False, "Not accessible"),
        (False, True, "Not accessible"),
        (False, False, "Not accessible"),
    ]
)
@patch("app.main.has_internet_connection")
@patch("app.main.valid_google_url")
def test_can_access_google_page(
        mock_valid_google_url: MagicMock,
        mock_has_internet_connection: MagicMock,
        valid_url: bool,
        has_internet: bool,
        expected: str
) -> None:
    # Set the fake return values for our mocked functions
    mock_valid_google_url.return_value = valid_url
    mock_has_internet_connection.return_value = has_internet

    # Call the actual function and assert the result
    assert app.main.can_access_google_page("http://some-url.com") == expected
