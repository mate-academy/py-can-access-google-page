from unittest.mock import patch
import pytest

import app.main


@pytest.mark.parametrize(
    "has_internet, valid_url, expected",
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
    mock_has_internet,
    mock_valid_url,
    has_internet,
    valid_url,
    expected,
):
    mock_has_internet.return_value = has_internet
    mock_valid_url.return_value = valid_url

    assert app.main.can_access_google_page("https://google.com") == expected
