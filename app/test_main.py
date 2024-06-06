from typing import Any
import pytest


import app.main


def test_should_access_google_page(monkeypatch: Any) -> None:
    monkeypatch.setattr(app.main, "has_internet_connection", lambda: True)
    monkeypatch.setattr(app.main, "valid_google_url", lambda url: True)
    assert app.main.can_access_google_page("google.com") == "Accessible"


@pytest.mark.parametrize(
    "has_internet, valid_url",
    [
        (True, False),
        (False, True),
        (False, False)
    ]
)
def test_should_not_access_google_page(monkeypatch: Any, has_internet: bool, valid_url: bool) -> None:
    monkeypatch.setattr(app.main, "has_internet_connection", lambda: has_internet)
    monkeypatch.setattr(app.main, "valid_google_url", lambda _: valid_url)
    assert app.main.can_access_google_page("google.com") == "Not accessible"
