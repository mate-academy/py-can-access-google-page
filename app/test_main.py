from unittest.mock import patch

import pytest

from app.main import can_access_google_page


@pytest.mark.parametrize(
    "has_internet, valid_url, expected",
    [
        (True, True, "Accessible"),
        (False, True, "Not accessible"),
        (True, False, "Not accessible"),
        (False, False, "Not accessible"),
    ],
)
@patch("app.main.valid_google_url")
@patch("app.main.has_internet_connection")
def test_can_access_google_page(
    mock_has_internet: patch,
    mock_valid_url: patch,
    has_internet: bool,
    valid_url: bool,
    expected: str,
) -> None:
    mock_has_internet.return_value = has_internet
    mock_valid_url.return_value = valid_url

    assert can_access_google_page("https://google.com") == expected
