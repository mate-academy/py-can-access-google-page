import pytest
from _pytest.monkeypatch import MonkeyPatch
from app.main import can_access_google_page


@pytest.mark.parametrize(
    "url, is_valid, has_connection, expected",
    [
        ("https://www.google.com", True, True, "Accessible"),
        ("https://www.goo!gle.com", False, True, "Not accessible"),
        ("https://www.google.com", True, False, "Not accessible"),
        ("https://www.goole.com", False, False, "Not accessible"),
    ],
)
def test_can_access_google_page(
    monkeypatch: MonkeyPatch,
    url: str,
    is_valid: bool,
    has_connection: bool,
    expected: str,
) -> None:
    monkeypatch.setattr("app.main.valid_google_url", lambda _: is_valid)
    monkeypatch.setattr(
        "app.main.has_internet_connection", lambda: has_connection
    )
    assert can_access_google_page(url) == expected
