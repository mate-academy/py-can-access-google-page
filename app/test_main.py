from app.main import can_access_google_page
import pytest


@pytest.mark.parametrize(
    "valid_url, has_conn, expected",
    [
        (True, True, "Accessible"),
        (True, False, "Not accessible"),
        (False, True, "Not accessible"),
        (False, False, "Not accessible"),
    ],
)
def test_can_access_google_page(
    monkeypatch: pytest.MonkeyPatch,
    valid_url: str,
    has_conn: bool,
    expected: str
) -> None:
    monkeypatch.setattr("app.main.valid_google_url", lambda url: valid_url)
    monkeypatch.setattr("app.main.has_internet_connection", lambda: has_conn)
    result = can_access_google_page("https://google.com")
    assert result == expected
