from typing import Any
import pytest
from app.main import can_access_google_page


@pytest.mark.parametrize(
    "url, internet_connection, valid_url, expected_result",
    [
        ("https://www.google.com", True, True, "Accessible"),
        ("https://www.asdffdsa.com", False, True, "Not accessible"),
        ("https://www.google.com", True, False, "Not accessible"),
        ("https://www.asdffdsa.com", False, False, "Not accessible"),
    ]
)
def test_can_access_google_page(
        monkeypatch: Any,
        url: str,
        internet_connection: bool,
        valid_url: bool,
        expected_result: str
) -> None:

    monkeypatch.setattr(
        "app.main.has_internet_connection",
        lambda: internet_connection
    )
    monkeypatch.setattr(
        "app.main.valid_google_url",
        lambda shadow_url: valid_url
    )

    result = can_access_google_page(url)

    assert result == expected_result
