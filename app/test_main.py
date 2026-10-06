import pytest
from pytest import MonkeyPatch

from app.main import can_access_google_page


@pytest.mark.parametrize(
    "connected, valid_url, expected",
    [
        (True, True, "Accessible"),
        (True, False, "Not accessible"),
        (False, True, "Not accessible"),
        (False, False, "Not accessible"),
    ],
)
def test_access_requires_connection_and_valid_url(
    monkeypatch: MonkeyPatch,
    connected: bool,
    valid_url: bool,
    expected: str,
) -> None:
    monkeypatch.setattr("app.main.has_internet_connection", lambda: connected)
    monkeypatch.setattr("app.main.valid_google_url", lambda url: valid_url)
    assert can_access_google_page("https://www.google.com") == expected
