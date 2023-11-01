from typing import Any

import pytest

from app.main import can_access_google_page


@pytest.mark.parametrize(
    "internet,valid_url,expected",
    [
        (True, True, "Accessible"),
        (True, False, "Not accessible"),
        (False, True, "Not accessible"),
        (False, False, "Not accessible"),
    ],
)
def test_access_google_page(
        monkeypatch: Any,
        internet: bool,
        valid_url: bool,
        expected: Any
) -> None:
    def mock_has_internet_connection() -> bool:
        return internet

    def mock_valid_google_url(url: str) -> bool:
        return valid_url

    monkeypatch.setattr(
        "app.main.has_internet_connection",
        mock_has_internet_connection
    )

    monkeypatch.setattr(
        "app.main.valid_google_url", mock_valid_google_url
    )

    assert expected == can_access_google_page("url")
