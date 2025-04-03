from app.main import can_access_google_page
from _pytest.monkeypatch import MonkeyPatch
import pytest

@pytest.mark.parametrize(
    "internet, google, result",
    [
        (True, True, "Accessible"),
        (True, False, "Not accessible"),
        (False, True, "Not accessible"),
    ]
)
def test_can_access_google_page_with_internet_and_valid_url(
        monkeypatch: MonkeyPatch,
        internet: bool,
        google: bool,
        result: str
) -> None:
    monkeypatch.setattr("app.main.has_internet_connection", lambda: internet)
    monkeypatch.setattr("app.main.valid_google_url", lambda x: google)
    assert can_access_google_page("ddd") == result
