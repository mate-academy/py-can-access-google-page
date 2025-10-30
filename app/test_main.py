from pytest import MonkeyPatch, mark
import app.main as main
from app.main import can_access_google_page


@mark.parametrize("valid_url, has_internet, result", [
    (True, True, "Accessible"),
    (False, False, "Not accessible"),
    (True, False, "Not accessible"),
    (False, True, "Not accessible")
])
def test_can_access_google_page_provides_access(
        monkeypatch: MonkeyPatch,
        valid_url: bool,
        has_internet: bool,
        result: str
) -> None:
    monkeypatch.setattr(main, "valid_google_url", lambda x: valid_url)
    monkeypatch.setattr(main, "has_internet_connection", lambda: has_internet)

    assert can_access_google_page("url") == result
