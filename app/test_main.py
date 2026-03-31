import pytest
from unittest.mock import patch, MagicMock
from app.main import can_access_google_page


@pytest.mark.parametrize(
    "internet, valid_url, expected",
    [
        (True, True, "Accessible"),
        (True, False, "Not accessible"),
        (False, True, "Not accessible"),
        (False, False, "Not accessible"),
    ],
)
@patch("app.main.valid_google_url")
@patch("app.main.has_internet_connection")
def test_can_access_google_page(
    mock_has_internet: MagicMock,
    mock_valid_url: MagicMock,
    internet: bool,
    valid_url: bool,
    expected: str,
) -> None:
    mock_has_internet.return_value = internet
    mock_valid_url.return_value = valid_url

    result = can_access_google_page("https://google.com")

    assert result == expected
