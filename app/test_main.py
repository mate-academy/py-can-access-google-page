from pytest import MonkeyPatch, mark, param
import app.main as main
from app.main import can_access_google_page


@mark.parametrize("is_valid_url, has_connection, expected", [
    param(True, True, "Accessible", id="valid-url_with_internet"),
    param(False, False, "Not accessible", id="invalid-url_no-internet"),
    param(True, False, "Not accessible", id="valid-url_no-internet"),
    param(False, True, "Not accessible", id="invalid-url_with-internet")
])
def test_can_access_google_page_various_scenarios(
        monkeypatch: MonkeyPatch,
        is_valid_url: bool,
        has_connection: bool,
        expected: str
) -> None:
    monkeypatch.setattr(main, "valid_google_url", lambda x: is_valid_url)
    monkeypatch.setattr(main,
                        "has_internet_connection", lambda: has_connection)

    assert can_access_google_page("url") == expected
