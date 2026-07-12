from typing import Any
from unittest.mock import patch
import pytest
from app.main import can_access_google_page


@pytest.mark.parametrize(
    "url_valid, has_internet, expected",
    [
        (True, True, "Accessible"),
        (False, True, "Not accessible"),
        (True, False, "Not accessible"),
        (False, False, "Not accessible"),
    ],
)
@patch("app.main.has_internet_connection")
@patch("app.main.valid_google_url")
def test_can_access_google_page_cases(
    mock_url: Any,
    mock_internet: Any,
    url_valid: bool,
    has_internet: bool,
    expected: str,
) -> None:
    mock_url.return_value = url_valid
    mock_internet.return_value = has_internet
    assert can_access_google_page("https://www.google.com") == expected


@pytest.mark.parametrize(
    "wrong_url",
    [
        123,
        15.5,
        None,
        True,
        False,
        ["https://www.google.com"],
    ],
)
def test_can_access_google_page_invalid_types(wrong_url: Any) -> None:
    with pytest.raises(TypeError):
        can_access_google_page(wrong_url)
