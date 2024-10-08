import pytest

from unittest.mock import patch

from app.main import can_access_google_page


@pytest.mark.parametrize(
    "valid_url, has_internet, expected_result",
    [
        (True, True, "Accessible"),
        (False, True, "Not accessible"),
        (True, False, "Not accessible"),
        (False, False, "Not accessible"),
    ]
)
@patch("app.main.valid_google_url")
@patch("app.main.has_internet_connection")
def test_can_access_google_page(
        mock_has_internet: patch,
        mock_valid_url: patch,
        valid_url: bool,
        has_internet: bool,
        expected_result: str
) -> None:
    mock_valid_url.return_value = valid_url
    mock_has_internet.return_value = has_internet

    result: str = can_access_google_page("http://www.google.com")

    assert result == expected_result
