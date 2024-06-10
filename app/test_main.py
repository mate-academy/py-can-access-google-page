from typing import Any
import pytest


import app.main


@pytest.mark.parametrize(
    "has_internet, valid_url, accessibility",
    [
        (True, False, "Not accessible"),
        (False, True, "Not accessible"),
        (False, False, "Not accessible"),
        (True, True, "Accessible")
    ]
)
def test_access_google_page(monkeypatch: Any, has_internet: bool, valid_url: bool, accessibility: str) -> None:
    monkeypatch.setattr(app.main, "has_internet_connection", lambda: has_internet)
    monkeypatch.setattr(app.main, "valid_google_url", lambda _: valid_url)
    assert app.main.can_access_google_page("google.com") == accessibility
