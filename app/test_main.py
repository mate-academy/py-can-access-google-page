from app.main import can_access_google_page
import pytest
from types import ModuleType


@pytest.mark.parametrize("url, internet_connection, expected", [
    ("https://www.google.com", True, "Accessible"),
    ("https://www.google.com", False, "Not accessible"),
    ("your.waifu", True, "Not accessible"),
])
def test_can_access_google_page(
        url: str, internet_connection: bool,
        expected: str,
        monkeypatch: ModuleType
) -> None:
    monkeypatch.setattr(
        "app.main.has_internet_connection",
        lambda: internet_connection
    )
    monkeypatch.setattr(
        "app.main.valid_google_url",
        lambda url_: url_ == "https://www.google.com"
    )
    result = can_access_google_page(url)
    assert result == expected
