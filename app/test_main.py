import pytest
from _pytest.monkeypatch import MonkeyPatch
from app.main import can_access_google_page


@pytest.mark.parametrize(
    "valid_url, has_connection, expected",
    [
        (True, False, "Not accessible"),
        (False, True, "Not accessible"),
        (False, False, "Not accessible"),
        (True, True, "Accessible"),
    ], ids=[
        "cannot access if only valid url",
        "cannot access if only has connection",
        "cannot access if no connection and invalid url",
        "have access if has connection and valid url"
    ]
)
def test_can_access_google_page(
        monkeypatch: MonkeyPatch,
        valid_url: bool,
        has_connection: bool,
        expected: str
) -> None:
    monkeypatch.setattr(
        "app.main.valid_google_url",
        lambda url: valid_url
    )
    monkeypatch.setattr(
        "app.main.has_internet_connection",
        lambda: has_connection
    )
    result = can_access_google_page("https://www.google.com")
    assert result == expected
