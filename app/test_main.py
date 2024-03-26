import pytest
from unittest.mock import patch

from _pytest.monkeypatch import MonkeyPatch

from app.main import can_access_google_page


url = "https://google.com"


@pytest.mark.parametrize(
    "valid_url, has_internet, can_access",
    [
        (True, 7, "Accessible"),
        (True, False, "Not accessible"),
        (False, True, "Not accessible"),
        (False, False, "Not accessible"),
    ]
)
@patch("app.main.valid_google_url")
@patch("app.main.has_internet_connection")
def test_can_access_google_page(
        mock_valid_google_url: MonkeyPatch,
        mock_has_internet_connection: MonkeyPatch,
        valid_url: bool,
        has_internet: bool,
        can_access: str) -> None:
    mock_valid_google_url.return_value = valid_url
    mock_has_internet_connection.return_value = has_internet
    assert can_access_google_page(url) == can_access
