from __future__ import annotations
from unittest.mock import patch, MagicMock
import pytest
from app.main import can_access_google_page


@pytest.mark.parametrize(
    "url, mock1, mock2, result",
    [
        ("https://www.google.com/", True, True, "Accessible"),
        ("https://www.google.com/", True, False, "Not accessible"),
        ("https://www.google.com/", False, True, "Not accessible"),
        ("https://www.google.com/", False, False, "Not accessible")
    ],
    ids=[
        "all is working",
        "no connection",
        "invalid google url",
        "invalid url and no connection"
    ]
)
@patch("app.main.has_internet_connection")
@patch("app.main.valid_google_url")
def test_my_function(mocked_valid: MagicMock,
                     mocked_internet: MagicMock,
                     url: str,
                     mock1: bool,
                     mock2: bool,
                     result: str) -> None:
    mocked_valid.return_value = mock1
    mocked_internet.return_value = mock2
    assert can_access_google_page(url) == result
