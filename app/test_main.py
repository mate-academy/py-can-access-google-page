from app.main import can_access_google_page
from _pytest.monkeypatch import MonkeyPatch


def test_function_acces(monkeypatch: MonkeyPatch) -> None:
    monkeypatch.setattr("app.main.has_internet_connection", lambda: True)
    monkeypatch.setattr("app.main.valid_google_url", lambda x: True)
    assert can_access_google_page("ddd") == "Accessible"
    monkeypatch.setattr("app.main.valid_google_url", lambda x: False)
    assert can_access_google_page("ddd") == "Not accessible"
    monkeypatch.setattr("app.main.has_internet_connection", lambda: False)
    monkeypatch.setattr("app.main.valid_google_url", lambda x: True)
    assert can_access_google_page("ddd") == "Not accessible"
